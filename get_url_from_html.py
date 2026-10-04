from bs4 import Tag
from bs4 import BeautifulSoup 
def get_urls_from_html(html: str) -> list[str]:
    html_soup = BeautifulSoup(html, "html.parser")
    urls = html_soup.find_all("a")
    normalized = []
    for i in urls:
        href=i.get("href")
        normalized.append(href)
    return normalized