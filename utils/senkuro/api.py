import httpx
from .types import MainPageResponse

from . import formatters, consts, queries_data


class SenkuroApi:
    def __init__(self):
        self.client = httpx.Client(headers=consts.headers)

    def get_main_page(self) -> MainPageResponse | None:
        json_data = queries_data.home.copy()

        json_response = self.client.post(
            consts.api_graphql,
            json=json_data,
        )
        if json_response.status_code == 200:
            json_data = json_response.json()["data"]
            return formatters.json_to_main_page_reponse(json_data)
        else:
            return None

    def get_catalog(self, page: int = 0) -> MainPageResponse | None:
        json_data = queries_data.catalog.copy()

        cursor = None
        json_response = None
        if page > 0:
            for _ in range(page):
                json_data["variables"]["after"] = cursor
                json_response = self.client.post(consts.api_graphql, json=json_data)
                cursor = json_response.json()["data"]["mangas"]["pageInfo"]["endCursor"]

        if json_response is None:
            json_data = json_response = self.client.post(
                consts.api_graphql,
                json=json_data,
            ).json()
        else:
            json_data = json_response.json()

        return formatters.json_to_main_page_reponse(json_data)
