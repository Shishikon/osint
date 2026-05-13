from django.shortcuts import render, redirect
from .forms import *

from bs4 import BeautifulSoup
import requests


def index(request):
    return render(request, 'index.html')


def osint(request):
    return render(request, 'osint.html')


def about_site(request):
    return render(request, 'about.html')


def comment(request):
    data = request.POST
    name = data['name']
    email = data['email']
    message = data['message']
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Message: {message}")

    return redirect('index')


def telegram_view(request):
    telegram_form = TelegramForm()
    context = {
        'telegram_form': telegram_form
    }

    if request.method == 'POST':
        telegram_form = TelegramForm(data=request.POST)
        if telegram_form.is_valid():
            data = request.POST
            tg_user_username = data['username']

            get_username = ""
            get_description = ""
            get_img = ""
            get_contact = ""

            telegram_username = f'https://t.me/{tg_user_username}'
            response = requests.get(telegram_username).text
            bs = BeautifulSoup(response, 'html.parser')

            tgme_page_wrap = bs.find_all('div', class_='tgme_page_wrap')

            for i in tgme_page_wrap:
                try:
                    get_username = i.find('span').text.strip()
                except Exception as username_error:
                    print('No username found!')

            for i in tgme_page_wrap:
                try:
                    get_description = i.find('div', class_='tgme_page_description').text.strip()
                except Exception as description_error:
                    print('No description found!')

            try:
                get_img = bs.find('img', class_='tgme_page_photo_image')['src']
            except Exception as avatar_error:
                print('No avatar image found!')

            try:
                get_contact = bs.find('a', class_='tgme_action_button_new shine')['href']
            except Exception as contact_error:
                print('No contact data found!')

            sub_context = {
                'username': get_username,
                'description': get_description,
                'img': get_img,
                'contact': get_contact,
            }

            return render(request, 'components/osint/projects/projects_detail/_telegram_detail.html',
                          context=sub_context)

    return render(request, 'components/osint/projects/_telegram.html', context=context)


def web_surfer_view(request):
    web_surfer_form = WebSurferForm()
    context = {
        'web_surfer_form': web_surfer_form
    }

    if request.method == 'POST':
        web_surfer_form = WebSurferForm(data=request.POST)
        if web_surfer_form.is_valid():
            data = request.POST
            link = data['link']

            get_title = ""
            get_description = ""
            get_thumbnail_or_avatar = ""

            response = requests.get(link).text
            bs = BeautifulSoup(response, 'html.parser')

            try:
                get_title = bs.find('title').text
            except Exception as title_error:
                print('No title found!')

            try:
                get_description = bs.find('meta', property="og:description")['content'].strip()
            except Exception as description_error:
                print('No description found!')

            try:
                get_thumbnail_or_avatar = bs.find('meta', property="og:image")['content']
            except Exception as thumbnail_error:
                print('An error occurred while searching for thumbnail!')

            sub_context = {
                'title': get_title,
                'description': get_description,
                'thumbnail_or_avatar': get_thumbnail_or_avatar,
            }

            return render(request, 'components/osint/projects/projects_detail/_web_surfer_detail.html',
                          context=sub_context)

    return render(request, 'components/osint/projects/_web_surfer.html', context)


def github_view(request):
    github_form = GitHubForm()
    context = {
        'github_form': github_form
    }

    if request.method == 'POST':
        github_form = GitHubForm(data=request.POST)
        if github_form.is_valid():
            data = request.POST
            git_user_username = data['username']

            get_title = ""
            get_name = ""
            get_avatar = ""
            get_bio = ""
            get_nofollow_me = ""
            get_location = ""

            link = f'https://github.com/{git_user_username}'
            response = requests.get(link).text
            bs = BeautifulSoup(response, 'html.parser')

            try:
                get_title = bs.find('title').text
            except Exception as title:
                print('An error occurred while searching for GitHub user title!')

            try:
                get_name = bs.find('span', class_='p-name vcard-fullname d-block overflow-hidden').text.strip()
            except Exception as name:
                print('An error occurred while searching for GitHub username!')

            try:
                get_avatar = bs.find('img', class_='avatar avatar-user width-full border color-bg-default')['src']
            except Exception as avatar:
                print("An error occurred while searching for GitHub user's avatar!")

            try:
                get_bio = bs.find('div', class_='p-note user-profile-bio mb-3 js-user-profile-bio f4').text.strip()
            except Exception as bio:
                print("An error occurred while searching for GitHub user's bio!")

            try:
                get_nofollow_me = bs.find('a', rel='nofollow me').text
            except Exception as nofollow_me:
                print('No any follow-me data given')

            try:
                get_location = bs.find('span', class_='p-label').text
            except Exception as location_error:
                print('No location data given!')

            sub_context = {
                'title': get_title,
                'name': get_name,
                'avatar': get_avatar,
                'bio': get_bio,
                'nofollow_me': get_nofollow_me,
                'location': get_location,
                'link': link
            }
            return render(request, 'components/osint/projects/projects_detail/_github_detail.html',
                          context=sub_context)

    return render(request, 'components/osint/projects/_github.html', context)


