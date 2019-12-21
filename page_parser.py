from bs4 import BeautifulSoup
from pathlib import Path
from yaml import safe_load


def get_files():
    return (item for item in Path('.').iterdir() if item.suffix == '.html')


def get_image_urls(file):
    with open(file) as infile:
        soup = BeautifulSoup(infile, features='lxml')
        reply_link_containers = soup.findAll('span', {'class': 'summary desktop'})
        thread_urls = [str(container.a.attrs['href']) for container in reply_link_containers]

        base_url = safe_load(Path('meme_tracker', 'spider_config.yaml').read_text())['urls']
        return [base_url[0] + thread_url for thread_url in thread_urls]


files = [file for file in get_files()]
urls = get_image_urls(files[0])
print('\n'.join(urls))
get_image_urls(files[0])
