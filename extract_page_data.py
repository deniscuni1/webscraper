from crawl import normalize_url
from typing import TypedDict
from get_heading_from_html import get_heading_from_html
from get_images_from_html import get_images_from_html
from get_url_from_html import get_urls_from_html
from urllib.parse import urljoin
class ExtractedData(TypedDict):
    url: str
    heading: str
    first_paragraph: str
    outgoing_links: list[str]
    image_urls: list[str]

def extract_page_data(html: str, page_url: str) -> ExtractedData:
    url = normalize_url(page_url)
    heading, paragraphs = get_heading_from_html(html)
    first_paragraph = paragraphs
    outgoing_links = get_urls_from_html(html)
    for i in range(len(outgoing_links)):
        outgoing_links[i] = urljoin(page_url, outgoing_links[i])
    image_urls =  get_images_from_html(html, url)
    data : ExtractedData = {"url": url, "heading": heading, "first_paragraph": first_paragraph, "outgoing_links": outgoing_links, "image_urls": image_urls}
    return data