import os

from django.http import JsonResponse


def vol_increase(request):
    os.system('pactl set-sink-volume 0 +5%  & pkill -RTMIN+1 i3blocks');
    return JsonResponse({'status':'success', 'msg':'volume increased by 5%'})

def vol_decrease(request):
    os.system('pactl set-sink-volume 0 -5%  & pkill -RTMIN+1 i3blocks');
    return JsonResponse({'status':'success', 'msg':'volume decreased by 5%'})
