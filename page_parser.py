from bs4 import BeautifulSoup
from pathlib import Path


def get_files():
    return (item for item in Path('.').iterdir() if item.suffix == '.html')


def get_image_urls(file):
    with open(file) as infile:
        soup = BeautifulSoup(infile, features='lxml')
        reply_link_containers = soup.findAll('span', {'class': 'summary desktop'})
        return [str(container.a.attrs['href']) for container in reply_link_containers]


files = [file for file in get_files()]
urls = get_image_urls(files[0])
print('\n'.join(urls))
