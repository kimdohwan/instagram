from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def post_list(request):
    return HttpResponse('포스트 리스트 페이지')

def post_detail(request, pk):
    return HttpResponse(f'포스트 디테일 페이지 pk: {pk}')