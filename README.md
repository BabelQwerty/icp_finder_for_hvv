# icp_finder_for_hvv

### install
```
python3 -m pip install requests parsel tldextract datetime 
```


### usage: 
```
┌──(qwerty㉿qwerty)-[/mnt/hgfs/workspace/python_workspace/]
└─$ python3 icp.py    
Traceback (most recent call last):
  File "/mnt/hgfs/workspace/python_workspace/icp.py", line 202, in <module>
    raise Exception(f"\nusage:\npython3 {argv[0]} domain\npython3 {argv[0]} companyName\npython3 {argv[0]} domain companyName\nor loop sub company query\npython3 {argv[0]} domain companyName -l ")
Exception: 
usage:
python3 icp.py domain
python3 icp.py companyName
python3 icp.py domain companyName
or loop sub company query
python3 icp.py domain companyName -l 
```

### exmaple:
```
┌──(kali㉿kali)-[/mnt/hgfs/workspace/python_workspace]
└─$ python3 icp.py 999.com.cn -d -l
INFO - 2023-04-10 16:17:58,719 - process: 3082189 - icp.py - icp - 213 - icp - ['999.com.cn']
INFO - 2023-04-10 16:18:00,350 - process: 3082189 - icp.py - icp - 193 - icp - company len: 12
999.com.cn
分支机构 
四川三九医药贸易有限公司|100%|华润三九医药股份有限公司
华润三九(南昌)药业有限公司|59.6%|华润三九医药股份有限公司
华润三九(六安)中药材产业发展有限公司|100%|华润三九医药股份有限公司
华润三九(郴州)制药有限公司|100%|华润三九医药股份有限公司
华润圣海健康科技有限公司|65%|华润三九医药股份有限公司
吉林三九金复康药业有限公司|65%|华润三九医药股份有限公司
浙江小九云药医药科技有限公司|51%|华润三九医药股份有限公司
雅安雨禾药业有限公司|90.09%|华润三九医药股份有限公司
INFO - 2023-04-10 16:18:00,352 - process: 3082189 - icp.py - icp - 221 - icp - 四川三九医药贸易有限公司|100%|华润三九医药股份有限公司
INFO - 2023-04-10 16:18:00,686 - process: 3082189 - icp.py - icp - 138 - icp - []
SUCCESS - 2023-04-10 16:18:00,687 - process: 3082189 - icp.py - icp - 81 - icp - page_link: 0
SUCCESS - 2023-04-10 16:18:00,687 - process: 3082189 - icp.py - icp - 81 - icp - company len: 0

INFO - 2023-04-10 16:18:00,687 - process: 3082189 - icp.py - icp - 221 - icp - 华润三九(南昌)药业有限公司|59.6%|华润三九医药股份有限公司
INFO - 2023-04-10 16:18:01,105 - process: 3082189 - icp.py - icp - 138 - icp - []
SUCCESS - 2023-04-10 16:18:01,105 - process: 3082189 - icp.py - icp - 81 - icp - page_link: 1
SUCCESS - 2023-04-10 16:18:01,493 - process: 3082189 - icp.py - icp - 81 - icp - company len: 0

INFO - 2023-04-10 16:18:01,495 - process: 3082189 - icp.py - icp - 221 - icp - 华润三九(六安)中药材产业发展有限公司|100%|华润三九医药股份有限公司
INFO - 2023-04-10 16:18:02,492 - process: 3082189 - icp.py - icp - 138 - icp - []
SUCCESS - 2023-04-10 16:18:02,492 - process: 3082189 - icp.py - icp - 81 - icp - page_link: 0
SUCCESS - 2023-04-10 16:18:02,492 - process: 3082189 - icp.py - icp - 81 - icp - company len: 0

INFO - 2023-04-10 16:18:02,492 - process: 3082189 - icp.py - icp - 221 - icp - 华润三九(郴州)制药有限公司|100%|华润三九医药股份有限公司
INFO - 2023-04-10 16:18:02,886 - process: 3082189 - icp.py - icp - 138 - icp - []
SUCCESS - 2023-04-10 16:18:02,887 - process: 3082189 - icp.py - icp - 81 - icp - page_link: 3
SUCCESS - 2023-04-10 16:18:04,318 - process: 3082189 - icp.py - icp - 81 - icp - company len: 0

INFO - 2023-04-10 16:18:04,319 - process: 3082189 - icp.py - icp - 221 - icp - 华润圣海健康科技有限公司|65%|华润三九医药股份有限公司
INFO - 2023-04-10 16:18:07,533 - process: 3082189 - icp.py - icp - 138 - icp - []
SUCCESS - 2023-04-10 16:18:07,533 - process: 3082189 - icp.py - icp - 81 - icp - page_link: 1
SUCCESS - 2023-04-10 16:18:09,736 - process: 3082189 - icp.py - icp - 81 - icp - company len: 2
sdshenghai.cn
huarunshenghai.cn
INFO - 2023-04-10 16:18:09,736 - process: 3082189 - icp.py - icp - 221 - icp - 吉林三九金复康药业有限公司|65%|华润三九医药股份有限公司
INFO - 2023-04-10 16:18:10,433 - process: 3082189 - icp.py - icp - 138 - icp - []
SUCCESS - 2023-04-10 16:18:10,434 - process: 3082189 - icp.py - icp - 81 - icp - page_link: 1
SUCCESS - 2023-04-10 16:18:12,792 - process: 3082189 - icp.py - icp - 81 - icp - company len: 0

INFO - 2023-04-10 16:18:12,793 - process: 3082189 - icp.py - icp - 221 - icp - 浙江小九云药医药科技有限公司|51%|华润三九医药股份有限公司
INFO - 2023-04-10 16:18:13,322 - process: 3082189 - icp.py - icp - 138 - icp - []
SUCCESS - 2023-04-10 16:18:13,322 - process: 3082189 - icp.py - icp - 81 - icp - page_link: 1
SUCCESS - 2023-04-10 16:18:13,660 - process: 3082189 - icp.py - icp - 81 - icp - company len: 1
999xjyy.com
INFO - 2023-04-10 16:18:13,660 - process: 3082189 - icp.py - icp - 221 - icp - 雅安雨禾药业有限公司|90.09%|华润三九医药股份有限公司
INFO - 2023-04-10 16:18:14,044 - process: 3082189 - icp.py - icp - 138 - icp - []
SUCCESS - 2023-04-10 16:18:14,044 - process: 3082189 - icp.py - icp - 81 - icp - page_link: 1
SUCCESS - 2023-04-10 16:18:14,411 - process: 3082189 - icp.py - icp - 81 - icp - company len: 0

INFO - 2023-04-10 16:18:14,411 - process: 3082189 - icp.py - icp - 221 - icp - 河南三九大药房连锁有限公司|100%|浙江小九云药医药科技有限公司
INFO - 2023-04-10 16:18:14,976 - process: 3082189 - icp.py - icp - 138 - icp - []
SUCCESS - 2023-04-10 16:18:14,976 - process: 3082189 - icp.py - icp - 81 - icp - page_link: 0
SUCCESS - 2023-04-10 16:18:14,976 - process: 3082189 - icp.py - icp - 81 - icp - company len: 0
```


