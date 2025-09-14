from django.db import models
#化学信息数据库
class Chem_mol(models.Model):
    CAS_Registry_Number_CAS = models.CharField(max_length=200, verbose_name="CAS", default=0)  # CAS
    Thermal_conductivity_Tcond = models.CharField(max_length=200, default=0)  # 导热系数
    Electrical_conductivity_econd = models.CharField(max_length=200, default=0)  # 电导率
    Normal_boiling_temperature_Tb = models.CharField(max_length=200, default=0, verbose_name="常沸点温度")  # 常沸点温度
    Normal_melting_temperature_Tm = models.CharField(max_length=200, default=0, verbose_name="正常熔化温度")  # 正常熔化温度
    Compound_Name = models.CharField(max_length=200, default=0, verbose_name="化合物名称")  # 化合物名称
    PubChem_CID = models.CharField(max_length=200, default=0, verbose_name="PubChem_CID")  # PubChem_CID
    photo = models.CharField(max_length=200, default=0, verbose_name="结构")  # 结构
    Chemical_Safety = models.CharField(max_length=200, default=0, verbose_name="化学品安全")  # 化学品安全
    Molecular_Formla = models.CharField(max_length=200, default=0, verbose_name="分子式")  # 分子式
    Synonyms = models.CharField(max_length=500, default=0, verbose_name="同义词")  # 同义词（搜索匹配框）
    Molecular_Weight = models.CharField(max_length=200, default=0, verbose_name="分子量")  # 分子量
    Description = models.CharField(max_length=200, default=0, verbose_name="描述")  # 描述
    IUPAC_Name = models.CharField(max_length=200, default=0, verbose_name="IUPAC名称")  # IUPAC名称
    InchI = models.CharField(max_length=200, default=0, verbose_name="InchI")  # InchI
    InchIkey = models.CharField(max_length=200, default=0, verbose_name="InchIkey")  # InchIkey
    SMILES = models.CharField(max_length=200, default=0, verbose_name="SMILES表示")  # SMILES表示
    Molecular_Structure_Formla = models.CharField(max_length=200, default=0, verbose_name="分子结构式")  # 分子结构式
    XLogP3 = models.CharField(max_length=200, default=0, verbose_name="XLogP3")  # XLogP3
    Hydrogen_Bond_Donor_Count = models.CharField(max_length=200, default=0, verbose_name="氢键供体计数")  # 氢键供体计数
    Hydrogen_Bond_Acceptor_Count = models.CharField(max_length=200, default=0, verbose_name="氢键受体计数")  # 氢键受体计数
    Rotatable_Bond_Count = models.CharField(max_length=200, default=0, verbose_name="可旋转的键数")  # 可旋转的键数
    Exact_Mass = models.CharField(max_length=200, default=0, verbose_name="精确质量")  # 精确质量
    Monoisotopic_Mass = models.CharField(max_length=200, default=0, verbose_name="单同位素质量")  # 单同位素质量
    Topological_Polar_Surface_Area = models.CharField(max_length=200, default=0, verbose_name="拓扑极表面积")  # 拓扑极表面积
    Heavy_Atom_Count = models.CharField(max_length=200, default=0, verbose_name="重原子计数")  # 重原子计数
    Complexity = models.CharField(max_length=200, default=0, verbose_name="复杂性")  # 复杂性
    Isotope_Atom_Count = models.CharField(max_length=200, default=0, verbose_name="同位素原子数")  # 同位素原子数
    Defined_Atom_Stereocenter_Count = models.CharField(max_length=200, default=0,
                                                       verbose_name="定义的原子立体中心计数")  # 定义的原子立体中心计数
    Undefined_Atom_Stereocenter_Count = models.CharField(max_length=200, default=0,
                                                         verbose_name="未定义的原子立体中心计数")  # 未定义的原子立体中心计数
    Defined_Bond_Stereocenter_Count = models.CharField(max_length=200, default=0,
                                                       verbose_name="定义的键立体中心计数")  # 定义的键立体中心计数
    Undefined_Bond_Stereocenter_Count = models.CharField(max_length=200, default=0,
                                                         verbose_name="未定义的键立体中心计数")  # 未定义的键立体中心计数
    Covalently_Bonded_Unit_Count = models.CharField(max_length=200, default=0, verbose_name="共价键合单位计数")  # 共价键合单位计数
    Compound_Is_Canonicalized = models.CharField(max_length=200, default=0, verbose_name="复合词被规范化")  # 复合词被规范化
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
    Database_Log = models.CharField(max_length=200, default=0, verbose_name="数据库日志")  # 数据库日志
    Stability = models.CharField(max_length=200, default=0, verbose_name="稳定性")  # 稳定性
    Shelf_Life = models.CharField(max_length=200, default=0, verbose_name="保质期")  # 保质期
    Decomposition = models.CharField(max_length=200, default=0, verbose_name="分解")  # 分解
    Dissociation_Constants = models.CharField(max_length=200, default=0, verbose_name="解离常数")  # 解离常数
    Collision_Cross_Section = models.CharField(max_length=200, default=0, verbose_name="碰撞横截面")  # 碰撞横截面
    Kovats_Retention_Index = models.CharField(max_length=200, default=0, verbose_name="Kovats_保留指数")  # Kovats_保留指数
    Other_Experimental_Properties = models.CharField(max_length=200, default=0, verbose_name="其他实验性质")  # 其他实验性质
    SpringerMaterials_Properties = models.CharField(max_length=200, default=0,
                                                    verbose_name="SpringerMaterials_属性")  # SpringerMaterials_属性
    Chemical_Classes = models.CharField(max_length=200, default=0, verbose_name="化学类别")  # 化学类别
    Drugs = models.CharField(max_length=200, default=0, verbose_name="药物")  # 药物
    Human_Drugs = models.CharField(max_length=200, default=0, verbose_name="人用药物")  # 人用药物
    Animal_Drugs = models.CharField(max_length=200, default=0, verbose_name="动物药品")  # 动物药品
    te_1D_NMR_Spectra = models.CharField(max_length=200, default=0, verbose_name="一维核磁共振波谱")  # 一维核磁共振波谱
    te_2D_NMR_Spectra = models.CharField(max_length=200, default=0, verbose_name="2D_NMR_波谱")  # 2D_NMR_波谱
    Mass_Spectrometry = models.CharField(max_length=200, default=0, verbose_name="质谱法")  # 质谱法
    UV_Spectra = models.CharField(max_length=200, default=0, verbose_name="紫外光谱")  # 紫外光谱
    IR_Spectra = models.CharField(max_length=200, default=0, verbose_name="红外光谱")  # 红外光谱
    Raman_Spectra = models.CharField(max_length=200, default=0, verbose_name="拉曼光谱")  # 拉曼光谱
    Other_Spectra = models.CharField(max_length=200, default=0, verbose_name="其他光谱 ")  # 其他光谱
    Related_Compounds = models.CharField(max_length=200, default=0, verbose_name="相关化合物")  # 相关化合物
    class Meta:
        verbose_name = '化学分子信息'
        verbose_name_plural = '化学分子数据库'
        #db_table = 'Chem_mol'   #在数据库中的表名









