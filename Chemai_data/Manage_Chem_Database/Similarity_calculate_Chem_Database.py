from Chemai_data.models import Similarity_data #Similarity_data.Sim

# 可选依赖导入
try:
    from rdkit import Chem
    from rdkit.Chem import rdMolDescriptors, DataStructs
    RDKIT_AVAILABLE = True
except ImportError:
    RDKIT_AVAILABLE = False
    print("警告: rdkit 未安装，某些功能可能不可用")

# 计算两个分子间的Tanimoto相似度
def calculate_similarity(smiles1, smiles2):
    try:
        # 将SMILES字符串转换为分子对象
        mol1 = Chem.MolFromSmiles(smiles1)
        mol2 = Chem.MolFromSmiles(smiles2)
        if mol1 is None or mol2 is None:
            raise ValueError("无效的SMILES字符串！无法解析:" ,str({smiles1}) ,str({smiles2}) )
        # 生成Morgan指纹（ECFP4），并计算Tanimoto相似度
        fp1 = rdMolDescriptors.GetMorganFingerprintAsBitVect(mol1, 2, nBits=1024)
        fp2 = rdMolDescriptors.GetMorganFingerprintAsBitVect(mol2, 2, nBits=1024)
        # 计算Tanimoto相似度
        similarity = DataStructs.TanimotoSimilarity(fp1, fp2)
        return int(similarity * 100) / 100
    except Exception as e:
        print("计算相似度时出错: ", {str(e)})
        return None
# 相似性比较
def data_similarity(queryset):
    for row in queryset:
        for len in queryset:
            smiles1 = row.SMILES
            smiles2 = len.SMILES
            if(smiles1 != smiles2):
                similarity = calculate_similarity(smiles1, smiles2)
                if similarity is not None and similarity > 0.25:  # 相似度大于30%
                    bool = Similarity_data.Sim.objects.filter(similarity_title=len.InchIkey,  test=row).exists()
                    if bool == 0:
                        Similarity_data.Sim.objects.create(similarity_title=len.InchIkey, similarity_photo=len.photo,
                                                           similarity_data=similarity, test=row,
                                                           similarity_mol=len.Molecular_Formla,)
                    #obj = Test.objects.filter(CAS_Registry_Number_CAS=CAS)  # 从数据库获得数据
                    #row.update()

