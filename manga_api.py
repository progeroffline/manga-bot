import requests


class SenkuroApi:
    def __init__(self):
        self.api_link = 'https://api.senkuro.com/graphql'
        self.session = requests.Session()
        self.session.headers = {
            'accept': 'application/graphql-response+json, application/graphql+json, application/json, text/event-stream, multipart/mixed',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
            'content-type': 'application/json',
            'origin': 'https://senkuro.com',
            'priority': 'u=1, i',
            'referer': 'https://senkuro.com/',
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        }

    def get_main_page(self):
        json_data = {
            'extensions': {
                'persistedQuery': {
                    'sha256Hash': 'a4da0008c5103bfe9ea914dfd51091a6a67924b9d417806196a9e077168cf663',
                    'version': 1,
                },
            },
            'operationName': 'fetchMainPage',
            'variables': {
                'genre': {
                    'exclude': [
                        'hentai',
                    ],
                },
            },
        }

        return self.session.post(self.api_link, json=json_data).json()


manga_api = SenkuroApi()
print(manga_api.get_main_page())
