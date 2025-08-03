import justpy as jp
import pandas
from datetime import datetime,timezone
from pytz import utc
import matplotlib.pyplot as plt
data = pandas.read_csv("reviews (1).csv",parse_dates=['Timestamp'])


data['Day'] = data['Timestamp'].dt.date
numeric_cols = data.select_dtypes(include=['number']).columns    #to make sure that only the numerical part is sselected for mean
day_avg = data.groupby(['Day'])[numeric_cols].mean()
chart_def = """
 {
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Day'
        },
        labels: {
            format: '{value} km'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Rating'
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} {point.y} '
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: [
            [0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]
        ]

    }]
}

"""
def app():
    wp = jp.QuasarPage() # quaserpage is the class for the website and wp is the object created 
    h1 = jp.QDiv(a=wp,text = "Analysis Of Course Reviews", classes = "text-h3 text-center q-pa-md") # h1 is header 
    p1 = jp.QDiv(a=wp, text = "These Graphs represent course review analysis", classes = "text-center") # p1 is paragraph 
    hc = jp.HighCharts(a=wp,options=chart_def) # converts js code to python dictionary. Options can be used to change the elements of the dictionary
    hc.options.title.text = "Average Rating By Day"
    hc.options.series[0].data = list(day_avg["Rating"]) 
    hc.options.xAxis.categories = list(day_avg.index)

    return wp

jp.justpy(app) # calling the app function

