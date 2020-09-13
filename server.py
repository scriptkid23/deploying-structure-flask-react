from flask import Flask, render_template, send_from_directory
from flask_restful import Api
from flask_cors import CORS
from api.routes import initialize_routes
import config.configDB

app = Flask(__name__, static_folder="build/static", template_folder="build")


cors = CORS(app)
api = Api(app)
initialize_routes(api)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/manifest.json")
def manifest():
    return send_from_directory('./build', 'manifest.json')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory('./build', 'favicon.ico')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
