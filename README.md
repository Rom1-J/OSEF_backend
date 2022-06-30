# OSEF

Open Storage for Encrypted Files

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: GPLv3

## Project Purpose

**OSEF** is a wep app, used to send end-to-end ecrypted files to your contacts.
Create a account, share your friend code to your friends, and you will be able to send files up to 20 Mb through our secure service. Unless many end-to-end ecryption services, you can use OSEF on different devices, using the same account!

### How does it work ?

- Create an account, and the server tells you if your password match a minimal robustness to go further.
- Validate your account in your mails
- At each login, keys will be generated client-side, keeping the secret one, and sending the oublic to the server. It will allow you to share files with other people
- Send your friend code to someone by the way you prefer, or add a friend, and it will open a discussion page.
- In this page, you will be able to send files to your contact.
- Each files are encrypted with your relatives keys at the time you upload it to your browser. Files will be send and saved encrypted, meaning that nobody else than you and your contact will be able to see their content, not even us!

### Things to know

- Login and encryption processes may take few seconds to complete, because of complex security functions
- Your secret key is stored only in your browser, and just the time of your session. It is never sent anywhere else. So do you, **NEVER SHARE IT**, or your files could be decrypted by someone else. Same thing for your password.
- Talking about password, use a strong password (min. 12 length, with capital letters, special caracters and numbers) and never forget it.
- If you ever change your **username, email, or password**, all your past files **won't be accessible anymore!** (because a new key will be generated, so it won't match the last one)


This is a school project after all, so things could be missing. Feel free to reach us, and tell us about that! 


-----

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create a **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy osef

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

### Email Server

In development, it is often nice to be able to see emails that are being sent from your application. If you choose to use [MailHog](https://github.com/mailhog/MailHog) when generating the project a local SMTP server with a web interface will be available.

1.  [Download the latest MailHog release](https://github.com/mailhog/MailHog/releases) for your OS.

2.  Rename the build to `MailHog`.

3.  Copy the file to the project root.

4.  Make it executable:

        $ chmod +x MailHog

5.  Spin up another terminal window and start it there:

        ./MailHog

6.  Check out <http://127.0.0.1:8025/> to see how it goes.

Now you have your own mail server running locally, ready to receive whatever you send it.

### Sentry

Sentry is an error logging aggregator service. You can sign up for a free account at <https://sentry.io/signup/?code=cookiecutter> or download and host it yourself.
The system is set up with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.

## Deployment

The following details how to deploy this application.
