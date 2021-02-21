# -*- coding: utf-8 -*-
'''
    excelde 操作接口
	依赖 xlwt
'''

import xlwt
import log

class CSheetObject(object):
	'''
		定义一个标签页的数据
		m_name: 标签名
		m_head: 第一行数据
		m_data: 数据
	'''
	def __init__(self, name, head_list, data_list):
		
		self.m_name = name
		self.m_head = head_list
		self.m_data = data_list
	
	def save(self, f):
		sheet = f.add_sheet(self.m_name, cell_overwrite_ok = True)
		for i, data in enumerate(self.m_head):
			sheet.write(0, i, data)
		for j,ls in enumerate(self.m_data):
			for i, data in enumerate(ls):
				sheet.write(j+1, i, data)


def save_excel(filename, sheetobj_list):
	'''
		将数据写入excel
		filename:保存的文件名，不带后缀
		sheetobj_list: 数据对象CSheetObject列表
	'''
	f =xlwt.Workbook()
	for obj in sheetobj_list:
		obj.save(f)
	f.save(filename+".xls")


if __name__ == "__main__":
	obj_list = []
	for i in range(10):
		head_list = [ "头_%s_%s"%(i,k) for k in range(10)]
		data_list = []
		for j in range(100):
			data_list.append(["数据_%s_%s_%s"%(i,k,j) for k in range(10)])
		obj_list.append(CSheetObject("标签"+str(i), head_list, data_list))
	print("save_data")
	save_excel("测试", obj_list)

