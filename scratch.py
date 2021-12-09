import requests
from bs4 import BeautifulSoup

youtube_trending_url =   'https://www.youtube.com/feed/trending'
 # Does not execut javascript
response = requests.get(youtube_trending_url)
print(response.status_code)

with open('trending.html', 'w') as f:
  f.write(response.text)

doc = BeautifulSoup(response.text, 'html.parser')
print(doc.title)
# Find all video divs
videos_div = doc.find_all('div',class_='ytd-video-renderer')
print(len(videos_div))