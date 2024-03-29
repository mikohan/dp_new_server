from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=500, blank=True)
    country = models.CharField(max_length=255, default="Россия", null=True, blank=True)

    def __str__(self):
        return self.user.username


class BlackListEmail(models.Model):
    email = models.EmailField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        self.email = self.email.strip()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Забанен"
        verbose_name_plural = "Забанены"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
