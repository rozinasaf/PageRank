import requests
import lxml.html
from collections import defaultdict
import random

prefix = "http://en.wikipedia.org"
graph = defaultdict(list)

#@pre: type = "REGULAR" or type = "LAST"
def crawl(url, graph, type):
    r = requests.get(prefix + url)
    doc = lxml.html.fromstring(r.content)
    urls = []
    condition = False
    i = 0
    for t in doc.xpath("//a[contains(@href, '/wiki/') and not(contains(@href, ':'))]/@href"):
        if type == "REGULAR":
            condition = t not in urls and t != url
        else:
            condition = t in graph and t not in urls and t != url
        if condition:
            graph[url].append(t)
            urls.append(t)
            i += 1
        if i >= 10:
            break
    if i == 0:
        graph[url].append(url)
        urls.append(url)
    return urls

def crawler(url):
    urls1 = crawl(url, graph, "REGULAR")
    urls2 = []
    urls3 = []
    for u1 in urls1:
        if u1 not in graph:
            urls2 += crawl(u1, graph, "REGULAR")

    for u2 in urls2:
        if u2 not in graph:
            urls3 += crawl(u2, graph, "REGULAR")
    
    for u3 in urls3:
        if u3 not in graph:
            crawl(u3, graph, "LAST")
    
    for node in graph:
        print(node, " = {", ", ".join(graph[node]), "}")
    
