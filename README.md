# pandas-highcharts #

## What is it ##

**pandas-highcharts** is a Python package which allows you to easily build [Highcharts plots](http://www.highcharts.com/ "Highcharts") with [pandas](https://github.com/pydata/pandas "pandas").[DataFrame](http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.html "DataFrame") objects.

## Motivation ##

* pandas is the best tool to handle data in Python
* pandas is able to produce matplotlib plots. They work pretty well but have two major drawbacks
 * Not very web friendly
 * Pretty ugly
* Highcharts produce nice, interactive plot in your browser and is very complete

## Features ##

* Same interface as DataFrame.plot
* Following parameters are handled
 * data
 * x
 * y
 * kind
 * figsize
 * use_index
 * title
 * grid
 * legend
 * style
 * logx
 * logy
 * loglog
 * xticks
 * yticks
 * xlim
 * ylim
 * rot
 * fontsize
 * position
 * stacked
 * sort_columns
 * secondary_y
 * mark_right
* Following parameters are not handled (yet) :
 * ax
 * ay
 * subplots
 * sharex
 * sharey
 * layout
 * colormap
 * colorbar
 * layout
 * table
 * yerr
 * xerr
 * kwds
* Static files (highcharts.js) are not embedded

## Installation ##

Install the package using pip

    pip install pandas-highcharts

Import it in your views

    import pandas_highcharts
    df = ... # create your dataframe here
    chart = pandas_highcharts.serialize(df, render_to = "my-chart")

In your templates

    <script type="text/javascript">{{chart|safe}}</script>