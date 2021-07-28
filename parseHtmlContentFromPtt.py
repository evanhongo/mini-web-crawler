from pyquery import PyQuery as pq

def parseHtmlContentFromPtt(htmlContent): 
    try:   
        posts = pq(htmlContent).find("a.e7-article-default").map(lambda i, elem: f'{pq(pq(elem).children()[0]).children().children().text()}\nhttps://www.pttweb.cc{pq(elem).attr("href")}')
        posts = posts.filter(lambda i, elem : elem.index("\n") != 0)
    except Exception as err:
        print(err)
        posts = ["There is something error"]
    return posts
