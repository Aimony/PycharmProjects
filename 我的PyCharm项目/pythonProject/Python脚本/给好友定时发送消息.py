
import win32gui
import win32con
import win32clipboard as w
import requests,re,time
from fake_useragent import UserAgent
from apscheduler.schedulers.blocking import BlockingScheduler

'''添加剪切板文本'''
def setText(string):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT,string)
    w.CloseClipboard()

'''执行发送操作'''
'''
    to:QQ消息接收人；
    msg:需要发送的消息
'''
def sendMsg(to,msg):
    setText(msg)
    qq = win32gui.FindWindow(None,to)
    win32gui.SendMessage(qq,258,22,2080193)
    win32gui.SendMessage(qq,770,0,0)
    win32gui.SendMessage(qq,win32con.WM_KEYDOWN,win32con.VK_RETURN,0) # 控制按键，按下
    win32gui.SendMessage(qq,win32con.WM_KEYUP,win32con.VK_RETURN,0) # 控制按键，放松

'''青云客机器人(免费api)'''
def qyk(msg):
    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg=' + msg
    ua = UserAgent()
    headers = {
        'User_Agent': ua.random # 伪装User_Agent信息
    }
    response = requests.get(url=url,headers = headers)
    response.encoding = 'utf-8'
    text = response.text
    info = re.findall(r'\"\[.*?\"',text)
    weather = info[0].replace('"','')
    return weather

'''定时任务'''
def timingJob(to,msg):
    scheduler = BlockingScheduler() # 创建调度器
    scheduler.add_job(sendMsg,'interval',seconds=30,args = [to,msg]) # interval间隔,10s
    # scheduler.add_job(sendMsg,'cron',hour='22-23',minute='49',second='*/10',args = [to,msg]) # cron定时,10s
    scheduler.start() # 开启定时任务

if __name__ == '__main__':
    to = input('请填写解接收人QQ ：')
    msg = qyk('重庆天气')
    timingJob(to,msg)