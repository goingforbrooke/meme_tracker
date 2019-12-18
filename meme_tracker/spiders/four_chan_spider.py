from datetime import datetime
from pathlib import Path
import scrapy
from yaml import safe_load


class FourChanSpider(scrapy.Spider):
    name = '4chan_images'
    start_urls = safe_load(Path('spider_config.yaml').read_text())['urls']

    def parse(self, response):
        thread_id = response.url.split('/')[-2]
        download_time = f'{datetime.now().isoformat(timespec="seconds")}'
        filename = f'{download_time}-{thread_id}.html'
        with open(filename, 'wb') as outfile:
            outfile.write(response.body)
        self.log(f'Saved content of {response.url} to {filename}.')
