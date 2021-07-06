import click
from getHtmlContent import getHtmlContent
from parseHtmlContent import parseHtmlContent

@click.command()
@click.option("-k", "--keyword", default="meow")
def main(keyword):
    if keyword == "八卦":
        htmlContent = getHtmlContent("https://www.pttweb.cc/hot/all/today")
        posts = parseHtmlContent(htmlContent)
        for post in posts:
            print(post)
    return 0


if __name__ == "__main__":
    main()
