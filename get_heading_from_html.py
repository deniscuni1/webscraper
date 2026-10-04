
def get_heading_from_html(html: str) -> (str, list[str]):
    h1 = html.split("<h1>")
    if len(h1)>1:
        h1=h1[1].split("</h1>")[0]
    paragraphs = html.split("<p>")[1:]
    paragraph_list = []
    for i in paragraphs:
        paragraph_list.append(i.split("</p>")[0])
    if len(h1)<=1:
        return paragraph_list
    elif paragraph_list == []:
        return h1
    else:
        return h1, paragraph_list


