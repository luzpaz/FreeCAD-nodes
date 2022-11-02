# -*- coding: utf-8 -*-
###################################################################################
#
#  text_text_in.py
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
from editor.nodes_conf import register_node
from editor.nodes_base_node import FCNNode
from nodes_locator import icon


@register_node
class TextIn(FCNNode):

    icon: str = icon("nodes_default.png")
    op_title: str = "Text In"
    op_category: str = "Text"
    content_label_objname: str = "fcn_node_bg"

    def __init__(self, scene):
        super().__init__(scene=scene,
                         inputs_init_list=[(3, "In", 1, "Enter text", False, ("str", ))],
                         outputs_init_list=[(3, "Out", 0, 0, True, ("str", ))],
                         width=150)

    def collapse_node(self, collapse: bool = False):
        super().collapse_node(collapse)

        if collapse is True:
            self.title = 'In: ' + str(self.sockets_input_data[0][0])
        else:
            self.title = self.default_title

    def eval_operation(self, sockets_input_data: list) -> list:
        self.collapse_node(self.content.isHidden())

        in_val: str = sockets_input_data[0][0]
        return [[in_val]]
