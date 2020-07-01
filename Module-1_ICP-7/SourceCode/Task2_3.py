import requests
import bs4

# set the url and create the beautifulSoup obj
baseurl = "https://en.wikipedia.org/wiki/Google"
page = requests.get(baseurl)
soup = bs4.BeautifulSoup(page.text, 'lxml')

# find the body
body = soup.find(id='mw-content-text')

# save in a file
with open('input.txt', 'w', encoding='utf-8') as fout:
    fout.write(str(body.text))

