from models import Accelerometer
import io
import base64

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


def generate_acceleration_2d_graphs():
    graphs = []
    accelerometer_data = Accelerometer.query.all()

    timestamps = []
    x_values = []
    y_values = []
    z_values = []

    for data in accelerometer_data:
        timestamps.append(data.timestamp)
        x_values.append(data.x_value)
        y_values.append(data.y_value)
        z_values.append(data.z_value)

    graphs.append(generate_graph(timestamps, x_values))
    graphs.append(generate_graph(timestamps, y_values))
    graphs.append(generate_graph(timestamps, z_values))

    encoded_graphs = [encode_graph(graph) for graph in graphs]

    return encoded_graphs


def graph_by_type(graph_type):
    pass


def generate_graph(x_points, y_points):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    axis.set_title("title")
    axis.set_xlabel("x-axis")
    axis.set_ylabel("y-axis")
    axis.grid()

    axis.plot(x_points, y_points)

    return fig


def encode_graph(fig):
    png_image = io.BytesIO()
    FigureCanvas(fig).print_png(png_image)

    encoded_png_string = "data:image/png;base64,"
    encoded_png_string += base64.b64encode(png_image.getvalue()).decode("utf8")

    return encoded_png_string
