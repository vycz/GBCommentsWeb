from flask import Flask, render_template, request,jsonify
from flask_bootstrap import Bootstrap
from flask_cors import CORS
import json
from GBComments import produceComments

 
app = Flask(__name__)
CORS(app, supports_credentials=True)
bootstrap = Bootstrap(app)
 
# @app.route('/', methods=["GET", "POST"])
# def main():
#     comments = None
#     _type = request.form.get("_type")
#     _class = request.form.get("_class")
#     if _type: comments = produceComments(_type, _class)
#     return render_template('/main.html', comments=comments)
 
@app.route('/api', methods=["POST"])
def main():
    comments = None
    _type = request.form.get("_type")
    _class = request.form.get("_class")
    if _type: 
        comments = produceComments(_type, _class)
    res = {
        'comments':comments
    }
    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=False)