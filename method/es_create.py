

import time
from os import walk
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import time








start = int(time.time()*1000)
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
def search(word):
    datas = [{
        'name': '美国留给叙利亚的是个烂摊子',
        'addr': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm'
    }, {
        "name": "python",
        "addr1": '河北省'
    },
    ]
    for i, data in enumerate(datas):
        es.create(index="blogs", doc_type="test_type",
                  id=i, ignore=[400, 409], body=data)
        result = es.get(index="blogs",doc_type="test_type",id=1)
        print('\n批量插入数据完成：\n',result['_source'])

    # print(ret)
    # print(len(ret['hits']['hits']))
    # print(ret['hits']['hits'])
    # for i in range(len(ret['hits']['hits'])):
    #     print(i)
    #     print(ret['hits']['hits'][i]['_source'])


search('健康')
end =  int(time.time()*1000)
