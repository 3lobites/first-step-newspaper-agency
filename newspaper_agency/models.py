from django.core.validators import MinValueValidator
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ("id", )

    def __str__(self):
        return f"{self.name}"


class Redactor(AbstractUser):
    MIN_YEAR_EXPERIENCE = 1
    years_of_experience = models.IntegerField(validators=[MinValueValidator(MIN_YEAR_EXPERIENCE)], default=1)

    class Meta:
        ordering = ("id", )

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("newspaper_agency:redactor-detail", kwargs={"pk": self.pk})


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(default="Blanked news, all very good.")
    published_date = models.DateTimeField(auto_now=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    publishers = models.ManyToManyField(Redactor, related_name="newspapers")

    def __str_(self):
        return f"{self.title} ({self.topic}, redactor: {self.publishers}, publication date - {self.published_date})"
