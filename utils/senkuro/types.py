from dataclasses import dataclass
from typing import Optional, List


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
