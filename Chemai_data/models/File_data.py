from django.db import models
from django import forms

#项目动态文件数据库
class UploadFileForm(forms.Form):
    file = forms.FileField()
class Fil(models.Model):
    file = models.FileField(u'文件', upload_to='Chemai_data/media', null=False, blank=False)
    file_name = models.CharField(u'文件名称', max_length=50, default='data.csv', null=False)
    create_time = models.DateTimeField(u'创建时间', null=False)
    host_ip = models.CharField(u'主机IP', max_length=50, default='127.0.0.1', null=False)
    comment = models.CharField(u'备注说明', max_length=100, null=False)
    isanalyse = models.BooleanField(u'是否分析', default='0', null=False)
    class Meta:
        verbose_name = '文件上传库信息'
        verbose_name_plural = '文件数据库'
        #db_table = 'Chem_Fil'   #在数据库中的表名