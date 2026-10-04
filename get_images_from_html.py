from bs4 import BeautifulSoup, Tag

def get_images_from_html(html: str, base_url: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    images = soup.find_all("img")
    links = []
    for i in images:
        source = i.get("src")
        if source != "":
            abs_url = base_url + source
            links.append(abs_url)
    return links
    
