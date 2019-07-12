from django.shortcuts import render,render_to_response
from Selfblog.models import *

def base(request):
    return render(request,'base.html')

def index(request):
    article=Article.objects.get(title='背影')
    article1=Article.objects.filter()[3:5]
    article2 = Article.objects.filter()[5:7]
    message=Message.objects.all().order_by('-time')[0:5]
    picture=Pictures.objects.filter()[:3]
    return render(request,'index.html',locals())

def article_list(request,id):
    article_lists=Article.objects.filter(types_id=id)
    typ=Types.objects.get(id=id)
    name=typ.types
    return render(request,'article_list.html',locals())
def article(request,id):
    arts=Article.objects.get(id=int(id))
    if not request.COOKIES.get('read'):
        arts.read_num+=1
        arts.save()
    response=render_to_response('article.html',locals())
    response.set_cookie('read','True')
    return response

def pictures(request):
    pict=Pictures.objects.all()
    return render(request,'pictures.html',locals())

def message(request):
    result={'data':''}
    message = Message.objects.all().order_by('-time')[0:5]
    if request.method=='POST':
        name=request.POST.get('name')
        message=request.POST.get('message')
        if name and message:
            mes=Message()
            mes.name=name
            mes.message=message
            mes.save()
            result['data']='留言成功'
        else:
            result['data']='填写不完整'
    return render(request,'message.html',result)
def contactme(request):
    reseult={'data':''}
    if request.method=='POST':
        touch=Touch()
        name=request.POST.get('name')
        gender=request.POST.get('gender')
        phone=request.POST.get('phone')
        if name and gender and phone:
            touch.name=name
            touch.gender=gender
            touch.phone=phone
            touch.save()
            reseult['data']='提交成功'
        else:
            reseult['data']='不能有空项哦'
    return render(request,'contactme.html',reseult)
# Create your views here.
