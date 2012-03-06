
from django.db import models
from django.contrib.auth.models import User

class TwitterInfo(models.Model):
    user = models.OneToOneField(User)
    
    screen_name      = models.CharField(max_length=15)
    id               = models.BigIntegerField(primary_key=True)

    token            = models.CharField(max_length=100)
    secret           = models.CharField(max_length=100)

    name             = models.CharField(max_length=35, default="")
    description      = models.CharField(max_length=160, default="")
    location         = models.CharField(max_length=35, default="")
    url              = models.CharField(max_length=255, default="")
    profile_image    = models.CharField(max_length=255, default="")
    lang             = models.CharField(max_length=5, default="")
    utc_offset       = models.IntegerField(null=True, blank=True)
    time_zone        = models.CharField(max_length=35, default="")

    joined_on        = models.DateTimeField(null=True, blank=True)
    protected        = models.BooleanField(default=False)
    statuses_count   = models.IntegerField(null=True, blank=True)
    favourites_count = models.IntegerField(null=True, blank=True)
    followers_count  = models.IntegerField(null=True, blank=True)
    friends_count    = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.screen_name
