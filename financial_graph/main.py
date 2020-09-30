# This is a sample Python script.
from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components

start = datetime.datetime(2016, 3, 1)
end = datetime.datetime(2016, 4, 10)

data_frame = data.DataReader(name="GOOG", data_source="yahoo", start=start, end=end)


def inc_dec(c, o):
    if c > o:
        value = "Increase"
    elif c < o:
        value = "Decrease"
    else:
        value = "Equal"

    return value


data_frame["Status"] = [inc_dec(c, o) for c, o in zip(data_frame.Close, data_frame.Open)]
data_frame["Middle"] = (data_frame.Open + data_frame.Close) / 2
data_frame["Height"] = abs(data_frame.Close - data_frame.Open)

plot = figure(x_axis_type="datetime", width=1000, height=300)
plot.title.text = "Candlestick Chart"

hours_12 = 12 * 60 * 60 * 1000

plot.segment(data_frame.index, data_frame.High, data_frame.index, data_frame.Low, color="Black")

plot.rect(data_frame.index[data_frame.Status == "Increase"], data_frame.Middle[data_frame.Status == "Increase"],
          hours_12, data_frame.Height[data_frame.Status == "Increase"], fill_color="#CCFFFF", line_color="black")

plot.rect(data_frame.index[data_frame.Status == "Decrease"], data_frame.Middle[data_frame.Status == "Decrease"],
          hours_12, data_frame.Height[data_frame.Status == "Decrease"], fill_color="#FF3333", line_color="black")

script1, dev1 = components(plot)


""" output_file("cs.html")
show(plot)
print(data_frame) """

