from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(
        max_length=150,
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()
    new_field = models.ForeignKey(
        "home.Demo",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="homepage_new_field",
    )

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Demo(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
    link = models.ForeignKey(
        "home.CustomText",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="demo_link",
    )

    class Meta:
        verbose_name_plural = "Custom Demo verbose"
