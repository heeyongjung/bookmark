from django.db import models
from django.urls import reverse
from datetime import datetime

from django.utils.dateformat import DateFormat



# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField("Site URL")
    pub_date = models.DateTimeField("date published",null=True)
    #memo = models.CharField(max_length=500)

    def __str__(self):
        return "이름 : "+self.site_name +", 주소 : "+self.url #+ "메모 : "+self.memo

    def get_absolute_url(self):
        return reverse('detail',args=[str(self.id)])




