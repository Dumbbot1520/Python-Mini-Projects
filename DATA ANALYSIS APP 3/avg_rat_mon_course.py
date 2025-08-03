import justpy as jp
import pandas 
from datetime import datetime,timezone
from pytz import utc
import matplotlib.pyplot as plt
data = pandas.read_csv("C:/Users/Om/OneDrive/Documents/GitHub/pythonudemy/INTERACTIVE DATA VISUALISATION USING BOKEH/DATA ANALYSIS APP 3/reviews (1).csv",parse_dates=['Timestamp'])


data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
numeric_cols = data.select_dtypes(include= ['number']).columns
monthly_avg_courses = data.groupby(['Month','Course Name'])[numeric_cols].count().unstack()

charts_def = """
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average Ratings for each Month and each Course '
    },
    subtitle: {
        text: 'Source: <a href="https://www.ssb.no/jord-skog-jakt-og-fiskeri/jakt" target="_blank">SSB</a>'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 120,
        y: 70,
        floating: false,
        borderWidth: 1,
        backgroundColor: '#ffffff'
    },
    xAxis: {
        // Highlight the last years where moose hunting quickly deminishes
        plotBands: [{
            from: 2020,
            to: 2023,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Quantity'
        }
    },
    tooltip: {
        shared: true,
        headerFormat: '<b>Hunting season starting autumn {point.x}</b><br>'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        series: {
            pointStart: 2000
        },
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'Moose',
        data:
            [
                38000,
                37300,
                37892,
                38564,
                36770,
                36026,
                34978,
                35657,
                35620,
                35971,
                36409,
                36435,
                34643,
                34956,
                33199,
                31136,
                30835,
                31611,
                30666,
                30319,
                31766,
                29278,
                27487,
                26007
            ]
    }, {
        name: 'Deer',
        data:
            [
                22534,
                23599,
                24533,
                25195,
                25896,
                27635,
                29173,
                32646,
                35686,
                37709,
                39143,
                36829,
                35031,
                36202,
                35140,
                33718,
                37773,
                42556,
                43820,
                46445,
                50048,
                52804,
                49317,
                52490
            ]
    }]
}
"""

def app():
    wp = jp.QuasarPage() # quaserpage is the class for the website and wp is the object created 
    h1 = jp.QDiv(a=wp,text = "Analysis Of Course Reviews", classes = "text-h3 text-center q-pa-md") # h1 is header 
    p1 = jp.QDiv(a=wp, text = "These Graphs represent course review analysis", classes = "text-center") # p1 is paragraph 
    hc = jp.HighCharts(a=wp,options = charts_def)
    hc.options.xAxis.categories = list(monthly_avg_courses.index) # months 

    # now we need to show courses names on y axis with data (ratings for each course)
    hc_data = [{"name":v1, "data":[v2 for v2 in monthly_avg_courses[v1]]} for v1 in monthly_avg_courses.columns]
    hc.options.series = hc_data
    return wp

jp.justpy(app) # calling the app function