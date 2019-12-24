# Meme Tracker

## Description
Meme tracker is a web scraper and image grouper for internet memes.

It scrapes a given URL for images and downloads them. Then, it groups similar
images together and displays those image groups as clusters of images in a 
browser.

## Installation

1. Install [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/) for your user.
    ```console
    user@pc:~$ pip install --user pipenv
    ```

2. Clone this repo.
    ```console
    user@pc:~/projects$ git clone git@github.com:Obleskar/meme_tracker.git
    ```

3. Install dependencies.
    ```console
    user@pc:~/projects/meme_tracker$ pipenv install
    ```

## Usage

1. Add the URLs that you want to scrape to the 
[YAML](https://pyyaml.org/wiki/PyYAMLDocumentation) config file.
    ```console
    user@pc:~/projects/meme_tracker$ vim spider_config.yaml
    ```
    ```yaml
    urls: [http://boards.4channel.org/v/] 
    ```

2. Run the image scraper.
    ```console
    user@pc:~/projects/meme_tracker$ scrapy crawl 4chan_images
    ```

3. Launch a local webserver to host the downloaded images.
    ```console
    user@pc:~/projects/meme_tracker$ python3 show_images.py
    ```

4. Navigate to http://localhost:5000 in a web browser to view the images in 
a grid.

## Motivation
To provide an easy way for researchers to view daily summaries of images on the
internet.
