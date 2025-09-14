from Chemai_data.models import Chem_Database #Chem_Database.Chem_mol
import csv
import pubchempy as pcp
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import inchi
# 读取 CSV 文件并转换为列表
def csv_to_list(filename):
    data_list = []
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)   #创建一个 csv.reader 对象，用于读取 CSV 文件
        for row in reader:
            data_list.append(row)
    return data_list

# 将文件数据读入数据库操作
def testdb_data_update(file):
    filename='C:\\Users\\86175\\Music\\01chemAIdatabase\\task1\\media\\Chemai_data\\media\\'+file
    data_list_tom = csv_to_list(filename)# 读取 CSV 文件
    # 更新或插入数据到数据库
    #if i >= 5:break
    i = 0
    for row in data_list_tom:
        i = i + 1
        if i == 1:
            continue
        try:
            SMILES = row[7]  # 从 CSV 行数据中提取关键字 .strip()
            Formula = row[1]
            InchIkey = row[6]
            obj, created = Chem_Database.Chem_mol.objects.get_or_create(
                InchIkey=InchIkey)  # 没有则创建
            obj = Chem_Database.Chem_mol.objects.filter(InchIkey=InchIkey)  # 从数据库获得数据
            obj.update(Molecular_Formla=Formula,
                       SMILES=SMILES, InchIkey=InchIkey,)
            if i % 100 == 0:
                print(i)
        except:
            continue

