#import requests
from requests.api import request


import requests

def getHtmlContent(url):
    res = requests.get(url)
    htmlContent = res.text
    return htmlContent