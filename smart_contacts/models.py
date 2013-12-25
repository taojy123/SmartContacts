# -*- coding: utf-8 -*-
from django.db import models

key_list =["YunDanBianHao", "JiJianRiQi", "JiJianWangDian", "MuDiDi", "JianShu", "ShiZhong", "FuKuanFangShi",
           "YunFei", "DaiShouHuoKuan", "QuJianYuan", "ZiDanHao", "JiJianRen", "JiJianGongSi", "ShouJianDianHua",
           "ShouJianRen", "ShouJianGongsi", "ShouJianDiZhi"]
show_list = ["运单编号", "寄件日期", "寄件网点", "目的地", "件数", "实重", "付款方式", "运费", "代收货款", "取件员",
             "子单号", "寄件人", "寄件公司", "收件电话", "收件人", "收件公司", "收件地址"]


class Contacts(models.Model):
    user_id = models.CharField(max_length=255, blank=True , null=True)
    KuaiDiGongSi = models.CharField(max_length=255, blank=True , null=True)
    ZhanDianMingCheng = models.CharField(max_length=255, blank=True , null=True)
    ZhanDianDaiMa = models.CharField(max_length=255, blank=True , null=True)
    ShengFen = models.CharField(max_length=255, blank=True , null=True)
    DiShi = models.CharField(max_length=255, blank=True , null=True)
    XianQu = models.CharField(max_length=255, blank=True , null=True)
    XiangZhen = models.CharField(max_length=255, blank=True , null=True)
    JieDao = models.CharField(max_length=255, blank=True , null=True)
    XingMing = models.CharField(max_length=255, blank=True , null=True)
    ZhiWu = models.CharField(max_length=255, blank=True , null=True)
    DianHua = models.CharField(max_length=255, blank=True , null=True)
    ShouJi = models.CharField(max_length=255, blank=True , null=True)
    QQHaoMa = models.CharField(max_length=255, blank=True , null=True)
    JingYingDiZhi = models.CharField(max_length=255, blank=True , null=True)
    FuWuFanWei = models.CharField(max_length=255, blank=True , null=True)
    ChaoQuFanWei = models.CharField(max_length=255, blank=True , null=True)
    BeiZhu = models.CharField(max_length=255, blank=True , null=True)


class Send(models.Model):
    user_id = models.CharField(max_length=255, blank=True , null=True)
    YunDanBianHao = models.CharField(max_length=255, blank=True , null=True)
    JiJianRiQi = models.CharField(max_length=255, blank=True , null=True)
    JiJianWangDian = models.CharField(max_length=255, blank=True , null=True)
    MuDiDi = models.CharField(max_length=255, blank=True , null=True)
    JianShu = models.CharField(max_length=255, blank=True , null=True)
    ShiZhong = models.CharField(max_length=255, blank=True , null=True)
    FuKuanFangShi = models.CharField(max_length=255, blank=True , null=True)
    YunFei = models.CharField(max_length=255, blank=True , null=True)
    DaiShouHuoKuan = models.CharField(max_length=255, blank=True , null=True)
    QuJianYuan = models.CharField(max_length=255, blank=True , null=True)
    ZiDanHao = models.CharField(max_length=255, blank=True , null=True)
    JiJianRen = models.CharField(max_length=255, blank=True , null=True)
    JiJianGongSi = models.CharField(max_length=255, blank=True , null=True)
    ShouJianDianHua = models.CharField(max_length=255, blank=True , null=True)
    ShouJianRen = models.CharField(max_length=255, blank=True , null=True)
    ShouJianGongsi = models.CharField(max_length=255, blank=True , null=True)
    ShouJianDiZhi = models.CharField(max_length=255, blank=True , null=True)
    is_load = models.CharField(max_length=255, blank=True , null=True)


class Img(models.Model):
    user_id = models.CharField(max_length=255, blank=True , null=True)
    name = models.CharField(max_length=255, blank=True , null=True)
    url = models.CharField(max_length=255, blank=True , null=True)
    type = models.CharField(max_length=255, blank=True , null=True)
    send_id = models.CharField(max_length=255, blank=True , null=True)
    is_load = models.CharField(max_length=255, blank=True , null=True)

    def type_name(self):
        if self.type == "fahuo":
            return "发货图片"
        if self.type == "shouhuo":
            return "收货图片"
        if self.type == "wentijian":
            return "问题件图片"
        return self.type



class Config_send(models.Model):
    user_id = models.CharField(max_length=255, blank=True , null=True)
    key = models.CharField(max_length=255, blank=True , null=True)
    name = models.CharField(max_length=255, blank=True , null=True)
    default = models.CharField(max_length=255, blank=True , null=True, default="")

    def show_key(self):
        if self.key in key_list:
            i = key_list.index(self.key)
            return show_list[i]

class User_info(models.Model):
    user_id = models.CharField(max_length=255, blank=True , null=True)
    city = models.CharField(max_length=255, blank=True , null=True)
    company = models.CharField(max_length=255, blank=True , null=True)


