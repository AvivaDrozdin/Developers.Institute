from bs4 import BeautifulSoup as bs
import urllib.request as ureq

# Website url
freblogg_url = 'http://freblogg.com'

# Fetch the website
website = ureq.urlopen(freblogg_url).read()

# Parse the html of the site with soup
soup = bs(website, "html.parser")

# Get all the headers
headers = soup.find_all('h2', {'class':'post-title entry-title'})

# Extract title text from each header
titles = list(map(lambda h: h.text.strip(), headers))

# Extract the url and the title of each article
titles_and_links = dict(map(lambda h: (h.text.strip(), h.find('a')['href']), headers))

print(titles_and_links)