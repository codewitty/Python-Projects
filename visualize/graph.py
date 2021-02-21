from bokeh.plotting import figure
from bokeh.io import output_file, show

# fake data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

output_file("line.html")

# figure object
f = figure()

# line plot
f.line(x,y)

show (f)
