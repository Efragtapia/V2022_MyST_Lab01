import numpy as np
import plotly.graph_objects as go 

def plot_lines(data_x, data_s1, data_s2, data_s3):
    
    x_data = list(range(0, len(data_x)))
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(x=x_data, y=data_s1, name= 's1', width=1, marker_color = 'blue'))
    
    fig.add_trace(go.Bar(x=x_data, y=data_s2, name= 's2', width=1, marker_color = 'red'))

    fig.add_trace(go.Bar(x=x_data, y=data_s3, name= 's3', width=1, marker_color = 'black'))
    
    return fig