from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from myrender import read_json,read_json2
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def hello_world():
    return render_template('top2.html')

@app.route('/detail')
def detail():
    title = "法被の試着体験会"
    details = read_json2(title,"./static/json/detail.json")
    return render_template('detail-experience.html',details= details,title=title)

@app.route('/craft')
def craft_view():
    title = "ハナヤマタ"
    anime = read_json(title,"./static/json/craft.json")
    return render_template('craft.html',anime=anime,title=title)

if __name__ == '__main__':
    app.run(debug=True)
