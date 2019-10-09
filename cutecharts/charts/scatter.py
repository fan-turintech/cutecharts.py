from typing import Iterable, Optional

from cutecharts.charts.basic import BasicChart


class Scatter(BasicChart):

    CHART_TYPE = "XY"

    def set_options(
        self,
        x_label: str = "",
        y_label: str = "",
        x_tick_count: int = 3,
        y_tick_count: int = 3,
        is_show_line: bool = False,
        dot_size: int = 1,
        time_format: Optional[str] = None,
        legend_pos: str = "upLeft",
        colors: Optional[Iterable] = None,
        font_family: Optional[str] = None,
    ):
        """
        :param x_label:
        :param y_label:
        :param x_tick_count:
        :param y_tick_count:
        :param is_show_line:
        :param dot_size:
        :param time_format:
        :param legend_pos:
        :param colors:
        :param font_family:
        """
        self.opts.update({"xLabel": x_label, "yLabel": y_label})
        self.opts["options"] = {
            "xTickCount": x_tick_count,
            "yTickCount": y_tick_count,
            "legendPosition": self._switch_pos(legend_pos),
            "dataColors": colors,
            "fontFamily": font_family,
            "showLine": is_show_line,
            "dotSize": dot_size,
            "timeFormat": time_format,
        }
        return self

    def add_series(self, name: str, data: Iterable):
        """
        :param name:
        :param data:
        """
        pairs = [{"x": item[0], "y": item[1]} for item in data]
        self.opts["data"]["datasets"].append({"label": name, "data": pairs})
        return self
