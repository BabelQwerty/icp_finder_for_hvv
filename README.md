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
┌──(qwerty㉿qwerty)-[/mnt/hgfs/workspace/python_workspace/icp_finder_for_hvv]
└─$ python3 icp.py -d -l liepin.com                                                                                
INFO - 2023-04-15 18:22:12,323 - process: 189238 - icp.py - icp - 213 - icp - finding liepin.com
liepin.cn
分支机构 
无锡万仕道教育咨询有限公司|100%|同道精英(天津)信息技术有限公司
浙江同道精英信息技术有限公司|100%|同道精英(天津)信息技术有限公司
同道快才(上海)劳务派遣有限公司|100%|同道精英(天津)信息技术有限公司
同道有薪(天津)信息技术有限公司|51%|同道精英(天津)信息技术有限公司
同道有才(广州)人力资源服务有限公司|100%|同道精英(天津)信息技术有限公司
猎聘凯普斯(天津)信息技术有限公司|51%|同道精英(天津)信息技术有限公司
同道有才(北京)人力资源服务有限公司|100%|同道精英(天津)信息技术有限公司
同道猎聘(北京)科技有限公司|100%|同道精英(天津)信息技术有限公司
上海德筑企业管理有限公司|51%|同道精英(天津)信息技术有限公司
INFO - 2023-04-15 18:22:26,966 - process: 189238 - icp.py - icp - 221 - icp - finding 无锡万仕道教育咨询有限公司|100%|同道精英(天津)信息技术有限公司 

INFO - 2023-04-15 18:22:27,884 - process: 189238 - icp.py - icp - 221 - icp - finding 浙江同道精英信息技术有限公司|100%|同道精英(天津)信息技术有限公司 

INFO - 2023-04-15 18:22:28,196 - process: 189238 - icp.py - icp - 221 - icp - finding 同道快才(上海)劳务派遣有限公司|100%|同道精英(天津)信息技术有限公司 

INFO - 2023-04-15 18:22:28,844 - process: 189238 - icp.py - icp - 221 - icp - finding 同道有薪(天津)信息技术有限公司|51%|同道精英(天津)信息技术有限公司 

INFO - 2023-04-15 18:22:29,925 - process: 189238 - icp.py - icp - 221 - icp - finding 同道有才(广州)人力资源服务有限公司|100%|同道精英(天津)信息技术有限公司 

INFO - 2023-04-15 18:22:30,338 - process: 189238 - icp.py - icp - 221 - icp - finding 猎聘凯普斯(天津)信息技术有限公司|51%|同道精英(天津)信息技术有限公司 

INFO - 2023-04-15 18:22:31,219 - process: 189238 - icp.py - icp - 221 - icp - finding 同道有才(北京)人力资源服务有限公司|100%|同道精英(天津)信息技术有限公司 

INFO - 2023-04-15 18:22:31,639 - process: 189238 - icp.py - icp - 221 - icp - finding 同道猎聘(北京)科技有限公司|100%|同道精英(天津)信息技术有限公司 