```
┌──(qwerty㉿qwerty)-[/mnt/hgfs/workspace/python_workspace]
└─$ python3 icp.py 华润电力工程服务有限公司 -d  -l                
INFO - 2023-04-10 15:18:08,832 - process: 3037216 - icp.py - icp - 213 - icp - ['华润电力工程服务有限公司']
INFO - 2023-04-10 15:18:09,232 - process: 3037216 - icp.py - icp - 138 - icp - []
SUCCESS - 2023-04-10 15:18:09,233 - process: 3037216 - icp.py - icp - 81 - icp - page_link: 1
SUCCESS - 2023-04-10 15:18:09,736 - process: 3037216 - icp.py - icp - 81 - icp - company len: 3
cr-power.com
crpower.com.cn
crp.net.cn
分支机构 
内蒙古华润金牛热电有限公司|75%|华润电力工程服务有限公司
沈阳华润热力有限公司|100%|华润电力工程服务有限公司
泸州华润水电开发有限公司|100%|华润电力工程服务有限公司
华润电力(广西)销售有限公司|100%|华润电力工程服务有限公司
华润电力(湖南)销售有限公司|100%|华润电力工程服务有限公司
深圳颐和置业有限公司|100%|华润电力工程服务有限公司
岚县润电新能源有限公司|51%|华润电力工程服务有限公司
广东润碳科技有限公司|51%|华润电力工程服务有限公司
深圳市润电投资有限公司|100%|华润电力工程服务有限公司
华润天能徐州煤电有限公司|100%|华润电力工程服务有限公司
INFO - 2023-04-10 15:18:09,737 - process: 3037216 - icp.py - icp - 221 - icp - 内蒙古华润金牛热电有限公司|75%|华润电力工程服务有限公司
INFO - 2023-04-10 15:18:10,050 - process: 3037216 - icp.py - icp - 138 - icp - []
SUCCESS - 2023-04-10 15:18:10,051 - process: 3037216 - icp.py - icp - 81 - icp - page_link: 1
SUCCESS - 2023-04-10 15:18:10,385 - process: 3037216 - icp.py - icp - 81 - icp - company len: 0

INFO - 2023-04-10 15:18:10,385 - process: 3037216 - icp.py - icp - 221 - icp - 沈阳华润热力有限公司|100%|华润电力工程服务有限公司
INFO - 2023-04-10 15:18:10,714 - process: 3037216 - icp.py - icp - 138 - icp - []
SUCCESS - 2023-04-10 15:18:10,714 - process: 3037216 - icp.py - icp - 81 - icp - page_link: 2
```