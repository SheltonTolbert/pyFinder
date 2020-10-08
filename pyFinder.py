from bs4 import BeautifulSoup as bs
import requests
import random


urls = []


def find_links(url):
    global urls

    page = requests.get(url)
    soup = bs(page.text, 'html.parser')

    for link in soup.findAll('a', {'class': 'package-snippet'}):
        try:
            href = str(link['href'])
            urls.append('https://pypi.org' + href)
        except KeyError:
            pass


def rand_pip():
    url = 'https://pypi.org/search/?q=&o=-zscore&c=Development+Status+%3A%3A+5+-+Production%2FStable'
    find_links(url)

    for i in range(2, 10):
        url = 'https://pypi.org/search/?c=Development+Status+%3A%3A+5+-+Production%2FStable&o=-zscore&q=&page=' + \
            str(i)

        find_links(url)

    index = random.randint(0, len(urls))

    return (urls[index])


if __name__ == '__main__':
    rand_pip()
