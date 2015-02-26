# -*- coding: UTF-8 -*-

from core import serialize
import pandas
from unittest import TestCase

df = pandas.DataFrame([{"a": 1, "b": 2, "c": 3}, {"a": 2, "b": 4, "c": 6}])


class CoreTest(TestCase):
    def test_type(self):
        self.assertIsInstance(serialize(df, render_to="chart"), str)
        obj = serialize(df, render_to="chart", output_type="json")
        self.assertIsInstance(obj, dict)
        obj = serialize(df, render_to="chart", output_type="json", zoom="xy")
        self.assertIn("chart", obj)
        self.assertIsInstance(obj["chart"], dict)
        self.assertIn("zoomType", obj["chart"])
        self.assertRaises(ValueError, serialize, df, **{"render_to": "chart", "zoom": "z"})
        obj = serialize(df, render_to="chart", output_type="json", kind="bar")
        self.assertIn("chart", obj)
        self.assertIsInstance(obj["chart"], dict)
        self.assertEqual(obj["chart"].get("type"), "column")
        self.assertRaises(ValueError, serialize, df, **{"render_to": "chart", "kind": "z"})
        obj = serialize(df, render_to="chart", output_type="json", secondary_y="a")
        self.assertTrue(obj.get("yAxis", [])[1].get('opposite'))
        obj = serialize(df, render_to="chart", output_type="json", rot=45)
        # self.assertTrue(False)
        # assert type(serialize(df, x="a", render_to="chart")) is str
        # assert type(serialize(df, x="a", y=("b",), render_to="chart")) is str
        # assert type(serialize(df, figsize=(100, 100), render_to="chart")) is str
