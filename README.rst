pandas-highcharts
=================

.. image:: https://travis-ci.org/gtnx/pandas-highcharts.svg?branch=master
    :target: https://travis-ci.org/gtnx/pandas-highcharts
.. image:: https://coveralls.io/repos/gtnx/pandas-highcharts/badge.svg
    :target: https://coveralls.io/r/gtnx/pandas-highcharts

What is it
----------

**pandas-highcharts** is a Python package which allows you to easily
build `Highcharts plots`_ with `pandas`_.\ `DataFrame`_ objects.

Motivation
----------

-  pandas is the best tool to handle data in Python
-  pandas is able to produce matplotlib plots. They work pretty well but
   have two major drawbacks

   -  Not very web friendly
   -  Pretty ugly

-  Highcharts produce nice, interactive plot in your browser and is very
   complete

Features
--------

-  Same interface as DataFrame.plot
-  Following parameters are handled

   -  data
   -  x
   -  y
   -  kind
   -  figsize
   -  use\_index
   -  title
   -  grid
   -  legend
   -  style
   -  logx
   -  logy
   -  loglog
   -  xticks
   -  yticks
   -  xlim
   -  ylim
   -  rot
   -  fontsize
   -  position
   -  stacked
   -  sort\_columns
   -  secondary\_y
   -  mark\_right

-  Following parameters are not handled (yet) :

   -  ax
   -  ay
   -  subplots
   -  sharex
   -  sharey
   -  layout
   -  colormap
   -  colorbar
   -  layout
   -  table
   -  yerr
   -  xerr
   -  kwds

-  You can specify those specific highcharts parameters:

   - tooltip

-  Static files (highcharts.js) are not embedded

Installation
------------

Install the package using pip

.. code:: shell

    pip install pandas-highcharts

Usage
-----

Import it in your views

.. code:: python

    import pandas_highcharts
    df = ... # create your dataframe here
    chart = pandas_highcharts.serialize(df, render_to='my-chart', output_type='json')

In your templates

.. code:: html

    <div id="my-chart"></div>
    <script type="text/javascript">
      new Highcharts.Chart({{chart|safe}});
    </script>

Contributing
------------

See CONTRIBUTING.rst for information on how to contribute to pandas-highcharts.

More examples
-------------

Some examples are available on `nbviewer`_.

Please read the doc for `DataFrame.plot`_.

For example, with the following dataset:


.. code:: python

    import pandas as pd
    from pandas_highcharts.core import serialize
    from pandas.compat import StringIO
    dat = """ts;A;B;C
    2015-01-01 00:00:00;27451873;29956800;113
    2015-01-01 01:00:00;20259882;17906600;76
    2015-01-01 02:00:00;11592256;12311600;48
    2015-01-01 03:00:00;11795562;11750100;50
    2015-01-01 04:00:00;9396718;10203900;43
    2015-01-01 05:00:00;14902826;14341100;53"""
    df = pd.read_csv(StringIO(dat), sep=';', index_col='ts', parse_dates='ts')

    # Basic line plot
    chart = serialize(df, render_to="my-chart", title="My Chart")
    # Basic column plot
    chart = serialize(df, render_to="my-chart", title="Test", kind="bar")
    # Basic column plot
    chart = serialize(df, render_to="my-chart", title="Test", kind="barh")
    # Plot C on secondary axis
    chart = serialize(df, render_to="my-chart", title="Test", secondary_y = ["C"])
    # Plot on a 1000x700 div
    chart = serialize(df, render_to="my-chart", title="Test", figsize = (1000, 700))

.. _Highcharts plots: http://www.highcharts.com/
.. _pandas: https://github.com/pydata/pandas
.. _DataFrame: http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.html
.. _DataFrame.plot: http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.plot.html
.. _nbviewer: http://nbviewer.ipython.org/github/gtnx/pandas-highcharts/blob/master/example.ipynb