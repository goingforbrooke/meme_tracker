# Meme Tracker

:frog: :frog: :frog: :frog: :frog: :frog: :frog: :frog: :frog: :frog:
:frog: :frog: :frog: :frog: :frog: :frog: :frog: :frog: :frog: :frog:
:frog: :frog: :frog: :frog: :frog: :frog: :frog: :frog:

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

2. Create a virtual environment for this project and activate it.
    ```console
    user@pc:~$ pip shell
    ```

3. Clone this repo.
    ```console
    user@pc:~/projects$ git clone git@github.com:Obleskar/meme_tracker.git
    ```

4. Install dependencies.
    ```console
    user@pc:~/projects/meme_tracker$ pipenv install
    ```

## Usage

1. Create a [YAML](https://pyyaml.org/wiki/PyYAMLDocumentation) file called 
`spider_config.yaml`, place it in the project's root directory, and add a list 
of URLs to scrape.

    The scraper's currently limited to 4chan boards and 4chan threads.

    ```console
    user@pc:~/projects/meme_tracker$ vim spider_config.yaml
    ```
    ```yaml
    urls: [http://boards.4channel.org/v/] 
    ```

2. Run the image scraper.

    If you provided a board, then every image from every thread on the board's
    first page will be downloaded.
    
    If you provided a thread, then every image in that thread will be
    downloaded.
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

## To Do

- [x] Feat: Scrape image URLs from /v
- [x] Feat: Download images
- [x] Feat: Show images in browser
- [ ] Feat: Generate thumbnails
- [ ] Feat: Justify image grid
- [ ] Internal: Change yaml config from dict to list
- [ ] Internal: Write names and locations to database
- [ ] Feat: Add JupyterNotebooks
- [ ] Feat: Add a dhashing notebook 
- [ ] Feat: Run dhashing notebook with papermill
- [ ] Feat: Cluster images
- [ ] Feat: Display image cluster "compass" in web browser
- [ ] Feat: Write origin post URLs to the database
- [ ] Feat: Click image to open origin post in new tab
