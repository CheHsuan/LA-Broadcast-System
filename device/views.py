from django.http import HttpResponse
from device.models import DeviceInfo
import xmlrpclib as rpc
import glob
import envsetting
import json
import os

def index(request):
    res = DeviceInfo.objects.all()
    return HttpResponse(res)

def __parser(instances, action, music="Minions.mp3"):
    if action == 'play':
        for instance in instances:
            pi = rpc.ServerProxy(instance.url, allow_none=True)
            res = pi.play(music)
    elif action == 'pause':
        for instance in instances:
            pi = rpc.ServerProxy(instance.url, allow_none=True)
            res = pi.pause()
    elif action == 'stop':
        for instance in instances:
            pi = rpc.ServerProxy(instance.url, allow_none=True)
            res = pi.stop()
    elif action == 'show':
        res = action
    else:
        res = "Action %s is not defined" % action
    
    return res

def device_control(request, device_id):
    try:
        ret = DeviceInfo.objects.filter(identification=device_id)
        if request.GET.get('action'):
            action = request.GET.get('action')
        else:
            action = "detail"
        if request.GET.get('music'):
            music = request.GET.get('music')
            res = __parser(ret, action, music)
        else:
            res = __parser(ret, action) 
    except Exception as e:
        print str(e)
        res = "Device {id} is not availible".format(id = device_id)

    return HttpResponse(res)

def group_control(request, group_id):
    try:
        ret = DeviceInfo.objects.filter(group=group_id)
        if request.GET.get('action'):
            action = request.GET.get('action')
        else:
            action = "detail"
        res = __parser(ret, action) 
    except Exception as e:
        print str(e)
        res = "Group {id} is not availible".format(id = group_id)

    return HttpResponse(res)

def show_list(request, group_id='all'):
    try:
        playlist = [os.path.basename(x) for x in glob.glob(envsetting.music_path[group_id]+"*.mp3")]
        res = dict()
        i = 0
        for item in playlist:
            res[i] = item
            i = i + 1
        res = json.dumps(res)
    except Exception as e:
        print str(e)
        res = "Music server error"

    return HttpResponse(res)
