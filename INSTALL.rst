============
Installation
============

Prerequisites
-------------

* Python interpreter
* PostgreSQL server
* Redis server

Python interpreter
^^^^^^^^^^^^^^^^^^

Install Python for your host system.

Assuming Ubuntu Server host and using PPA:

.. code-block:: bash

    $ sudo apt update && sudo apt upgrade -y
    $ sudo apt install software-properties-common -y
    $ sudo add-apt-repository ppa:deadsnakes/ppa
    $ sudo apt install python3.10
    $ sudo apt install python3.10-venv

.. note:: Note: this project has been developed using python 3.10, 3.9 should work but hasn't been tested.


Downloading dependencies
^^^^^^^^^^^^^^^^^^^^^^^^

Assuming PostgreSQL already installed and project cloned in /var/www/osef:

.. code-block:: bash

    $ cd /var/www/osef
    $ python3.10 -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements/production.txt


Configuration
^^^^^^^^^^^^^

Copy the ``.env.example`` file and adjust for your settings.

.. code-block:: bash

    $ cp .env.example .env

.. note:: If you don't want to use `Sentry <https://sentry.io>`_, comments the following parts:

    :file:`config/settings/production.py`

    L154-L158

    L169-L182


Systemd
^^^^^^^

Create 2 systemd services, one to handle the socket, the other to handle the wsgi app.

:file:`/etc/systemd/system/gunicorn.socket`

.. code-block:: ini

    [Unit]
    Description=gunicorn socket

    [Socket]
    ListenStream=/var/www/osef/gunicorn.sock

    [Install]
    WantedBy=sockets.target


:file:`/etc/systemd/system/gunicorn.service`

.. code-block:: ini

    [Unit]
    Description=gunicorn daemon
    Requires=gunicorn.socket
    After=network.target

    [Service]
    Environment="DJANGO_READ_DOT_ENV_FILE=True"
    Environment="DJANGO_SETTINGS_MODULE=config.settings.production"
    WorkingDirectory=/var/www/osef
    ExecStart=/var/www/backend/osef/bin/python /var/www/osef/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/var/www/osef/gunicorn.sock config.wsgi

    [Install]
    WantedBy=multi-user.target

NGINX
^^^^^^^^^^^^^^^

Create nginx server block with these settings:

.. code-block:: nginx

    server {
        listen 80;
        server_name example.com;

        location = /favicon.ico {
                access_log off;
                log_not_found off;
        }

        location /static/ {
                alias /var/www/osef/staticfiles/;
        }

        location /media/ {
                alias /var/www/osef/osef/media/;
        }

        location / {
            include proxy_params;

            proxy_pass http://unix:/var/www/osef/gunicorn.sock;

            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "Upgrade";

            client_max_body_size 15M;
        }
    }
