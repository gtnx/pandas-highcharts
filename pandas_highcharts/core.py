# -*- coding: utf-8 -*-

# @Author: phil
# @Date:   2016-11-25T10:16:14+08:00
# @Last modified by:   phil
# @Last modified time: 2016-11-28T10:56:32+08:00
from string import Template

import pandas
import copy

import re

_pd2hc_kind = {
    "bar": "column",
    "barh": "bar",
    "area": "area",
    "line": "line",
    "pie": "pie"
}


def pd2hc_kind(kind):
    if kind not in _pd2hc_kind:
        raise ValueError("%(kind)s plots are not yet supported" % locals())
    return _pd2hc_kind[kind]


_pd2hc_linestyle = {
    "-": "Solid",
    "--": "Dash",
    "-.": "DashDot",
    ":": "Dot"
}


def pd2hc_linestyle(linestyle):
    if linestyle not in _pd2hc_linestyle:
        raise ValueError("%(linestyle)s linestyles are not yet supported" % locals())
    return _pd2hc_linestyle[linestyle]


def json_encode(obj):
    return pandas.io.json.dumps(obj)


def serialize(df, output_type="javascript", chart_type="default", *args, **kwargs):
    def serialize_chart(df, output, *args, **kwargs):
        output["chart"] = {}
        if 'render_to' in kwargs:
            output['chart']['renderTo'] = kwargs['render_to']
        if "figsize" in kwargs:
            output["chart"]["width"] = kwargs["figsize"][0]
            output["chart"]["height"] = kwargs["figsize"][1]
        if "kind" in kwargs:
            output["chart"]["type"] = pd2hc_kind(kwargs["kind"])
        if kwargs.get('polar'):
            output['chart']['polar'] = True

    def serialize_colors(df, output, *args, **kwargs):
        pass

    def serialize_credits(df, output, *args, **kwargs):
        pass

    def serialize_data(df, output, *args, **kwargs):
        pass

    def serialize_drilldown(df, output, *args, **kwargs):
        pass

    def serialize_exporting(df, output, *args, **kwargs):
        pass

    def serialize_labels(df, output, *args, **kwargs):
        pass

    def serialize_legend(df, output, *args, **kwargs):
        output["legend"] = {
            "enabled": kwargs.get("legend", True)
        }

    def serialize_loading(df, output, *args, **kwargs):
        pass

    def serialize_navigation(df, output, *args, **kwargs):
        pass

    def serialize_noData(df, output, *args, **kwargs):
        pass

    def serialize_pane(df, output, *args, **kwargs):
        pass

    def serialize_plotOptions(df, output, *args, **kwargs):
        pass

    def serialize_series(df, output, *args, **kwargs):
        def is_secondary(c, **kwargs):
            return c in kwargs.get("secondary_y", [])

        if kwargs.get('sort_columns'):
            df = df.sort_index()
        series = df.to_dict('series')
        output["series"] = []
        for name, data in series.items():
            if df[name].dtype.kind in "biufc":
                sec = is_secondary(name, **kwargs)
                d = {
                    "name": name if not sec or not kwargs.get("mark_right", True) else name + " (right)",
                    "yAxis": int(sec),
                    "data": list(zip(df.index, data.values.tolist()))
                }
                if kwargs.get('polar'):
                    d['data'] = [v for k, v in d['data']]
                if kwargs.get("kind") == "area" and kwargs.get("stacked", True):
                    d["stacking"] = 'normal'
                if kwargs.get("style"):
                    d["dashStyle"] = pd2hc_linestyle(kwargs["style"].get(name, "-"))
                output["series"].append(d)
        output['series'].sort(key=lambda s: s['name'])

    def serialize_subtitle(df, output, *args, **kwargs):
        pass

    def serialize_title(df, output, *args, **kwargs):
        if "title" in kwargs:
            output["title"] = {"text": kwargs["title"]}

    def serialize_tooltip(df, output, *args, **kwargs):
        if 'tooltip' in kwargs:
            # if we want to display more info in tooltip,
            # we should provide `field__additional_info`
            additional_info_keys = [key for key in kwargs['tooltip'] if 'additional_info' in key]
            if additional_info_keys:
                for key in additional_info_keys:
                    field, _ = key.split('__')
                    additional_info = kwargs['tooltip'].pop(key)
                    field_idx = [idx for idx, dic in enumerate(output['series']) if dic['name'] == field][0]
                    dic = output['series'][field_idx]
                    dic['data'] = [{'x': x, 'y': y, 'additional_info': additional_info[idx]} for idx, (x, y) in
                                   enumerate(dic['data'])]

            output['tooltip'] = kwargs['tooltip']

            if 'formatter' in output['tooltip']:
                output['___functions___']['tooltip__formatter'] = output['tooltip'].pop('formatter')
                output['tooltip']['formatter'] = "$tooltip__formatter"

            if 'pointFormatter' in output['tooltip']:
                output['___functions___']['tooltip__pointFormatter'] = output['tooltip'].pop('pointFormatter')
                output['tooltip']['pointFormatter'] = '$tooltip_pointFormatter'

    def serialize_xAxis(df, output, *args, **kwargs):
        output["xAxis"] = {}
        if df.index.name:
            output["xAxis"]["title"] = {"text": df.index.name}
        if df.index.dtype.kind in "M":
            output["xAxis"]["type"] = "datetime"
        if df.index.dtype.kind == 'O':
            output['xAxis']['categories'] = sorted(list(df.index)) if kwargs.get('sort_columns') else list(df.index)
        if kwargs.get("grid"):
            output["xAxis"]["gridLineWidth"] = 1
            output["xAxis"]["gridLineDashStyle"] = "Dot"
        if kwargs.get("loglog") or kwargs.get("logx"):
            output["xAxis"]["type"] = 'logarithmic'
        if "xlim" in kwargs:
            output["xAxis"]["min"] = kwargs["xlim"][0]
            output["xAxis"]["max"] = kwargs["xlim"][1]
        if "rot" in kwargs:
            output["xAxis"]["labels"] = {"rotation": kwargs["rot"]}
        if "fontsize" in kwargs:
            output["xAxis"].setdefault("labels", {})["style"] = {"fontSize": kwargs["fontsize"]}
        if "xticks" in kwargs:
            output["xAxis"]["tickPositions"] = kwargs["xticks"]

    def serialize_yAxis(df, output, *args, **kwargs):
        yAxis = {}
        if kwargs.get("grid"):
            yAxis["gridLineWidth"] = 1
            yAxis["gridLineDashStyle"] = "Dot"
        if kwargs.get("loglog") or kwargs.get("logy"):
            yAxis["type"] = 'logarithmic'
        if "ylim" in kwargs:
            yAxis["min"] = kwargs["ylim"][0]
            yAxis["max"] = kwargs["ylim"][1]
        if "rot" in kwargs:
            yAxis["labels"] = {"rotation": kwargs["rot"]}
        if "fontsize" in kwargs:
            yAxis.setdefault("labels", {})["style"] = {"fontSize": kwargs["fontsize"]}
        if "yticks" in kwargs:
            yAxis["tickPositions"] = kwargs["yticks"]
        output["yAxis"] = [yAxis]
        if kwargs.get("secondary_y"):
            yAxis2 = copy.deepcopy(yAxis)
            yAxis2["opposite"] = True
            output["yAxis"].append(yAxis2)

    def serialize_zoom(df, output, *args, **kwargs):
        if "zoom" in kwargs:
            if kwargs["zoom"] not in ("x", "y", "xy"):
                raise ValueError("zoom must be in ('x', 'y', 'xy')")
            output["chart"]["zoomType"] = kwargs["zoom"]

    output = {'___functions___': {}}
    df_copy = copy.deepcopy(df)
    if "x" in kwargs:
        df_copy.index = df_copy.pop(kwargs["x"])
    if kwargs.get("use_index", True) is False:
        df_copy = df_copy.reset_index()
    if "y" in kwargs:
        df_copy = pandas.DataFrame(df_copy, columns=kwargs["y"])
    serialize_chart(df_copy, output, *args, **kwargs)
    serialize_colors(df_copy, output, *args, **kwargs)
    serialize_credits(df_copy, output, *args, **kwargs)
    serialize_data(df_copy, output, *args, **kwargs)
    serialize_drilldown(df_copy, output, *args, **kwargs)
    serialize_exporting(df_copy, output, *args, **kwargs)
    serialize_labels(df_copy, output, *args, **kwargs)
    serialize_legend(df_copy, output, *args, **kwargs)
    serialize_loading(df_copy, output, *args, **kwargs)
    serialize_navigation(df_copy, output, *args, **kwargs)
    serialize_noData(df_copy, output, *args, **kwargs)
    serialize_pane(df_copy, output, *args, **kwargs)
    serialize_plotOptions(df_copy, output, *args, **kwargs)
    serialize_series(df_copy, output, *args, **kwargs)
    serialize_subtitle(df_copy, output, *args, **kwargs)
    serialize_title(df_copy, output, *args, **kwargs)
    serialize_tooltip(df_copy, output, *args, **kwargs)
    serialize_xAxis(df_copy, output, *args, **kwargs)
    serialize_yAxis(df_copy, output, *args, **kwargs)
    serialize_zoom(df_copy, output, *args, **kwargs)

    functions = output.pop('___functions___')
    if output_type == "dict":
        def update_dict(d, up):
            for k, v in d.items():
                if isinstance(v, str) and v.startswith('$'):
                    d[k] = up[v.replace('$', '')]
                if isinstance(v, dict):
                    update_dict(v, up)
        # fixme: this is wrong!!!
        update_dict(output, functions)
        return output
    json_output = """{}""".format(json_encode(output))
    json_output = re.sub('"(\$\w+)"', r'\1', json_output)
    if output_type == "json":
        template = Template("""{}""".format(json_output))
        return template.substitute(functions)
    if chart_type == "stock":
        high_stocks = Template("""new Highcharts.StockChart(%s);""" % json_output)
        return high_stocks.substitute(functions)
    high_charts = Template("new Highcharts.Chart(%s);" % json_output)
    return high_charts.substitute(functions)
