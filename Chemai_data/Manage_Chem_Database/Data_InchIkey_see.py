from Chemai_data.models import Chem_Database #Chem_Database.Chem_mol
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import inchi

# InchIkey重构
def data_InchIkey_see(queryset):
    for row in queryset:
        mol = Chem.MolFromSmiles(row.SMILES)
        inchi_str = inchi.MolToInchi(mol)
        InchIkey = inchi.InchiToInchiKey(inchi_str)
        obj = Chem_Database.Chem_mol.objects.filter(SMILES=row.SMILES)
        obj.update(InchIkey=InchIkey)
