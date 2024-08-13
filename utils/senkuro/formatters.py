from typing import Any, Optional
from .types import CatalogResponse, HomeResponse, Manga, MangaResponse, SearchResponse
from .consts import home


def json_to_manga(data: dict[str, Any]) -> Manga:
    titles = {title["lang"]: title["content"] for title in data["titles"]}
    return Manga(
        id=data["id"],
        slug=data["slug"],
        status=data["status"],
        type=data["type"],
        raiting=data.get("rating"),
        title_ru=titles["RU"],
        title_en=titles.get("EN"),
        title_ja=titles.get("JA"),
        picture_url=data["cover"]["original"]["url"]
        if data["cover"] is not None
        else None,
        page_url=home.format(slug=data["slug"]),
    )


def json_to_home_response(data: dict[str, Any]) -> HomeResponse:
    return HomeResponse(
        mangas=[json_to_manga(node["node"]) for node in data["mangas"]["edges"]],
        last_manga_chapters=[
            json_to_manga(node["node"]) for node in data["lastMangaChapters"]["edges"]
        ],
        manga_popular_by_period=[
            json_to_manga(node) for node in data["mangaPopularByPeriod"]
        ],
    )


def json_to_catalog_reponse(
    edges: list[dict[str, Any]], cursor: Optional[str]
) -> CatalogResponse:
    return CatalogResponse(
        cursor=cursor,
        mangas=[json_to_manga(node["node"]) for node in edges],
    )


def json_to_search_reponse(edges: list[dict[str, Any]]) -> SearchResponse:
    return SearchResponse(
        mangas=[json_to_manga(node["node"]) for node in edges],
    )


def json_to_manga_response(manga: dict[str, Any]) -> MangaResponse:
    return MangaResponse(manga=json_to_manga(manga))
