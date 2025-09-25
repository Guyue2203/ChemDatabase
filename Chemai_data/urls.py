
from django.urls import path
from .views import Index,Add_Test_htm,Search_htm
from django.urls import re_path as url
from .Search_Chem_Database import Search
from .Manage_Chem_Database import Add_Test_Chem_Database,Batch_Add_Chem_Database,\
    Similarity_calculate_Chem_Database,To_CSV_Test_Chem_Database
from .views import Back_end_See_File

app_name = "Chemai_data"
urlpatterns = [
    path("", Index.index, name="index"), #前端界面
    path("stru/", Index.stru, name="stru"), #图像界面
    path("test/", Search_htm.indextest, name="indextest"),  # 前端用户搜索界面
    path('testdb/', Add_Test_htm.Add_test_htm),   # 前端用户提交数据界面
    url('testdb_url/', Add_Test_Chem_Database.Add_Test),  # 数据库前端添加操作
    path('Search_Chem_Database/Search/<q_canshu>/', Search.search),  # 接收请求数据
    path('Search_Chem_Database/Search_de/<q_canshu>/', Search.search_de),  # 详细数据
    path('Search_Chem_Database/Search_sm/<q_canshu>/', Search.search_sm),  # 详细数据
]