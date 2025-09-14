from Chemai_data.models import Chem_Database #Chem_Database.Chem_mol
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import inchi
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
