from typing import Any, Dict, Union
import requests
from .cls_types import Manga, NewManga, MainPageResponse, NewMangaMainPageResonse, CatalogResponse


class SenkuroApi:

    def __init__(self):
        self.api_link = "https://api.senkuro.com/graphql"
        self.session = requests.Session()
        self.session.headers = {
            'accept': 'application/graphql-response+json, application/graphql+json, application/json, text/event-stream, multipart/mixed',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'content-type': 'application/json',
            'origin': 'https://senkuro.com',
            'priority': 'u=1, i',
            'referer': 'https://senkuro.com/',
            'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        }

    @staticmethod
    def reformat_json_to_manga_object(json_data: Dict[str, Any]) -> Manga:
        titles = {title["lang"]: title["content"]
                  for title in json_data["titles"]}
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
            page_url=f"https://senkuro.com/manga/{
                json_data['slug']}/chapters",
        )

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

        json_response = self.session.post(self.api_link, json=json_data)
        if json_response.ok:
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
        print('Запуcтил метод get_catalog')
        json_data = {
            'extensions': {
                'persistedQuery': {
                    'sha256Hash': '6547bf3c404812150e9e0429adba781f36a0ef17b12d4cb31d8caf1d8bac91e1',
                    'version': 1,
                },
            },
            'operationName': 'fetchMangas',
            'variables': {
                'after': None,
                'bookmark': {
                    'exclude': [],
                    'include': [],
                },
                'chapters': {},
                'format': {
                    'exclude': [],
                    'include': [],
                },
                'genre': {
                    'exclude': [
                        'hentai',
                    ],
                    'include': [],
                },
                'orderDirection': 'DESC',
                'orderField': 'CREATED_AT',
                'originCountry': {
                    'exclude': [],
                    'include': [],
                },
                'rating': {
                    'exclude': [],
                    'include': [],
                },
                'search': None,
                'source': {
                    'exclude': [],
                    'include': [],
                },
                'status': {
                    'exclude': [],
                    'include': [],
                },
                'tag': {
                    'exclude': [],
                    'include': [],
                },
                'translitionStatus': {
                    'exclude': [],
                    'include': [],
                },
                'type': {
                    'exclude': [],
                    'include': [],
                },
            },
        }

        print('Create json_data var')

        cursor = None
        print('Create cursor var')
        json_response = None
        print('Create json_response')
        if page > 0:
            print("Pereshlo li uslovie")
            for _ in range(page):
                json_data['variables']['after'] = cursor
                print('Prisvoeniye cursoru')
                json_response = self.session.post(
                    self.api_link, json=json_data)
                print('json_responce vipolnilsya')
                cursor = json_response.json(
                )['data']['mangas']['pageInfo']['endCursor']
                print("Put` cursora")

        if json_response is None:
            print("Json_response is None?")
            json_data = json_response = self.session.post(
                self.api_link, json=json_data
            ).json()['data']
            print("Poluchenie json_none")
        else:
            json_data = json_response.json()['data']
            print("Json_response is not none?")
        print("return result")
        return CatalogResponse(
            mangas=[
                self.reformat_json_to_manga_object(node["node"])
                for node in json_data["mangas"]["edges"]
            ]
        )


class NewMangaApi:

    def __init__(self):
        self.api_link = "https://api.newmanga.org/v2/projects/popular"
        self.session = requests.Session()
        self.session.headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6",
            "origin": "https://newmanga.org",
            "priority": "u=1, i",
            "referer": "https://newmanga.org/",
            "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        }

    def get_main_page(self) -> Union[NewMangaMainPageResonse, None]:
        params = {"size": "30"}

        def reformat_json_to_manga_object(params: Dict[str, Any]) -> NewManga:
            return NewManga(
                id=params["id"],
                slug=params["slug"],
                description=params["description"],
                type=params["type"],
                raiting=params["rating"],
                likes=params["hearts"],
                title_ru=params["title"]["ru"],
                title_en=params["title"]["en"],
                picture_url=f"https://img.newmanga.org/ProjectLarge/webp/{
                    params['image']['name']}",
                page_url=f"https://newmanga.org/p/{params['slug']}",
            )

        json_response = self.session.get(self.api_link, json=params)
        if json_response.ok:
            params = json_response.json()

            return NewMangaMainPageResonse(
                items=[
                    reformat_json_to_manga_object(item)
                    for item in params["items"]
                ],
            )
        else:
            return None
