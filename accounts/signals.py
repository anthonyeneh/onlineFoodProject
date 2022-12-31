from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import User, UserProfile


@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)
        # print('User profile is created')
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
            print('User is updated')
        except:
            # Create the userprofile if not exist
            UserProfile.objects.create(user=instance)
        #     print('Profile was not exist, but one has been created')
        # print('User is updated - 2')

@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    pass
    # print(instance.username, 'this user is being saved')
# post_save.connect(post_save_create_profile_receiver, sender=User)
