import os

from bokeh.properties import Dict, String, Any
from bokeh.models.widgets.layouts import BaseBox
from bokeh.properties import Int, Instance, List

from examples.app.crossfilter.models.helpers import load_component

class StyleableBox(BaseBox):
    '''
    styleable box inherits from base box and is able to take a dictionary
    of arbitary css to apply at the element level.
    '''
    __implementation__ = load_component('./styleable_box.coffee')
    css_properties = Dict(String, Any, default=None)
    orientation = String(default='vertical')

class StatsBox(BaseBox):
    __implementation__ = load_component('./stats_box.coffee')
    stylesheet = String(default='//s3.amazonaws.com/bcollins/stats_box.css')
    display_items = Dict(String, Any, default=None)