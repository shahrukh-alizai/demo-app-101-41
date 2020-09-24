from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )
    test = models.FloatField(
        null=True,
        blank=True,
    )
    hello = models.ForeignKey(
        "home.DemoModel",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="user_hello",
    )

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
