
# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.models import User
from models import *
import os
import uuid
import json


def index(request):
    return render_to_response('index.html', locals())


def add_contacts(request):
    user_id = request.REQUEST.get('user_id', '')
    id = request.REQUEST.get('_id', '')
    KuaiDiGongSi = request.REQUEST.get('KuaiDiGongSi', '')
    ZhanDianMingCheng = request.REQUEST.get('ZhanDianMingCheng', '')
    ZhanDianDaiMa = request.REQUEST.get('ZhanDianDaiMa', '')
    ShengFen = request.REQUEST.get('ShengFen', '')
    DiShi = request.REQUEST.get('DiShi', '')
    XianQu = request.REQUEST.get('XianQu', '')
    XiangZhen = request.REQUEST.get('XiangZhen', '')
    JieDao = request.REQUEST.get('JieDao', '')
    XingMing = request.REQUEST.get('XingMing', '')
    ZhiWu = request.REQUEST.get('ZhiWu', '')
    DianHua = request.REQUEST.get('DianHua', '')
    ShouJi = request.REQUEST.get('ShouJi', '')
    QQHaoMa = request.REQUEST.get('QQHaoMa', '')
    JingYingDiZhi = request.REQUEST.get('JingYingDiZhi', '')
    FuWuFanWei = request.REQUEST.get('FuWuFanWei', '')
    ChaoQuFanWei = request.REQUEST.get('ChaoQuFanWei', '')
    BeiZhu = request.REQUEST.get('BeiZhu', '')

    ob = Contacts()
    ob.user_id = user_id
    ob.KuaiDiGongSi = KuaiDiGongSi
    ob.ZhanDianMingCheng = ZhanDianMingCheng
    ob.ZhanDianDaiMa = ZhanDianDaiMa
    ob.ShengFen = ShengFen
    ob.DiShi = DiShi
    ob.XianQu = XianQu
    ob.XiangZhen = XiangZhen
    ob.JieDao = JieDao
    ob.XingMing = XingMing
    ob.ZhiWu = ZhiWu
    ob.DianHua = DianHua
    ob.ShouJi = ShouJi
    ob.QQHaoMa = QQHaoMa
    ob.JingYingDiZhi = JingYingDiZhi
    ob.FuWuFanWei = FuWuFanWei
    ob.ChaoQuFanWei = ChaoQuFanWei
    ob.BeiZhu = BeiZhu
    if id:
        ob.id = id
    ob.save()
    return HttpResponse("ok")


def get_contacts(request, id):
    c = Contacts.objects.filter(id=id)
    d = {}
    if c:
        c = c[0]
        d["_id"] = c.id
        d["user_id"] = c.user_id
        d["KuaiDiGongSi"] = c.KuaiDiGongSi
        d["ZhanDianMingCheng"] = c.ZhanDianMingCheng
        d["ZhanDianDaiMa"] = c.ZhanDianDaiMa
        d["ShengFen"] = c.ShengFen
        d["DiShi"] = c.DiShi
        d["XianQu"] = c.XianQu
        d["XiangZhen"] = c.XiangZhen
        d["JieDao"] = c.JieDao
        d["XingMing"] = c.XingMing
        d["ZhiWu"] = c.ZhiWu
        d["DianHua"] = c.DianHua
        d["ShouJi"] = c.ShouJi
        d["QQHaoMa"] = c.QQHaoMa
        d["JingYingDiZhi"] = c.JingYingDiZhi
        d["FuWuFanWei"] = c.FuWuFanWei
        d["ChaoQuFanWei"] = c.ChaoQuFanWei
        d["BeiZhu"] = c.BeiZhu
        output = json.dumps(d, ensure_ascii=False)
    else:
        output = "Have No Record"

    return HttpResponse(output)


