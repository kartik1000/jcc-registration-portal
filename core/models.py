from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
import uuid


class Team(models.Model, Importable):
    team_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    team_name = models.CharField(max_length=255, blank=True, null=True)
    player_one_name = models.CharField(
        max_length=255, default="No Player Assigned")
    player_one_email = models.EmailField(
        max_length=255, default="No Email Provided")
    player_one_contact = PhoneNumberField(null=False, blank=False, unique=True)
    player_one_hall = models.CharField(max_length=255, blank=True, null=True)
    player_two_name = models.CharField(
        max_length=255, default="No Player Assigned")
    player_two_email = models.EmailField(
        max_length=255, default="No Email Provided")
    player_two_contact = PhoneNumberField(null=False, blank=False, unique=True)
    player_two_hall = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    unique_team_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.team_name)
