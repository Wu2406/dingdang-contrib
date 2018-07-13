# -*- coding: utf-8-*-                                                                                                                                                         # 天气插件
import sys
import json, urllib,requests
reload(sys)
sys.setdefaultencoding('utf8')
# Standard module stuff                                                                                                                                                     WORDS = []
SLUG = "headline_news"
WORDS = ["XINWEN"]
API = "http://www.tuling123.com/openapi/api"
params = {
        "key":"7a9a22943621490cab7627e6b6a6e1e2",
        "info":"今日新闻"
    }
def handle(text, mic, profile, wxbot=None):
    if SLUG not in profile or \
       'key' not in profile[SLUG]:
        mic.say(u"新闻插件配置有误，插件使用失败", cache=True)
        return
    key = profile[SLUG]['key']
    params = {
        "key":key,
        "info":"今日新闻"
    }

    mic.say("正在获取中，请稍后")
    result = requests.get(API, params, timeout=1)
    json_dict = json.loads(result.text)
    news_for_tts = "转换完成，以下是今日新闻:"
    mic.say("亲，已帮您找到相关新闻,正在转为语音")
    for item in json_dict['list']:
		title = item['article']
		news_for_tts = news_for_tts + title + '，'
    mic.say(news_for_tts)
    mic.say('新闻播放结束', cache=True)
    pass

def isValid(text):
    """
        Returns True if the input is related to weather.
        Arguments:
        text -- user-input, typically transcribed speech
    """
    return u"新闻" in text
