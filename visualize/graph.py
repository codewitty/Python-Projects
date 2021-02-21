from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

df = pandas.read_csv("data.csv")
x = df["Month"]
y = df["PushUps"]

output_file("line.html")

# figure object
p = figure(plot_width=1200,plot_height=800, tools='pan')
p.title.text="Cool Data"
p.title.text_color="Gray"
p.title.text_font="times"
p.title.text_font_style="bold"
p.xaxis.minor_tick_line_color=None
p.yaxis.minor_tick_line_color=None
p.xaxis.axis_label="Month"
p.yaxis.axis_label="No of Pushups"

# line plot
p.line(x,y)

show (p)
