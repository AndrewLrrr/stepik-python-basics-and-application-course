import re
import requests


def request_html_document(url):
    response = requests.get(url)
    return response.text


def parse_domains_from_html(html):
    result = set()
    regex = r'<a.*?href\s*?=\s*?[\'\"]?(?:(?:ftp|http|https):\/\/)?([\w]+((?:\.|\-)[^\/\s\>\"\'\<\&\?]+)?\2*\.[^\/\s\>\"\'\<\:\&\?]+)[\'\"]?.*?>'
    matches = re.findall(regex, html, re.IGNORECASE)
    for match in matches:
        result.add(match[0])
    return result


link = input().strip()

domains = parse_domains_from_html(request_html_document(link))

for idx, domain in enumerate(sorted(domains)):
    print(domain.strip())
