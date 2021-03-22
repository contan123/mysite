# coding:utf-8
import requests
from bs4 import BeautifulSoup
from http.cookiejar import CookieJar
import datetime
import random
import re

def ver(obj,date):
    #验证是否能成功填报
    login_url = 'https://cas.njcit.cn/login/login?service=https%3A%2F%2Fi.njcit.cn%2FEIP%2Fuser%2Findex.htm'

    head = {}

    user_agent_list = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/61.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
    ]
    head['User-Agent'] = random.choice(user_agent_list)

    list = [obj]

    for i in list:

        try:
            session = requests.session()
            session.cookies = CookieJar()
            r = session.get(login_url, headers=head)
            soup = BeautifulSoup(r.text, 'lxml')
            lt = soup.find('input', {'name': 'lt'})['value']
            execution = soup.find('input', {'name': 'execution'})['value']
            _eventId = soup.find('input', {'name': '_eventId'})['value']
            postData = {
                'username': i.get('username'),
                'password': i.get('password'),
                'lt': lt,
                'captcha': '',
                'execution': execution,
                '_eventId': _eventId,
            }

            r = session.post(login_url, headers=head, data=postData)

            time = datetime.date.today()

            name = i.get('name')
            XY = i.get("XY")
            BJ = i.get('BJ')
            FDY = i.get("FDY")
            SSH = i.get('SSH')
            post = {}
            post['formJson'] = r'[{"id":"","TBSJ":' + str(time) + ',"XM":"' + name + '","XH":' + postData[
                'username'] + ',"XY":"' + XY + '","BJ":"' + BJ + '",' \
                                                                 r'"SSH":"' + SSH + '","FDY":"' + FDY + '","DRSTZK":"1@#@健康","STBSSM":"","XZHS":"320000@#@江苏省",' \
                                                                                                        r'"XZHSS":"320100@#@南京市","XZHQ":"320113@#@栖霞区","SFFR":"2@#@否","SFJCFR":"2@#@否",' \
                                                                                                        r'"SFQGGF":"2@#@否","SFQGGAT":"2@#@否","SFJCGW":"2@#@否","SFQGQD":"2@#@否","SFJCQDRY":"2@#@否",' \
                                                                                                        r'"SFQGFY":"2@#@否","SFQGDJ":"2@#@否","SFQGKS":"2@#@否","SFJCKS":"2@#@否","HT4A7A19":"2@#@否",' \
                                                                                                        r'"HT375D9E":"2@#@否","SFSCTB":"2@#@否","CFSJ":"","DXSJ":"","CFDD":"","TXRXM":"","TXRLXFS":"",' \
                                                                                                        r'"JTGJ":"","CZSJ":"","HCXX":"","FJJTXX":"","HCJTXX":"","DBJTXX":"","DTJTXX":"","GJTJXX":"",' \
                                                                                                        r'"WYCJTXX":"","SJCJTXX":"","QTJTXX":"","pagesize":10,"HT11E434":"无","HTDD18DB":"无",' \
                                                                                                        r'"WCCZH":"无","SQLXQK":"","formId":"5e407b9770f7847701712e33bc946b4a","SFQGGFX":"2@#@否",' \
                                                                                                        r'"SWDD":"[{\"_id\":1,\"_uid\":1,\"_state\":\"added\",\"SWDDXZ\":\"宿舍1-10栋\",' \
                                                                                                        r'\"SWDDXZ##text\":\"宿舍1-10栋\",\"SYSJ\":\"' + str(
                time) + r'T10:53:59\"}]",' \
                        r'"ZWDD":"[{\"ZWSJ\":\"' + str(time) + r' 10:54\",\"_id\":2,\"_uid\":2,\"_state\":\"added\",' \
                                                               r'\"ZWDD\":\"宿舍1-10栋\",\"ZWDD##text\":\"宿舍1-10栋\"}]","XWDD":"[{\"XWSJ\":\"' + str(
                time) + r' 10:54\",' \
                        r'\"_id\":3,\"_uid\":3,\"_state\":\"added\",\"XWDD\":\"宿舍1-10栋\",\"XWDD##text\":\"宿舍1-10栋\"}]",' \
                        r'"HTBD059F":"[{\"WSSJ\":\"' + str(
                time) + r' 10:54\",\"_id\":4,\"_uid\":4,\"_state\":\"added\",' \
                        r'\"WSDD\":\"宿舍1-10栋\",\"WSDD##text\":\"宿舍1-10栋\"}]","JCFTBR":"[]"}]'
            post['instJson'] = '{"id":"","wfInfoId":"5e407b9770f7847701712e33bc8c6b49","barCode":"","secLevle":"普通",' \
                               '"urgentLevel":"普通","title":"校内学生每日信息填报表","makeCopy":"","flow":"","checkFlow":"",' \
                               '"formId":"5e407b9770f7847701712e33bc946b4a","tStatus":"send","tType":"pub","ifArchive":"0",' \
                               '"flowJson":"","auditJson":"[]","correlation":"","uniqueIdentify":"'
            post[
                'flowJson'] = r'[{"id":"1de6734b8de247f08410b7fbe8ec312c","nodeId":"0","rightsConfig":{"formFiledDefaultValue":[{"field":"TBSJ","fieldtype":"mini-datepicker",' \
                              r'"_state":"modified","_id":2,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"TBSJ","cnname":"校内学生每日信息填报表","rightKey":"defaultValue",' \
                              r'"cnfield":"填报时间","_uid":2,"rightType":"noedit"},{"field":"XM","fieldtype":"mini-textbox","_state":"modified","_id":3,' \
                              r'"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"XM","cnname":"校内学生每日信息填报表","rightKey":"defaultValue",' \
                              r'"cnfield":"姓名","_uid":3,"rightType":"noedit"},{"field":"XH","fieldtype":"mini-textbox","_state":"modified","_id":4,' \
                              r'"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"XH","cnname":"校内学生每日信息填报表","rightKey":"defaultValue",' \
                              r'"cnfield":"学号","_uid":4,"rightType":"noedit"},{"field":"XY","fieldtype":"mini-textbox","_state":"modified","_id":5,' \
                              r'"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"XY","cnname":"校内学生每日信息填报表","rightKey":"defaultValue","cnfield":"学院",' \
                              r'"_uid":5,"rightType":"noedit"},{"field":"BJ","fieldtype":"mini-textbox","_state":"modified","_id":6,"formId":"5e407b9770f7847701712e33bc946b4a",' \
                              r'"enfield":"BJ","cnname":"校内学生每日信息填报表","rightKey":"defaultValue","cnfield":"班级","_uid":6,"rightType":"noedit"},' \
                              r'{"field":"SSH","fieldtype":"mini-textbox","_id":7,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"SSH","cnname":"校内学生每日信息填报表",' \
                              r'"cnfield":"宿舍号","_uid":7},{"field":"FDY","fieldtype":"mini-textbox","_id":8,"formId":"5e407b9770f7847701712e33bc946b4a",' \
                              r'"enfield":"FDY","cnname":"校内学生每日信息填报表","cnfield":"辅导员","_uid":8},{"field":"DRSTZK","fieldtype":"mini-combobox",' \
                              r'"_id":9,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"DRSTZK","cnname":"校内学生每日信息填报表","cnfield":"当日身体状况",' \
                              r'"_uid":9},{"field":"STBSSM","fieldtype":"mini-textbox","_id":10,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"STBSSM",' \
                              r'"cnname":"校内学生每日信息填报表","cnfield":"身体不适说明","_uid":10},{"field":"SFSCTB","fieldtype":"mini-radiobuttonlist","_id":11,' \
                              r'"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"SFSCTB","cnname":"校内学生每日信息填报表","cnfield":"是否首次填报","_uid":11},' \
                              r'{"field":"CFSJ","fieldtype":"mini-datepicker","_id":12,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"CFSJ","cnname":"校内学生每日信息填报表",' \
                              r'"cnfield":"出发时间","_uid":12},{"field":"DXSJ","fieldtype":"mini-datepicker","_id":13,"formId":"5e407b9770f7847701712e33bc946b4a",' \
                              r'"enfield":"DXSJ","cnname":"校内学生每日信息填报表","cnfield":"到校时间","_uid":13},{"field":"CFDD","fieldtype":"mini-textarea","_id":14,' \
                              r'"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"CFDD","cnname":"校内学生每日信息填报表","cnfield":"出发地点","_uid":14},{"field":"TXRXM",' \
                              r'"fieldtype":"mini-textbox","_id":15,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"TXRXM","cnname":"校内学生每日信息填报表",' \
                              r'"cnfield":"同行人姓名","_uid":15},{"field":"TXRLXFS","fieldtype":"mini-textbox","_id":16,"formId":"5e407b9770f7847701712e33bc946b4a",' \
                              r'"enfield":"TXRLXFS","cnname":"校内学生每日信息填报表","cnfield":"同行人联系方式","_uid":16},{"field":"JTGJ","fieldtype":"mini-combobox",' \
                              r'"_id":17,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"JTGJ","cnname":"校内学生每日信息填报表","cnfield":"交通工具","_uid":17},' \
                              r'{"field":"CZSJ","fieldtype":"mini-textbox","_id":18,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"CZSJ","cnname":"校内学生每日信息填报表",' \
                              r'"cnfield":"乘坐时间","_uid":18},{"field":"HCXX","fieldtype":"mini-textarea","_id":19,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"HCXX",' \
                              r'"cnname":"校内学生每日信息填报表","cnfield":"换乘信息","_uid":19},{"field":"FJJTXX","fieldtype":"mini-textbox","_id":20,' \
                              r'"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"FJJTXX","cnname":"校内学生每日信息填报表","cnfield":"飞机具体信息","_uid":20},' \
                              r'{"field":"HCJTXX","fieldtype":"mini-textbox","_id":21,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"HCJTXX",' \
                              r'"cnname":"校内学生每日信息填报表","cnfield":"火车具体信息","_uid":21},{"field":"DBJTXX","fieldtype":"mini-textbox","_id":22,' \
                              r'"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"DBJTXX","cnname":"校内学生每日信息填报表","cnfield":"大巴具体信息","_uid":22},' \
                              r'{"field":"DTJTXX","fieldtype":"mini-textbox","_id":23,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"DTJTXX",' \
                              r'"cnname":"校内学生每日信息填报表","cnfield":"地铁具体信息","_uid":23},{"field":"GJTJXX","fieldtype":"mini-textbox","_id":24,' \
                              r'"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"GJTJXX","cnname":"校内学生每日信息填报表","cnfield":"公交具体信息","_uid":24},' \
                              r'{"field":"WYCJTXX","fieldtype":"mini-textbox","_id":25,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"WYCJTXX",' \
                              r'"cnname":"校内学生每日信息填报表","cnfield":"网约车具体信息","_uid":25},{"field":"SJCJTXX","fieldtype":"mini-textbox","_id":26,' \
                              r'"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"SJCJTXX","cnname":"校内学生每日信息填报表","cnfield":"私家车具体信息","_uid":26},' \
                              r'{"field":"QTJTXX","fieldtype":"mini-textbox","_id":27,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"QTJTXX",' \
                              r'"cnname":"校内学生每日信息填报表","cnfield":"其他具体信息","_uid":27},{"field":"DD","fieldtype":"mini-combobox","_id":28,' \
                              r'"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"DD","cnname":"校内学生每日信息填报表","cnfield":"地点","_uid":28},' \
                              r'{"field":"DDZH","fieldtype":"mini-textarea","_id":29,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"DDZH",' \
                              r'"cnname":"校内学生每日信息填报表","cnfield":"地点转换","_uid":29},{"field":"JTWZ","fieldtype":"mini-textbox","_id":30,' \
                              r'"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"JTWZ","cnname":"校内学生每日信息填报表","cnfield":"具体位置","_uid":30},' \
                              r'{"field":"DD1","fieldtype":"mini-combobox","_id":31,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"DD1",' \
                              r'"cnname":"校内学生每日信息填报表","cnfield":"地点","_uid":31},{"field":"DDZH1","fieldtype":"mini-textarea","_id":32,' \
                              r'"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"DDZH1","cnname":"校内学生每日信息填报表","cnfield":"地点转换",' \
                              r'"_uid":32},{"field":"JTWZ1","fieldtype":"mini-textbox","_id":33,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"JTWZ1",' \
                              r'"cnname":"校内学生每日信息填报表","cnfield":"具体位置","_uid":33},{"field":"DD2","fieldtype":"mini-combobox","_id":34,' \
                              r'"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"DD2","cnname":"校内学生每日信息填报表","cnfield":"地点","_uid":34},' \
                              r'{"field":"DDZH2","fieldtype":"mini-textarea","_id":35,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"DDZH2",' \
                              r'"cnname":"校内学生每日信息填报表","cnfield":"地点转换","_uid":35},{"field":"JTWZ2","fieldtype":"mini-textbox","_id":36,' \
                              r'"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"JTWZ2","cnname":"校内学生每日信息填报表","cnfield":"具体位置","_uid":36},' \
                              r'{"field":"DD3","fieldtype":"mini-combobox","_id":37,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"DD3",' \
                              r'"cnname":"校内学生每日信息填报表","cnfield":"地点","_uid":37},{"field":"DDZH3","fieldtype":"mini-textarea","_id":38,' \
                              r'"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"DDZH3","cnname":"校内学生每日信息填报表","cnfield":"地点转换",' \
                              r'"_uid":38},{"field":"JTWZ3","fieldtype":"mini-textbox","_id":39,"formId":"5e407b9770f7847701712e33bc946b4a",' \
                              r'"enfield":"JTWZ3","cnname":"校内学生每日信息填报表","cnfield":"具体位置","_uid":39},{"field":"SQLXQK","fieldtype":"mini-textarea",' \
                              r'"_id":40,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"SQLXQK","cnname":"校内学生每日信息填报表",' \
                              r'"cnfield":"申请离校情况","_uid":40}],"opRight":[{"rightName":"print","rightKey":"nodeRight","rightValue":"yes"},' \
                              r'{"rightName":"finish","rightKey":"nodeRight","rightValue":"yes"},{"rightName":"reminder","rightKey":"nodeRight",' \
                              r'"rightValue":"yes"}],"showForms":"5e407b9770f7847701712e33bc946b4a"},"level":1,"name":"' + \
                              postData['username'] + '","typeStr":"user",' \
                                                     r'"left":10,"type":6,"nodeEvent":"[{\"implWay\":\"internalImpl\",\"attestationId\":\"\",\"serviceId\":\"5e407e176cb7ff75016ccbaf81d90098\",' \
                                                     r'\"serviceName\":\"数据采集节点事件\",\"parameters\":\"[{\\\"id\\\":\\\"5e407e176cb7ff75016ccbb03cb90099\\\",\\\"paramName\\\":\\\"ruleId\\\",' \
                                                     r'\\\"paramValue\\\":\\\"d3f36ed44a0e45e09abc75aa7fabe56c@_@CollectRuleValue\\\",\\\"paramType\\\":\\\"2\\\",\\\"dataType\\\":\\\"String\\\",' \
                                                     r'\\\"paramDesc\\\":null,\\\"serviceId\\\":\\\"5e407e176cb7ff75016ccbaf81d90098\\\",\\\"createTime\\\":\\\"2019-08-26T02:10:20.000Z\\\",' \
                                                     r'\\\"paramText\\\":\\\"校内学生每日填报采集\\\"}]\"}]","top":225.5,"displayOrder":0,"pId":0,"title":"' + name + '"}]'
            post['defaultFormContent'] = ''
            post['annexJson'] = '[]'
            post['makeCopeJson'] = ''
            post['auditJson'] = '[]'
            post['flowVerJson'] = '{"id":"5e407b9770f7847701712e33bc8c6b49","wfname":"校内学生每日信息填报表","wfversion":"1.0",' \
                                  '"flowId":"5e407b9770f7847701712e33bc8c6b49","flowKey":"24997",' \
                                  '"cooperativeTypeId":"11b8c1e5e7624ae0815e26fb7d90e385","cooperativeTypeName":"2020肺炎疫情防控"}'
            post['formVerJson'] = '[{"id":"5e407b9770f7847701712e33bc946b4a",' \
                                  '"formId":"5e407b9770f7847701712e33bc946b4a","version":"1.0","cnname":"校内学生每日信息填报表"}]'
            post['externalFieldRightsConfigJson'] = '[]'
            post['flowId'] = '5e407b9770f7847701712e33bc8c6b49'
            post['starterFormId'] = '5e407b9770f7847701712e33bc946b4a'
            post['px'] = ''
            post['py'] = ''

            get_id_url = 'https://i.njcit.cn/EIP/flowNode/createNodeIdByNum.htm'
            post_flow_id = {}
            post_flow_id['num'] = '1'
            r = session.post(
                url='https://i.njcit.cn/EIP/cooperative/openCooperative.htm?flowId=5e407b9671529b9901715d9201d05ba1',
                headers=head)
            post['instJson'] = post['instJson'] + r.text[1997:2029] + '"}'

            r = session.post(url=get_id_url, headers=head, data=post_flow_id)
            r = session.post(url=get_id_url, headers=head, data=post_flow_id)

            post['flowJson'] = '[{"id":' + r.text[
                                           1:-1] + r',"nodeId":"0","rightsConfig":{"formFiledDefaultValue":[{"field":"TBSJ","fieldtype":"mini-datepicker",' \
                                                   r'"_state":"modified","_id":2,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"TBSJ","cnname":"校内学生每日信息填报表","rightKey":"defaultValue",' \
                                                   r'"cnfield":"填报时间","_uid":2,"rightType":"noedit"},{"field":"XM","fieldtype":"mini-textbox","_state":"modified","_id":3,' \
                                                   r'"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"XM","cnname":"校内学生每日信息填报表","rightKey":"defaultValue",' \
                                                   r'"cnfield":"姓名","_uid":3,"rightType":"noedit"},{"field":"XH","fieldtype":"mini-textbox","_state":"modified","_id":4,' \
                                                   r'"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"XH","cnname":"校内学生每日信息填报表","rightKey":"defaultValue",' \
                                                   r'"cnfield":"学号","_uid":4,"rightType":"noedit"},{"field":"XY","fieldtype":"mini-textbox","_state":"modified","_id":5,' \
                                                   r'"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"XY","cnname":"校内学生每日信息填报表","rightKey":"defaultValue","cnfield":"学院",' \
                                                   r'"_uid":5,"rightType":"noedit"},{"field":"BJ","fieldtype":"mini-textbox","_state":"modified","_id":6,"formId":"5e407b9770f7847701712e33bc946b4a",' \
                                                   r'"enfield":"BJ","cnname":"校内学生每日信息填报表","rightKey":"defaultValue","cnfield":"班级","_uid":6,"rightType":"noedit"},' \
                                                   r'{"field":"SSH","fieldtype":"mini-textbox","_id":7,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"SSH","cnname":"校内学生每日信息填报表",' \
                                                   r'"cnfield":"宿舍号","_uid":7},{"field":"FDY","fieldtype":"mini-textbox","_id":8,"formId":"5e407b9770f7847701712e33bc946b4a",' \
                                                   r'"enfield":"FDY","cnname":"校内学生每日信息填报表","cnfield":"辅导员","_uid":8},{"field":"DRSTZK","fieldtype":"mini-combobox",' \
                                                   r'"_id":9,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"DRSTZK","cnname":"校内学生每日信息填报表","cnfield":"当日身体状况",' \
                                                   r'"_uid":9},{"field":"STBSSM","fieldtype":"mini-textbox","_id":10,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"STBSSM",' \
                                                   r'"cnname":"校内学生每日信息填报表","cnfield":"身体不适说明","_uid":10},{"field":"SFSCTB","fieldtype":"mini-radiobuttonlist","_id":11,' \
                                                   r'"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"SFSCTB","cnname":"校内学生每日信息填报表","cnfield":"是否首次填报","_uid":11},' \
                                                   r'{"field":"CFSJ","fieldtype":"mini-datepicker","_id":12,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"CFSJ","cnname":"校内学生每日信息填报表",' \
                                                   r'"cnfield":"出发时间","_uid":12},{"field":"DXSJ","fieldtype":"mini-datepicker","_id":13,"formId":"5e407b9770f7847701712e33bc946b4a",' \
                                                   r'"enfield":"DXSJ","cnname":"校内学生每日信息填报表","cnfield":"到校时间","_uid":13},{"field":"CFDD","fieldtype":"mini-textarea","_id":14,' \
                                                   r'"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"CFDD","cnname":"校内学生每日信息填报表","cnfield":"出发地点","_uid":14},{"field":"TXRXM",' \
                                                   r'"fieldtype":"mini-textbox","_id":15,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"TXRXM","cnname":"校内学生每日信息填报表",' \
                                                   r'"cnfield":"同行人姓名","_uid":15},{"field":"TXRLXFS","fieldtype":"mini-textbox","_id":16,"formId":"5e407b9770f7847701712e33bc946b4a",' \
                                                   r'"enfield":"TXRLXFS","cnname":"校内学生每日信息填报表","cnfield":"同行人联系方式","_uid":16},{"field":"JTGJ","fieldtype":"mini-combobox",' \
                                                   r'"_id":17,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"JTGJ","cnname":"校内学生每日信息填报表","cnfield":"交通工具","_uid":17},' \
                                                   r'{"field":"CZSJ","fieldtype":"mini-textbox","_id":18,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"CZSJ","cnname":"校内学生每日信息填报表",' \
                                                   r'"cnfield":"乘坐时间","_uid":18},{"field":"HCXX","fieldtype":"mini-textarea","_id":19,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"HCXX",' \
                                                   r'"cnname":"校内学生每日信息填报表","cnfield":"换乘信息","_uid":19},{"field":"FJJTXX","fieldtype":"mini-textbox","_id":20,' \
                                                   r'"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"FJJTXX","cnname":"校内学生每日信息填报表","cnfield":"飞机具体信息","_uid":20},' \
                                                   r'{"field":"HCJTXX","fieldtype":"mini-textbox","_id":21,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"HCJTXX",' \
                                                   r'"cnname":"校内学生每日信息填报表","cnfield":"火车具体信息","_uid":21},{"field":"DBJTXX","fieldtype":"mini-textbox","_id":22,' \
                                                   r'"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"DBJTXX","cnname":"校内学生每日信息填报表","cnfield":"大巴具体信息","_uid":22},' \
                                                   r'{"field":"DTJTXX","fieldtype":"mini-textbox","_id":23,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"DTJTXX",' \
                                                   r'"cnname":"校内学生每日信息填报表","cnfield":"地铁具体信息","_uid":23},{"field":"GJTJXX","fieldtype":"mini-textbox","_id":24,' \
                                                   r'"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"GJTJXX","cnname":"校内学生每日信息填报表","cnfield":"公交具体信息","_uid":24},' \
                                                   r'{"field":"WYCJTXX","fieldtype":"mini-textbox","_id":25,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"WYCJTXX",' \
                                                   r'"cnname":"校内学生每日信息填报表","cnfield":"网约车具体信息","_uid":25},{"field":"SJCJTXX","fieldtype":"mini-textbox","_id":26,' \
                                                   r'"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"SJCJTXX","cnname":"校内学生每日信息填报表","cnfield":"私家车具体信息","_uid":26},' \
                                                   r'{"field":"QTJTXX","fieldtype":"mini-textbox","_id":27,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"QTJTXX",' \
                                                   r'"cnname":"校内学生每日信息填报表","cnfield":"其他具体信息","_uid":27},{"field":"DD","fieldtype":"mini-combobox","_id":28,' \
                                                   r'"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"DD","cnname":"校内学生每日信息填报表","cnfield":"地点","_uid":28},' \
                                                   r'{"field":"DDZH","fieldtype":"mini-textarea","_id":29,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"DDZH",' \
                                                   r'"cnname":"校内学生每日信息填报表","cnfield":"地点转换","_uid":29},{"field":"JTWZ","fieldtype":"mini-textbox","_id":30,' \
                                                   r'"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"JTWZ","cnname":"校内学生每日信息填报表","cnfield":"具体位置","_uid":30},' \
                                                   r'{"field":"DD1","fieldtype":"mini-combobox","_id":31,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"DD1",' \
                                                   r'"cnname":"校内学生每日信息填报表","cnfield":"地点","_uid":31},{"field":"DDZH1","fieldtype":"mini-textarea","_id":32,' \
                                                   r'"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"DDZH1","cnname":"校内学生每日信息填报表","cnfield":"地点转换",' \
                                                   r'"_uid":32},{"field":"JTWZ1","fieldtype":"mini-textbox","_id":33,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"JTWZ1",' \
                                                   r'"cnname":"校内学生每日信息填报表","cnfield":"具体位置","_uid":33},{"field":"DD2","fieldtype":"mini-combobox","_id":34,' \
                                                   r'"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"DD2","cnname":"校内学生每日信息填报表","cnfield":"地点","_uid":34},' \
                                                   r'{"field":"DDZH2","fieldtype":"mini-textarea","_id":35,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"DDZH2",' \
                                                   r'"cnname":"校内学生每日信息填报表","cnfield":"地点转换","_uid":35},{"field":"JTWZ2","fieldtype":"mini-textbox","_id":36,' \
                                                   r'"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"JTWZ2","cnname":"校内学生每日信息填报表","cnfield":"具体位置","_uid":36},' \
                                                   r'{"field":"DD3","fieldtype":"mini-combobox","_id":37,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"DD3",' \
                                                   r'"cnname":"校内学生每日信息填报表","cnfield":"地点","_uid":37},{"field":"DDZH3","fieldtype":"mini-textarea","_id":38,' \
                                                   r'"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"DDZH3","cnname":"校内学生每日信息填报表","cnfield":"地点转换",' \
                                                   r'"_uid":38},{"field":"JTWZ3","fieldtype":"mini-textbox","_id":39,"formId":"5e407b9770f7847701712e33bc946b4a",' \
                                                   r'"enfield":"JTWZ3","cnname":"校内学生每日信息填报表","cnfield":"具体位置","_uid":39},{"field":"SQLXQK","fieldtype":"mini-textarea",' \
                                                   r'"_id":40,"formId":"5e407b9770f7847701712e33bc946b4a","enfield":"SQLXQK","cnname":"校内学生每日信息填报表",' \
                                                   r'"cnfield":"申请离校情况","_uid":40}],"opRight":[{"rightName":"print","rightKey":"nodeRight","rightValue":"yes"},' \
                                                   r'{"rightName":"finish","rightKey":"nodeRight","rightValue":"yes"},{"rightName":"reminder","rightKey":"nodeRight",' \
                                                   r'"rightValue":"yes"}],"showForms":"5e407b9770f7847701712e33bc946b4a"},"level":1,"name":"' + \
                               postData['username'] + '","typeStr":"user",' \
                                                      r'"left":10,"type":6,"nodeEvent":"[{\"implWay\":\"internalImpl\",\"attestationId\":\"\",\"serviceId\":\"5e407e176cb7ff75016ccbaf81d90098\",' \
                                                      r'\"serviceName\":\"数据采集节点事件\",\"parameters\":\"[{\\\"id\\\":\\\"5e407e176cb7ff75016ccbb03cb90099\\\",\\\"paramName\\\":\\\"ruleId\\\",' \
                                                      r'\\\"paramValue\\\":\\\"d3f36ed44a0e45e09abc75aa7fabe56c@_@CollectRuleValue\\\",\\\"paramType\\\":\\\"2\\\",\\\"dataType\\\":\\\"String\\\",' \
                                                      r'\\\"paramDesc\\\":null,\\\"serviceId\\\":\\\"5e407e176cb7ff75016ccbaf81d90098\\\",\\\"createTime\\\":\\\"2019-08-26T02:10:20.000Z\\\",' \
                                                      r'\\\"paramText\\\":\\\"校内学生每日填报采集\\\"}]\"}]","top":225.5,"displayOrder":0,"pId":0,"title":"' + name + '"}]'

            r = session.post(url='https://i.njcit.cn/EIP/cooperative/sendCooperative.htm', headers=head, data=post)

            if(re.search('提交成功',r.text) or re.search('每天只能打卡一次哦',r.text)):
                date['status'] = 'SUCCESS'
                date['info'] = '验证成功'
            else:
                date['status'] = 'ERROR'
                date['info'] = '验证错误'
        except Exception as e:
            date['status'] = 'ERROR'
            date['info'] = '发送错误，请重试'
    return date
