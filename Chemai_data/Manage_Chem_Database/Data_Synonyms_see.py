from Chemai_data.models import Chem_Database #Chem_Database.Chem_mol
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import inchi

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
        tem += row.Molecular_Structure_Formla + ' '
        obj = Chem_Database.Chem_mol.objects.filter(SMILES=row.SMILES)
        obj.update(Synonyms=tem)