INFO - 2023-04-15 18:22:32,418 - process: 189238 - icp.py - icp - 221 - icp - finding 上海德筑企业管理有限公司|51%|同道精英(天津)信息技术有限公司 
cgladvisory.cn
wearecgl.cn
rencaigeili.com
wearecgl.com
cgladvisory.com
sts-partner.com
```


```
┌──(qwerty㉿qwerty)-[/mnt/hgfs/workspace/python_workspace/icp_finder_for_hvv]
└─$ python3 icp.py -d -l 同道精英(天津)信息技术有限公司                 
INFO - 2023-04-15 18:42:30,370 - process: 206992 - icp.py - icp - 213 - icp - finding 同道精英(天津)信息技术有限公司
liepin.cn
分支机构 
无锡万仕道教育咨询有限公司|100%|同道精英(天津)信息技术有限公司
浙江同道精英信息技术有限公司|100%|同道精英(天津)信息技术有限公司
同道快才(上海)劳务派遣有限公司|100%|同道精英(天津)信息技术有限公司
同道有薪(天津)信息技术有限公司|51%|同道精英(天津)信息技术有限公司
同道有才(广州)人力资源服务有限公司|100%|同道精英(天津)信息技术有限公司
猎聘凯普斯(天津)信息技术有限公司|51%|同道精英(天津)信息技术有限公司
同道有才(北京)人力资源服务有限公司|100%|同道精英(天津)信息技术有限公司
同道猎聘(北京)科技有限公司|100%|同道精英(天津)信息技术有限公司
上海德筑企业管理有限公司|51%|同道精英(天津)信息技术有限公司
INFO - 2023-04-15 18:42:55,929 - process: 206992 - icp.py - icp - 221 - icp - finding 无锡万仕道教育咨询有限公司|100%|同道精英(天津)信息技术有限公司 

INFO - 2023-04-15 18:42:57,022 - process: 206992 - icp.py - icp - 221 - icp - finding 浙江同道精英信息技术有限公司|100%|同道精英(天津)信息技术有限公司 

INFO - 2023-04-15 18:42:59,445 - process: 206992 - icp.py - icp - 221 - icp - finding 同道快才(上海)劳务派遣有限公司|100%|同道精英(天津)信息技术有限公司 

INFO - 2023-04-15 18:42:59,900 - process: 206992 - icp.py - icp - 221 - icp - finding 同道有薪(天津)信息技术有限公司|51%|同道精英(天津)信息技术有限公司 

INFO - 2023-04-15 18:43:01,028 - process: 206992 - icp.py - icp - 221 - icp - finding 同道有才(广州)人力资源服务有限公司|100%|同道精英(天津)信息技术有限公司 

INFO - 2023-04-15 18:43:01,353 - process: 206992 - icp.py - icp - 221 - icp - finding 猎聘凯普斯(天津)信息技术有限公司|51%|同道精英(天津)信息技术有限公司 

INFO - 2023-04-15 18:43:02,805 - process: 206992 - icp.py - icp - 221 - icp - finding 同道有才(北京)人力资源服务有限公司|100%|同道精英(天津)信息技术有限公司 

INFO - 2023-04-15 18:43:03,337 - process: 206992 - icp.py - icp - 221 - icp - finding 同道猎聘(北京)科技有限公司|100%|同道精英(天津)信息技术有限公司 

