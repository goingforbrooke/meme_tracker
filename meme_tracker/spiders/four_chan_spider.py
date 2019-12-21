from bs4 import BeautifulSoup
from datetime import datetime
from pathlib import Path
import scrapy
from yaml import safe_load


class FourChanSpider(scrapy.Spider):
    """A webcrawler for 4chan boards."""
    name = '4chan_images'

    def start_requests(self):
        """Yield request objects for the given URLs."""
        start_urls = safe_load(Path('spider_config.yaml').read_text())['urls']
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """Get thread links or image links from a response's HTML content."""
        soup = BeautifulSoup(response.body, features='lxml')
        if 'thread' in response.url:
            self.log(f'Parsing image links for board: {response.url}.')
        elif response.url.endswith('/'):
            self.log(f'Parsing thread links for thread: {response.url}.')
            reply_link_containers = soup.findAll('span', {'class': 'summary desktop'})
            thread_ids = [str(container.a.attrs['href']) for container in reply_link_containers]
            if thread_ids:
                for thread_id in thread_ids:
                    thread_url = response.urljoin(thread_id)
                    self.log(f'Thread URL: {thread_url}.')
                    #yield scrapy.Request(thread_url, callback=self.parse)

    def response_to_file(self, response):
        """Save the HTML content of the given Requests response to a file."""
        thread_id = response.url.split('/')[-2]
        download_time = f'{datetime.now().isoformat(timespec="seconds")}'
        filename = f'{download_time}-{thread_id}.html'
        with open(filename, 'wb') as outfile:
            outfile.write(response.body)
        self.log(f'Saved content of {response.url} to {filename}.')

    def get_local_files(self):
        """Return the names of all HTML files in the working directory."""
        return (item for item in Path('.').iterdir() if item.suffix == '.html')
