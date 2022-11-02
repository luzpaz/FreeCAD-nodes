# -*- coding: utf-8 -*-
###################################################################################
#
#  number_number_range.py
#
#  Copyright (c) 2022 Ronny Scharf-Wildenhain <ronny.scharf08@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
###################################################################################
import awkward as ak
import numpy as np

from editor.nodes_conf import register_node
from editor.nodes_base_node import FCNNode
from nodes_locator import icon


@register_node
class NumberRange(FCNNode):

    icon: str = icon("nodes_default.png")
    op_title: str = "Number Range"
    op_category: str = "Number"
    content_label_objname: str = "fcn_node_bg"

    def __init__(self, scene):
        super().__init__(scene=scene,
                         inputs_init_list=[(0, "Start", 1, 0, True, ('int', 'float')),
                                           (0, "Stop", 1, 10, True, ('int', 'float')),
                                           (0, "Step", 1, 1, False, ('int', 'float'))],
                         outputs_init_list=[(0, "Out", 0, 0, True, ('int', 'float'))],
                         width=150)

    def eval_operation(self, sockets_input_data: list) -> list:
        # Inputs
        start = sockets_input_data[0]
        stop = sockets_input_data[1]
        step = sockets_input_data[2][0]

        # Force array broadcast
        start, stop = ak.broadcast_arrays(start, stop)

        res = []
        for idx, _start in enumerate(ak.flatten(start, axis=None)):
            _stop = ak.flatten(stop, axis=None)[idx]
            res.append(np.arange(_start, _stop, step).tolist())

        return [res]
