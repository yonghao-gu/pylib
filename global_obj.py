# -*- coding: utf-8 -*-

g_objs = {}

def set(name, obj):
    global g_objs
    assert(not name in g_objs)
    g_objs[name] = obj

def get(name):
    return g_objs[name]




