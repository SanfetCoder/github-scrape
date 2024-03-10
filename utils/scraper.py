from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_github_profile(url = "https://github.com/SanfetCoder?tab=repositories"):
    html_bytes = urlopen(url).read()
    html = html_bytes.decode('utf-8')
    # create a soup with Beautifulsoup using read html
    soup = BeautifulSoup(html, 'html.parser')
    # get profile image
    images = soup.find_all('img')
    for image in images:
        if 'avatar' in image['class']:
            profile_image = image['src']
    print(profile_image)    
    return html

get_github_profile()