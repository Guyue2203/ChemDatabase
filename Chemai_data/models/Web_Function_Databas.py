from django.db import models
import datetime
from django.utils import timezone


#前端展示界面数据库(具体功能跳转）
class Fun(models.Model):
    question_text = models.CharField(max_length=200)
    ans_text = models.CharField(max_length=200, default=0)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    class Meta:
        verbose_name = '网站功能信息'
        verbose_name_plural = '网站功能链接数据库'
        #db_table = 'Chem_Fun'   #在数据库中的表名