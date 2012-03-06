
from datetime import datetime
from django.contrib.auth.models import User

from twitter_users.models import TwitterInfo
from twitter_users import settings

class TwitterBackend(object):
    def authenticate(self, twitter_id=None, screen_name=None, token=None, secret=None, user_info=None):
        # find or create the user

        def copy_info(user_info, info):
            # There must be a better way of doing this. I don't know :$
            if user_info['lang']: info.lang = user_info['lang']
            if user_info['created_at']: info.joined = datetime.strptime(user_info['created_at'], "%a %b %d %H:%M:%S +0000 %Y")
            if user_info['url']: info.url = user_info['url']
            if user_info['profile_image_url']: info.profile_image = user_info['profile_image_url']
            if user_info['protected']: info.protected = user_info['protected']
            if user_info['name']: info.name = user_info['name']
            if user_info['description']: info.description = user_info['description']
            if user_info['statuses_count']: info.statuses_count = user_info['statuses_count']
            if user_info['favourites_count']: info.favourites_count = user_info['favourites_count']
            if user_info['followers_count']: info.followers_count = user_info['followers_count']
            if user_info['friends_count']: info.friends_count = user_info['friends_count']
            if user_info['utc_offset']: info.utc_offset = user_info['utc_offset']
            if user_info['location']: info.location = user_info['location']
            if user_info['time_zone']: info.time_zone = user_info['time_zone']

        try:
            info = TwitterInfo.objects.get(id=twitter_id)
            # make sure the screen name is current
            if info.screen_name != screen_name:
                info.screen_name = screen_name
            if user_info:
                copy_info(user_info, info)
            info.save()
            user = info.user
        except TwitterInfo.DoesNotExist:
            email    = "%s@twitter.com" % screen_name
            user     = User.objects.create_user(settings.USERS_FORMAT % screen_name, email)
            user.save()
            info = TwitterInfo(user=user, screen_name=screen_name, id=twitter_id, token=token, secret=secret)
            if user_info:
                copy_info(user_info, info)
            info.save()
        return user
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
