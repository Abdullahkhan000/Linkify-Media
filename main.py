import requests
import re
from pprint import pprint
from decouple import config

TMDB_API_KEY = config("TMDB_API_KEY")
TMDB_BASE_URL = "https://api.themoviedb.org/3"

def slugify(title: str):
    title = title.lower()
    title = re.sub(r"[^\w\s]", "", title)
    title = re.sub(r"\s+", "_", title)
    return title

def rt_url_exists(url: str):
    try:
        r = requests.head(url, timeout=5, allow_redirects=True)
        return r.status_code == 200
    except:
        return False

def fetch_tmdb_data(title: str, media_type="movie"):
    search_url = f"{TMDB_BASE_URL}/search/{media_type}"
    resp = requests.get(
        search_url,
        params={"api_key": TMDB_API_KEY, "query": title},
        timeout=10
    ).json()

    if not resp.get("results"):
        return None, None, None

    tmdb_id = resp["results"][0]["id"]
    tmdb_link = f"https://www.themoviedb.org/{media_type}/{tmdb_id}"

    if media_type == "movie":
        details = requests.get(
            f"{TMDB_BASE_URL}/movie/{tmdb_id}",
            params={"api_key": TMDB_API_KEY},
            timeout=10
        ).json()
    else:
        details = requests.get(
            f"{TMDB_BASE_URL}/tv/{tmdb_id}",
            params={"api_key": TMDB_API_KEY},
            timeout=10
        ).json()

    official_title = details.get("title") or details.get("name")
    imdb_id = details.get("imdb_id")
    imdb_link = f"https://www.imdb.com/title/{imdb_id}/" if imdb_id else None

    return official_title, tmdb_link, imdb_link

# <<< NEW function for testing >>>
def generate_links_for(title: str, media="movie"):
    if not title:
        return {}

    media = media.lower()
    if media not in ("movie", "tv"):
        media = "movie"

    rt_type = "m" if media == "movie" else "tv"
    slug = slugify(title)
    rt_link = f"https://www.rottentomatoes.com/{rt_type}/{slug}"

    if rt_url_exists(rt_link):
        rt_final = rt_link
    else:
        official_title, tmdb_link, imdb_link = fetch_tmdb_data(title, media)
        if official_title:
            slug = slugify(official_title)
            rt_link = f"https://www.rottentomatoes.com/{rt_type}/{slug}"
            if rt_url_exists(rt_link):
                rt_final = rt_link
            else:
                rt_final = "RT page not found"
        else:
            tmdb_link = None
            imdb_link = None
            rt_final = "RT page not found"

    if 'tmdb_link' not in locals() or tmdb_link is None:
        official_title, tmdb_link, imdb_link = fetch_tmdb_data(title, media)

    return {
        "Official Title": official_title,
        "TMDB Link": tmdb_link,
        "IMDb Link": imdb_link,
        "Rotten Tomatoes Link": rt_final
    }

def generate_links():
    title = input("Enter Movie or TV Series Name: ").strip()
    if not title:
        return {}
    media = input("Type 'movie' or 'tv' (default movie): ").strip().lower()
    if media not in ("movie", "tv"):
        media = "movie"
    links = generate_links_for(title, media)
    pprint(links, sort_dicts=False)
    return links

if __name__ == "__main__":
    generate_links()
