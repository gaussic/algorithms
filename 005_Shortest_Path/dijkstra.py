#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import deque

def build_graph():
    graph = {}
    graph['a'] = {'b': 5, 'd': 0}
    graph['b'] = {'c': 15, 'e': 20}
    graph['c'] = {'f': 20}
    graph['d'] = {'c': 30, 'e': 35}
    graph['e'] = {'f': 10}
    graph['f'] = {}

    return graph

def dijkstra(graph, start, finish):
    def find_lowest():
        lowest = infinity
        lowest_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest and node not in processed:
                lowest = cost
                lowest_node = node
        return lowest_node


    processed = []
    infinity = float('inf')
    costs = {}
    costs['a'] = infinity
    costs['b'] = infinity
    costs['c'] = infinity
    costs['d'] = infinity
    costs['e'] = infinity
    costs['f'] = infinity
    costs[start] = 0

    parents = {}
    parents['a'] = None
    parents['b'] = None
    parents['c'] = None
    parents['d'] = None
    parents['e'] = None
    parents['f'] = None

    node = find_lowest()
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest()
    return costs[finish], parents


if __name__ == '__main__':
    graph = build_graph()
    cost, parents = dijkstra(graph, 'a', 'f')
    print(cost)
    path = 'f'
    end = 'f'
    while parents[end] != 'a':
        path += ' <- ' + parents[end]
        end = parents[end]
    print(path + ' <- a')
