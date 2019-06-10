from django.contrib import admin
from imageupload.models import UploadImage

# Register the UploadedImage Model for the Admin Page
admin.site.register(UploadImage)