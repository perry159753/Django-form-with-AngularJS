import os
import uuid
from multiselectfield import MultiSelectField
from PIL import Image
from django.db import models
from django.conf import settings

def create_thumbnail(input_image, thumbnail_size=(256,256)):
    if not input_image or input_image=='':
        return None
    image=Image.open(input_image)
    image.thumbnail(thumbnail_size, Image.ANTIALIAS)
    filename=scramble_uploaded_filename(None, os.path.basename(input_image.name))
    arrdata = filename.split(".")
    extension = arrdata.pop()
    basename="".join(arrdata)
    new_filename="{}_thumb.{}".format(basename, extension)
    image.save(os.path.join(settings.MEDIA_ROOT, new_filename))
    return new_filename

def scramble_uploaded_filename(instance, filename):
    extension = filename.split(".")[-1]
    return "{}.{}".format(uuid.uuid4(), extension)


class UploadImage(models.Model):
    BRANCH_CHOICES = (
        ('cse', 'CSE'),
        ('it', 'IT'),
    )
    name = models.TextField("Name of the student", max_length=255, default="")
    emailid = models.TextField("EmailId of the student", max_length=255, default="")
    number = models.TextField("Contact number of the student", max_length=10, default="")
    branch = models.TextField("Branch",max_length=100, choices=BRANCH_CHOICES,default="")
    image = models.ImageField("Uploaded image", upload_to=scramble_uploaded_filename)
    thumbnail = models.ImageField("Thumbnail of the uploaded image", blank="True")
    videofile = models.FileField("Uploaded video",upload_to=scramble_uploaded_filename, default="")

    def save(self, force_insert=False, false_update=False, using=None, update_fields=None):
        self.thumbnail=create_thumbnail(self.image)
        super(UploadImage, self).save()

