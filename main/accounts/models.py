from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)




    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        # Save the profile instance itself
        super(Profile, self).save(*args, **kwargs)

        # If the profile is newly created, create a new Profile object
        if not hasattr(self, '_creating') or self._creating:
            self._creating = False
            profile, created = Profile.objects.get_or_create(user=self.user)

            if created:
                profile.image = self.image
                profile.first_name = self.first_name
                profile.last_name = self.last_name
                profile.save()
