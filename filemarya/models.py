from django.db import models


class Data(models.Model):
    file=models.FileField(upload_to='myfiles/',blank=True)
    
    class Meta:
        app_label = 'filemarya'
