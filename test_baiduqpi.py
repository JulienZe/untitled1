# import requests
# import random
# import hashlib
#
# query = '["adult","beautiful","bouquet","bride","flower","fun","grass","happiness","marriage","outdoors","park","person","portrait","trees","wedding","white dress","woman","young"]'
# from_language = 'en'
# to_language = 'zh'
# appid = '20190118000257610'  #你的appid
# secret_key = 'uRyguzezk35B5kJSwqgl'    #你的密钥
# salt = random.randint(32768, 65536)
# sign = appid+query+str(salt)+secret_key
# sign = hashlib.md5(sign.encode('UTF-8')).hexdigest()
#
# baidu_api = 'https://api.fanyi.baidu.com/api/trans/vip/translate?q={query}&from={from_language}&' \
#             'to={to_language}&appid={appid}&salt={salt}&sign={sign}'.format(query=query, from_language=from_language,
#                                                                             to_language=to_language, appid=appid,
#                                                                             salt=salt,
#                                                                             sign=sign)
#
# response = requests.get(baidu_api)
# print(response.json())

#
# import hashlib
#
# query = '小黑裙'
#
# appKey = '5f4646739cbb0ae6'
# salt = '2'
# key = '42zUNzwm3D0f8SoYduvof3dFTWAerXwV'
#
# src = appKey+query+salt+key
# m = hashlib.md5()
# m.update(src.encode('utf-8'))
#
# md5value = m.hexdigest()
#
# import json
# import requests
# import urllib.parse
#
# query = urllib.parse.quote(query)
# url = "http://openapi.youdao.com/api?q={}&from=auto&to=auto&appKey={}&salt={}&sign={}".format(query,appKey,salt,md5value)
# try:
#     res = requests.get(url,timeout=0.3)
# except:
#     pass
#
# res = res.json()
# print (res)

import requests
from PIL import Image
from io import BytesIO
a = requests.get('https://mydesycdn.mydesy.com/wp-content/uploads/2015/03/haibao1.jpg')
#
import datetime
# start = datetime.datetime.now()
# m = Image.open(BytesIO(a.content))
# width, height = m.size
# print(width,height)
# end = datetime.datetime.now()
# print(end-start)

import imagesize
print(dir(imagesize))
exit(0)
start = datetime.datetime.now()

width, height = imagesize.get(a.content)
print(width, height)
end = datetime.datetime.now()
