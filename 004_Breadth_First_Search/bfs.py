#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import deque

def build_graph():
    graph = {}
    graph['you'] = ['alice', 'bob', 'claire']
    graph['bob'] = ['anuj', 'peggy']
    graph['alice'] = ['peggy']
    graph['claire'] = ['thom', 'peggy']
    graph['anuj'] = []
    graph['peggy'] = []
    graph['thom'] = []
    graph['jonny'] = []

    return graph

def person_is_seller(name):
    return name[-1] == 'm'

def bfs():
    graph = build_graph()

    search_queue = deque()
    search_queue += graph['you']

    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person in searched:
            continue
        if person_is_seller(person):
            print(person + " is a mango seller!")
            return True
        search_queue += graph[person]
        searched.append(person)
    return False

if __name__ == '__main__':
    print(bfs())
