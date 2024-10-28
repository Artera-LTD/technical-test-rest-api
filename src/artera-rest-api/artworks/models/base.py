from django.db import models
from django.contrib.postgres.fields import ArrayField
from users.models import Profiles
from .types import ArtworkTypeChoices, ArtworkPrivacyChoices
import uuid

DEFAULT_ARTWORK_NAME = "Untitled"

class Artworks(models.Model):
    artwork_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    artwork_type = models.TextField(choices=ArtworkTypeChoices.choices)
    artwork_privacy = models.TextField(choices=ArtworkPrivacyChoices.choices, default=ArtworkPrivacyChoices.PUBLIC)
    artwork_name = models.TextField(default=DEFAULT_ARTWORK_NAME)
    artwork_date = models.DateTimeField(blank=True, null=True)
    artwork_images = models.JSONField(blank=True, default=dict)
    artwork_location = models.TextField(blank=True)
    artwork_description = models.TextField(blank=True)
    artwork_likes_counter = models.IntegerField(default=0)
    artwork_comments_counter = models.IntegerField(default=0)
    artwork_views_counter = models.IntegerField(default=0)
    artwork_collections_counter = models.IntegerField(default=0)
    artwork_shares_counter = models.IntegerField(default=0)
    artwork_main_image_height = models.IntegerField(blank=True, null=True)
    artwork_main_image_width = models.IntegerField(blank=True, null=True)
    profile = models.ForeignKey(Profiles, on_delete=models.CASCADE, blank=True, null=True)
    # artwork_admin_list = ArrayField(models.UUIDField(), blank=True, default=list)
