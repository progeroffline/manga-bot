from dataclasses import dataclass
from typing import List, Optional


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
class NewManga:
    id: int
    slug: str
    description: str
    type: str
    raiting: float
    likes: int

    title_ru: str
    title_en: Optional[str]

    picture_url: str
    page_url: str


@dataclass()
class MainPageResponse:
    mangas: List[Manga]
    last_manga_chapters: List[Manga]
    manga_popular_by_period: List[Manga]


@dataclass()
class NewMangaMainPageResonse:
    items: List[NewManga]


@dataclass()
class CatalogResponse:
    mangas: List[Manga]
