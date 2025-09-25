from django.http import HttpResponse

from Chemai_data.models import Test_Chem_Database #Test_Chem_Database.Test_Chem_mol

# 数据库前端添加操作
def Add_Test(request):
    test1 = Test_Chem_Database.Test_Chem_mol(
        # 基本信息
        InchIkey=request.GET.get('关键字', ''),
        Normal_boiling_temperature_Tb=request.GET.get('正常沸点温度', ''),
        Normal_melting_temperature_Tm=request.GET.get('正常熔化温度', ''),
        Compound_Name=request.GET.get('化合物名称', ''),
        PubChem_CID=request.GET.get('PubChem_CID', ''),
        photo=request.GET.get('结构', ''),
        Chemical_Safety=request.GET.get('化学品安全', ''),
        Molecular_Formla=request.GET.get('分子式', ''),
        Molecular_Weight=request.GET.get('分子量', ''),
        Description=request.GET.get('描述', ''),
        
        # 化学标识符
        IUPAC_Name=request.GET.get('IUPAC_Name', ''),
        InchI=request.GET.get('InChI', ''),
        SMILES=request.GET.get('SMILES', ''),
        Molecular_Structure_Formla=request.GET.get('分子结构式', ''),
        CAS_Registry_Number_CAS=request.GET.get('CAS', ''),
        
        # 分子属性
        XLogP3=request.GET.get('XLogP3', ''),
        Hydrogen_Bond_Donor_Count=request.GET.get('氢键供体计数', ''),
        Hydrogen_Bond_Acceptor_Count=request.GET.get('氢键受体计数', ''),
        Rotatable_Bond_Count=request.GET.get('可旋转的键数', ''),
        Exact_Mass=request.GET.get('精确质量', ''),
        Monoisotopic_Mass=request.GET.get('单同位素质量', ''),
        Topological_Polar_Surface_Area=request.GET.get('拓扑极表面积', ''),
        Heavy_Atom_Count=request.GET.get('重原子计数', ''),
        Complexity=request.GET.get('复杂性', ''),
        Isotope_Atom_Count=request.GET.get('同位素原子数', ''),
        
        # 立体化学
        Defined_Atom_Stereocenter_Count=request.GET.get('定义的原子立体中心计数', ''),
        Undefined_Atom_Stereocenter_Count=request.GET.get('未定义的原子立体中心计数', ''),
        Defined_Bond_Stereocenter_Count=request.GET.get('定义的键立体中心计数', ''),
        Undefined_Bond_Stereocenter_Count=request.GET.get('未定义的键立体中心计数', ''),
        Covalently_Bonded_Unit_Count=request.GET.get('共价键合单位计数', ''),
        Compound_Is_Canonicalized=request.GET.get('复合词被规范化', ''),
        
        # 物理性质
        Physical_Description=request.GET.get('物理描述', ''),
        Color=request.GET.get('颜色', ''),
        Form=request.GET.get('形状 ', ''),
        Odor=request.GET.get('气味', ''),
        Boiling_Point=request.GET.get('沸点', ''),
        Melting_Pointnt=request.GET.get('熔点', ''),
        Flash_Point=request.GET.get('闪点', ''),
        Solubility=request.GET.get('溶解度', ''),
        Density=request.GET.get('密度', ''),
        Vapor_Pressure=request.GET.get('蒸气压', ''),
        
        # 其他属性
        Database_Log=request.GET.get('数据库日志', ''),
        Stability=request.GET.get('稳定性', ''),
        Shelf_Life=request.GET.get('保质期', ''),
        Decomposition=request.GET.get('分解', ''),
        Dissociation_Constants=request.GET.get('解离常数', ''),
        Collision_Cross_Section=request.GET.get('碰撞横截面', ''),
        Kovats_Retention_Index=request.GET.get('Kovats_保留指数', ''),
        Other_Experimental_Properties=request.GET.get('其他实验性质', ''),
        SpringerMaterials_Properties=request.GET.get('SpringerMaterials_属性', ''),
        
        # 分类信息
        Chemical_Classes=request.GET.get('化学类别', ''),
        Drugs=request.GET.get('药物', ''),
        Human_Drugs=request.GET.get('人用药物 ', ''),
        Animal_Drugs=request.GET.get('动物药品', ''),
        
        # 光谱数据
        _1D_NMR_Spectra=request.GET.get('一维核磁共振波谱', ''),
        _2D_NMR_Spectra=request.GET.get('2D_NMR_波谱', ''),
        Mass_Spectrometry=request.GET.get('质谱法', ''),
        UV_Spectra=request.GET.get('紫外光谱', ''),
        IR_Spectra=request.GET.get('红外光谱', ''),
        Raman_Spectra=request.GET.get('拉曼光谱', ''),
        Other_Spectra=request.GET.get('其他光谱', ''),
        Related_Compounds=request.GET.get('相关化合物', ''),
    )
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")