import json
from random import choice
from django.http import HttpResponse
# from django.shortcuts import render
import requests
# W92a22dE411LJHEQG2MszRingLZsRI33LMAGhfng8Uo
# 20CE57016F931069C39BBE0976EBAB2A

# Create your views here.
def get_reply(request):
    reply_list = ["请问下一个问题！", "我还没吃饱，忘记这个问题该怎么回答了^-^", "请我五百年的时间考虑怎么回答你。",
                  "可以换一个问题吗？", "发生了异常！", "唔---", "emmmmmmm", "2333333333"]
    # data = requests.post.get
    if request.method == 'GET':
        data = request.GET.get('data')
        tokon = request.GET.get('tokon')
    elif request.method == 'POST':
        data = request.POST.get('data')
        tokon = request.POST.get('tokon')
    else:
        return HttpResponse("俺也不知道发生了什么！")
    url = "https://api.ownthink.com/bot"
    body = {
        "spoken": data,
        "appid": "f2a2c494b2a7022199e95d22572635e4",
        "userid": "hehe"
    }
    try:
        res = requests.post(url, data=json.dumps(body))
        reply = res.text()
        if not reply:
            reply = choice(reply_list)
    except:
        reply = choice(reply_list)
    # return HttpResponse(reply)
    if tokon == "20CE57016F931069C39BBE0976EBAB2A":
        return HttpResponse("20CE57016F931069C39BBE0976EBAB2A")
