"""Display collected images in a web browser.

Run `python3 show_images.py` and navigate to
`http://localhost:5000<http://localhost:5000>` in a web browser.
"""
from flask import Flask, render_template, url_for
from pathlib import Path


app = Flask(__name__, static_folder='saved_images/full', template_folder='web/templates')


@app.route('/')
def show_local_images():
    """Display all images from saved_images/full/ in their native format. """
    image_urls = [url_for('static', filename=item.name)
                  for item in Path('saved_images', 'full').iterdir() if item.is_file()]
    return render_template('image_grid.html', image_urls=image_urls)


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
