import requests
import bs4

baseurl = "https://en.wikipedia.org/wiki/Deep_learning"
page = requests.get(baseurl)
soup = bs4.BeautifulSoup(page.text, 'lxml')
# alternative to the previous line
# soup = bs4.BeautifulSoup(page.text, "html.parser")

# a. Print out the title of the page
title = soup.title.string
# alternative to the previous line
# title = soup.select('title')[0].getText()
print(f"Title: {title}")

# b. Find all the links in the page (‘a’ tag)
mylist = soup.select('a')
# alternative to the previous line
# mylist = soup.findAll('a')
# print(mylist)
print("\n".join(str(mylist).replace("[","").replace("]","").split(',')))  # to print each in a new line

# c. Iterate over each tag(above) then return the link using attribute "href" using get
my_href_list = []
for item in mylist:
    my_href_list.append(item.get('href'))

# d. Save all the links in the file
with open("result.out", "w") as outfile:
    for counter,link in enumerate(my_href_list):
        outfile.write(f"{counter+1}  {link}\n")
