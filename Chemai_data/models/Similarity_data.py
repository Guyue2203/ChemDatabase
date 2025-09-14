from django.db import models
from .Chem_Database import Chem_mol

#相似性比较数据体
class Sim(models.Model):
    test = models.ForeignKey(Chem_mol, on_delete=models.CASCADE, )
    similarity_title = models.CharField(max_length=200, default=0, verbose_name="相似性名字")#相似性名字
    similarity_mol = models.CharField(max_length=200, default=0, verbose_name="分子式")  # 分子名字
    similarity_photo = models.CharField(max_length=200, default=0, verbose_name="结构")  # 结构
    similarity_data = models.CharField(max_length=200, default=0, verbose_name="相似性比例") #相似性比例
    CAS_Registry_Number_CAS = models.CharField(max_length=200, default=0,verbose_name="CAS")  # CAS
    Electrical_conductivity_econd = models.CharField(max_length=200, default=0)  # 电导率
    Compound_Name = models.CharField(max_length=200, default=0, verbose_name="化合物名称")  # 化合物名称
    PubChem_CID = models.CharField(max_length=200, default=0, verbose_name="PubChem_CID")  # PubChem_CID
    photo = models.CharField(max_length=200, default=0, verbose_name="结构")  # 结构
    Molecular_Formla = models.CharField(max_length=200, default=0, verbose_name="分子式")  # 分子式
    Synonyms = models.CharField(max_length=500, default=0, verbose_name="同义词")  # 同义词（搜索匹配框）
    Molecular_Weight = models.CharField(max_length=200, default=0, verbose_name="分子量")  # 分子量
    Description = models.CharField(max_length=200, default=0, verbose_name="描述")  # 描述
    IUPAC_Name = models.CharField(max_length=200, default=0, verbose_name="IUPAC名称")  # IUPAC名称
    InchI = models.CharField(max_length=200, default=0, verbose_name="InchI")  # InchI
    InchIkey = models.CharField(max_length=200, default=0, verbose_name="InchIkey")  # InchIkey
    SMILES = models.CharField(max_length=200, default=0, verbose_name="SMILES表示")  # SMILES表示
    Molecular_Structure_Formla = models.CharField(max_length=200, default=0, verbose_name="分子结构式")  # 分子结构式
    Physical_Description = models.CharField(max_length=200, default=0, verbose_name="物理描述")  # 物理描述
    Color = models.CharField(max_length=200, default=0, verbose_name="颜色")  # 颜色
    Form = models.CharField(max_length=200, default=0, verbose_name="形状")  # 形状
    Odor = models.CharField(max_length=200, default=0, verbose_name="气味")  # 气味
    Boiling_Point = models.CharField(max_length=200, default=0, verbose_name="沸点")  # 沸点
    Melting_Pointnt = models.CharField(max_length=200, default=0, verbose_name="熔点")  # 熔点
    Flash_Point = models.CharField(max_length=200, default=0, verbose_name="闪点")  # 闪点
    Solubility = models.CharField(max_length=200, default=0, verbose_name="溶解度")  # 溶解度
    Density = models.CharField(max_length=200, default=0, verbose_name="密度")  # 密度
    Vapor_Pressure = models.CharField(max_length=200, default=0, verbose_name="蒸气压")  # 蒸气压
    Related_Compounds = models.CharField(max_length=200, default=0, verbose_name="相关化合物")  # 相关化合物
    class Meta:
        ordering = ['-similarity_data']
