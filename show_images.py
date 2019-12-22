from flask import Flask
from pathlib import Path


app = Flask(__name__)

@app.route('/')
def show_local_images():
    images = [item for item in Path('saved_images') if item.is_file()]
    return 'test'


if __name__ == '__main__':
    app.run(host='localhost', port=5000)