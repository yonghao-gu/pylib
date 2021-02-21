# -*- coding: utf-8 -*-

import threading
import tools

class CThread(threading.Thread):

    def set_func(self, func, args_list):
        self.m_func = func
        self.m_args = args_list
        self.m_result = []

    def run(self):
        if not self.m_func:
            return
        l = len(self.m_args)
        i=0
        for args in self.m_args:
            r = self.m_func(self, *args)
            i+=1
            print("run:", l -i, str(self))
            if r:
                self.m_result.append(r)
        print("thread_end:",str(self))
    
    def result(self):
        return self.m_result




def start_thread(func, thread_args, pool_size = 5):
    '''
    简单的线程池，函数内不能有竞争
    分配pool个线程做执行同一个函数
    '''

    
    thread_list = []
    result_list = []
    i=0
    thead_args_list = tools.split_list(thread_args, pool_size)
    for args_list in thead_args_list:
        i+=1
        obj = CThread()
        obj.setName("thread_%d"%i)
        obj.set_func(func, args_list)
        thread_list.append(obj)
        obj.start()
    
    for obj in thread_list:
        obj.join()
        print("done:",str(obj))
        result_list.extend(obj.result())
    return result_list

if __name__ == "__main__":
    import time
    def f(tobj, s):
        print("hello",s)
        return s
    ls = [(i,) for i in range(100)]
    print(start_thread(f, ls, 5))
