from django.shortcuts import render
from django.http import FileResponse, HttpResponseRedirect, JsonResponse, HttpResponse

import plotly.express as px
import plotly.graph_objects as go
import datetime
import pandas as pd
from urllib.request import urlopen
import csv
# Create your views here.
# @login_required(login_url='/login')
def main(request):
    data = dict()
    
    if request.method == "POST":
        url = request.POST.get("link")
        print(url)
        # df = pd.read_csv(url) # Add encoding='utf-8' if needed
        # print(df.head())
        with urlopen(url) as response:
            lines = [l.decode('utf-8') for l in response.readlines()]
            reader = csv.reader(lines)
            for row in reader:
                print(row)
    
    if request.method == "GET":
        plot1 = px.choropleth_map(
            locations=['USA', 'CAN', 'MEX', 'BRA', 'RUS', "PT"],
            # locationmode='ISO-3',
            color=[100, 100, 100, 100, 100, 100],
            color_continuous_scale='Viridis',
            title='Choropleth with ISO-3 Country Codes'
        )
        plot1.update_layout(map_style="open-street-map")
        data['plot1'] = plot1.to_html(full_html=False)
        
        plot2 = px.bar(x=[1,2,3,4],
            y=[1,2,3,4])
        data['plot2'] = plot2.to_html(full_html=False)
        
        plot4 = px.line(
            x=[1,2,3,4],
            y=[1,2,3,4],
            markers=True,
            title="Test"
        )
        data['plot4'] = plot4.to_html(full_html=False)
    
    rend = render(request, 'main.html', data)
    resp = HttpResponse(rend)
    return resp