import hashlib
import json
from random import choice
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt  # 解除csrf验证
from wechat_sdk import WechatConf
from wechat_sdk import WechatBasic

from wechat_sdk.exceptions import ParseError
# from django.shortcuts import render
import requests

# W92a22dE411LJHEQG2MszRingLZsRI33LMAGhfng8Uo
# 20CE57016F931069C39BBE0976EBAB2A

conf = WechatConf(  # 实例化配置信息对象
    token='20CE57016F931069C39BBE0976EBAB2A',  # 服务器配置-Token
    appid='gh_25a68465759f',  # 公众号开发信息-开发者ID
    appsecret='glz123456',  # 公众号开发信息-开发者密码
    encrypt_mode='normal',  # 服务器配置-明文模式
    encoding_aes_key='W92a22dE411LJHEQG2MszRingLZsRI33LMAGhfng8Uo'  # 服务器配置-EncodingAESKey
)

wechat = WechatBasic(token="20CE57016F931069C39BBE0976EBAB2A", appid="wxc03bd4226a49bbbd",
                     appsecret="W92a22dE411LJHEQG2MszRingLZsRI33LMAGhfng8Uo")
reply_list = ["请问下一个问题！", "我还没吃饱，忘记这个问题该怎么回答了^-^", "请我五百年的时间考虑怎么回答你。",
              "可以换一个问题吗？", "发生了异常！", "唔---", "emmmmmmm", "2333333333"]


# @csrf_exempt  # 去除csrf验证
# def get_reply(request):
#     signature = request.GET.get('signature')  # 获取请求信息
#     timestamp = request.GET.get('timestamp')
#     nonce = request.GET.get('nonce')
#     wechat_instance = WechatBasic(conf=conf)  # 实例化微信基类对象
#     if not wechat_instance.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):  # 检查验证请求的签名
#         return HttpResponseBadRequest('Verify Failed')
#     else:
#         if request.method == 'GET':
#             return HttpResponse(request.GET.get('echostr', None))  # 返回请求中的回复信息


@csrf_exempt
def get_reply(request):
    signature = request.GET.get('signature')  # 获取请求信息
    timestamp = request.GET.get('timestamp')
    nonce = request.GET.get('nonce')
    wechat_instance = WechatBasic(conf=conf)  # 实例化微信基类对象
    if not wechat_instance.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):  # 检查验证请求的签名
        return HttpResponseBadRequest('Verify Failed')
    else:
        # if request.method == 'GET':
        #     return HttpResponse(request.GET.get('echostr', None))  # 返回请求中的回复信息

        # data = requests.post.get
        # if request.method == 'GET':
        #     data = request.GET.get('data')
        # elif request.method == 'POST':
        #     data = request.POST.get('data')
        # else:
        #     return HttpResponse("俺也不知道发生了什么！")

        try:
            wechat.parse_data(data=request.body)
        except ParseError:
            return HttpResponseBadRequest('无效的xml数据')
        message = wechat.get_message()
        data = message.content.strip()
        print(data)
        url = "https://api.ownthink.com/bot"
        body = {
            "spoken": data,
            "appid": "f2a2c494b2a7022199e95d22572635e4",
            "userid": "hehe"
        }
        try:
            res = requests.post(url, data=json.dumps(body))
            data = json.loads(res.text)
            if data["message"] == "success":
                reply = data["data"]["info"]["text"]
                print(reply)
                if not reply:
                    reply = choice(reply_list)
            else:
                reply = "服务器异常"

        except:
            reply = choice(reply_list)
        result = wechat.response_text(content=reply)
        return HttpResponse(result, content_type='application/xml')
