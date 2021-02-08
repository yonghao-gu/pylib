# -*- coding: utf-8 -*-
'''
    excelde 操作接口
'''

def write_result(filename, head_list, data_list):
	f=xlwt.Workbook()
	sheet = f.add_sheet("结果", cell_overwrite_ok=True)

	#0行标题
	def write_head(sheet):
		for i in range(len(head_list)):
			sheet.write(0, i, head_list[i])

	def wirte_data(sheet, index=None, key = None):
		j=0
		for ls in data_list:
			bwrite = True
			if index and len(ls) > index and ls[index] != key:
				bwrite = False
			if bwrite:
				j+=1
				for i in range(len(ls)):
					sheet.write(j, i, ls[i])

	write_head(sheet)
	wirte_data(sheet)

	index = g_conf[conf_key_2].index(spec_key_type)

	global g_fund_type
	for k, v in g_fund_type.items():
		sheet = f.add_sheet(k, cell_overwrite_ok=True)
		write_head(sheet)
		wirte_data(sheet, index, k)

	f.save(filename)



#读取配置
def read_config(filename):
	book_xlrd = xlrd.open_workbook(filename,formatting_info=True)
	#获取列表
	key = "关注基金"
	sheet = book_xlrd.sheet_by_name(key)
	assert sheet.nrows > 1, "配置文件 %s 标签 没有数据"%(key)
	global g_target_list
	for i in range(sheet.nrows-1):
		code = sheet.cell_value(i+1, 0)
		if type(code) != str:
			print("单元格类型错误：%d  %s %s"%(i+1, code, type(code)))
			continue
		if len(code) > 0 and not code in g_target_list :
			g_target_list.append(code)
	global g_conf
	key = "配置"
	sheet = book_xlrd.sheet_by_name(key)
	for i in range(sheet.nrows):
		name = sheet.cell_value(i, 0)
		vale = sheet.cell_value(i, 1)
		g_conf[name] = vale


	assert conf_key_1 in g_conf, "%s 配置不存在"%(conf_key_1)
	assert conf_key_2 in g_conf, "%s 配置不存在"%(conf_key_2)

	vale = g_conf[conf_key_1]
	g_conf[conf_key_1] = vale.split(",")
	vale = g_conf[conf_key_2]
	g_conf[conf_key_2] = vale.split(",")
	
