import aiohttp
import asyncio


platforms = [
    "https://github.com/{}",
    "https://reddit.com/user/{}",
    "https://m.facebook.com/{}?_rdr",
    "https://www.youtube.com/user/{}",
    "https://nitter.net/{}",
    "https://t.me/{}",
    "https://www.tiktok.com/@{}",
    "https://tinder.com/@{}",
    "https://pinterest.com/{}/",
    "https://feelinsonice.appspot.com/web/deeplink/snapcode?username={}&size=400&type=SVG",
    "https://www.reddit.com/user/{}/about.json",
    "https://soundcloud.com/{}",
    "https://steamcommunity.com/id/{}/",
    "https://linktr.ee/{}",
    "https://www.xboxgamertag.com/search/{}",
    "https://profiles.wordpress.org/{}/",
    "https://allmylinks.com/{}",
    "https://archive.org/details/@{}",
    "https://www.ebay.com/usr/{}",
    "https://www.duolingo.com/2017-06-30/users?username={}&_=1628308619574",
    "https://www.chess.com/member/{}",
    "https://{}.myshopify.com/",
    "https://playerdb.co/api/player/minecraft/{}",
    "https://www.patreon.com/{}",
    "https://hub.docker.com/v2/users/{}/",
    "https://www.gamespot.com/profile/{}/",
    "https://www.shutterstock.com/pt/g/{}/about",
    "https://www.tripadvisor.com/Profile/{}",
    "https://rapidapi.com/user/{}",
    "https://en.wikipedia.org/w/api.php?action=query&format=json&list=users&ususers={}&usprop=cancreate&formatversion=2&errorformat=html&errorsuselocal=true&uselang=en",
    "https://www.buymeacoffee.com/{}",
    "https://tracker.gg/lol/profile/riot/NA/{}/overview",
    "https://ideas.lego.com/profile/{}/entries?query=&sort=top",
    "https://medium.com/@{}",
    "https://hackerone.com/{}?type=user",
    "https://onecompiler.com/api/users/{}",
    "https://tryhackme.com/p/{}",
    "https://community.cloudflare.com/u/{}",
    "https://www.freelancer.com/u/{}",
    "https://dev.to/{}",
    "https://bitbucket.org/{}/",
    "https://www.hackerearth.com/@{}",
    "https://open.spotify.com/user/{}",
    "https://story.snapchat.com/s/{}",
    "https://www.codewars.com/users/{}",
    "https://bugbounty.gg/members/{}/",
    "https://giphy.com/channel/{}",
    "https://bandcamp.com/{}",
    "https://www.hackster.io/{}",
]



async def check(session, url, username, sem):

    async with sem:

        try:

            async with session.get(url) as response:

                text = await response.text()

                text = text.lower()

                username = username.lower()

                if response.status == 200:

                    if username in text:

                        return {
                            "url": url,
                            "status": "FOUND"
                        }

                    return {
                        "url": url,
                        "status": "POSSIBLY NOT FOUND"
                    }

                return {
                    "url": url,
                    "status": "NOT FOUND"
                }

        except Exception as e:

            return {
                "url": url,
                "status": "ERROR",
                "error": str(e)
            }

async def main(username):

    sem = asyncio.Semaphore(10)  # 👈 inside loop

    timeout = aiohttp.ClientTimeout(total=5)

    async with aiohttp.ClientSession(timeout=timeout) as session:

        tasks = []

        for site in platforms:
            url = site.format(username)

            tasks.append(check(session, url, username, sem))

        return await asyncio.gather(*tasks)