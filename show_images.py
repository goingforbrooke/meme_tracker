from flask import Flask, render_template, url_for
from pathlib import Path


app = Flask(__name__, static_url_path='/static')

@app.route('/')
def show_local_images():
    image_urls = [url_for('static', filename=item.name)
                  for item in Path('saved_images', 'full').iterdir() if item.is_file()]
    return render_template('image_grid.html', image_urls=image_urls)


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
