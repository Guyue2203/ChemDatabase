
from django.shortcuts import render

#前端用户提交数据界面
def Add_test_htm(request):
    return render(request, "Chemai_data/Add_Test_Submit.html")