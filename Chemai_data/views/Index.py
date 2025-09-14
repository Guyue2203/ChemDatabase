from Chemai_data.models import Web_Function_Databas #Web_Function_Databas.Fun
from django.shortcuts import render
#前端界面
def index(request):
    latest_question_list = Web_Function_Databas.Fun.objects.order_by("-pub_date")[:5] #按照提交时间对数据库排序
    context = {"latest_question_list": latest_question_list} #便于传html界面
    return render(request, "Chemai_data/index.html", context)

def stru(request):
    return render(request, "Chemai_data/structure_to_smiles.html")