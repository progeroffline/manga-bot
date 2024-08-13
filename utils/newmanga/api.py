import httpx

from typing import Any

from .types import NewManga, NewMangaMainPageResonse


class NewMangaApi:
    def __init__(self):
        self.api_link = "https://api.newmanga.org/v2/projects/popular"
        self.client = httpx.Client(
            headers={
                "Accept": "application/json, text/plain, */*",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            }
        )

    def get_main_page(self) -> NewMangaMainPageResonse | None:
        params = {"size": "30"}
        json_response = self.client.get(self.api_link, params=params).json()

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

        json_response = self.client.get(self.api_link, params=params)
        if json_response.status_code == 200:
            params = json_response.json()

            return NewMangaMainPageResonse(
                items=[reformat_json_to_manga_object(item) for item in params["items"]],
            )
        else:
            return None
