from typing import Any
import requests

from .types import NewManga, NewMangaMainPageResonse


class NewMangaApi:
    def __init__(self):
        self.api_link = "https://api.newmanga.org/v2/projects/popular"
        self.session = requests.Session()
        self.session.headers = {
            "accept": "application/json, text/plain, */*",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        }

    def get_main_page(self) -> NewMangaMainPageResonse | None:
        params = {"size": "30"}
        json_response = self.session.get(self.api_link, params=params).json()

        def reformat_json_to_manga_object(params: dict[str, Any]) -> NewManga:
            return NewManga(
                id=params["id"],
                slug=params["slug"],
                description=params["description"],
                type=params["type"],
                raiting=params["rating"],
                likes=params["hearts"],
                title_ru=params["title"]["ru"],
                title_en=params["title"]["en"],
                picture_url=f"https://img.newmanga.org/ProjectLarge/webp/{params['image']['name']}",
                page_url=f"https://newmanga.org/p/{params['slug']}",
            )

        json_response = self.session.get(self.api_link, json=params)
        if json_response.ok:
            params = json_response.json()

            return NewMangaMainPageResonse(
                items=[reformat_json_to_manga_object(item) for item in params["items"]],
            )
        else:
            return None
