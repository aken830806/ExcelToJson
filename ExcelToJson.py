import xlrd
import json

data1 = xlrd.open_workbook('./quest.xlsx')
# 讀取第一個工作表
table = data1.sheets()[0]
# 統計行數
n_rows = table.nrows

data = []

for v in range(1, n_rows):
    # 每一行資料形成一個列表
    values = table.row_values(v)
    # 列表形成字典
    data.append({'question': values[0],
                 'answers': [values[1], values[2], values[3], values[4]],
                 'correct': int(values[5])
                 })
with open('./quest.json', 'w') as f:
    json.dump(data, f)
