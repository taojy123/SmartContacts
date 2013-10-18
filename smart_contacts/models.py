
# -*- coding: utf-8 -*-
from django.db import models

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




