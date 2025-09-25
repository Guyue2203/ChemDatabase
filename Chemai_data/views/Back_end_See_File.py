#后端文件预览
from django.shortcuts import redirect
def get_file(request):
    # 进行字符串切割，取文件的名字。  -1参数代表 数组的最后一个
    filename = request.path.split('/')[-1]
    return redirect('/media/' + filename)
def get_file_see(request,q_canshu):
    return redirect('/media/' + q_canshu)