from flask import Flask, render_template, request, redirect
import youtube_dl
from pytube import YouTube

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/download', methods=["POST", "GET"])
def download():
    url = request.form["url"]
    print("Someone just tried to download", url)
    with youtube_dl.YoutubeDL() as ydl:
        url = ydl.extract_info(url, download=False)
        print(url)
        try:
            download_link = url["entries"][-1]["formats"][-1]["url"]
        except:
            download_link = url["formats"][-1]["url"]
        return redirect(download_link + "&dl=1")


@app.route('/downloadyt', methods=["POST", "GET"])
def downloadyt():
    video_url = request.form['urll']
    yt = YouTube(video_url)
    ys = yt.streams.get_highest_resolution()
    download_link = ys.url
    return redirect(download_link)


if __name__ == '__main__':
    app.run(port=80, debug=True)
