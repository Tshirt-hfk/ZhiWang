# -*- coding: utf-8 -*-
import scrapy
import datetime
from mytest.items import MytestItem
import json

class ZhiwangSpider(scrapy.Spider):
    name = 'zhiwang'
    start_urls = [r'http://kns.cnki.net/kns/brief/brief.aspx?curpage=2&RecordsPerPage=50&QueryID=25&ID=&turnpage=1&tpagemode=L&dbPrefix=SCDB&Fields=&DisplayMode=listmode&PageName=ASP.brief_result_aspx']

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0],headers={
            'user-agent': r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            'Host' : 'kns.cnki.net'
        },cookies={
            '_pk_ses':'*',
            '_pk_id':'1632ae3d-edb2-4de9-bb30-9b83dc5609a1.1523601889.4.1528770405.1528769760.',
            '_pk_ref':r'%5B%22%22%2C%22%22%2C1523612921%2C%22http%3A%2F%2Fwww.cnki.net%2F%22%5D',
            'ASP.NET_SessionId':'g4poz4nocz55zzcrcuovnx0i',
            'cnkiUserKey':'af2c6e3b-5007-5b00-977f-ba12664c2ff4',
            'CNZZDATA3258975':r'cnzz_eid%3D907412175-1527851513-http%253A%252F%252Fxueshu.baidu.com%252F%26ntime%3D1527851513',
            'Ecp_ClientId':1180413144103895888,
            'Ecp_notFirstLogin':"XSC3BR",
            'Ecp_session':1,
            'LID':'WEEvREcwSlJHSldRa1Fhb09jSnZqemk0dlUzUERwSTR3bkRsTmExK05RMD0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!',
            'RsPerPage':50,
            'SID_klogin':125142,
            'SID_kns':123124,
            'SID_krsnew':125134,
            'UM_distinctid':'162bdbf72711dc-09b7e0dfbb20c5-b34356b-144000-162bdbf7272da4'
        })

    def parse(self, response):
        f=open('result.json',"w")
        for result in response.xpath(r'//*[@class="GridTableContent"]/tr'):
            result.
            item=MytestItem()
            item["title"]=result.xpath(r'./td[2]/a/text()').extract()
            item['author']=result.xpath(r'./td[3]/a/text()').extract()
            item['orign']=result.xpath(r'./td[4]/a/text()').extract()
            print(json.dumps(dict(item)))
            # yield item
        # f=open('out.txt',"w")
        # text2=response.xpath(r'//*[@class="GridTableContent"]/tr/td[2]/a/text()').extract()
        # text3=response.xpath(r'//*[@class="GridTableContent"]/tr/td[3]/a/text()').extract()
        # text4=response.xpath(r'//*[@class="GridTableContent"]/tr/td[4]/a/text()').extract()
        # print(text3,file=f)