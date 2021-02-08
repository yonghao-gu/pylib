# -*- coding: utf-8 -*-
import requests

from urllib.parse import urlencode, quote

def js2py_val(val):
    import demjson
    import ast
    try:
        val = ast.literal_eval(val) 
    except BaseException as error:
        val = demjson.decode(val)
    return val

def url_encode(url,data):
    return url + "?" + urlencode(data)

def _set_headers(headers = None):
    headers = headers if headers else {}
    if not "User-Agent" in headers:
        headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"
    return headers

def is_not_ok(result):
    if result.status_code == 200:
        return False
    return True


def get_url(url, **kwg):
    headers = _set_headers(kwg.get("headers", None))
    session = kwg.get("session", None)
    params = kwg.get("params", None)
    
    if session:
        getfunc = session.get
    else:
        getfunc = requests.get
    result = getfunc(url = url, headers = headers, params = params)
    result.encoding ="utf-8"
    return result,session

def new_session():
    return requests.session()




