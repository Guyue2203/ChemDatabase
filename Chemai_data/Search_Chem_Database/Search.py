from django.http import HttpResponse
from django.shortcuts import render
from Chemai_data.models import Chem_Database #Chem_Database.Chem_mol
#from Chemai_data.models import Similarity_data    Similarity_data.Sim

# 可选依赖导入
try:
    from rdkit import Chem
    from rdkit.Chem import inchi
    RDKIT_AVAILABLE = True
except ImportError:
    RDKIT_AVAILABLE = False
    print("警告: rdkit 未安装，某些功能可能不可用")
# 接收前端用户请求数据用于搜索
def search(request,q_canshu):
    request.encoding = 'utf-8'
    tem = request.GET.get('q')#获取用户输入关键字
    if tem == None :
        tem = q_canshu #跳转查询，直接用参数作为关键字

    obj = Chem_Database.Chem_mol.objects.filter(Synonyms__icontains=tem)
    bool = Chem_Database.Chem_mol.objects.filter(Synonyms__icontains=tem).exists() #判断是否存在于数据库
    if bool == 0:
        return HttpResponse("<p>数据搜不到</p>")
    context_html = {}
    message = "message"
    context_html[message] = []
    for ob in obj:
        print(ob.InchIkey)
        print(ob.photo)
        context_html[message].append(ob)   # 传化学分子数据
    #context_html["message"] = ob  # 传化学分子数据
    #objlist = ob.sim_set.all  # 搜索化学分子相似性数据
    #context_html['simil'] = objlist #传化学分子相似性数据
    return render(request, "Chemai_data/data_all.html", context_html)#将查得数据返回展示界面
def search_sm(request,q_canshu):
    tem = q_canshu #跳转查询，直接用参数作为关键字
    obj = Chem_Database.Chem_mol.objects.filter(InchIkey=tem).first()  # 从数据库获得数据
    objlist = obj.sim_set.all  # 搜索化学分子相似性数据
    context_html = {}
    context_html['simil'] = objlist #传化学分子相似性数据
    return render(request, "Chemai_data/data_details.html", context_html)#将查得数据返回展示界面
def search_de(request,q_canshu):
    request.encoding = 'utf-8'
    tem = request.GET.get('q')  # 获取用户输入关键字
    if tem == None:
        tem = q_canshu  # 跳转查询，直接用参数作为关键字
    obj = Chem_Database.Chem_mol.objects.filter(Synonyms__icontains=tem)
    bool = Chem_Database.Chem_mol.objects.filter(Synonyms__icontains=tem).exists()  # 判断是否存在于数据库
    if bool == 0:
        return HttpResponse("<p>数据搜不到</p>")
    for ob in obj:
        context_html = {"message": ob}  # 传化学分子数据
        objlist = ob.sim_set.all  # 搜索化学分子相似性数据
    context_html['simil'] = objlist #传化学分子相似性数据
    return render(request, "Chemai_data/data_details_de.html", context_html)#将查得数据返回展示界面

