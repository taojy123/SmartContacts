# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.models import User
from models import *
import os
import uuid
import json
import xlwt
import time
import zipfile



def readme(request):
    return render_to_response('readme.html', locals())


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
    return HttpResponse(str(ob.id))


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

    if user_id == "0":
        cs = list(cs) + list(Contacts.objects.filter(user_id=""))
        ss = list(ss) + list(Send.objects.filter(user_id=""))
        cs = list(cs) + list(Contacts.objects.filter(user_id=None))
        ss = list(ss) + list(Send.objects.filter(user_id=None))
        
    cids = [str(c.id) for c in cs]
    sids = [str(s.id) for s in ss]
    #cids = ",".join(cids)
    #sids = ",".join(sids)
    d = dict(cids=cids, sids=sids)
    output = json.dumps(d, ensure_ascii=False)
    return HttpResponse(output)



def upload_img(request, user_id):
    type = request.REQUEST.get("type", "images")
    send_id = request.REQUEST.get("send_id", "")
    file = request.FILES.get('u_file')
    if not file:
        return HttpResponse("no pic")
    filename, ext = os.path.splitext(file.name)

    permanent_file_name =  file.name
    if send_id:
        permanent_file_name = send_id + ext
    else:
        send_id = filename

    if not os.path.exists(os.path.join(os.getcwd(), 'static', type)):
        os.makedirs(os.path.join(os.getcwd(), 'static', type))

    raw_file = os.path.join(os.getcwd(), 'static', type, permanent_file_name)
    destination = open(raw_file, 'wb+')
    for chunk in file.chunks():
        destination.write(chunk)
    destination.close()
    url = "http://" + request.get_host() + "/static/"+ type +"/" + permanent_file_name

    im = Img()
    im.user_id = user_id
    im.name = filename
    im.type = type
    im.send_id = send_id
    im.url = url
    im.save()

    return HttpResponse(url)




def show_img(request, user_id):
    ims = Img.objects.filter(user_id=user_id)
    return render_to_response('show_img.html', locals())


def list_img(request, user_id):
    ims = Img.objects.filter(user_id=user_id)
    ls = [im.url for im in ims]
    ls = json.dumps(ls, ensure_ascii=False)
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
    rp = HttpResponseRedirect("/")
    if request.user.is_authenticated():
        auth.logout(request)
        rp.set_cookie("user_id", "")
        rp.set_cookie("username", "")
    return rp
#======================================================================





key_list =["YunDanBianHao", "JiJianRiQi", "JiJianWangDian", "MuDiDi", "JianShu", "ShiZhong", "FuKuanFangShi",
           "YunFei", "DaiShouHuoKuan", "QuJianYuan", "ZiDanHao", "JiJianRen", "JiJianGongSi", "ShouJianDianHua",
           "ShouJianRen", "ShouJianGongsi", "ShouJianDiZhi"]
show_list = ["运单编号", "寄件日期", "寄件网点", "目的地", "件数", "实重", "付款方式", "运费", "代收货款", "取件员",
             "子单号", "寄件人", "寄件公司", "收件电话", "收件人", "收件公司", "收件地址"]


def index(request):
    YunDanBianHao = request.REQUEST.get('YunDanBianHao')
    if YunDanBianHao:
        rs = Send.objects.filter(YunDanBianHao=YunDanBianHao)
        if rs:
            send = rs[0]
        else:
            send = None

        img_list = Img.objects.filter(send_id=YunDanBianHao)


    if request.user.is_authenticated():
        user_id = request.user.id
        if not Config_send.objects.filter(user_id=user_id):
            for key, show in zip(key_list, show_list):
                cs = Config_send()
                cs.user_id = user_id
                cs.key = key
                cs.name = show
                cs.save()

    return render_to_response('index.html', locals())




def output(request):
    #if not request.user.is_authenticated():
    if not request.COOKIES.get("user_id"):
        return HttpResponse("<script>alert('请先登录用户');top.location='/login_page/'</script>")
    user_id = request.COOKIES.get("user_id")
    username = request.COOKIES.get("username")

    #user_id = request.user.id
    #username = request.user.username

    workBook = xlwt.Workbook()
    workBook.add_sheet("bill")
    sheet = workBook.get_sheet(0)

    cs_list = Config_send.objects.filter(user_id=user_id).order_by('id')

    i = 0
    for cs in cs_list:
        sheet.write(0, i, cs.name)
        i += 1

    sends = Send.objects.filter(user_id=user_id)

    n = 1
    for send in sends:
        if send.is_load:
            continue
        i = 0
        for cs in cs_list:
            value = getattr(send, cs.key, "")
            #value = value.decode("utf8")
            sheet.write(n, i, value)
            send.is_load = "1"
            send.save()
            i += 1
        n += 1

    filename = username + "_" + time.strftime('%Y%m%d_%H%M') + ".xls"
    workBook.save("static/send/" + filename)

    if n == 1:
        return HttpResponse("<script>alert('暂时没有未导出的记录')</script>")

    return HttpResponseRedirect("/static/send/" + filename)



