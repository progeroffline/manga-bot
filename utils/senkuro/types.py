from dataclasses import dataclass
from typing import Optional, List


@dataclass()
class Manga:
    id: str
    slug: str
    status: str
    type: str
    raiting: str | None

    title_ru: str
    title_en: Optional[str]
    title_ja: Optional[str]

    picture_url: str | None
    page_url: str


@dataclass()
class HomeResponse:
    mangas: List[Manga]
    last_manga_chapters: List[Manga]
    manga_popular_by_period: List[Manga]


@dataclass()
class CatalogResponse:
    mangas: List[Manga]
    cursor: str | None


@dataclass()
class SearchResponse:
    mangas: List[Manga]


@dataclass()
class MangaResponse:
    manga: Manga
