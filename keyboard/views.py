from django.shortcuts import render
from django.http import JsonResponse

from pykeyboard import PyKeyboard


k = PyKeyboard()

def tap_character(response, character):
    k.tap_key(character)
    return JsonResponse({'status':'success', 'msg': character + ' key pressed'})

def tap_left_key(response):
    k.tap_key(k.left_key)
    return JsonResponse({'status':'success', 'msg':'left key pressed'})

def tap_right_key(response):
    k.tap_key(k.right_key)
    return JsonResponse({'status':'success', 'msg':'right key pressed'})

def tap_up_key(response):
    k.tap_key(k.up_key)
    return JsonResponse({'status':'success', 'msg':'up key pressed'})

def tap_down_key(response):
    k.tap_key(k.down_key)
    return JsonResponse({'status':'success', 'msg':'down key pressed'})

def tap_space_key(response):
    k.tap_key(' ')
    return JsonResponse({'status':'success', 'msg':'space key pressed'})

def tap_return_key(response):
    k.tap_key(k.return_key)
    return JsonResponse({'status':'success', 'msg':'space key pressed'})

def tap_backspace_key(response):
    k.tap_key(k.backspace_key)
    return JsonResponse({'status':'success', 'msg':'backspace key pressed'})


def press_ctrl_key(response):
    k.press_key(k.control_key)
    return JsonResponse({'status':'success', 'msg':'control key pressed'})

def release_ctrl_key(response):
    k.release_key(k.control_key)
    return JsonResponse({'status':'success', 'msg':'control key released'})

def press_shift_key(response):
    k.press_key(k.shift_key)
    return JsonResponse({'status':'success', 'msg':'shift key pressed'})

def release_shift_key(response):
    k.release_key(k.shift_key)
    return JsonResponse({'status':'success', 'msg':'shift key released'})

def press_alt_key(response):
    k.press_key(k.alt_key)
    return JsonResponse({'status':'success', 'msg':'alt key pressed'})

def release_alt_key(response):
    k.release_key(k.alt_key)
    return JsonResponse({'status':'success', 'msg':'alt key released'})

def press_win_key(response):
    k.press_key(k.windows_l_key)
    return JsonResponse({'status':'success', 'msg':'windows(super) key pressed'})

def release_win_key(response):
    k.release_key(k.windows_l_key)
    return JsonResponse({'status':'success', 'msg':'windows(super) key released'})