INFO - 2023-04-15 18:43:06,790 - process: 206992 - icp.py - icp - 221 - icp - finding 上海德筑企业管理有限公司|51%|同道精英(天津)信息技术有限公司 
sts-partner.com
cgladvisory.com
rencaigeili.com
cgladvisory.cn
wearecgl.cn
wearecgl.com
```

run with subfinder/httpx automate:
```
┌──(qwerty㉿qwerty)-[/mnt/hgfs/workspace/python_workspace/icp_finder_for_hvv]
└─$ python3 icp.py -d -l liepin.com | grep -E   "[a-zA-Z0-9.\\/_&=@$%?~#-]" |  ./subfinder -silent | ./httpx -silent       
[INF] Detected old /home/qwerty/.config/subfinder/config.yaml config file, trying to migrate providers to /home/qwerty/.config/subfinder/provider-config.yaml
[INF] Migration successful from /home/qwerty/.config/subfinder/config.yaml to /home/qwerty/.config/subfinder/provider-config.yaml.
INFO - 2023-04-15 18:54:18,727 - process: 219824 - icp.py - icp - 213 - icp - finding liepin.com
分支机构 
无锡万仕道教育咨询有限公司|100%|同道精英(天津)信息技术有限公司
浙江同道精英信息技术有限公司|100%|同道精英(天津)信息技术有限公司
同道快才(上海)劳务派遣有限公司|100%|同道精英(天津)信息技术有限公司
同道有薪(天津)信息技术有限公司|51%|同道精英(天津)信息技术有限公司
同道有才(广州)人力资源服务有限公司|100%|同道精英(天津)信息技术有限公司
猎聘凯普斯(天津)信息技术有限公司|51%|同道精英(天津)信息技术有限公司
同道有才(北京)人力资源服务有限公司|100%|同道精英(天津)信息技术有限公司
同道猎聘(北京)科技有限公司|100%|同道精英(天津)信息技术有限公司
上海德筑企业管理有限公司|51%|同道精英(天津)信息技术有限公司
INFO - 2023-04-15 18:54:50,282 - process: 219824 - icp.py - icp - 221 - icp - finding 无锡万仕道教育咨询有限公司|100%|同道精英(天津)信息技术有限公司 
INFO - 2023-04-15 18:54:55,052 - process: 219824 - icp.py - icp - 221 - icp - finding 浙江同道精英信息技术有限公司|100%|同道精英(天津)信息技术有限公司 
INFO - 2023-04-15 18:54:55,406 - process: 219824 - icp.py - icp - 221 - icp - finding 同道快才(上海)劳务派遣有限公司|100%|同道精英(天津)信息技术有限公司 
INFO - 2023-04-15 18:54:55,814 - process: 219824 - icp.py - icp - 221 - icp - finding 同道有薪(天津)信息技术有限公司|51%|同道精英(天津)信息技术有限公司 
INFO - 2023-04-15 18:54:57,556 - process: 219824 - icp.py - icp - 221 - icp - finding 同道有才(广州)人力资源服务有限公司|100%|同道精英(天津)信息技术有限公司 
INFO - 2023-04-15 18:54:58,206 - process: 219824 - icp.py - icp - 221 - icp - finding 猎聘凯普斯(天津)信息技术有限公司|51%|同道精英(天津)信息技术有限公司 
INFO - 2023-04-15 18:54:58,969 - process: 219824 - icp.py - icp - 221 - icp - finding 同道有才(北京)人力资源服务有限公司|100%|同道精英(天津)信息技术有限公司 
INFO - 2023-04-15 18:54:59,392 - process: 219824 - icp.py - icp - 221 - icp - finding 同道猎聘(北京)科技有限公司|100%|同道精英(天津)信息技术有限公司 
INFO - 2023-04-15 18:55:00,705 - process: 219824 - icp.py - icp - 221 - icp - finding 上海德筑企业管理有限公司|51%|同道精英(天津)信息技术有限公司 
https://cgl.cgladvisory.com
https://www.cgladvisory.com
https://jipin.liepin.cn
https://gtm-cn-n6w1wwww011.liepin.cn
https://m-crecruit.liepin.cn
https://m-c.liepin.cn
https://web-lp-other.op.liepin.cn
https://m-inviteapply.liepin.cn
https://rivers.liepin.cn
https://liepin.cn
https://openapi.rencaigeili.com
https://file.rencaigeili.com
https://website.rencaigeili.com
https://file-zm.test.rencaigeili.com
https://baizhong.liepin.cn
https://file-zm.rencaigeili.com
https://zm.api.rencaigeili.com
https://oms.rencaigeili.com
https://web-lp-b.op.liepin.cn
https://oms.api.rencaigeili.com
https://api.rencaigeili.com
https://wow.liepin.cn
https://website.api.rencaigeili.com
https://caice.liepin.cn
https://m-jipin.liepin.cn
https://app-crecruit.liepin.cn
https://qa-wow.liepin.cn
https://file-mdl.test.rencaigeili.com
https://file.test.rencaigeili.com
https://www.liepin.cn
https://touchway.liepin.cn
https://app-tongdao.liepin.cn
https://www.wearecgl.com
https://file-website.rencaigeili.com
https://file-mdl.rencaigeili.com
https://passport.liepin.cn
https://web-lp-c.op.liepin.cn
http://global.wearecgl.com
```