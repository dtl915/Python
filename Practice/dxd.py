import json
import requests
from bs4 import BeautifulSoup
import csv
def get_json_from_url(url:str,encoding:str)->str:
    """
    功能：给定url和编码，将获取的java script格式的json字符串转化为标准的json字符串并返回
    """
    r = requests.get(url, headers = {'user-agent': 'Mozilla/5.0'})
    r.encoding = encoding
    soup = BeautifulSoup(r.text, "html.parser")
    a=soup.contents[0]
    b=a.find('=')
    if  b>0:   json_str=a[a.index('=')+1:a.rindex('}')+1]
    elif b==0: raise Exception("错误的JSON字符串")
    else:      json_str=a[a.index('{'):a.rindex('}')+1]   
    return json_str
f=open('股票数据.csv','w',encoding='gbk',newline='')
f1=csv.writer(f)

translate={
'SECURITY_CODE':'股票代码','SECURITY_NAME_ABBR':'股票简称','BASIC_EPS':'每股收益','TOTAL_OPERATE_INCOME':'营业收入','YSTZ':'营业收入同比增长','YSHZ':'营业收入季度环比增长(%)',
'PARENT_NETPROFIT':'净利润','SJLTZ':'净利润同比增长(%)','SJLHZ':'净利润度环比增长(%)',
'BPS':'每股净资产','WEIGHTAVG_ROE':'净资产收益率(%)','MGJYXJJE':'每股经营现金流(元)','XSMLL':'销售毛利率(%)',
'ASSIGNDSCRPT':'利润分配','PUBLISHNAME':'所处行业','UPDATE_DATE':'最新公告日期'}
for num in range(1,10):
    lst1=[]

    url=f"""
    http://datacenter-web.eastmoney.com/api/data/get?callback=jQuery112306593734528082602_1631270787440&st=UPDATE_DATE%2CSECURITY_CODE&sr=-1%2C-1&ps=500&p={num}&type=RPT_LICO_FN_CPD&sty=ALL&token=894050c76af8597a853f5b408b759f5d&filter=(SECURITY_TYPE_CODE+in+(%22058001001%22%2C%22058001008%22))(REPORTDATE%3D%272021-06-30%27)
    """
    a=get_json_from_url(url,"UTF-8")
    a=json.loads(a)
    b=a['result']['data']
    lst=[]
    header=list(translate.keys())
    header1=list(translate.values())
    if num==1:
        f1.writerow(header1)
    for x in range(len(b)):
        templst=[]
        for i in header:
            templst.append(b[x][i])
        lst1.append(templst)
    f1.writerows(lst1)
f.close()