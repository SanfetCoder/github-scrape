from urllib.request import urlopen

def get_github_profile(url):
    html_bytes = urlopen(url).read()
    html = html_bytes.decode('utf-8')
    return html