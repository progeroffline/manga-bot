import random
from manga_base.api import SenkuroApi

service = SenkuroApi()
page_0 = service.get_catalog()
# page_1 = service.get_catalog(3)

# print(page_0, page_1)
