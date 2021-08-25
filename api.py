import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    f = open("msc_execution.log", "r")
    return f.read()

app.run(host='0.0.0.0', port=4447)