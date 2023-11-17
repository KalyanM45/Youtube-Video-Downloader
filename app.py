# app.py
from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    video = YouTube(url)
    stream = video.streams.get_highest_resolution()
    stream.download()
    return render_template('success.html', title=video.title, thumbnail=video.thumbnail_url)

if __name__ == '__main__':
    app.run(debug=True)
