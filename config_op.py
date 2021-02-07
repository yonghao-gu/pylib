# -*- coding: utf-8 -*-

import json


def load_config(file):
    f = open(file, "r", encoding="utf-8")
    s = f.read()
    data = json.loads(s)
    f.close()
    return data


    



