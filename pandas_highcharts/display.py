# -*- coding: utf-8 -*-

from __future__ import absolute_import

"""Functions to quickly display charts in a Notebook.
"""

import string
import random
import json
import copy

from IPython.core import getipython
from IPython.core.display import display, HTML

from .core import serialize


# Note that Highstock includes all Highcharts features.
HIGHCHARTS_SCRIPTS = """
<script src="//code.highcharts.com/stock/highstock.js"></script>
<script src="//code.highcharts.com/highcharts-more.js"></script>
<script src="//code.highcharts.com/modules/exporting.js"></script>
"""


def load_highcharts():
    return display(HTML(HIGHCHARTS_SCRIPTS))

# Automatically insert the script tag into your Notebook.
# Call when you import this module.
if 'IPKernelApp' in getipython.get_ipython().config:
    load_highcharts()


def _generate_div_id_chart(prefix="chart_id", digits=8):
    """Generate a random id for div chart.
    """
    choices = (random.randrange(0, 52) for _ in range(digits))
    return prefix + "".join((string.ascii_letters[x] for x in choices))


def display_charts(df, chart_type="default", render_to=None, **kwargs):
    """Display you DataFrame with Highcharts.

    df: DataFrame
    chart_type: str
        'default' or 'stock'
    render_to: str
        div id for plotting your data
    """
    if chart_type not in ("default", "stock"):
        raise ValueError("Wrong chart_type: accept 'default' or 'stock'.")
    chart_id = render_to if render_to is not None else _generate_div_id_chart()
    json_data = serialize(df, render_to=chart_id, chart_type=chart_type,
                          **kwargs)
    content = """<div id="{chart_id}"</div>
    <script type="text/javascript">{data}</script>"""
    return display(HTML(content.format(chart_id=chart_id,
                                       data=json_data)))


def _series_data_filter(data):
    """Replace each 'data' key in the list stored under 'series' by "[...]".

    Use to not store and display the series data when you just want display and
    modify the Highcharts parameters.

    data: dict
        Serialized DataFrame in a dict for Highcharts

    Returns: a dict with filtered values

    See also `core.serialize`
    """
    data = copy.deepcopy(data)
    if "series" in data:
        for series in data["series"]:
            series["data"] = "[...]"
    return data


def pretty_params(data, indent=2):
    """Pretty print your Highcharts params (into a JSON).

    data: dict
        Serialized DataFrame in a dict for Highcharts
    """
    data_to_print = _series_data_filter(data)
    print(json.dumps(data_to_print, indent=indent))
