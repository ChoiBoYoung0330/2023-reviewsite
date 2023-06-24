from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import basic_info, detail_info, graph, review_info

# Create your views here.
def index(request):
    """
    pybo 목록 출력
    """
    basic_info_list = basic_info.objects.order_by('-open_date')
    basic_info_score = basic_info.objects.order_by('-total_score')
    context = {'basic_info_list': basic_info_list, 'basic_info_score': basic_info_score}
    return render(request, 'pybo/basic_info_list.html', context)

def detail(request, title_id):
    basic_title = basic_info.objects.get(id=title_id)
    detail_title = detail_info.objects.get(id=title_id)
    graph_title = basic_info.objects.get(id=title_id)
    review_title = basic_info.objects.get(id=title_id)
    context = {'basic_title': basic_title, 'detail_title': detail_title,
               'graph_title': graph_title, 'review_title': review_title}
    return render(request, 'pybo/title_detail.html', context)
