
from django.shortcuts import render
from django.shortcuts import get_object_or_404

#前端用户搜索界面
def indextest(request):
    return render(request, "Chemai_data/indextext.html")


