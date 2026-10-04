
def normalize_url(url: str) -> str:
    no_protocol = url.split("//")[1]
    semi_normalized = no_protocol.split("/")
    normalized_url = semi_normalized[0]
    for i in semi_normalized[1:]:
        if i == "":
            continue
        normalized_url += "/" + i
    return normalized_url
