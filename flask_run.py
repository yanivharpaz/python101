from flask import Flask, Response
import json


app = Flask(__name__)

print(__name__)


@app.route('/too')
def hello_world():
    data = {
        'hello'  : 'world',
        'number' : 3
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://luisrei.com'

    # return resp
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

app.run(port=5000)

