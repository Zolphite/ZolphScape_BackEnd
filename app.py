from flask import Flask, render_template, json
from flask_cors import CORS
import dash
import dash_core_components as dcc
import dash_html_components as html
import Scripts.api_functions as api_functions

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
dash_app = dash.Dash(__name__,
    server=app,
    routes_pathname_prefix='/dash/')

dash_app.layout = html.Div("My Dash app")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    my_dict = { "title": "Name", "genre": "Rock"}
    return json.dumps(my_dict)

@app.route('/api/test')
def api_test():
    return api_functions.covid_graph(app)

@app.route('/api/rdd-test')
def rdd_test():
    return api_functions.rdd_test_graph()

@app.route('/api/sim-rank-test')
def sim_rank_test():
    return api_functions.sim_rank_graph()

@app.route('/api/get-img-test')
def get_image_test():
    return api_functions.get_image_test()
    
if __name__ == "__main__":
    print("server is running on localhost!!")
    dash_app.run_server(debug=True)