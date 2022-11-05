import requests
import bs4
from bs4 import BeautifulSoup as bs

github_user = input("Input Github User: ")

url = 'https://github.com/' + github_user

# Webscrapping will fetch HTML content of page using Beautiful soup API
r = requests.get(url)

soup = bs(r.content,'html.parser')

print(soup)

profile_image = soup.find('img',{'alt':'Avatar'})['src']

print(profile_image)

