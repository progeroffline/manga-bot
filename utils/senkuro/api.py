from typing import Any, Iterator, Literal, Optional
import httpx
from .types import CatalogResponse, HomeResponse, MangaResponse, SearchResponse

from . import formatters, consts, queries_data


class SenkuroApi:
    def __init__(self):
        self.client = httpx.Client(headers=consts.headers)

    def get_main_page(self) -> HomeResponse | None:
        json_data = queries_data.home.copy()

        response = self.client.post(
            consts.api_graphql,
            json=json_data,
        )
        if response.status_code == 200:
            json_data = response.json()["data"]
            return formatters.json_to_home_response(json_data)
        return None

    def catalog(self, cursor: Optional[str] = None) -> Iterator[CatalogResponse]:
        json_data = queries_data.catalog.copy()
        json_data["variables"]["genre"]["include"] = ["yaoi"]

        has_next_page = True
        response = None
        while has_next_page:
            response = self.client.post(consts.api_graphql, json=json_data).json()
            has_next_page = response["data"]["mangas"]["pageInfo"]["hasNextPage"]
            cursor = response["data"]["mangas"]["pageInfo"]["endCursor"]
            json_data["variables"]["after"] = cursor

            yield formatters.json_to_catalog_reponse(
                response["data"]["mangas"]["edges"], cursor
            )

    def search(self, query: Optional[str] = None) -> SearchResponse:
        json_data = queries_data.search.copy()
        json_data["variables"]["query"] = query

        response = self.client.post(consts.api_graphql, json=json_data)
        response_json = response.json()
        return formatters.json_to_search_reponse(
            response_json["data"]["search"]["edges"]
        )

    def manga(self, slug: str) -> MangaResponse:
        json_data = queries_data.manga.copy()
        json_data["variables"]["slug"] = slug

        response = self.client.post(consts.api_graphql, json=json_data).json()
        print(response)
        return formatters.json_to_manga_response(response["data"]["manga"])
