# coding=utf-8
import xlrd

data1 = xlrd.open_workbook('./dict.xlsx')
# 讀取第一個工作表
table = data1.sheets()[0]
# 統計行數
n_rows = table.nrows

data = {}

for v in range(0, n_rows):
    # 每一行資料形成一個列表
    values = table.row_values(v)
    print("'"+values[0]+"':'"+values[1]+"',")
