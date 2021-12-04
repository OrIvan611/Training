from bs4 import BeautifulSoup
import requests
import networkx as nx
import matplotlib.pyplot as plt

from consts import *


def get_new_url(url):
    """
    Gets the next valid url.
    A valid url is a url to a different, existing Wikipedia page.
    """
    soup = BeautifulSoup(requests.get(url).text, HTML_PARSER)
    for paragraph in soup.find_all(PARAGRAPH_SIGN):
        text = paragraph.text
        links = paragraph.find_all(LINK_SIGN)
        if not links or text == '\n':
            # The paragraph has no content. Try next one.
            continue

        # The paragraph has links and text.
        for link in links:
            if link.string and not link_in_parenthesize(link, text=text):
                # The link has text and it is not in parenthesize.
                new_url = WIKIPEDIA_URL_START + link.get('href').split('/')[-1]
                if is_wiki_url(new_url) and not is_link_to_current_page(url, new_url) and page_exists(new_url):
                    # new_url is a url to a different, existing Wikipedia page.
                    return new_url


def is_link_to_current_page(url, new_url):
    """
    check if the new url has the same start as the one before.
    """
    return new_url.startswith(url)


def link_in_parenthesize(link, text):
    """
    This function checks if the link in parenthesize. (any type).
    """
    if '[' in link.string:
        # This is a reference url. e.g. [1].
        return True
    for x in range(len(text)):
        if text[text.find(link.string) - x] == ')':
            # A parenthesize was closed before our link, so this link is not in one.
            return False
        elif text[text.find(link.string) - x] == '(':
            # The link is in a parenthesize.
            return True
    # We got to the end of the sentence, so the link is not in a parenthesize.


def check_if_title_match(url):
    """
    Checking if the url is the one we are looking for.
    """
    response = requests.get(url=url)
    soup = BeautifulSoup(response.content, HTML_PARSER)
    title = soup.find(id=HTML_TITLE)

    return title.string == TARGET_VALUE


def is_wiki_url(url):
    """
    Checking if the url is a Wikipedia url.
    """
    if url and url.startswith(WIKIPEDIA_URL_START):
        return True


def page_exists(url):
    """
    Checking if the url is an existing page online.
    """
    response = requests.get(url)
    return response.status_code == OK_STATUS


def plot_graph(urls):
    """
    Plots the path of the urls we visited.
    """
    edges = []
    for i in range(len(urls)-1):
        edges.append((urls[i].split('/')[-1], urls[i + 1].split('/')[-1]))

    G = nx.Graph()
    G.add_edges_from(edges)
    nx.draw(G, cmap=plt.get_cmap('jet'), arrows=True, with_labels=True, node_size=NODE_SIZE)
    plt.show()

