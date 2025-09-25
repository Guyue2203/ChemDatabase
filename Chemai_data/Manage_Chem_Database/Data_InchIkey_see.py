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

# InchIkey重构
def data_InchIkey_see(queryset):
    for row in queryset:
        mol = Chem.MolFromSmiles(row.SMILES)
        inchi_str = inchi.MolToInchi(mol)
        InchIkey = inchi.InchiToInchiKey(inchi_str)
        obj = Chem_Database.Chem_mol.objects.filter(SMILES=row.SMILES)
        obj.update(InchIkey=InchIkey)
