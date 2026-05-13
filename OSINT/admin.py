from django.contrib import admin
from .models import *



class TelegramSearchAdminSite(admin.ModelAdmin):
    list_display = ('searched_username', 'contact', 'searched_at')
    list_display_links = ('searched_username', 'contact')



class GitHubSearchAdminSite(admin.ModelAdmin):
    list_display = ('searched_username', 'link', 'searched_at', 'organization')
    list_display_links = ('searched_username', 'link')



admin.site.register(TelegramSearch, TelegramSearchAdminSite)
admin.site.register(GitHubSearch, GitHubSearchAdminSite)