def add_send(request):
    user_id = request.REQUEST.get('user_id', '')
    id = request.REQUEST.get('_id', '')
    YunDanBianHao = request.REQUEST.get('YunDanBianHao', '')
    JiJianRiQi = request.REQUEST.get('JiJianRiQi', '')
    JiJianWangDian = request.REQUEST.get('JiJianWangDian', '')
    MuDiDi = request.REQUEST.get('MuDiDi', '')
    JianShu = request.REQUEST.get('JianShu', '')
    ShiZhong = request.REQUEST.get('ShiZhong', '')
    FuKuanFangShi = request.REQUEST.get('FuKuanFangShi', '')
    YunFei = request.REQUEST.get('YunFei', '')
    DaiShouHuoKuan = request.REQUEST.get('DaiShouHuoKuan', '')
    QuJianYuan = request.REQUEST.get('QuJianYuan', '')
    ZiDanHao = request.REQUEST.get('ZiDanHao', '')
    JiJianRen = request.REQUEST.get('JiJianRen', '')
    JiJianGongSi = request.REQUEST.get('JiJianGongSi', '')
    ShouJianDianHua = request.REQUEST.get('ShouJianDianHua', '')
    ShouJianRen = request.REQUEST.get('ShouJianRen', '')
    ShouJianGongsi = request.REQUEST.get('ShouJianGongsi', '')
    ShouJianDiZhi = request.REQUEST.get('ShouJianDiZhi', '')

    if not YunDanBianHao:
        return HttpResponse("no YunDanBianHao")
        
    ob = Send()
    ob.user_id = user_id
    ob.YunDanBianHao = YunDanBianHao
    ob.JiJianRiQi = JiJianRiQi
    ob.JiJianWangDian = JiJianWangDian
    ob.MuDiDi = MuDiDi
    ob.JianShu = JianShu
    ob.ShiZhong = ShiZhong
    ob.FuKuanFangShi = FuKuanFangShi
    ob.YunFei = YunFei
    ob.DaiShouHuoKuan = DaiShouHuoKuan
    ob.QuJianYuan = QuJianYuan
    ob.ZiDanHao = ZiDanHao
    ob.JiJianRen = JiJianRen
    ob.JiJianGongSi = JiJianGongSi
    ob.ShouJianDianHua = ShouJianDianHua
    ob.ShouJianRen = ShouJianRen
    ob.ShouJianGongsi = ShouJianGongsi
    ob.ShouJianDiZhi = ShouJianDiZhi
    if id:
        ob.id = id
    ob.save()

    return HttpResponse("ok")


def get_send(request, id):
    c = Send.objects.filter(id=id)
    d = {}
    if c:
        c = c[0]
        d["_id"] = c.id
        d["user_id"] = c.user_id
        d["YunDanBianHao"] = c.YunDanBianHao
        d["JiJianRiQi"] = c.JiJianRiQi
        d["JiJianWangDian"] = c.JiJianWangDian
        d["MuDiDi"] = c.MuDiDi
        d["JianShu"] = c.JianShu
        d["ShiZhong"] = c.ShiZhong
        d["FuKuanFangShi"] = c.FuKuanFangShi
        d["YunFei"] = c.YunFei
        d["DaiShouHuoKuan"] = c.DaiShouHuoKuan
        d["QuJianYuan"] = c.QuJianYuan
        d["ZiDanHao"] = c.ZiDanHao
        d["JiJianRen"] = c.JiJianRen
        d["JiJianGongSi"] = c.JiJianGongSi
        d["ShouJianDianHua"] = c.ShouJianDianHua
        d["ShouJianRen"] = c.ShouJianRen
        d["ShouJianGongsi"] = c.ShouJianGongsi
        d["ShouJianDiZhi"] = c.ShouJianDiZhi
        output = json.dumps(d, ensure_ascii=False)
    else:
        output = "Have No Record"

    return HttpResponse(output)


def get_user_info(request, user_id):
    cs = Contacts.objects.filter(user_id=user_id)
    ss = Send.objects.filter(user_id=user_id)
    cids = [str(c.id) for c in cs]
    sids = [str(s.id) for s in ss]
    cids = ",".join(cids)
    sids = ",".join(sids)
    d = dict(cids=cids, sids=sids)
    output = json.dumps(d, ensure_ascii=False)
    return HttpResponse(output)



