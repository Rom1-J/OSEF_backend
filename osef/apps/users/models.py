import datetime
import uuid

from django.db import models


class User(models.Model):
    id = models.UUIDField("Identification", primary_key=True, default=uuid.uuid4(), editable=False)
    username = models.CharField("Username", max_length=20)
    email = models.EmailField("Email", max_length=20)
    password = models.CharField("Password", max_length=20)
    avatar = models.ImageField("Avatar")
    creation_date = models.DateField("Creation Date", default=datetime.date.today)
    last_connection = models.DateField("Last Connection")
    friend_code = models.IntegerField("Friend code")
    pub_key = models.CharField("Public Key")


class Transaction(models.Model):
    token = models.UUIDField("Token", primary_key=True, default=uuid.uuid4(), editable=False)
    user1_id = models.CharField("User 1 Identification")
    user2_id = models.CharField("User 1 Identification")
    creation_date = models.DateField("Creation Date", default=datetime.date.today)
    nb_new_file = models.IntegerField("Number of New Files")


class File(models.Model):
    id = models.UUIDField("Identification", primary_key=True, default=uuid.uuid4(), editable=False)
    filename = models.CharField("Filename", max_length=30)
    data = models.CharField("Data")
    checksum = models.CharField("Checksum")
    upload_date = models.DateField("Upload Date")
    owner = models.CharField("Owner")
    receiver = models.CharField("Receiver")
    times_downloaded = models.IntegerField("Times Downloaded")
    transaction_token = models.CharField("Transaction Token")

