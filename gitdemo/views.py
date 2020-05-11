# -*- coding: utf-8 -*-
from django.http import HttpResponse


def hh():
    print('哈哈哈')
    return HttpResponse('hello!')
