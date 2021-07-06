from pyquery import PyQuery as pq

def parseHtmlContent(htmlContent):    
    posts = pq(htmlContent).find(
        "a.e7-article-default").map(lambda i, elem: f'{pq(pq(pq(elem).children()[0]).children()[0]).text()}\nhttps://www.pttweb.cc{pq(elem).attr("href")}')
    return posts
