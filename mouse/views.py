from django.shortcuts import render
from django.http import JsonResponse

from pymouse import PyMouse


m = PyMouse()

def offset(request, xpos, ypos):
    (x, y) = m.position()
    m.move(x+int(xpos), y+int(ypos))
    return JsonResponse({'status':'success', 'msg':'mouse moved'})

def left_click(request):
    (x, y) = m.position()
    m.click(x, y, 1)
    return JsonResponse({'status':'success', 'msg':'left mouse button clicked'})

def right_click(request):
    (x, y) = m.position()
    m.click(x, y, 2)
    return JsonResponse({'status':'success', 'msg':'right mouse button clicked'})
