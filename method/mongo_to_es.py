import pymongo
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.converter import TextConverter, PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfpage import PDFPage
from os import walk
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import time
import os
import uuid
from vts import video_to_text
name_list = []

file_dir = "./static/crossmind/pdf"
video_file = "./static/crossmind/video1"


def listdir(path):

    file_list = []
    for file in os.listdir(path):
        file_list.append(file.split('.')[0])
    return file_list

crossmind_pdf_file = listdir(file_dir)
crossmind_video_file = listdir(video_file)


def pdf_to_text(pdf_name):
    print('zhuanpdf')
    # print(pdf_name)
    text_list = ''
    # 获取pdf文档
    try:
        with open(f'./static/crossmind/pdf/{pdf_name.split(".")[0]}/{pdf_name}', 'rb') as fp:
                        # 创建一个与文档相关的解释器
            parser = PDFParser(fp)
            # pdf文档的对象，与解释器连接起来
            doc = PDFDocument(parser=parser)
            parser.set_document(doc=doc)
            # 创建pdf资源管理器
            resource = PDFResourceManager()
            # 参数分析器
            laparam = LAParams()
            # 创建一个聚合器
            device = PDFPageAggregator(resource, laparams=laparam)
            # 创建pdf页面解释器
            interpreter = PDFPageInterpreter(resource, device)
            # 获取页面的集合
            for page in PDFPage.get_pages(fp):
                        # 使用页面解释器来读取
                interpreter.process_page(page)
                # 使用聚合器来获取内容
                layout = device.get_result()
                for out in layout:
                    # pass
                    try:
                        # text_list.append(out.get_text())
                        text_list += out.get_text()
                    except:
                        pass
            print('chenggong')
            # quit()
            return text_list
    except Exception as e:
        # print(e)
        # fp.close()
        return


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


def insert_es(id_, datas):

    try:
        name_list.append(datas['author'])
        # print(datas)
        es.create(index="crossmind_v2", doc_type="doc",
                  id=id_, ignore=[400, 409], body=datas)
        print('成功')
        # quit()
    except:
        pass


def mongo_to_es():
    datas = []
    i = 0
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["ceshi"]
    mycol = mydb["crossmind"]
    x = mycol.find()
    y_count = 0
    for y in x:
        y_count += 1

        if y_count < 478:
            i += 1
            continue
        try:
            y.pop('_id')
            y['author'] = y['author']['name']

            try:
                y['description'] = ''.join(
                    [aa.replace('\n', '') for aa in y["description"]])

            except:
                pass

            pdf_list = pdf_to_text(y['pdf_path'].split('/')[-1])

        except Exception as e:
            print(e)
        else:

            if pdf_list:
                # print(pdf_list)

                y['pdf_text'] = ''.join([aa.replace('\n', '')
                                         for aa in pdf_list])

                # print(y['description'])
                # print(y['pdf_text'])
        # 		# quit()
        try:
            # print(y)
            # print(crossmind_video_file)
            # quit(/)
            # video = y['video_path']
            # ip_curr = 'http://39.96.43.48/'
            # if video and 'crossmind' in video:
            # 	video = video.split('/')[-2]
            # 	video_name = video.split('/')[-1].split('.')[-1]

            # 	if video in crossmind_video_file:
            # 		video = ip_curr + f'static/crossmind/video1/{video}.mp4'
            # 		# print(video)
            # 		# = "http://39.96.43.48/static/crossmind/video1/123.mp4"
            # 		result = video_to_text(video,0)
            # 		y['video'] = result

            # 		insert_es(i,y)
            # 		i += 1
            pass

        except Exception as e:
            # print(e)
            pass

        insert_es(i, y)
        i += 1


if __name__ == '__main__':
    # mongo_to_es()
    mongo_to_es()
    with open('author.txt', 'w', encoding='utf-8') as f:
        for i in name_list:
            f.write(i.strip())
            f.write('\n')
