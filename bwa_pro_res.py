import pandas as pd
io = 'peach_p3.xlsx'
data = pd.read_excel(io,sheet_name="Sheet1",index_col=[0],nrows=17)
sum_reads = data.values[-1]
use_row = data.iloc[0:16].values.tolist()
res = []
for rows in use_row:
    value1 = []
    for i in range(len(sum_reads)):
        x = round(rows[i]/sum_reads[i],4)
        value1.append(x)
    res.append(value1)
output = pd.DataFrame(res)
output.to_excel("./res_peach_p3.xlsx")
