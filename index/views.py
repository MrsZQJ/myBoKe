from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from .models import Banner,Category,Article
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage

# Create your views here.
BASE_URL = 'http://127.0.0.1:8000/'

def index(request):
    return render(request,'index.html')

def s_banner(request):
    """
    查询轮播图数据
    :param request:
    :return:
    """
    banner_list = Banner.objects.filter(is_active=True)
    banner_obj = []
    for i in banner_list:
        data = {}
        data['img_url'] = BASE_URL + str(i.img)
        data['link_url'] = i.link_url
        data['text_info'] = i.text_info
        banner_obj.append(data)
    return JsonResponse(banner_obj,safe=False)

def s_category(request):
    """
    查询博客分类数据
    :param request:
    :return:
    """
    category_list = Category.objects.all().order_by('-index')
    c_data = []
    for i in category_list:
        data = {}
        data['c_name'] = i.name
        data['link_url'] = i.link_url
        c_data.append(data)
    return JsonResponse(c_data,safe=False)

def s_new_article(request):
    """
    查询最新文章10篇
    :param request:
    :return:
    """
    new_article = Article.objects.all().order_by('-id')[0:10]
    article_list = []
    for i in new_article:
        data = {}
        data['id'] = i.id
        data['title'] = i.title
        data['excerpt'] = i.excerpt
        data['category'] = str(i.category)
        data['img'] = BASE_URL + str(i.img)
        data['user'] = str(i.user)
        # data['views'] = i.views
        data['created_time'] = str(i.created_time).split(' ')[0]
        article_list.append(data)
    return JsonResponse(article_list,safe=False)

def s_detail_artical(request):
    """
    查询文章内容
    :param request:
    :return:
    """
    a_detail = Article.objects.filter(id=request.GET.get('a_id'))
    a_detaila_data = {}
    for i in a_detail:
        a_detaila_data['id'] = i.id
        a_detaila_data['title'] = i.title
        a_detaila_data['category'] = str(i.category)
        a_detaila_data['body'] = i.body
        a_detaila_data['user'] = str(i.user)
        a_detaila_data['created_time'] = str(i.created_time).split(' ')[0]
    return JsonResponse(a_detaila_data,safe=False)

def s_web(request):
    """
    查询web文章类的数据
    :param request:
    :return:
    """
    category_id = Category.objects.filter(name="web前端").values()
    category_id = list(category_id)[0]['id']
    web_data = Article.objects.filter(category_id=category_id).order_by('-id')
    paginator = Paginator(web_data,15)
    if request.method == "GET":
        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page')
        try:
            lists = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            lists = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            lists = paginator.page(paginator.num_pages)
    r_w_data = []
    for i in lists:
        data = {}
        data['id'] = i.id
        data['title'] = i.title
        data['excerpt'] = i.excerpt
        data['category'] = str(i.category)
        data['img'] = BASE_URL + str(i.img)
        data['user'] = str(i.user)
        # data['views'] = i.views
        data['created_time'] = str(i.created_time).split(' ')[0]
        r_w_data.append(data)
    all_data = {}
    all_data['data'] = r_w_data
    all_data['count'] = paginator.count
    all_data['num_pages'] = int(page)
    all_data['totalPage'] = paginator.num_pages
    return JsonResponse(all_data,safe=False)

def s_python(request):
    """
    查询python文章类的数据
    :param request:
    :return:
    """
    category_id = Category.objects.filter(name="python").values()
    category_id = list(category_id)[0]['id']
    web_data = Article.objects.filter(category_id=category_id).order_by('-id')
    paginator = Paginator(web_data, 15)
    if request.method == "GET":
        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page')
        try:
            lists = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            lists = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            lists = paginator.page(paginator.num_pages)
    r_w_data = []
    for i in lists:
        data = {}
        data['id'] = i.id
        data['title'] = i.title
        data['excerpt'] = i.excerpt
        data['category'] = str(i.category)
        data['img'] = BASE_URL + str(i.img)
        data['user'] = str(i.user)
        # data['views'] = i.views
        data['created_time'] = str(i.created_time).split(' ')[0]
        r_w_data.append(data)
    all_data = {}
    all_data['data'] = r_w_data
    all_data['count'] = paginator.count
    all_data['num_pages'] = int(page)
    all_data['totalPage'] = paginator.num_pages
    return JsonResponse(all_data, safe=False)

def s_myself(request):
    """
    查询我的日记文章类的数据
    :param request:
    :return:
    """
    category_id = Category.objects.filter(name="我的日记").values()
    category_id = list(category_id)[0]['id']
    web_data = Article.objects.filter(category_id=category_id).order_by('-id')
    paginator = Paginator(web_data, 15)
    if request.method == "GET":
        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page')
        try:
            lists = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            lists = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            lists = paginator.page(paginator.num_pages)
    r_w_data = []
    for i in lists:
        data = {}
        data['id'] = i.id
        data['title'] = i.title
        data['excerpt'] = i.excerpt
        data['category'] = str(i.category)
        data['img'] = BASE_URL + str(i.img)
        data['user'] = str(i.user)
        # data['views'] = i.views
        data['created_time'] = str(i.created_time).split(' ')[0]
        r_w_data.append(data)
    all_data = {}
    all_data['data'] = r_w_data
    all_data['count'] = paginator.count
    all_data['num_pages'] = int(page)
    all_data['totalPage'] = paginator.num_pages
    return JsonResponse(all_data, safe=False)

def search(request):
    """
    搜索结果显示返回
    :param request:
    :return:
    """
    strs = request.GET.get('str')
    data_list = Article.objects.filter(title__icontains=strs).reverse()
    list = []
    for i in data_list:
        data = {}
        data['id'] = i.id
        data['title'] = i.title
        data['excerpt'] = i.excerpt
        data['category'] = str(i.category)
        data['img'] = BASE_URL + str(i.img)
        data['user'] = str(i.user)
        # data['views'] = i.views
        data['created_time'] = str(i.created_time).split(' ')[0]
        list.append(data)
    return JsonResponse(list,safe=False)