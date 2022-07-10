from bokeh.io import show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource

x_values = range(10)
y_values = [x ** 2 for x in x_values]
data_source = ColumnDataSource(data=dict(x=x_values, y=y_values))

plot = figure(title = 'f(x) = x^2')
plot.line('x', 'y', source = data_source, line_width=3, line_alpha=0.6)
show(plot)



