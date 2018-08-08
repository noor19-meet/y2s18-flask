from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    players = ["Mesut Ozil", "Pier-amerik Aubamyang", "Alexander Lacazate"]
    return render_template(
        "index.html",
        likes_same_sport=False,
        players=players)

if __name__ == '__main__':
   app.run(debug = True)