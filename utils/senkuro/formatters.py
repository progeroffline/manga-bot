from typing import Any
from .types import MainPageResponse, Manga
from .consts import home


def json_to_manga(data: dict[str, Any]) -> Manga:
    titles = {title["lang"]: title["content"] for title in data["titles"]}
    return Manga(
        id=data["id"],
        slug=data["slug"],
        status=data["status"],
        type=data["type"],
        raiting=data["rating"],
        title_ru=titles["RU"],
        title_en=titles.get("EN"),
        title_ja=titles.get("JA"),
        picture_url=data["cover"]["original"]["url"],
        page_url=home.format(slug=data["slug"]),
    )


def json_to_main_page_reponse(data: dict[str, Any]) -> MainPageResponse:
    return MainPageResponse(
        mangas=[json_to_manga(node["node"]) for node in data["mangas"]["edges"]],
        last_manga_chapters=[
            json_to_manga(node["node"]) for node in data["lastMangaChapters"]["edges"]
        ],
        manga_popular_by_period=[
            json_to_manga(node) for node in data["mangaPopularByPeriod"]
        ],
    )
