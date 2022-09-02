import uuid
from django.db import models
from django import forms
import django

class schematics(models.Model):

    categoryChoices = [
        ("redstone", "Redstone"),
        ("build", "Build"),
        ("misc", "Miscellaneous")
    ]
    sourceChoices = [
        ("downloadedMap", "Downloaded map and created schematic"),
        ("downloadedSchematic", "Downloaded schematic directly"),
    ]
    min = pow(10, 10-1)
    max = pow(10, 10) - 1
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, help_text="Title for the schematic")
    shortDescription = models.CharField(max_length=255, help_text="A short description for showing in the lists")
    description = models.TextField(help_text="The actual description shown in the dedicated page for the schematic")
    image = models.CharField(max_length=1024, help_text="link to the image for the schematic thumbnail")
    #category = models.ch
    sourceType = models.CharField(max_length=20, choices=sourceChoices, default="downloadedSchematic")
    sourceLink = models.CharField(max_length=255, help_text="The source for the downloaded map/downloaded schematic")
    keyWords = models.CharField(max_length=255, help_text="Key words for finding the schematic")
    fileLink = models.CharField(max_length=1024, help_text="link to the file for the schematic file")
    currentDateTime = models.DateTimeField(default=django.utils.timezone.now)
    downloadCount = models.PositiveIntegerField(default=0, null=False, blank=False)
    downloadCountHR = models.CharField(max_length=128, editable=False, default=0)
    def __str__(self):
        return self.title
    class Meta:
        ordering =  ("-downloadCount",)
    def increment_download_count(self):
        self.downloadCount += 1

