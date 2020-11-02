import pandas as pd
import plotly.express as px
import urllib.request, json
from json import dumps
from flask import render_template
from flask import send_file
import base64 #For image conversion

def covid_graph(app):
    with urllib.request.urlopen("https://covidtracking.com/api/v1/states/current.json") as url:
        data = json.loads(url.read().decode())

    state = []
    positive = []
    negative = []
    hospCurrently = []
    recovered = []
    for i in data:
        j, l, m, n, o = i['state'], i['positive'], i['negative'], i['hospitalizedCurrently'], i['recovered']
        state.append(j)
        positive.append(l)
        negative.append(m)
        hospCurrently.append(n)
        recovered.append(o)
        
    d = {'state':state, 'positive':positive, 'negative':negative, 'hospitalizedCurrently':hospCurrently, 'recovered':recovered}
    df = pd.DataFrame(d)

    fig = px.choropleth(df,  # Input Pandas DataFrame
                        locations="state",  # DataFrame column with locations
                        color="positive",  # DataFrame column with color values
                        color_continuous_scale="pubu",
                        hover_name="state", # DataFrame column hover info
                        hover_data={'positive', 'negative', 'recovered', 'hospitalizedCurrently'},
                        locationmode='USA-states',)  # Set to plot as US States
                        
    fig.update_layout(
        title_text = '', # Create a Title
        geo_scope='usa',  # Plot only the USA instead of globe
        margin={"r":0,"t":0,"l":0,"b":0},
        # width=100,
        # height=100,
    )

    import os

    if not os.path.exists("images"):
        os.mkdir("images")
    
    fig.write_html("templates/Graphs/CovidGraph.html", default_width='100%', default_height='97.5vh',)
    fig.write_image("static/assets/graph_img/CovidGraph.png")

    # Read and convert saved image to base64 byte string
    my_string = ''
    with open("static/assets/graph_img/CovidGraph.png", "rb") as img_file:
        my_string = base64.b64encode(img_file.read())

    # test = json.dumps(my_string.decode('utf-8'))

    # print(json.dumps(my_string))

    sending_dic = {  'title': 'Covid Graph',
                     'plotly_html': render_template("Graphs/CovidGraph.html"),
                     'image_path': my_string.decode('ASCII')}

    #  render_template("Graphs/TestGraph.html")
    # return app.send_static_file("static/assets/graph_img/test.png")
    return sending_dic

def rdd_test_graph():
    my_string = ''
    with open("static/assets/graph_img/RDD_Graph.png", "rb") as img_file:
        my_string = base64.b64encode(img_file.read())

    sending_dic = { 'title': 'RDD Network',
                     'plotly_html': render_template("Graphs/RDD_Test.html"),
                     'image_path': my_string.decode('ASCII')}
    return sending_dic

def sim_rank_graph():
    my_string = ''
    with open("static/assets/graph_img/Simrank_Graph.png", "rb") as img_file:
        my_string = base64.b64encode(img_file.read())

    sending_dic = { 'title': 'Simrank Network',
                     'plotly_html': render_template("Graphs/Sim_Rank.html"),
                     'image_path': my_string.decode('ASCII')}
    return sending_dic

def get_image_test():
    my_string = ''
    with open("static/assets/graph_img/CovidGraph.png", "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
    return my_string