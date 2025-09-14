import csv
# 将数据库数据写入文件操作
def testdb_data_download(queryset):
    filename = 'C:\\Users\\86175\\Music\\01chemAIdatabase\\task1\\media\\newsreport\\media\\data.csv'
    # 写入 CSV 文件
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['关键字', '沸点', '熔点'])  # 写入表头
        for row in queryset:
            list = [row.CAS_Registry_Number_CAS, row.Normal_boiling_temperature_Tb, row.Normal_melting_temperature_Tm]
            writer.writerow(list)  # 写入每一行数据