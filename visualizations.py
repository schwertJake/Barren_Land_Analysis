import plotly.offline.offline as py
import plotly.graph_objs as go


def visualize(max_x, max_y, barren_land_dicts):

    trace0 = go.Scatter(
        x=[1.5, 4.5],
        y=[0.75, 0.75],
    )
    data = [trace0]
    layout = {
        'xaxis': {
            'range': [0, max_x],
            'showgrid': True,
            'fixedrange': True
        },
        'yaxis': {
            'range': [0, max_y],
            'fixedrange': True
        },
        'shapes': barren_land_dicts
    }
    fig = go.Figure( data=data, layout=layout)
    py.plot(fig, filename='barren_plot.html', auto_open=True)

if __name__ == "__main__":
    visualize(400, 600, [{
        "x0": 0,
        "y0": 292,
        "x1": 399,
        "y1": 307,
        'type': 'rect',
        'line': {
            'color': 'rgba(255, 69, 0, 1)',
            'width': 2,
        },
        'fillcolor': 'rgba(255, 69, 0, 0.7)'
    }])