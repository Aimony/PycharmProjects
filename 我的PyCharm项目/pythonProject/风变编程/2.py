import json
import time
import random
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tbp.v20190627 import tbp_client, models


def request(comment):
    try:
        cred = credential.Credential("AKIDVwLZaNvEKJBqHTQ8bpoY4LM9h16wXt0s", "iAMIyOYS9bolSt51lHYZMxLVQ7ZmlW2J")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "tbp.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = tbp_client.TbpClient(cred, "", clientProfile)

        req = models.TextProcessRequest()
        params = {
            "BotId": "22f597c9-56fc-4475-aec4-6b54a2f8c194",
            "BotEnv": "release",
            "TerminalId": str(random.randint(1, 9999)),
            "InputText": comment
        }
        req.from_json_string(json.dumps(params))

        resp = client.TextProcess(req)
        return json.loads(resp.to_json_string())['ResponseMessage']['GroupList'][0]['Content']

    except TencentCloudSDKException as err:
        print('今天我出了一点小问题~快联系助教帮忙解决一下~~')
        exit()


def robot_think():
    print('\n思考中', end='')
    for i in range(6):
        print('.', end='')
        time.sleep(0.3)
    print('\n')


def robot_say(content):
    print('机器人：' + content, end='\n\n')
    time.sleep(1)


def ask():
    comment = input('> 我想说：')
    robot_think()
    content = request(comment)
    robot_say(content)


dialogues = [
    '大家好！我是你的聊天机器人。',
    '我有问必答，有人会问我“今天深圳天气怎么样？”，也有人问我“学编程有什么用？”',
    '快来问我问题呀，欢迎来撩！',
    '再来问我点啥吧！我把我知道的都告诉你，嘻嘻！',
    '我有点饿了，再和你聊完最后一句，我就要下线啦！你还有什么要问我的？',
    '我走啦，下次见！'
]

for i in dialogues[:3]:
    robot_say(i)

for i in dialogues[3:]:
    ask()
    robot_say(i)
