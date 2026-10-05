from extract_page_data import ExtractedData, extract_page_data
from crawl import normalize_url
from get_html import get_html
def domain(url:str) -> str:
    no_protocol = url.split("//")[1]
    semi_normalized = no_protocol.split("/")[0]
    return semi_normalized
def crawl(base_url, current_url = None, page_data = None):
    html = ""
    if page_data == None:
        page_data = {}
    if current_url == None:
        current_url = base_url
    html = get_html(current_url)
    data = extract_page_data(html, current_url)
    page_data[normalize_url(current_url)] = data
    print(data["url"], data["heading"], data["first_paragraph"], data["image_urls"])
    for i in data["outgoing_links"]:
        if normalize_url(i) in page_data:
            continue
        elif domain(i) != domain(base_url):
            continue
        else:
            crawl_page(base_url, i, page_data)
    return 