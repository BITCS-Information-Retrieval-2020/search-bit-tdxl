import time
from os import walk
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import time
start = int(time.time() * 1000)
ES = [
    '127.0.0.1:9200'
]

# 创建elasticsearch客户端
es = Elasticsearch(
    ES,
    # 启动前嗅探es集群服务器
    sniff_on_start=True,
    # es集群服务器结点连接异常时是否刷新es节点信息
    sniff_on_connection_fail=True,
    # 每60秒刷新节点信息
    sniffer_timeout=60
)



# def search_video(query = 'Deep white balance editing'):

#     query = 

def parse_year(year):
    years = year.split(',')
    year_list = []
    for year in years:
        timeArray = time.strptime(year, "%Y")
        timeStamp = time.mktime((timeArray))
        year_list.append(timeStamp * 1000)
        timeArray = time.strptime(str(int(year) + 1), "%Y")
        timeStamp = time.mktime((timeArray))
        year_list.append(timeStamp * 1000)
    return min(year_list), max(year_list)


def search_es(key_word, themes='', order='1', year='', page=1):



    # 基础查询语句
    query = {"query": {"bool": {"should": []}}}

    try:
        key_word = eval(key_word)
    except Exception as e:
        print(e)
    print(key_word)
    #判断是否为高级检索

    must_not_flag = 1
    if isinstance(key_word,dict):

        logic = key_word.get('logic','')
        if not logic:
            return []
        key_word.pop('logic')
        print(key_word)
        if logic == 'or':
            for key,value in key_word.items():
                if key == 'abstract':
                    key ='description'
                query["query"]["bool"]["should"].append(
                    {"match": {key: value}})

        elif logic == 'and':
            query = {"query": {"bool": {"must": []}}}
            for key,value in key_word.items():
                if key == 'abstract':
                    key ='description'
                query["query"]["bool"]["must"].append(
                    {"match": {key: value}})
                print(query)

        elif logic == 'not':
            query = {"query": {"bool": {"must": []}}}
            for key,value in key_word.items():
                if key == 'abstract':
                    key ='description'
                if must_not_flag:
                    must_not_flag = 0
                    query["query"]["bool"]["must"].append(
                    {"match": {key: value}})

                else:
                    query['query']['bool']['must_not'] = []
                    query["query"]["bool"]["must_not"].append(
                        {"match": {key: value}})

    else:

        if themes:
            # 有搜索主题，添加搜索主题
            themes = themes.split(',')
            for theme in themes:
                theme = theme if theme != 'adbtract' else "description"
                query["query"]["bool"]["should"].append(
                    {"match": {theme: key_word}})

        else:
            # 无搜索主题，默认全搜索
            query["query"]["bool"]["should"].append(
                {"match": {"author": key_word}})
            query["query"]["bool"]["should"].append(
                {"match": {"description": key_word}})
            query["query"]["bool"]["should"].append({"match": {"title": key_word}})
            query["query"]["bool"]["should"].append({"match": {"video": key_word}})
            query["query"]["bool"]["should"].append({"match": {"pdf_text": key_word}})


        # 如果有时间限制，添加时间查询
        if year:
            start_time, end_time = parse_year(year)
            if start_time and end_time:
                query["query"]["bool"]["must"] = [
                    {"range": {"published_at": {"gte": start_time, "lte": end_time}}}]

        # 设置排序
        if order:

            query["sort"] = {"published_at": {"order": "asc"}
                             } if order == "1" else {"published_at": {"order": "desc"}}


    # 分页 每页10条
    query["size"] = 10
    query["from"] = (page - 1) * 10
    print(query)
    ret = es.search(body=query, index='crossmind_v2')
    # print(ret['hits']['total'])
    return ret['hits']['hits'],ret['hits']['total']


if __name__ == '__main__':

    theme = "adbtract"
    order = "2"
    year = "2020"
    page = 1
    key_word = 'HazyResearch'
    print(search_es(key_word, theme, order, year, page))
    # print(parse_year("2018,2021"))