def upload_img(request, user_id):
    type = request.REQUEST.get("type")
    send_id = request.REQUEST.get("send_id")
    file = request.FILES.get('u_file')
    if not file:
        return HttpResponse("no pic")
    filename, ext = os.path.splitext(file.name)
    if not ext.lower() in ['.jpg','.gif','.png','.bmp']:
        HttpResponse("type error")
    permanent_file_name =  file.name
    if 'SERVER_SOFTWARE' in os.environ:
        import sae.storage
        s = sae.storage.Client()
        ob = sae.storage.Object(file.read())
        url = s.put('images', permanent_file_name, ob)
    else:
        raw_file = os.path.join(os.getcwd(), 'static', 'images', permanent_file_name)
        destination = open(raw_file, 'wb+')
        for chunk in file.chunks():
            destination.write(chunk)
        destination.close()
        url = "http://" + request.get_host() + "/static/images/" + permanent_file_name
    im_exist = Img.objects.filter(name=filename)
    if im_exist:
        im = im_exist[0]
    else:
        im = Img()
    im.user_id = user_id
    im.name = filename
    im.url = url
    im.type = type
    im.send_id = send_id
    im.save()
    return HttpResponse(url)


def show_img(request, user_id):
    ims = Img.objects.filter(user_id=user_id)
    return render_to_response('show_img.html', locals())


def list_img(request, user_id):
    ims = Img.objects.filter(user_id=user_id)
    ls = [im.url for im in ims]
    return HttpResponse(str(ls))


def del_img(request, id):
    im = Img.objects.get(id=id)
    user_id = im.user_id
    im.delete()
    return HttpResponseRedirect("/show_img/" + user_id + "/")


def find_img(request):
    url = ""
    YunDanBianHao = request.REQUEST.get("YunDanBianHao")
    im = Img.objects.filter(send_id=YunDanBianHao)
    if im:
        im = im[0]
        url = im.url
    return HttpResponse(url)


def search_send(request):
    YunDanBianHao = request.REQUEST.get("YunDanBianHao")
    c = Send.objects.filter(YunDanBianHao=YunDanBianHao)
    d = {}
    if c:
        c = c[0]
        d["_id"] = c.id
        d["user_id"] = c.user_id
        d["YunDanBianHao"] = c.YunDanBianHao
        d["JiJianRiQi"] = c.JiJianRiQi
        d["JiJianWangDian"] = c.JiJianWangDian
        d["MuDiDi"] = c.MuDiDi
        d["JianShu"] = c.JianShu
        d["ShiZhong"] = c.ShiZhong
        d["FuKuanFangShi"] = c.FuKuanFangShi
        d["YunFei"] = c.YunFei
        d["DaiShouHuoKuan"] = c.DaiShouHuoKuan
        d["QuJianYuan"] = c.QuJianYuan
        d["ZiDanHao"] = c.ZiDanHao
        d["JiJianRen"] = c.JiJianRen
        d["JiJianGongSi"] = c.JiJianGongSi
        d["ShouJianDianHua"] = c.ShouJianDianHua
        d["ShouJianRen"] = c.ShouJianRen
        d["ShouJianGongsi"] = c.ShouJianGongsi
        d["ShouJianDiZhi"] = c.ShouJianDiZhi
        output = json.dumps(d, ensure_ascii=False)
    else:
        output = "Have No Record"

    return HttpResponse(output)




#====================login=============================================
def reg(request):
    username = request.REQUEST.get('username', '')
    password = request.REQUEST.get('password', '')
    print "====reg===="
    print username
    print password
    if User.objects.filter(username = username):
        return HttpResponse("Exist")
    u = User()
    u.username = username
    u.set_password(password)
    u.save()
    return HttpResponse(u.id)

def login(request):
    username = request.REQUEST.get('username', '')
    password = request.REQUEST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponse(user.id)
    else:
        return HttpResponse("Failure")


def logout(request):
    if request.user.is_authenticated():
        auth.logout(request)
    return HttpResponse("ok")
#======================================================================
