from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from myrender import read_json,read_json2
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def top_page():
    anime_link = read_json2("img_link","./static/json/anime.json")
    return render_template('top2.html',anime_link=anime_link)

@app.route('/detail/<title>')
def detail(title):
    details = read_json2(title,"./static/json/detail.json")
    return render_template('detail.html',details= details,title=title)

@app.route('/craft/<title>')
def craft_view(title):
    anime = read_json(title,"./static/json/craft.json")
    return render_template('craft.html',anime=anime,title=title)

if __name__ == '__main__':
    app.run(debug=True)
