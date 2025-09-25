from Chemai_data.models import Chem_Database #Chem_Database.Chem_mol

# 可选依赖导入
try:
    from rdkit import Chem
    from rdkit.Chem import Draw
    from rdkit.Chem import inchi
    RDKIT_AVAILABLE = True
except ImportError:
    RDKIT_AVAILABLE = False
    print("警告: rdkit 未安装，某些功能可能不可用")
    # 占位符导入
    Chem = None
    Draw = None
    inchi = None

# Synonyms重构
def data_Synonyms_see(queryset):
    for row in queryset:
        tem = row.CAS_Registry_Number_CAS + ' '
        tem += row.Compound_Name + ' '
        tem += row.PubChem_CID + ' '
        tem += row.Molecular_Formla + ' '
        tem += row.IUPAC_Name + ' '
        tem += row.InchIkey + ' '
        tem += row.SMILES + ' '
        row.Synonyms = tem
        row.save()