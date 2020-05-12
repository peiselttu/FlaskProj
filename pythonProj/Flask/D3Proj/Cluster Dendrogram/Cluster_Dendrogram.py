from flask import Flask,render_template
from flask_bootstrap import Bootstrap
import json

app=Flask(__name__)
bootstrap=Bootstrap(app)


@app.route("/")
def index():
    with open("flare-2.json") as f:
        flare=json.loads(f.read())
    return render_template('index.html',flare=flare,l=len(flare))


if __name__=="__main__":
    app.run(debug=True)