def output_img(request):
    #if not request.user.is_authenticated():
    if not request.COOKIES.get("user_id"):
        return HttpResponse("<script>alert('请先登录用户');top.location='/login_page/'</script>")
    user_id = request.COOKIES.get("user_id")
    username = request.COOKIES.get("username")

    #user_id = request.user.id
    #username = request.user.username

    img_list = Img.objects.filter(user_id=user_id)

    filename = username + "_" + time.strftime('%Y%m%d_%H%M') + ".zip"
    zf = zipfile.ZipFile("static/img/" + filename, "w", zipfile.zlib.DEFLATED)
    flag = False
    for img in img_list:
        if img.is_load:
            continue
        url = img.url
        name = url.split("/")[-1]
        type = url.split("/")[-2]
        if os.path.exists("static/" + type + "/" + name):
            zf.write("static/" + type + "/" + name, type + "/" + name)
        img.is_load = "1"
        img.save()
        flag = True
    zf.close()

    if not flag:
        return HttpResponse("<script>alert('暂时没有未导出的图片')</script>")

    return HttpResponseRedirect("/static/img/" + filename)




def login_page(request):
    return render_to_response('login.html', locals())



def login_user(request):
    username = request.REQUEST.get('username', '')
    password = request.REQUEST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        rp = HttpResponseRedirect("/")
        rp.set_cookie("user_id", user.id)
        rp.set_cookie("username", user.username)
        return rp
    else:
        return HttpResponse("<script>alert('密码错误 请重试');top.location='/login_page/'</script>")


def config(request):
    #if not request.user.is_authenticated():
    if not request.COOKIES.get("user_id"):
        return HttpResponse("<script>alert('请先登录用户');top.location='/login_page/'</script>")
    user_id = request.COOKIES.get("user_id")
    username = request.COOKIES.get("username")

    #user_id = request.user.id
    #username = request.user.username

    rs = Config_send.objects.filter(user_id=user_id).order_by('id')

    key_show = zip(key_list, show_list)

    return render_to_response('config.html', locals())


def update_config(request):
    #if not request.user.is_authenticated():
    if not request.COOKIES.get("user_id"):
        return HttpResponse("<script>alert('请先登录用户');top.location='/login_page/'</script>")
    user_id = request.COOKIES.get("user_id")
    username = request.COOKIES.get("username")

    #user_id = request.user.id
    #username = request.user.username

    key_list = request.REQUEST.get('key_list', '')
    if key_list:
        key_list = key_list.split(",")
    else:
        key_list = []

    name_list = request.REQUEST.get('name_list', '')
    if name_list:
        name_list = name_list.split(",")
    else:
        name_list = []

    default_list = request.REQUEST.get('default_list', '')
    if default_list:
        default_list = default_list.split(",")
    else:
        default_list = []

    if key_list:
        Config_send.objects.filter(user_id=user_id).delete()

    for key, name, default in zip(key_list, name_list, default_list):
        cs = Config_send()
        cs.user_id = user_id
        cs.key = key
        cs.name = name
        cs.default = default
        cs.save()

    return HttpResponse("保存成功")



def regist(request):
    return render_to_response('regist.html', locals())



def register(request):

    username = request.REQUEST.get('username', '')
    password = request.REQUEST.get('password', '')
    password2 = request.REQUEST.get('password2', '')

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

    if not(KuaiDiGongSi and XingMing and DianHua):
        return HttpResponse("<script>alert('请输入带*的必要信息');top.location='/regist/'</script>")

    if password != password2:
        return HttpResponse("<script>alert('两次输入密码不一致');top.location='/regist/'</script>")

    if User.objects.filter(username = username):
        return HttpResponse("<script>alert('该用户已存在,换个用户名吧');top.location='/regist/'</script>")


    u = User()
    u.username = username
    u.set_password(password)
    u.save()

    c = Contacts()
    c.user_id = 0
    c.KuaiDiGongSi = KuaiDiGongSi
    c.ZhanDianMingCheng = ZhanDianMingCheng
    c.ZhanDianDaiMa = ZhanDianDaiMa
    c.ShengFen = ShengFen
    c.DiShi = DiShi
    c.XianQu = XianQu
    c.XiangZhen = XiangZhen
    c.JieDao = JieDao
    c.XingMing = XingMing
    c.ZhiWu = ZhiWu
    c.DianHua = DianHua
    c.ShouJi = ShouJi
    c.QQHaoMa = QQHaoMa
    c.JingYingDiZhi = JingYingDiZhi
    c.FuWuFanWei = FuWuFanWei
    c.ChaoQuFanWei = ChaoQuFanWei
    c.BeiZhu = BeiZhu
    c.save()

    return HttpResponse("<script>alert('恭喜,注册成功!');top.location='/'</script>")


def send(request):
    #if not request.user.is_authenticated():
    if not request.COOKIES.get("user_id"):
        return HttpResponse("<script>alert('请先登录用户');top.location='/login_page/'</script>")
    user_id = request.COOKIES.get("user_id")
    username = request.COOKIES.get("username")

    #user_id = request.user.id
    #username = request.user.username

    return render_to_response('send.html', locals())


def waybill(request, YunDanBianHao):

    rs = Send.objects.filter(YunDanBianHao=YunDanBianHao)
    if rs:
        send = rs[0]
    else:
        send = None

    rs = Img.objects.filter(send_id=YunDanBianHao)
    if rs:
        img_url = rs[0].url
    else:
        img_url = None

    return render_to_response('waybill.html', locals())



def get_ip(request):
    ip = request.META.get('REMOTE_ADDR','1.1.1.1')
    return HttpResponse(ip)
