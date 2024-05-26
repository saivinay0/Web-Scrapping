from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)
def scraper(url):
    content=requests.get(url)
    with open("cont.html","w",encoding='utf-8') as w:
        w.write(content.text)
    with open("cont.html","r",encoding='utf-8') as f:
        parse=f.read()
    soup = BeautifulSoup(parse, 'html.parser')
    titles=[h1.get_text() for h1 in soup.find_all('h1')]
    return titles
    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form['url']
    titles = scraper(url)
    return render_template('scrape.html', titles=titles)

if __name__ == '__main__':
    app.run(debug=True)
