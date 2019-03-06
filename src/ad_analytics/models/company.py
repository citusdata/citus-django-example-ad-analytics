from django.db import models


def get_image_path(instance, filename):
    return os.path.join('images', 'companies', get_filename(filename))


class Company(models.Model):
    name = models.TextField()
    image = models.ImageField(upload_to=get_image_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
