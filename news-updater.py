from newsapi import NewsApiClient
import os
from dotenv import load_dotenv
load_dotenv() 

newsapi = NewsApiClient(api_key=os.getenv('newapiFreekeyonRegistration'))

top_headlines = newsapi.get_top_headlines(q='india',
                                          category='business',
                                          language='en',)

dt = top_headlines['articles']
for x,y in enumerate(dt):
    print(f'{x} {y["description"]}')