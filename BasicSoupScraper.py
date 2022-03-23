from bs4 import BeautifulSoup
import requests
import re

# creates a User Agent header simulating Mozilla browser. Some websites will still be able
# to detect 'automation' specifically websites that use perimeterx.
# Doing some research I believe I can bypass this using Selenium in order to simulate user activity.
headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

# extracts html code from website url
def getHTMLdoc(url):
    # request HTML doc from url
    response = requests.get(url)
    # JSON format
    return response.text


target_url = "https://www.dtlr.com/products/air-jordan-retro-6-low-cny-dh6928-073"

html_dest = getHTMLdoc(target_url)

caldo = BeautifulSoup(html_dest, 'html.parser')

# find all the anchor tags with "href"
# attribute starting with "https://"
for link in caldo.find_all('a', attrs={'href': re.compile("^https://")}):
    # display the actual urls
    print(link.get('href'))
