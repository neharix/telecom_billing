import datetime

import pytz
from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    full_name = models.CharField(max_length=400)
    phone_number = models.CharField(max_length=20, unique=True)
    balance = models.FloatField()
    appraisal = models.ForeignKey("Appraisal", on_delete=models.CASCADE)
    services = models.ManyToManyField("Service", blank=True)

    def __str__(self):
        return f"{self.phone_number} {self.full_name}"

    class Meta:
        verbose_name = "abonent"
        verbose_name_plural = "abonentler"


class Appraisal(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "nyrhnama"
        verbose_name_plural = "nyrhnamalar"


class Service(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "hyzmat"
        verbose_name_plural = "hyzmatlar"


class Package(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "bukja"
        verbose_name_plural = "bukjalar"


class ClientPackage(models.Model):
    package = models.ForeignKey("Package", on_delete=models.CASCADE)
    client = models.ForeignKey("Client", on_delete=models.CASCADE)
    ends_at = models.DateTimeField()

    class Meta:
        verbose_name = "ulanyjy bukjasy"
        verbose_name_plural = "ulanyjy bukjalary"

    def __str__(self):
        return f"{self.client.full_name} {self.package.name} {self.ends_at}"
