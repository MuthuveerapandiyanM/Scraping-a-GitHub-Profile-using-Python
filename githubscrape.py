import requests
from bs4 import BeautifulSoup as bs
gitup_profile = "https://github.com/MuthuveerapandiyanM"
req = requests.get(gitup_profile)
scraper = bs(req.content,"html.parser")
profile_picture = scraper.find('img',{"alt": "Avatar"})["src"]
print(profile_picture)
