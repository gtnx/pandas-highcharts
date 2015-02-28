# -*- coding: utf-8 -*-

"""Functions to quickly display charts in a Notebook.
"""

import string
import random

from IPython.core import getipython
from IPython.core.display import display, HTML

from core import serialize


HIGHCHARTS_SCRIPTS = """<script src="http://code.highcharts.com/highcharts.js"></script>
<script src="http://code.highcharts.com/modules/exporting.js"></script>
"""

# Automatically insert the script tag into your Notebook.
# Call when you import this module.
if 'IPKernelApp' in getipython.get_ipython().config:
    display(HTML(HIGHCHARTS_SCRIPTS))

def load_highcharts():
    return display(HTML(HIGHCHARTS_SCRIPTS))

def _generate_div_id_chart(prefix="chart_id", digits=8):
    """Generate a random id for div chart.
    """
    choices = (random.randrange(0, 52) for _ in xrange(digits))
    return prefix + "".join((string.ascii_letters[x] for x in choices))

def display_highcharts(df, render_to=None, **kwargs):
    """Display you DataFrame with Highcharts.

    df: DataFrame
    render_to: str
        div id for plotting your data
    """
    chart_id = render_to if render_to is not None else _generate_div_id_chart()
    json_data = serialize(df, render_to=chart_id, **kwargs)
    content = """<div id="{chart_id}""</div>
    <script type="text/javascript">{data}</script>"""
    return display(HTML(content.format(chart_id=chart_id,
                                       data=json_data)))
