from flask import Flask, url_for, render_template, request, get_flashed_messages, flash, redirect
from helper import keyword_search
from config import SCRAPER_SECRET

app = Flask(__name__)
app.secret_key = SCRAPER_SECRET


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    elif request.method == 'POST':
        page_to_scrape = request.values['page']
        search_term = request.values['keyword']

        result,category = keyword_search(page_to_scrape, search_term)
        flash(result,category=category)
        return render_template('home.html', msgType=category)
    else:
        return 'Unsupported Method'

if __name__ == '__main__':
    app.run(debug=True)
