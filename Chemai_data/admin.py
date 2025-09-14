from django.contrib import admin
from .models import Chem_Database #Chem_Database.Chem_mol
from .models import Similarity_data #Similarity_data.Sim
from .models import Test_Chem_Database #Test_Chem_Database.Test_Chem_mol
from .models import Web_Function_Databas #Web_Function_Databas.Fun
from .models import File_data  # File_data.Fil
from .Manage_Chem_Database import Batch_Add_Chem_Database,Similarity_calculate_Chem_Database,\
    To_CSV_Test_Chem_Database,Data_InchIkey_see,Data_Synonyms_see,Data_CAS_see

class SimilarityInline(admin.TabularInline):
    model = Similarity_data.Sim
    extra = 0

#搜索引擎数据库
class TestAdmin(admin.ModelAdmin):
    inlines = [SimilarityInline]  # Inline
    admin.site.site_title = "化学分子数据"         #标签页标题
    admin.site.site_header = "数据库管理页面"              #页面标题
    admin.site.index_title = "数据平台管理-后台管理主页"

    fieldsets = (#关键字 #CAS # 分子名称 #SMILES表示 #正常沸点温度  #正常熔化温度  #密度  #导热系数  #电导率
        ["化学物质", {"fields":
                      ("InchIkey","CAS_Registry_Number_CAS", "Molecular_Formla","SMILES","Normal_boiling_temperature_Tb",
                       "Normal_melting_temperature_Tm",)
         }],
        ["其他信息", { 'classes': ('collapse',), # CSS
                      "fields": ("photo","Density", "Thermal_conductivity_Tcond", "Electrical_conductivity_econd","Synonyms",)
                  }],
    )
    search_fields = ('CAS_Registry_Number_CAS',) #后端关键字搜索
    list_display = ["CAS_Registry_Number_CAS", "Molecular_Formla"]# 在后台页面显示的字段
    actions = ['data_similarity', 'data_InchIkey_see', 'data_Synonyms_see', 'data_CAS_see']  # 自定义actions
    def data_similarity(self, request, queryset):
        Similarity_calculate_Chem_Database.data_similarity(queryset)  # 相似性比较
    data_similarity.short_description = "相似性比较"
    def data_InchIkey_see(self, request, queryset):
        Data_InchIkey_see.data_InchIkey_see(queryset)  # InchIkey重构
    data_InchIkey_see.short_description = "InchIkey重构"
    def data_Synonyms_see(self, request, queryset):
        Data_Synonyms_see.data_Synonyms_see(queryset)  # 搜索框架重构
    data_Synonyms_see.short_description = "搜索框架重构"
    def data_CAS_see(self, request, queryset):
        Data_CAS_see.data_CAS_see(queryset)  # CAS重构
    data_CAS_see.short_description = "CAS重构"
admin.site.register(Chem_Database.Chem_mol, TestAdmin)

#前端/用户上传数据库（待审核）
class TestAdmin_urser(admin.ModelAdmin):
    admin.site.site_title = "待审核化学分子数据"  # 标签页标题
    #admin.site.site_header = "待审核数据页面"  # 页面标题
    #admin.site.index_title = "待审核数据平台管理-后台管理主页标题"

    fieldsets = [
        ("关键字", {"fields": ["CAS_Registry_Number_CAS"]}),
        ("正常沸点温度", {"fields": ["Normal_boiling_temperature_Tb"]}),
        ("正常熔化温度", {"fields": ["Normal_melting_temperature_Tm"]}),
        ("密度", {"fields": ["Density"]}),
        ("导热系数", {"fields": ["Thermal_conductivity_Tcond"]}),
        ("电导率", {"fields": ["Electrical_conductivity_econd"]}),
    ]
    search_fields = ('CAS_Registry_Number_CAS',)  # 后端关键字搜索
    list_display = ["CAS_Registry_Number_CAS", "Normal_boiling_temperature_Tb"]# 在后台页面显示的字段
    actions = ['data_download'] #自定义actions
    def data_download(self, request, queryset):
        To_CSV_Test_Chem_Database.testdb_data_download(queryset) #写选择数据至文件
    data_download.short_description = "写数据库至文件"
admin.site.register(Test_Chem_Database.Test_Chem_mol, TestAdmin_urser)


#前端展示界面数据库
class QuestionAdmin(admin.ModelAdmin):
    admin.site.site_title = "网站链接数据"  # 标签页标题
    #admin.site.site_header = "网站功能页面"  # 页面标题
    #admin.site.index_title = "网站功能链接数据平台管理-后台管理主页标题"
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("ans", {"fields": ["ans_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    list_display = ["question_text", "ans_text", "pub_date", "was_published_recently"]# 在后台页面显示的字段
admin.site.register(Web_Function_Databas.Fun, QuestionAdmin)

#上传文件至项目
@admin.register(File_data.Fil)
class FilesAdmin(admin.ModelAdmin):
    admin.site.site_title = "文件上传数据"  # 标签页标题
    #admin.site.site_header = "文件信息数据页面"  # 页面标题
    #admin.site.index_title = "文件数据平台管理-后台管理主页标题"
    list_per_page = 10# 每页显示为10条
    list_display = ('id', 'file', 'file_name', 'create_time', 'host_ip', 'comment', 'isanalyse')# 在后台页面显示的字段
    actions = ['data_update']#自定义actions
    def data_update(self, request, queryset):
        for obj in queryset:
         Batch_Add_Chem_Database.testdb_data_update(obj.file_name)
    data_update.short_description = "读文件数据至数据库"

