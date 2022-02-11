from django.shortcuts import render
from django.http import JsonResponse
from . import starbucks02


def index(request):
    return render(request, 'index.html')


def starbucks(request):
    list_all = list()
    sido_all = starbucks02.getSiDo()
    for sido in sido_all:
        if sido == '17':
            result = starbucks02.getStore(sido_code=sido)
            print(result)
            list_all.extend(result)
        else:
            gugun_all = starbucks02.getGuGun(sido)
            for gugun in gugun_all:
                result = starbucks02.getStore(gugun_code=gugun)
                print(result)
                list_all.extend(result)

    result_dict = dict()
    result_dict['list'] = list_all
    
    # dictionary로 요청하면 json으로 바꿔서 응답해줌
    return JsonResponse(result_dict)
