from src.machine import *
import re
import networkx as nx
import matplotlib.pyplot as plt
from src.scraping import *
import random


class Model:
    def __init__(self):
        self.graph = nx.MultiDiGraph()
        self.graph.add_node(0)
        self.data = {}

    def add_step(self, step, function, prev_step=0, inputs=[], save_data=False):
        self.graph.nodes(step)
        self.graph.add_edge(prev_step, step, outputs=None)
        self.graph.nodes[step]["function"] = function
        self.graph.nodes[step]["inputs"] = inputs
        self.graph.nodes[step]["save_data"] = save_data

    def run(self):
        edges = self.graph.out_edges(0)
        next_nodes = [edge[1] for edge in edges]

        while next_nodes:
            current_nodes = next_nodes
            next_nodes = []

            for node in current_nodes:
                # Get the function
                function = self.graph.nodes[node]["function"]
                inputs = self.graph.nodes[node]["inputs"]
                save_data = self.graph.nodes[node]["save_data"]

                # Call the function
                in_edges = self.graph.in_edges(node, keys=True)
                data = self._get_data_from_in_edges(in_edges)
                outputs = self._get_outputs_from_function(function, data, inputs, save_data)

                # Save outputs to edge data
                edges = self.graph.out_edges(node, keys=True)
                for edge in edges:
                    next_nodes.append(edge[1])
                    t_edge = self.graph.edges[edge]
                    t_edge["outputs"] = outputs
        return

    def _get_data_from_in_edges(self, edges):
        for edge in edges:
            data = self.graph.edges[edge]["outputs"]
            return data

    def _run_function(self):
        return

    def _get_outputs_from_function(self, function, data, inputs, save_data=False):
        if type(data) is dict:
            t_data = function(*inputs, **data)
        elif type(data) is list:
            t_data = function(*inputs, *data)
        else:
            t_data = function(*inputs, data)

        if save_data:
            for d in t_data:
                self.data[d] = t_data[d]
        return t_data

