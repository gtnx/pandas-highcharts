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
```shell
pip install pandas-highcharts
```

## Usage ##

Import it in your views
```python
import pandas_highcharts
df = ... # create your dataframe here
chart = pandas_highcharts.serialize(df, render_to = "my-chart")
```

In your templates
```html
<script type="text/javascript">{{chart|safe}}</script>
```

## More examples ##

Please read the doc for [DataFrame.plot](http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.plot.html "DataFrame plot").

For example, with the following dataset:
```
                             A          B     C
ts                                             
2015-01-01 00:00:00   27451873   29956800   113
2015-01-01 01:00:00   20259882   17906600    76
2015-01-01 02:00:00   11592256   12311600    48
2015-01-01 03:00:00   11795562   11750100    50
2015-01-01 04:00:00    9396718   10203900    43
2015-01-01 05:00:00   14902826   14341100    53
2015-01-01 06:00:00   27878455   27450700   109
2015-01-01 07:00:00   62563571   77761700   279
2015-01-01 08:00:00  123979183  158475200   584
2015-01-01 09:00:00  159733967  186497100   697
2015-01-01 10:00:00  224024455  274005300  1059
2015-01-01 11:00:00  203558997  240244500   949
2015-01-01 12:00:00  181730017  220095200   872
2015-01-01 13:00:00  183521529  210786800   813
2015-01-01 14:00:00  184333340  196088000   792
2015-01-01 15:00:00  198958135  225854600   929
2015-01-01 16:00:00  227565646  281281500  1192
2015-01-01 17:00:00  264734170  304714000  1355
2015-01-01 18:00:00  253035493  291283300  1302
2015-01-01 19:00:00  228659067  278433700  1216
2015-01-01 20:00:00  216566461  253334000  1169
2015-01-01 21:00:00  184539542  217624800  1003
2015-01-01 22:00:00  132411838  159676700   741
2015-01-01 23:00:00   72335111   75259700   363
2015-01-02 00:00:00   36097469   40844200   191
2015-01-02 01:00:00   18945926   18913200    86
2015-01-02 02:00:00    9954998   12976500    51
2015-01-02 03:00:00    7887019   10425600    40
2015-01-02 04:00:00    9708571    7487000    36
2015-01-02 05:00:00   18935553   20825500    92
2015-01-02 06:00:00   43805222   50144200   191
2015-01-02 07:00:00   91625552   94582900   382
2015-01-02 08:00:00  155759760  180028900   756
2015-01-02 09:00:00  198733831  213857100   836
2015-01-02 10:00:00  220696225  242112100   934
2015-01-02 11:00:00  197343578  228084400   875
2015-01-02 12:00:00  206145921  211427800   853
2015-01-02 13:00:00  147601735  169716500   638
```

