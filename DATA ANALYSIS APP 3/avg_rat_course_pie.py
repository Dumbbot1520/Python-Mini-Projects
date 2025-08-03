import justpy as jp
import justpy as jp
import pandas 
from datetime import datetime,timezone
from pytz import utc
import matplotlib.pyplot as plt
data = pandas.read_csv("C:/Users/Om/OneDrive/Documents/GitHub/pythonudemy/INTERACTIVE DATA VISUALISATION USING BOKEH/DATA ANALYSIS APP 3/reviews (1).csv",parse_dates=['Timestamp'])

share = data.groupby(["Course Name"])["Rating"].count()

chart_def = """
{
    chart: {
        type: 'pie',
        zooming: {
            type: 'xy'
        },
        panning: {
            enabled: true,
            type: 'xy'
        },
        panKey: 'shift'
    },
    title: {
        text: 'Ratings By Each Course'
    },
    tooltip: {
        valueSuffix: ''
    },
    subtitle: {
        text:
        'Source:<a href="https://www.mdpi.com/2072-6643/11/3/684/htm" target="_default">MDPI</a>'
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: [{
                enabled: true,
                distance: 20
            }, {
                enabled: true,
                distance: -40,
                format: '{point.percentage:.1f}%',
                style: {
                    fontSize: '1.2em',
                    textOutline: 'none',
                    opacity: 0.7
                },
                filter: {
                    operator: '>',
                    property: 'percentage',
                    value: 10
                }
            }]
        }
    },
    series: [
        {
            name: 'Count',
            colorByPoint: true,
            data: [
                {
                    name: 'Water',
                    y: 55.02
                },
                {
                    name: 'Fat',
                    sliced: true,
                    selected: true,
                    y: 26.71
                },
                {
                    name: 'Carbohydrates',
                    y: 1.09
                },
                {
                    name: 'Protein',
                    y: 15.5
                },
                {
                    name: 'Ash',
                    y: 1.68
                }
            ]
        }
    ]
}
"""
def app():
    wp = jp.QuasarPage() # quaserpage is the class for the website and wp is the object created 
    h1 = jp.QDiv(a=wp,text = "Analysis Of Course Reviews", classes = "text-h3 text-center q-pa-md") # h1 is header 
    p1 = jp.QDiv(a=wp, text = "These Graphs represent course review analysis", classes = "text-center") # p1 is paragraph 
    hc = jp.HighCharts(a=wp,options = chart_def)
    hc_data = [{"name":v1,"y":v2} for v1,v2 in zip(share.index,share)]
    hc.options.series[0].data = hc_data
    return wp

jp.justpy(app) # calling the app function