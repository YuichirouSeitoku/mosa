from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from myrender import craft
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def hello_world():
    return render_template('template.html', my_string="Hello world", my_list=[0,1,2,3,4,5])

@app.route('/craft/<title>')
def craft_view(title):
    anime = craft(title)
    return render_template('craft.html',anime=anime,title=title)

if __name__ == '__main__':
    app.run(debug=True)
