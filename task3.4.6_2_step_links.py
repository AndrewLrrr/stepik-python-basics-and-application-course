import requests
import re


def get_domain(url):
    matches = re.search(r'(http[s]?://[^\&\?\s\/]+)', url)
    return matches.group(1)


# def get_url(url):
#     matches = re.search(r'(http[s]?://[^\&\?\s]+)(?:\?|\&)?', url)
#     return matches.group(1)
#
#
# def parse_url_query(url):
#     matches = re.findall(r'(?:\&|\?)(.*?)\=([^\&\?\s]+)', url)
#     return dict(matches)


def parse_links(text, domain):
    links = []
    matches = re.findall(r'href=[\'\"](.*?)[\'\"]', text)
    for match in matches:
        if 'http' not in match:
            match = domain + '/' + match
        links.append(match.strip().lower())
    return links


def do_request(link):
    response = requests.get(link)
    return response


def link_search_spider(links, searching_link, depth_level=2, search_level=2):
    success = False

    def recursive_link_spider(current_links, current_level):
        nonlocal success
        if current_level <= depth_level:
            for current_link in current_links:
                response = do_request(current_link)
                response_links = parse_links(response.text, get_domain(current_link))
                if searching_link.lower() not in response_links:
                    recursive_link_spider(response_links, current_level + 1)
                else:
                    if search_level != current_level:
                        recursive_link_spider(response_links, current_level + 1)
                    else:
                        success = True

    recursive_link_spider(links, 1)
    return success


link1 = input().strip()
link2 = input().strip()

if link_search_spider([link1], link2):
    print('Yes')
else:
    print('No')
