from django.db import models

class TelegramSearch(models.Model):

    searched_username = models.CharField(null=True, max_length=255)
    username = models.CharField(null=True, max_length=255, blank=True)
    description = models.TextField(null=True, blank=True)
    img = models.TextField(null=True, blank=True)
    contact = models.TextField(null=True, blank=True)
    searched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.searched_username

class GitHubSearch(models.Model):

    searched_username = models.CharField(null=True, max_length=255)
    fullname = models.CharField(null=True, max_length=255, blank=True)
    bio = models.TextField(null=True, blank=True)
    avatar = models.URLField(null=True, blank=True)
    followers = models.IntegerField(null=True, blank=True)
    following = models.IntegerField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    organization = models.CharField(null=True, blank=True)
    repositories = models.IntegerField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    searched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.searched_username