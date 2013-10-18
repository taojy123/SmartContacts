
# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
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
        output = json.dumps(d)
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
        output = json.dumps(d)
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
    output = json.dumps(d)
    return HttpResponse(output)



#====================login=============================================
def login(request):
    username = request.REQUEST.get('username', '')
    password = request.REQUEST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
    return HttpResponseRedirect("/admin/")

def logout(request):
    if request.user.is_authenticated():
        auth.logout(request)
    return HttpResponseRedirect("/admin/")
#======================================================================
