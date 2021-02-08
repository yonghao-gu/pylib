# -*- coding: utf-8 -*-
import time
import log
import types

def __default_log(*args):
    print("已用时",args)

def check_use_time(time_limit = 0, log = None, desc = None):
    log = log if log else print
    desc = desc if desc else "流程总用时："
    def default_decorator(func):
        def wrappend_func(*args, **kwargs):
            fs = time.time()
            ret = func(*args, **kwargs) 
            if time.time() - fs > time_limit:
                if type(desc) == types.FunctionType:
                    s = desc(*args, **kwargs)
                    if s:
                        log("%s %d"%(s, time.time() - fs))
                    else:
                        log("desc function false")
                else:
                    log("%s %d"%(desc, time.time() - fs))
            return ret
        return wrappend_func
    return default_decorator


def global_log(*args):
    log.Sys(*args)

def is_float(s):
    try:
        float(s)
    except BaseException as e:
        return False
    return True


def tofloat(s, point = 2):
    if not is_float(s) :
        return 0.0
    fmt = "%%.%df"%(point)
    return float(fmt%(float(s)))

def split_list(ls, n):
    '''
    将ls列表切分为n份
    '''
    length = len(ls)
    step = int(length/n)+1
    newlist = []
    for i in range(0, length, step):
        newlist.append(ls[i:i+step])
    return newlist