def instagram_view(request):
    instagram_form = InstagramForm()
    context = {
        'instagram_form': instagram_form
    }

    if request.method == 'POST':
        instagram_form = InstagramForm(data=request.POST)
        if instagram_form.is_valid():
            data = request.POST
            insta_user_username = data['username']

            get_username = ""
            get_description = ""
            get_avatar = ""
            get_posts = ""
            get_followers = ""
            get_following = ""

            link = f"https://www.picuki.com/profile/{insta_user_username}"

            response = requests.get(link).text
            bs = BeautifulSoup(response, 'html.parser')

            try:
                get_username = bs.find('h1', class_='profile-name-top').text
            except Exception as username_error:
                print(f'No name found while searching for {insta_user_username}.\nCheck the correction of name!')

            try:
                get_description = bs.find('div', class_='profile-description').text.strip()
            except Exception as description_error:
                print("No description found!")

            try:
                get_avatar = bs.find('a', class_='profile-hd-link')['href'].strip()
            except Exception as avatar_error:
                print("No avatar image found!")

            try:
                get_posts = bs.find('span', class_='total_posts').text
            except Exception as posts_error:
                print("No posts found!")

            try:
                get_followers = bs.find('span', class_='followed_by').text
            except Exception as followers_error:
                print("No followers found!")

            try:
                get_following = bs.find('span', class_='follows').text
            except Exception as following_error:
                print("No following data found!")

            sub_context = {
                'username': get_username,
                'description': get_description,
                'avatar': get_avatar,
                'posts': get_posts,
                'followers': get_followers,
                'following': get_following,
            }

            return render(request, 'components/osint/projects/projects_detail/_instagram_detail.html',
                          context=sub_context)

    return render(request, 'components/osint/projects/_instagram.html', context)


def twitch_view(request):
    twitch_form = TwitchForm()
    context = {
        'twitch_form': twitch_form
    }

    if request.method == 'POST':
        twitch_form = TwitchForm(data=request.POST)
        if twitch_form.is_valid():
            data = request.POST
            twitch_user_username = data['username']

            get_username = ""
            get_avatar = ""

            link = f'https://www.twitch.tv/{twitch_user_username}'

            response = requests.get(link).text
            bs = BeautifulSoup(response, 'html.parser')

            try:
                get_username = bs.find('meta', property='og:title')['content'].replace('-', '').replace("Twitch", '')
            except Exception as username_error:
                print(f'No username found while searching for {twitch_user_username}!')

            try:
                get_avatar = bs.find('meta', property='og:image')['content']
            except Exception as avatar_error:
                print(f'No username found while searching for {twitch_user_username}!')

            sub_context = {
                'username': get_username,
                'avatar': get_avatar,
                'link': link,
            }

            return render(request, 'components/osint/projects/projects_detail/_twitch_detail.html',
                          context=sub_context)

    return render(request, 'components/osint/projects/_twitch.html', context)


def steam_view(request):
    steam_form = SteamForm()
    context = {
        'steam_form': steam_form
    }

    if request.method == 'POST':
        steam_form = SteamForm(data=request.POST)
        if steam_form.is_valid():
            data = request.POST
            steam_user_username = data['username']

            get_real_name = ""
            get_location = ""
            get_description = ""
            get_profile_image = ""

            link = f"https://steamcommunity.com/id/{steam_user_username}"

            response = requests.get(link).text
            bs = BeautifulSoup(response, 'html.parser')

            try:
                get_real_name = bs.find('span', class_='actual_persona_name').text
            except Exception as real_name_error:
                print(
                    f'An error occurred while searching for {steam_user_username}.\nPlease make sure that name of '
                    f'steam user is correct.')

            try:
                get_location = bs.find('div', class_='header_real_name ellipsis').text.strip()
            except Exception as location:
                print('No location data given!')

            try:
                get_description = bs.find('meta', property='og:description')['content']
            except Exception as description_error:
                print('No description data given!')

            try:
                get_profile_image = bs.find('link', rel='image_src')['href']
            except Exception as profile_image_error:
                print('No profile image found!')

            sub_context = {
                'real_name': get_real_name,
                'description': get_description,
                'location': get_location,
                'avatar': get_profile_image,
                'link': link,
            }

            return render(request, 'components/osint/projects/projects_detail/_steam_detail.html',
                          context=sub_context)

    return render(request, 'components/osint/projects/_steam.html', context)
