from Chemai_data.models import Chem_Database #Chem_Database.Chem_mol

# 可选依赖导入
try:
    from rdkit import Chem
    RDKIT_AVAILABLE = True
except ImportError:
    RDKIT_AVAILABLE = False
    print("警告: rdkit 未安装，某些功能可能不可用")
    # 占位符导入
    Draw = None
    inchi = None
import re
# CAS重构
def data_CAS_see(queryset):
    for row in queryset:
        match = re.match('(\d{2,7}-\d\d-\d)', row.CAS_Registry_Number_CAS)
        if match:
            CAS = row.CAS_Registry_Number_CAS
        else:
            CAS = '无'
        obj = Chem_Database.Chem_mol.objects.filter(SMILES=row.SMILES)
        obj.update(CAS_Registry_Number_CAS=CAS)
