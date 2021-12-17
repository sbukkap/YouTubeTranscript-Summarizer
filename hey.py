"""just practising code from corey schafer's flask tutorails :) """
from flask import Flask,render_template
app = Flask(__name__)

food = [
{'name':'Shreekar','meal':'dosa','fruit':'mango'},
{'name':'Shredder','meal':'blood','fruit':'ballz'}
]

@app.route("/")
@app.route('/also')
def hello():
    return render_template('home.html',l1=food,title='Homepg')

@app.route('/about')
def about():
    return render_template('about.html',title='aboutpg')

if __name__ == "__main__":
    app.run(debug=True)
