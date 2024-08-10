import httpx
from typing import Any
from .types import MainPageResponse, Manga


class SenkuroApi:
    def __init__(self):
        self.api_link = "https://api.senkuro.com/graphql"
        self.client = httpx.Client(
            headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0",
                "Content-Type": "application/json",
            }
        )

    @staticmethod
    def reformat_json_to_manga_object(json_data: dict[str, Any]) -> Manga:
        titles = {title["lang"]: title["content"] for title in json_data["titles"]}
        return Manga(
            id=json_data["id"],
            slug=json_data["slug"],
            status=json_data["status"],
            type=json_data["type"],
            raiting=json_data["rating"],
            title_ru=titles["RU"],
            title_en=titles.get("EN"),
            title_ja=titles.get("JA"),
            picture_url=json_data["cover"]["original"]["url"],
            page_url=f"https://senkuro.com/manga/{json_data['slug']}/chapters",
        )

    def get_main_page(self) -> MainPageResponse | None:
        json_data = {
            "extensions": {
                "persistedQuery": {
                    "sha256Hash": "a4da0008c5103bfe9ea914dfd51091a6a67924b9d417806196a9e077168cf663",
                    "version": 1,
                },
            },
            "operationName": "fetchMainPage",
            "variables": {
                "genre": {
                    "exclude": [
                        "hentai",
                    ],
                },
            },
        }

        json_response = self.client.post(self.api_link, json=json_data)
        if json_response.status_code == 200:
            json_data = json_response.json()["data"]

            return MainPageResponse(
                mangas=[
                    self.reformat_json_to_manga_object(node["node"])
                    for node in json_data["mangas"]["edges"]
                ],
                last_manga_chapters=[
                    self.reformat_json_to_manga_object(node["node"])
                    for node in json_data["lastMangaChapters"]["edges"]
                ],
                manga_popular_by_period=[
                    self.reformat_json_to_manga_object(node)
                    for node in json_data["mangaPopularByPeriod"]
                ],
            )
        else:
            return None

    def get_catalog(self, page: int = 0):
        json_data = {
            "extensions": {
                "persistedQuery": {
                    "sha256Hash": "6547bf3c404812150e9e0429adba781f36a0ef17b12d4cb31d8caf1d8bac91e1",
                    "version": 1,
                },
            },
            "operationName": "fetchMangas",
            "variables": {
                "after": None,
                "bookmark": {
                    "exclude": [],
                    "include": [],
                },
                "chapters": {},
                "format": {
                    "exclude": [],
                    "include": [],
                },
                "genre": {
                    "exclude": [
                        "hentai",
                    ],
                    "include": [],
                },
                "orderDirection": "DESC",
                "orderField": "CREATED_AT",
                "originCountry": {
                    "exclude": [],
                    "include": [],
                },
                "rating": {
                    "exclude": [],
                    "include": [],
                },
                "search": None,
                "source": {
                    "exclude": [],
                    "include": [],
                },
                "status": {
                    "exclude": [],
                    "include": [],
                },
                "tag": {
                    "exclude": [],
                    "include": [],
                },
                "translitionStatus": {
                    "exclude": [],
                    "include": [],
                },
                "type": {
                    "exclude": [],
                    "include": [],
                },
            },
        }

        cursor = None
        json_response = None
        if page > 0:
            for _ in range(page):
                json_data["variables"]["after"] = cursor
                json_response = self.client.post(self.api_link, json=json_data)
                cursor = json_response.json()["data"]["mangas"]["pageInfo"]["endCursor"]

        if json_response is None:
            json_data = json_response = self.client.post(
                self.api_link, json=json_data
            ).json()
        else:
            json_data = json_response.json()

        return MainPageResponse(
            mangas=[
                self.reformat_json_to_manga_object(node["node"])
                for node in json_data["mangas"]["edges"]
            ],
            last_manga_chapters=[
                self.reformat_json_to_manga_object(node["node"])
                for node in json_data["lastMangaChapters"]["edges"]
            ],
            manga_popular_by_period=[
                self.reformat_json_to_manga_object(node)
                for node in json_data["mangaPopularByPeriod"]
            ],
        )
