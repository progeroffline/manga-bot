import requests


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

    def get_main_page(self):
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

        return self.session.post(self.api_link, json=json_data).json()
