from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_github_profile(url = "https://github.com/SanfetCoder?tab=repositories"):
    html_bytes = urlopen(url).read()
    html = html_bytes.decode('utf-8')
    # create a soup with Beautifulsoup using read html
    soup = BeautifulSoup(html, 'html.parser')
    # get profile id
    profile_id = soup.find_all("span", {"class" : "p-nickname"})[0].text.strip().split(".")[0]
    # get profile name
    profile_name = soup.find_all("span", {"class" : "p-name"})[0].text
    # get profile introduction
    profile_introduction = ""
    profileTargetDivs = soup.find_all("div", {"class" : "js-user-profile-bio"})
    if (len(profileTargetDivs) > 0):
        profileTargetDivsChildrens = profileTargetDivs[0].findChildren(["div"])
        if len(profileTargetDivsChildrens) > 0:
            profile_introduction = profileTargetDivsChildrens[0].text
    # get profile image
    images = soup.find_all('img')
    for image in images:
        if 'avatar' in image['class']:
            profile_image = image['src']
    # get a list of repositories
    repos = []
    links = soup.select('a[itemprop="name codeRepository"]')
    for link in links:
        repo_name = link.text.replace("\n", "").strip()
        repos.append(repo_name)
    return {
        "profile_id" : profile_id,
        "profile_name" : profile_name,
        "profile_introduction" : profile_introduction,
        "profile_image" : profile_image,
        "repos" : repos
    }
