import requests
import json
import time
import ast
import os


# 易班打卡
def main(checkinfo):
    global date
    date = time.strftime("%Y-%m-%d", time.localtime())
    i = 0
    L = list(checkinfo.keys())
    L.sort()
    err = {}
    while i < len(checkinfo):
        post(checkinfo["{0}".format(L[i])][0],
             checkinfo["{0}".format(L[i])][1])
    # 先判断再推送
        if yb_result["code"] == 555555:
            err['{0}'.format(L[i])] = yb_result["msg"]
        elif yb_result["code"] != 0:
            err['{0}'.format(L[i])] = yb_result["msg"]
        i = i+1
    if len(err) != 0:
        print("{0}打卡失败".format(date))
        tuisong(err)
    else:
        print("{0}打卡完成".format(date))
        tuisong2()


def post(loginToken, studentID):
    global yb_result
    session = requests.Session()
    url_1 = "http://f.yiban.cn/iapp378946/i/{0}".format(loginToken)
    a = session.get(url=url_1, allow_redirects=False)
    url_2 = "http://f.yiban.cn{0}".format(a.headers['Location'])
    b = session.get(url=url_2, allow_redirects=False)
    if "Location" not in b.headers:
        yb_result = {'code': 555555, 'msg': 'loginToken错误，请修改'}
        return yb_result
    else:
        url_get = b.headers["Location"]
        c = session.get(url=url_get, allow_redirects=False)
        url_bind = "https://ygj.gduf.edu.cn/Handler/device.ashx?flag=checkBindDevice"
        bind = session.get(url=url_bind)
        url_save = "https://ygj.gduf.edu.cn/Handler/health.ashx?"
        data_yb_save = {
            "flag": "save",
            "studentID": "{0}".format(studentID),
            "date": "{0}".format(date),
            "health": "体温37.3℃以下（正常）",
            "address": "广东省广州市天河区龙洞街道广东金融学院校本部",
            "isTouch": "否",
            "isPatient": "不是"
        }
        d = session.post(url=url_save, data=data_yb_save)
        yb_result = json.loads(
            str(d.content, encoding="utf-8").encode("utf-8").decode('unicode_escape'))
        return yb_result


# 推送判断
def tuisong(err):
    # Server酱推送
    api = "https://sc.ftqq.com/{0}.send".format(SCKEY)
    data = {"text": "易班打卡异常提醒", "desp": str(err)}
    req = requests.post(api, data=data)
def tuisong2():
    api = "https://sc.ftqq.com/{0}.send".format(SCKEY)
    data = {"text": "易班打卡成功", "desp":"{0}打卡完成".format(date)}
    req = requests.post(api, data=data)



# 未完善的改良
def get_sectets(USERS):
    while True:
        try:
            info = USERS.split(',')
            checkinfo[info[0]] = [info[1], info[2]]
            return checkinfo
        except:
            break


if __name__ == "__main__":
    # sectets字段录入
    SCKEY = os.environ["SCKEY"]
    USERS = os.environ["USERS"]
    USERS = ast.literal_eval(USERS)

    # 调用改良
    # checkinfo = {}
    # get_sectets(USERS)
    # print(checkinfo)

    # 调用原版
    main(USERS)
