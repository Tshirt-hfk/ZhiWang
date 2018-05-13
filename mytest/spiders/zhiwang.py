# -*- coding: utf-8 -*-
import scrapy
import datetime


class ZhiwangSpider(scrapy.Spider):
    name = 'zhiwang'
    start_urls = [r'http://kns.cnki.net/kns/brief/brief.aspx?curpage=3&RecordsPerPage=50&QueryID=47&ID=&turnpage=1&tpagemode=L&dbPrefix=SCDB&Fields=&DisplayMode=listmode&PageName=ASP.brief_result_aspx']

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0],headers={
            'user-agent': r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            'Host' : 'kns.cnki.net'
        },cookies={
            'Ecp_notFirstLogin':'ipJyNJ',
            'ASP.NET_SessionId':'tzlgg5c3ipprp3d1qkc4rzsm',
            'Ecp_ClientId':1180413144103895888,
            'Ecp_LoginStuts':r'%7B%22IsAutoLogin%22%3Afalse%2C%22UserName%22%3A%22K10053%22%2C%22ShowName%22%3A%22%25E5%258C%2597%25E4%25BA%25AC%25E8%2588%25AA%25E7%25A9%25BA%25E8%2588%25AA%25E5%25A4%25A9%25E5%25A4%25A7%25E5%25AD%25A6%22%2C%22UserType%22%3A%22bk%22%2C%22r%22%3A%22ipJyNJ%22%7D',
            'Ecp_lout':1,
            'Ecp_session':1,
            'LID':'WEEvREcwSlJHSldRa1FhdXNXa0hIeTFjNnEzQ2h3Vi9FZnZQbFpHeEJGRT0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!',
            'SID_kns':123107,
            'SID_kmycnki':125122,
            'SID_klogin':125144,
            'SID_kinfo':125105,
            'UM_distinctid':'162bdbf72711dc-09b7e0dfbb20c5-b34356b-144000-162bdbf7272da4',
            'SID_crrs':125134,
            'SID_krsnew':125131,
            'cnkiUserKey':'af2c6e3b-5007-5b00-977f-ba12664c2ff4',
            'RsPerPage':50,
            '_pk_ref':r'%5B%22%22%2C%22%22%2C1523612921%2C%22http%3A%2F%2Fwww.cnki.net%2F%22%5D',
            '_pk_ses':'*',
            'KNS_DisplayModel':'listmode@SCDB',
            '_pk_id':'1632ae3d-edb2-4de9-bb30-9b83dc5609a1.1523601889.2.1523618200.1523612921.',
            'c_m_LinID':r'LinID=WEEvREcwSlJHSldRa1FhdXNXa0hIeTFjNnEzQ2h3Vi9FZnZQbFpHeEJGRT0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!&ot=04/13/2018'+datetime.datetime.now().strftime(' %H:%M:%S'),
            'c_m_expire':'2018-04-13'+datetime.datetime.now().strftime(' %H:%M:%S')
        })

    def parse(self, response):
        f=open('out.html',"w")
        text=response.xpath(r'//*[@class="GridTableContent"]').extract()
        print(text,file=f)

        text2=response.xpath(r'//*[@class="GridTableContent"]/tr[2]/td[2]/a/text()').extract()
        print(text2)