#!/usr/bin/env python
import requests
import re
from urllib import parse
from time import strftime, gmtime
def izhichen(userno, name):
    username = parse.quote(name)
    nowtime = strftime('%Y' + '-' + '%m' + '-' + '%d') + '%2000%3A01%3A03'
    urlse = 'http://dw10.fdzcxy.edu.cn/datawarn/ReportServer?formlet=app/sjkrb.frm&op=h5&userno=' + userno + '&token=eyJhbGciOiJSUzUxMiJ9.eyJBVFRSX3VzZXJObyI6IjIxMjEwNjYxOSIsInN1YiI6IjIxMjEwNjYxOSIsImlzcyI6InRva2VuLmZkemN4eS5lZHUuY24iLCJkZXZpY2VJZCI6Ilh0NHBtQW1EdnB3REFJQlBRY2F1UHhDSyIsIkFUVFJfaWRlbnRpdHlUeXBlSWQiOiJhNGFlNWIyMGZmNjIxMWViYjIzMTI1ZDkyY2RlZjNkNSIsIkFUVFJfYWNjb3VudElkIjoiYTJhYjNhNTBmZjcxMTFlYmM4YWNmYWIwOTY2ZjU0NTYiLCJBVFRSX3VzZXJJZCI6ImEyOWM5NDUwZmY3MTExZWJjOGFjZmFiMDk2NmY1NDU2IiwiQVRUUl9pZGVudGl0eVR5cGVDb2RlIjoiUzIwMjEiLCJBVFRSX2lkZW50aXR5VHlwZU5hbWUiOiIyMDIx57qn5a2m55SfIiwiQVRUUl9vcmdhbml6YXRpb25OYW1lIjoi6K6h566X5py65bel56iL57O7IiwiQVRUUl91c2VyTmFtZSI6Iuael-eri-ixqiIsImV4cCI6MTY0MzEyNzA0NCwiQVRUUl9vcmdhbml6YXRpb25JZCI6IjIxMzA3MDAwIiwiaWF0IjoxNjQwNTM1MDQ0LCJqdGkiOiJJZC1Ub2tlbi1Sb0xvTFJMSXJzcmdIZWZ6IiwicmVxIjoiY29tLmxhbnR1Lk1vYmlsZUNhbXB1cy56Y3h5IiwiQVRUUl9vcmdhbml6YXRpb25Db2RlIjoiMjEzMDcwMDAifQ.V2UvL6RuNRpd7aRRB6o26-rXYdl8iNwGFM4mtcthY4CVTUkM2__A6V6KOdm-qRCxoiVrMYnd4EzbVAWti6AlC0coIEjggWfUaJdRRowQndOLL0Y13xOnjh_hcTMUAIeYiXDa9UUBhuBa-e5PChbra0QBSatW684d4y6eDIn4MtU#/form'
    resse = requests.get(urlse)

    lst = re.findall(r"get sessionID\(\) \{return '(.*?)'},", resse.text)
    sessionID = lst[0]
    print(sessionID)
    urljs = "http://dw10.fdzcxy.edu.cn/datawarn/decision/view/form?sessionID=" + sessionID + "&op=fr_form&cmd=load_content&toVanCharts=tr"
    res = requests.get(urljs)
    jsConfId = re.findall(r'jsConfId:\"(.*?)\"', res.text)[0]
    callbackConfId = re.findall(r'callbackConfId:\"(.*?)\"', res.text)[0]
    print(jsConfId)
    print(callbackConfId)

    url = "http://dw10.fdzcxy.edu.cn/datawarn/decision/view/form"
    headers = {
        'sessionID': sessionID,
    }
    data = {
        'op': 'dbcommit',
        '__parameters__': '%7B%22jsConfId%22%3A%22' + jsConfId + '%22%2C%22callbackConfId%22%3A%22' + callbackConfId + '%22%2C%22LABEL2%22%3A%22%20%20%E6%AF%8F%E6%97%A5%E5%81%A5%E5%BA%B7%E4%B8%8A%E6%8A%A5%22%2C%22XH%22%3A%22' + userno + '%22%2C%22XM%22%3A%22' + username + '%22%2C%22LABEL12%22%3A%22%22%2C%22LABEL0%22%3A%221.%20%E7%9B%AE%E5%89%8D%E6%89%80%E5%9C%A8%E4%BD%8D%E7%BD%AE%3A%22%2C%22SHENG%22%3A%22350000%22%2C%22SHI%22%3A%22%E7%A6%8F%E5%B7%9E%E5%B8%82%22%2C%22QU%22%3A%22%E9%BC%93%E6%A5%BC%E5%8C%BA%22%2C%22LABEL11%22%3A%222.%E5%A1%AB%E6%8A%A5%E6%97%B6%E9%97%B4%3A%22%2C%22SJ%22%3A%22' + nowtime + '%22%2C%22LABEL1%22%3A%223.%20%E4%BB%8A%E6%97%A5%E4%BD%93%E6%B8%A9%E6%98%AF%E5%90%A6%E6%AD%A3%E5%B8%B8%EF%BC%9F(%E4%BD%93%E6%B8%A9%E5%B0%8F%E4%BA%8E37.3%E4%B8%BA%E6%AD%A3%E5%B8%B8)%22%2C%22TWZC%22%3A%22%E6%AD%A3%E5%B8%B8%22%2C%22LABEL6%22%3A%22%E7%9B%AE%E5%89%8D%E4%BD%93%E6%B8%A9%E4%B8%BA%EF%BC%9A%22%2C%22TW%22%3A%220%22%2C%22TXWZ%22%3A%22%E7%A6%8F%E5%BB%BA%E7%9C%81%E7%A6%8F%E5%B7%9E%E5%B8%82%E9%BC%93%E6%A5%BC%E5%8C%BA%22%2C%22LABEL9%22%3A%224.%20%E6%98%A8%E6%97%A5%E5%8D%88%E6%A3%80%E4%BD%93%E6%B8%A9%3A%22%2C%22WUJ%22%3A%2236.4%22%2C%22LABEL8%22%3A%225.%20%E6%98%A8%E6%97%A5%E6%99%9A%E6%A3%80%E4%BD%93%E6%B8%A9%3A%22%2C%22WJ%22%3A%2236.5%22%2C%22LABEL10%22%3A%226.%20%E4%BB%8A%E6%97%A5%E6%99%A8%E6%A3%80%E4%BD%93%E6%B8%A9%3A%22%2C%22CJ%22%3A%2236.4%22%2C%22LABEL3%22%3A%227.%20%E4%BB%8A%E6%97%A5%E5%81%A5%E5%BA%B7%E7%8A%B6%E5%86%B5%EF%BC%9F%22%2C%22JK%22%3A%5B%22%E5%81%A5%E5%BA%B7%22%5D%2C%22JKZK%22%3A%22%22%2C%22QTB%22%3A%22%E8%AF%B7%E8%BE%93%E5%85%A5%E5%85%B7%E4%BD%93%E7%97%87%E7%8A%B6%EF%BC%9A%22%2C%22QT%22%3A%22%20%22%2C%22LABEL4%22%3A%228.%20%E8%BF%9114%E6%97%A5%E4%BD%A0%E5%92%8C%E4%BD%A0%E7%9A%84%E5%85%B1%E5%90%8C%E5%B1%85%E4%BD%8F%E8%80%85(%E5%8C%85%E6%8B%AC%E5%AE%B6%E5%BA%AD%E6%88%90%E5%91%98%E3%80%81%E5%85%B1%E5%90%8C%E7%A7%9F%E4%BD%8F%E7%9A%84%E4%BA%BA%E5%91%98)%E6%98%AF%E5%90%A6%E5%AD%98%E5%9C%A8%E7%A1%AE%E8%AF%8A%E3%80%81%E7%96%91%E4%BC%BC%E3%80%81%E6%97%A0%E7%97%87%E7%8A%B6%E6%96%B0%E5%86%A0%E6%84%9F%E6%9F%93%E8%80%85%EF%BC%9F%22%2C%22WTSQK%22%3A%5B%22%E6%97%A0%E4%BB%A5%E4%B8%8B%E7%89%B9%E6%AE%8A%E6%83%85%E5%86%B5%22%5D%2C%22SFXG%22%3A%22%22%2C%22LABEL5%22%3A%229.%20%E4%BB%8A%E6%97%A5%E9%9A%94%E7%A6%BB%E6%83%85%E5%86%B5%EF%BC%9F%22%2C%22GLQK%22%3A%22%E6%97%A0%E9%9C%80%E9%9A%94%E7%A6%BB%22%2C%22LABEL7%22%3A%22*%20%E6%9C%AC%E4%BA%BA%E6%89%BF%E8%AF%BA%E4%BB%A5%E4%B8%8A%E6%89%80%E5%A1%AB%E6%8A%A5%E7%9A%84%E5%86%85%E5%AE%B9%E5%85%A8%E9%83%A8%E7%9C%9F%E5%AE%9E%EF%BC%8C%E5%B9%B6%E6%84%BF%E6%84%8F%E6%89%BF%E6%8B%85%E7%9B%B8%E5%BA%94%E8%B4%A3%E4%BB%BB%E3%80%82%22%2C%22CHECK%22%3Atrue%2C%22WZXXXX%22%3A%222%22%2C%22DWWZ%22%3A%7B%7D%2C%22SUBMIT%22%3A%22%E6%8F%90%E4%BA%A4%E4%BF%A1%E6%81%AF%22%7D'

    }
    request = requests.post(url, data=data, headers=headers)
    print(request.text)
    print("提交完毕")
izhichen('212104127','苏睿宁')
