from pyecharts.charts import Line
from pyecharts.options import TitleOpts
line = Line()
line.add_xaxis(["2017-10-24", "2017-10-25", "2017-10-26", "2017-10-27", "2017-10-28", "2017-10-29", "2017-10-30"])
line.add_yaxis("商家A", [11, 12, 13, 14, 15, 16, 17])
line.add_yaxis("商家B", [21, 22, 23, 24, 25, 26, 27])
line.add_yaxis("商家C", [31, 32, 33, 34, 35, 36, 37])
line.set_global_opts(
    title_opts=TitleOpts(title="某商场销售数据", subtitle="纯属虚构",pos_left="center", pos_top="1%")
)
line.render()