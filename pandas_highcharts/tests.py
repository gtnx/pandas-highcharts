# -*- coding: utf-8 -*-

from core import serialize
import pandas


df = pandas.DataFrame([{"a": 1, "b": 2, "c": 3}, {"a": 2, "b": 4, "c": 6}])


def test_type():
    assert type(serialize(df, render_to="chart")) is str
    assert type(serialize(df, x="a", render_to="chart")) is str
    assert type(serialize(df, x="a", zoom="x", render_to="chart")) is str
    assert type(serialize(df, x="a", y=("b",), render_to="chart")) is str
    assert type(serialize(df, figsize=(100, 100), render_to="chart")) is str
