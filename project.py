import os, requests, bs4

# Make image download location
def cd(path):
    os.chdir(os.path.expanduser(path))
os.makedirs('wikipedia', exist_ok=True)

url = requests.get('https://en.wikipedia.org/wiki/Special:Random')
# download page
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)
# find/download the image
images = soup.find('a',{'class':'image'})
# Retrieve image location
imgSrc = [soup.find('img').get('src')]
# Make the image location into a URL
imgUrl = 'http:' + imgSrc[0]
# save image to ./wikipedia
imageFile = open(os.path.join('wikipedia', os.path.basename(imgUrl)), 'wb')
for chunk in res.iter_content(100000):
    imageFile.write(chunk)
imageFile.close()
