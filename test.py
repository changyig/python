import xlrd
import xlwt

data = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\tableExport.xlsx')
table = data.sheets()[0] # 打开第一张表
nrows = table.nrows # 获取表的行数
ncols = table.ncols # 获取表的列数
for i in range(nrows): # 循环逐行打印
    if i == 0:# 跳过第一行
        continue
    print (table.row_values(i) )# 取前十三列

