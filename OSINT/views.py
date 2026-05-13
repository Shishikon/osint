from django.shortcuts import render
from .forms import *
import asyncio
from bs4 import BeautifulSoup
import requests
from .async_checker import main

from .models import TelegramSearch


def index(request):
    return render(request, 'index.html')


def osint(request):
    return render(request, 'osint.html')


def about_site(request):
    return render(request, 'about.html')


async def web_surfer_view(request):
    web_surfer_form = WebSurferForm()
    context = {
        'web_surfer_form': web_surfer_form
    }

    if request.method == 'POST':
        web_surfer_form = WebSurferForm(data=request.POST)
        if web_surfer_form.is_valid():
            username = web_surfer_form.cleaned_data['link']
            results = await main(username)
            context = {
                'web_surfer_form': web_surfer_form,
                'results': results,
                'username': username
            }


            return render(request, 'components/osint/projects/projects_detail/_web_surfer_detail.html', context)

    return render(request, 'components/osint/projects/_web_surfer.html', context)


def telegram_view(request):

    telegram_form = TelegramForm()

    context = {
        'telegram_form': telegram_form
    }

    if request.method == 'POST':

        telegram_form = TelegramForm(request.POST)

        if telegram_form.is_valid():

            tg_user_username = telegram_form.cleaned_data['searched_username']

            url = f'https://t.me/{tg_user_username}'

            try:
                response = requests.get(url, timeout=10).text
                bs = BeautifulSoup(response, 'html.parser')

            except Exception:
                return render(request, 'error.html')

            get_username = None
            get_description = None
            get_img = None
            get_contact = None

            wrap = bs.find('div', class_='tgme_page_wrap')

            if wrap:

                username_tag = wrap.find('span')
                if username_tag:
                    get_username = username_tag.text.strip()

                desc_tag = wrap.find('div', class_='tgme_page_description')
                if desc_tag:
                    get_description = desc_tag.text.strip()

            img_tag = bs.find('img', class_='tgme_page_photo_image')
            if img_tag:
                get_img = img_tag.get('src')

            contact_tag = bs.find('a', class_='tgme_action_button_new shine')
            if contact_tag:
                get_contact = contact_tag.get('href')

            telegram_search = telegram_form.save(commit=False)

            telegram_search.username = get_username
            telegram_search.description = get_description
            telegram_search.img = get_img
            telegram_search.contact = get_contact

            telegram_search.save()

            return render(request,
                'components/osint/projects/projects_detail/_telegram_detail.html',
                {
                    'username': get_username,
                    'description': get_description,
                    'img': get_img,
                    'contact': get_contact,
                }
            )

    return render(request, 'components/osint/projects/_telegram.html', context)


def github_view(request):
    github_form = GitHubForm()
    context = {
        'github_form': github_form
    }

    if request.method == 'POST':
        github_form = GitHubForm(data=request.POST)

        if github_form.is_valid():

            git_user_username = github_form.cleaned_data['searched_username']

            fullname = ""
            username = ""
            get_avatar = ""
            get_bio = ""
            followers_count = ""
            following_count = ""
            location = ""
            organization = ""
            repositories = ""

            link = f'https://github.com/{git_user_username}'
            response = requests.get(link).text
            bs = BeautifulSoup(response, 'html.parser')

            # fullname
            try:
                fullname = bs.find('span', class_='p-name vcard-fullname d-block overflow-hidden').text.strip()
            except Exception as name:
                fullname = None

            # username
            try:
                username = bs.find('span', class_='p-nickname vcard-username d-block').text.strip()
            except Exception as name:
                username = None

            # bio
            try:
                get_bio = bs.find('div', class_='p-note user-profile-bio tmp-mb-3 js-user-profile-bio f4').text.strip()
            except Exception as name:
                get_bio = None

            # avatar
            try:
                get_avatar = bs.find('a', class_='d-block')['href']
            except Exception as name:
                get_avatar = None

            # followers
            try:
                followers = bs.find('a', class_='Link--secondary no-underline no-wrap',
                                    href=f"https://github.com/{git_user_username}?tab=followers")
                followers_count = followers.find('span').text.strip()
            except Exception as name:
                followers_count = None

            # following
            try:
                following = bs.find('a', class_='Link--secondary no-underline no-wrap',
                                    href=f"https://github.com/{git_user_username}?tab=following")
                following_count = following.find('span').text.strip()
            except Exception as name:
                following_count = None

            # location
            try:
                location = bs.find('li', class_='vcard-detail pt-1 hide-sm hide-md',
                                   itemprop="homeLocation").text.strip()
            except Exception as name:
                location = None

            # organization
            try:
                organization = bs.find('li', class_='vcard-detail pt-1 hide-sm hide-md',
                                       itemprop="worksFor").text.strip()
            except Exception as name:
                organization = "None"

            # repos
            try:
                repositories = bs.find('span', class_="Counter").text.strip()
            except Exception as name:
                repositories = None

            git_search = github_form.save(commit=False)

            git_search.searched_username = username
            git_search.fullname = fullname
            git_search.bio = get_bio
            git_search.avatar = get_avatar
            git_search.followers = followers_count
            git_search.following = following_count
            git_search.location = location
            git_search.organization = organization
            git_search.repositories = repositories
            git_search.link = link
            git_search.save()

            sub_context = {
                'fullname': fullname,
                'username': username,
                'avatar': get_avatar,
                'bio': get_bio,
                'location': location,
                'followers_count': followers_count,
                'following_count': following_count,
                'organization': organization,
                'repos': repositories,
                'link': link
            }
            return render(request, 'components/osint/projects/projects_detail/_github_detail.html',
                          context=sub_context)

    return render(request, 'components/osint/projects/_github.html', context)



