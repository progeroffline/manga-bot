from typing import Any, Dict, List, Optional, Union
import requests
from dataclasses import dataclass


@dataclass()
class Manga:
    id: str
    slug: str
    status: str
    type: str
    raiting: str

    title_ru: str
    title_en: Optional[str]
    title_ja: Optional[str]

    picture_url: str
    page_url: str


@dataclass()
class MainPageResponse:
    mangas: List[Manga]
    last_manga_chapters: List[Manga]
    manga_popular_by_period: List[Manga]


class SenkuroApi:

    def __init__(self):
        self.api_link = "https://api.senkuro.com/graphql"
        self.session = requests.Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0",
            "Accept": "application/graphql-response+json, application/graphql+json, application/json, text/event-stream, multipart/mixed",
            "Accept-Language": "ru",
            "Content-Type": "application/json",
            "Referer": "https://senkuro.com/",
            "Origin": "https://senkuro.com",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Connection": "keep-alive",
        }

    def get_main_page(self) -> Union[MainPageResponse, None]:
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

        def reformat_json_to_manga_object(json_data: Dict[str, Any]) -> Manga:
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

        json_response = self.session.post(self.api_link, json=json_data)
        if json_response.ok:
            json_data = json_response.json()["data"]

            return MainPageResponse(
                mangas=[
                    reformat_json_to_manga_object(node["node"])
                    for node in json_data["mangas"]["edges"]
                ],
                last_manga_chapters=[
                    reformat_json_to_manga_object(node["node"])
                    for node in json_data["lastMangaChapters"]["edges"]
                ],
                manga_popular_by_period=[
                    reformat_json_to_manga_object(node)
                    for node in json_data["mangaPopularByPeriod"]
                ],
            )
        else:
            return None
