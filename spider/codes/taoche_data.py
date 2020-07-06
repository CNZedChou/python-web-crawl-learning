# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  taoche_data.py
@Description    :  
@CreateTime     :  2020-7-6 10:29
------------------------------------
@ModifyTime     :  
"""
# 所有城市列表
CITY_CODE = ['quanguo', 'shijiazhuang', 'tangshan', 'qinhuangdao', 'handan', 'xingtai', 'baoding', 'zhangjiakou',
             'chengde', 'cangzhou', 'langfang', 'hengshui', 'taiyuan', 'datong', 'yangquan', 'changzhi', 'jincheng',
             'shuozhou', 'jinzhong', 'yuncheng', 'xinzhou', 'linfen', 'lvliang', 'huhehaote', 'baotou', 'wuhai',
             'chifeng', 'tongliao', 'eerduosi', 'hulunbeier', 'bayannaoer', 'wulanchabu', 'xinganmeng',
             'xilinguolemeng', 'alashanmeng', 'changchun', 'jilin', 'hangzhou', 'ningbo', 'wenzhou', 'jiaxing',
             'huzhou', 'shaoxing', 'jinhua', 'quzhou', 'zhoushan', 'tz', 'lishui', 'bozhou', 'chizhou', 'xuancheng',
             'nanchang', 'jingdezhen', 'pingxiang', 'jiujiang', 'xinyu', 'yingtan', 'ganzhou', 'jian', 'yichun', 'jxfz',
             'shangrao', 'xian', 'tongchuan', 'baoji', 'xianyang', 'weinan', 'yanan', 'hanzhong', 'yl', 'ankang',
             'shangluo', 'lanzhou', 'jiayuguan', 'jinchang', 'baiyin', 'tianshui', 'wuwei', 'zhangye', 'pingliang',
             'jiuquan', 'qingyang', 'dingxi', 'longnan', 'linxia', 'gannan', 'xining', 'haidongdiqu', 'haibei',
             'huangnan', 'hainanzangzuzizhizho', 'guoluo', 'yushu', 'haixi', 'yinchuan', 'shizuishan', 'wuzhong',
             'guyuan', 'zhongwei', 'wulumuqi', 'kelamayi', 'shihezi', 'tulufandiqu', 'hamidiqu', 'changji', 'boertala',
             'bazhou', 'akesudiqu', 'xinjiangkezhou', 'kashidiqu', 'hetiandiqu', 'yili', 'tachengdiqu', 'aletaidiqu',
             'xinjiangzhixiaxian', 'changsha', 'zhuzhou', 'xiangtan', 'hengyang', 'shaoyang', 'yueyang', 'changde',
             'zhangjiajie', 'yiyang', 'chenzhou', 'yongzhou', 'huaihua', 'loudi', 'xiangxi', 'guangzhou', 'shaoguan',
             'shenzhen', 'zhuhai', 'shantou', 'foshan', 'jiangmen', 'zhanjiang', 'maoming', 'zhaoqing', 'huizhou',
             'meizhou', 'shanwei', 'heyuan', 'yangjiang', 'qingyuan', 'dongguan', 'zhongshan', 'chaozhou', 'jieyang',
             'yunfu', 'nanning', 'liuzhou', 'guilin', 'wuzhou', 'beihai', 'fangchenggang', 'qinzhou', 'guigang',
             'yulin', 'baise', 'hezhou', 'hechi', 'laibin', 'chongzuo', 'haikou', 'sanya', 'sanshashi', 'qiongbeidiqu',
             'qiongnandiqu', 'hainanzhixiaxian', 'chengdu', 'zigong', 'panzhihua', 'luzhou', 'deyang', 'mianyang',
             'guangyuan', 'suining', 'neijiang', 'leshan', 'nanchong', 'meishan', 'yibin', 'guangan', 'dazhou', 'yaan',
             'bazhong', 'ziyang', 'aba', 'ganzi', 'liangshan', 'guiyang', 'liupanshui', 'zunyi', 'anshun',
             'tongrendiqu', 'qianxinan', 'bijiediqu', 'qiandongnan', 'qiannan', 'kunming', 'qujing', 'yuxi', 'baoshan',
             'zhaotong', 'lijiang', 'puer', 'lincang', 'chuxiong', 'honghe', 'wenshan', 'xishuangbanna', 'dali',
             'dehong', 'nujiang', 'diqing', 'siping', 'liaoyuan', 'tonghua', 'baishan', 'songyuan', 'baicheng',
             'yanbian', 'haerbin', 'qiqihaer', 'jixi', 'hegang', 'shuangyashan', 'daqing', 'yc', 'jiamusi', 'qitaihe',
             'mudanjiang', 'heihe', 'suihua', 'daxinganlingdiqu', 'shanghai', 'tianjin', 'chongqing', 'nanjing', 'wuxi',
             'xuzhou', 'changzhou', 'suzhou', 'nantong', 'lianyungang', 'huaian', 'yancheng', 'yangzhou', 'zhenjiang',
             'taizhou', 'suqian', 'lasa', 'changdudiqu', 'shannan', 'rikazediqu', 'naqudiqu', 'alidiqu', 'linzhidiqu',
             'hefei', 'wuhu', 'bengbu', 'huainan', 'maanshan', 'huaibei', 'tongling', 'anqing', 'huangshan', 'chuzhou',
             'fuyang', 'sz', 'chaohu', 'luan', 'fuzhou', 'xiamen', 'putian', 'sanming', 'quanzhou', 'zhangzhou',
             'nanping', 'longyan', 'ningde', 'jinan', 'qingdao', 'zibo', 'zaozhuang', 'dongying', 'yantai', 'weifang',
             'jining', 'taian', 'weihai', 'rizhao', 'laiwu', 'linyi', 'dezhou', 'liaocheng', 'binzhou', 'heze',
             'zhengzhou', 'kaifeng', 'luoyang', 'pingdingshan', 'jiyuan', 'anyang', 'hebi', 'xinxiang', 'jiaozuo',
             'puyang', 'xuchang', 'luohe', 'sanmenxia', 'nanyang', 'shangqiu', 'xinyang', 'zhoukou', 'zhumadian',
             'henanzhixiaxian', 'wuhan', 'huangshi', 'shiyan', 'yichang', 'xiangfan', 'ezhou', 'jingmen', 'xiaogan',
             'jingzhou', 'huanggang', 'xianning', 'qianjiang', 'suizhou', 'xiantao', 'tianmen', 'enshi',
             'hubeizhixiaxian', 'beijing', 'shenyang', 'dalian', 'anshan', 'fushun', 'benxi', 'dandong', 'jinzhou',
             'yingkou', 'fuxin', 'liaoyang', 'panjin', 'tieling', 'chaoyang', 'huludao', 'anhui', 'fujian', 'gansu',
             'guangdong', 'guangxi', 'guizhou', 'hainan', 'hebei', 'henan', 'heilongjiang', 'hubei', 'hunan', 'jl',
             'jiangsu', 'jiangxi', 'liaoning', 'neimenggu', 'ningxia', 'qinghai', 'shandong', 'shanxi', 'shaanxi',
             'sichuan', 'xizang', 'xinjiang', 'yunnan', 'zhejiang', 'jjj', 'jzh', 'zsj', 'csj', 'ygc']

# 品牌类型列表
CAR_CODE_LIST = ['southeastautomobile', 'sma', 'audi', 'hummer', 'tianqimeiya', 'seat', 'lamborghini', 'weltmeister',
                 'changanqingxingche-281', 'chevrolet', 'fiat', 'foday', 'eurise', 'dongfengfengdu', 'lotus-146', 'jac',
                 'enranger', 'bjqc', 'luxgen', 'jinbei', 'sgautomotive', 'jonwayautomobile', 'beijingjeep', 'linktour',
                 'landrover', 'denza', 'jeep', 'rely', 'gacne', 'porsche', 'wey', 'shenbao', 'bisuqiche-263',
                 'beiqihuansu', 'sinogold', 'roewe', 'maybach', 'greatwall', 'chenggongqiche', 'zotyeauto', 'kaersen',
                 'gonow', 'dodge', 'siwei', 'ora', 'lifanmotors', 'cajc', 'hafeiautomobile', 'sol', 'beiqixinnengyuan',
                 'dorcen', 'lexus', 'mercedesbenz', 'ford', 'huataiautomobile', 'jmc', 'peugeot', 'kinglongmotor',
                 'oushang', 'dongfengxiaokang-205', 'chautotechnology', 'faw-hongqi', 'mclaren', 'dearcc',
                 'fengxingauto', 'singulato', 'nissan', 'saleen', 'ruichixinnengyuan', 'yulu', 'isuzu', 'zhinuo',
                 'alpina', 'renult', 'kawei', 'cadillac', 'hanteng', 'defu', 'subaru', 'huasong', 'casyc', 'geely',
                 'xpeng', 'jlkc', 'sj', 'nanqixinyatu1', 'horki', 'venucia', 'xinkaiauto', 'traum',
                 'shanghaihuizhong-45', 'zhidou', 'ww', 'riich', 'brillianceauto', 'galue', 'bugatti',
                 'guagnzhouyunbao', 'borgward', 'qzbd1', 'bj', 'changheauto', 'faw', 'saab', 'fuqiautomobile', 'skoda',
                 'citroen', 'mitsubishi', 'opel', 'qorosauto', 'zxauto', 'infiniti', 'mazda', 'arcfox-289',
                 'jinchengautomobile', 'kia', 'mini', 'tesla', 'gmc-109', 'chery', 'daoda-282', 'joylongautomobile',
                 'hafu-196', 'sgmw', 'wiesmann', 'acura', 'yunqueqiche', 'volvo', 'lynkco', 'karry', 'chtc', 'gq',
                 'redstar', 'everus', 'kangdi', 'chrysler', 'cf', 'maxus', 'smart', 'maserati', 'dayu', 'besturn',
                 'dadiqiche', 'ym', 'huakai', 'buick', 'faradayfuture', 'leapmotor', 'koenigsegg', 'bentley',
                 'rolls-royce', 'iveco', 'dongfeng-27', 'haige1', 'ds', 'landwind', 'volkswagen', 'sitech', 'toyota',
                 'polarsunautomobile', 'zhejiangkaersen', 'ladaa', 'lincoln', 'weilaiqiche', 'li', 'ferrari', 'jetour',
                 'honda', 'barbus', 'morgancars', 'ol', 'sceo', 'hama', 'dongfengfengguang', 'mg-79', 'ktm',
                 'changankuayue-283', 'suzuki', 'yudo', 'yusheng-258', 'fs', 'bydauto', 'jauger', 'foton', 'pagani',
                 'shangqisaibao', 'guangqihinomotors', 'polestar', 'fujianxinlongmaqichegufenyouxiangongsi',
                 'alfaromeo', 'shanqitongjia1', 'xingchi', 'lotus', 'hyundai', 'kaiyi', 'isuzu-132', 'bmw', 'ssangyong',
                 'astonmartin']