from django.http import HttpResponse

from Chemai_data.models import Test_Chem_Database #Test_Chem_Database.Test_Chem_mol

# 数据库前端添加操作
def Add_Test(request):
    test1 = Test_Chem_Database.Test_Chem_mol(Inchikey=request.GET['关键字'], Normal_boiling_temperature_Tb=request.GET['正常沸点温度'],
                       Normal_melting_temperature_Tm=request.GET['正常熔化温度'],)
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")