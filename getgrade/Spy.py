import re
import http.cookiejar
import urllib.request
import urllib.parse

def getGrade(stuid,pw):
    
    cookie=http.cookiejar.CookieJar()
    opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    postdata=urllib.parse.urlencode({'code':stuid,'password':pw}).encode('utf-8')
    req=urllib.request.Request(url='http://zdgxyplatform.ecust.edu.cn/zdxy/logon.action',data=postdata)
    opener.open(req)
    result=opener.open('http://zdgxyplatform.ecust.edu.cn/zdxy/examScoreSearchDo.action').read().decode('utf-8')
    re_pattag=r'<td nowrap.*?>\s*(.*?)\s*<'
    
    grade_now=re.findall(re_pattag,result)
    
    i=1
    row={}
    nameid=1
    gradeid=9
    strname=""
    strgrade=""
    for k in range(len(grade_now)-1):
        if(i%nameid==0):
            strname=grade_now[i]
            nameid=nameid+11
        elif(i%gradeid==0):
            gradeid=gradeid+11
            row[strname]=grade_now[i]
        i=i+1
    return row

# print(getGrade(,))  # 此处输入你的用户名和学号
