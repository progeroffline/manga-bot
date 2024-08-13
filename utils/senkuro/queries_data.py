home = {
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

catalog = {
    "extensions": {
        "persistedQuery": {
            "sha256Hash": "6547bf3c404812150e9e0429adba781f36a0ef17b12d4cb31d8caf1d8bac91e1",
            "version": 1,
        },
    },
    "operationName": "fetchMangas",
    "variables": {
        "after": None,
        "bookmark": {
            "exclude": [],
            "include": [],
        },
        "chapters": {},
        "format": {
            "exclude": [],
            "include": [],
        },
        "genre": {
            "exclude": [
                "hentai",
            ],
            "include": [],
        },
        "orderDirection": "DESC",
        "orderField": "CREATED_AT",
        "originCountry": {
            "exclude": [],
            "include": [],
        },
        "rating": {
            "exclude": [],
            "include": [],
        },
        "search": None,
        "source": {
            "exclude": [],
            "include": [],
        },
        "status": {
            "exclude": [],
            "include": [],
        },
        "tag": {
            "exclude": [],
            "include": [],
        },
        "translitionStatus": {
            "exclude": [],
            "include": [],
        },
        "type": {
            "exclude": [],
            "include": [],
        },
    },
}

search = {
    "extensions": {
        "persistedQuery": {
            "sha256Hash": "1ab1c7cb8e180824ce68dddf5269f74b431de99bf5c6c00e7228ca313fc5f2c5",
            "version": 1,
        }
    },
    "operationName": "search",
    "variables": {
        "query": None,
        "type": "MANGA",
    },
}

manga = {
    "extensions": {
        "persistedQuery": {
            "sha256Hash": "3d72e774b12b6760d58f729c468ce2c5e8839c8e47e90b73bd70dc2b1b7905d6",
            "version": 1,
        },
    },
    "operationName": "fetchManga",
    "variables": {
        "slug": "rebirth-of-the-ultimate-master",
    },
}
