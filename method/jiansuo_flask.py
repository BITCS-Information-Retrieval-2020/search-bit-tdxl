import flask
from flask_cors import *
from es_search import search_es
import os
import sys
import time
from flask import send_from_directory
from flask import Flask, request, jsonify
import threading
import random
import os

app = Flask(__name__, static_url_path='/static')
app.config['JSON_AS_ASCII'] = False
CORS(app, suports_credentitals=True)

ip_curr = 'http://39.96.43.48/'
# ip_curr = 'http://127.0.0.1/'


def video_to_text(list1, query):
    for x in list1:
        if query in x['text']:
            # print(x['time_start'],x['time_end'])
            return x['time_start'] + '--' + x['time_end']

file_dir = "./static/crossmind/pdf"
video_file = "./static/crossmind/video1"


def listdir(path):
    print(path)
    file_list = []
    for file in os.listdir(path):
        file_list.append(file)
    return file_list

crossmind_pdf_file = listdir(file_dir)
crossmind_video_file = [x.split('.')[0] for x in listdir(video_file)]
print(crossmind_video_file)


def strQ2B(ustring):
    """全角转半角"""
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 12288:
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374):
            inside_code -= 65248
        rstring += chr(inside_code)
    return rstring

name_list = []
with open('author.txt', 'r', encoding='utf-8') as f:
    for i in f:
        name_list.append(i.strip())
name_list = list(set(name_list))


def get_lower(a, b):

    a = ''.join([x.lower() for x in a])
    b = ''.join([x.lower() for x in b])
    if a.startswith(b):
        return 1
    elif b in a:
        return 2


@app.route('/suggestion')
def get_end_value():

    list1 = []
    name = request.args.get('keyword')
    insert_count = 0
    for i in name_list:

        result = get_lower(i, name)
        if result == 1:
            insert_count += 1
            list1.insert(0, {'value': i})
        elif result == 2:
            list1.append({'value': i})

        if insert_count >= 10:
            break

    return jsonify(list1[:10])


@app.route('/search')
def get_search():
    query = request.args.get('query')
    page = request.args.get('page')
    theme = request.args.get('theme')
    order = request.args.get('order')
    try:
        if int(order) == 1:
            order == '1'
        else:
            order == '2'
    except:
        order == '1'
    try:
        page = int(page) if int(page) else 1
    except:
        page = 1

    if not query:
        return jsonify({'code': 0, 'rea': 'query cannot be empty'})
    try:
        page = int(page)
    except:
        page = 1

    try:
        year = int(year) if int(year) else ''
    except:
        year = ''

    result, total = search_es(query, theme, order, year, page)

    data_list = []
    for i in range(len(result)):

        video_text_dict = result[i]['_source'].get('video', '')
        video_to_text_time = video_to_text(video_text_dict, query)

        data = {}
        author = result[i]['_source'].get('author', '')
        abstract = result[i]['_source'].get('description', '')

        dataset_url = ''
        keyword_in_video_time = ''
        pdf = result[i]['_source'].get('pdf_path', '')
        # print(pdf)
        if pdf and 'crossmind' in pdf:
            pdf = pdf.split('/')[-1].split('.')[0]
            if pdf in crossmind_pdf_file:
                pdf = ip_curr + f'static/crossmind/pdf/{pdf}/{pdf}.pdf'
            else:
                pdf = ''
        else:
            pdf = result[i]['_source'].get('PDF', '')

        video = result[i]['_source'].get('video_path', '')

        if video and 'crossmind' in video:
            video = video.split('/')[-2]
            video_name = video.split('/')[-1].split('.')[-1]
            if video in crossmind_video_file:
                video = ip_curr + f'static/crossmind/video1/{video}.mp4'
            else:
                video = result[i]['_source'].get('video_url', '')
        else:
            video = result[i]['_source'].get('video_path', '')
        timeStamp = result[i]['_source'].get('published_at', '')
        timeArray = time.localtime(int(str(timeStamp)[:10]))
        published_at = time.strftime(
            "%Y--%m--%d %H:%M:%S", timeArray).replace('--', '-')
        publisher = result[i]['_source'].get('published_at', '')
        title = result[i]['_source'].get('title', '')
        data['abstract'] = abstract
        data['author'] = author
        data['dataset_url'] = dataset_url
        data['keyword_in_video_time'] = video_to_text_time if video_to_text_time else ''
        data['pdf'] = pdf
        data['publish_at'] = published_at
        data['publisher'] = ''
        data['title'] = title
        data['video'] = video
        data_list.append(data)

    return jsonify({'code': 1,
                    'data': data_list,
                    'total': total
                    })
# search_es(key_word, theme, order, year, page)


if __name__ == '__main__':
    # print(name_list)
    app.run(host='0.0.0.0', port=80, debug=True)
    # file_dir = "./crossmind/pdf"
    # file_name(file_dir)
