#%%

import webbrowser as web
import requests

def search_google(text: str) -> 'urllink':

    with requests.session() as c:

        url = 'https://www.google.com/search'

        query = {'q': text}

        urllink = requests.get(url, params=query)

        return urllink.url


def google(text: str) -> "search results":

    web.open(search_google(text))


def is_link(text: str):

    try:
        
        if requests.get(f'http://{text}').status_code == 200:

            web.open(f'http://{text}')

    except (requests.exceptions.ConnectionError, requests.exceptions.InvalidURL):

        print(f'Connection Refused for http://{text}')





# %%
