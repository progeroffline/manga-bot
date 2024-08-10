from dataclasses import dataclass
from typing import Optional


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
class NewMangaMainPageResonse:
    items: list[NewManga]
