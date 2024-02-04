from bokeh.plotting import figure, output_file, show
from bokeh.models.callbacks import CustomJS
import json

# Sample data
x = [1.0, 2.5, 3.7, 4.2, 5.8]
y = [2.3, 5.1, 8.0, 2.9, 7.5]

# Create the plot
plot = figure(title="Zoomable Plot", tools="pan,box_zoom,reset,tap", width=400, height=400)

# Plot the data
line = plot.line(x, y, line_width=2)

# Define the JavaScript code directly
tap_code = """
    // Get the clicked coordinates
    var x_clicked = cb_obj.x;
    var y_clicked = cb_obj.y;

    // Get the data coordinates
    var x_data = %s;
    var y_data = %s;

    // Initialize variables to store the nearest point on the line
    var nearest_x, nearest_y;
    var min_distance = Number.POSITIVE_INFINITY;

    // Iterate through all line segments formed by consecutive data points
    for (var i = 0; i < x_data.length - 1; i++) {
        var x1 = x_data[i];
        var y1 = y_data[i];
        var x2 = x_data[i + 1];
        var y2 = y_data[i + 1];

        // Calculate the perpendicular distance from the clicked point to the line segment
        var distance = Math.abs((x2 - x1) * (y1 - y_clicked) - (x1 - x_clicked) * (y2 - y1)) / Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));

        // Update the nearest point on the line if the distance is smaller
        if (distance < min_distance) {
            min_distance = distance;

            // Calculate the coordinates of the nearest point on the line
            var t = ((x_clicked - x1) * (x2 - x1) + (y_clicked - y1) * (y2 - y1)) / (Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
            nearest_x = x1 + t * (x2 - x1);
            nearest_y = y1 + t * (y2 - y1);
        }
    }

    // Check if the click is within a certain range of the line
    if (min_distance < 0.1) {  // Adjust the threshold as needed
        // Display an alert with the coordinates of the nearest point on the line
        alert("Nearest point on line: (" + nearest_x.toFixed(2) + ", " + nearest_y.toFixed(2) + ")");
    }
""" % (json.dumps(x), json.dumps(y))

# Add a Tap event callback using the JavaScript code
plot.js_on_event('tap', CustomJS(code=tap_code))

# Output the plot to an HTML file (optional)
output_file("zoomable_plot.html")

# Show the plot
show(plot)
