
import requests
import json
import time

import hashlib
import datetime
import random


def get_md5(b):
    b = b + '-70d331397e3380dbcaa23d3d189cef11'
    m = hashlib.md5()
    b = b.encode(encoding='utf-8')
    m.update(b)
    return m.hexdigest()


def get_ip():
    return get_ip_qing()
    # result = random.choice([1,2])

    # if result ==1:
    # 	return get_ip_qing()
    # return get_ip_a()


def get_ip_qing():
    today = datetime.date.today()
    url = f'http://211.145.49.146:8017/getip?token={get_md5(str(today))}'
    #url = 'http://39.106.118.223:8888/getip'
    while 1:
        try:

            response = requests.get(url, timeout=3).text
            if requests == '校验失败':
                print('token校验失败')
                time.sleep(1)
            else:
                return {'http': response,
                        'https': response}
        except Exception as e:
            print(e)
            time.sleep(1)


def get_ip_a():
    proxyHost = "proxy.abuyun.com"
    proxyPort = "9020"
    # 代理隧道验证信息
    proxyUser = "HDB1660449Z961YD"
    proxyPass = "C2B25DC13174A7F4"
    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {"host": proxyHost, "port": proxyPort, "user": proxyUser,
                                                                "pass": proxyPass, }

    proxies = {"http": proxyMeta, "https": proxyMeta, }
    return proxies

# if __name__ == '__main__':
# 	print(get_ip())


def format_s(s):
    return {item.split(':', 1)[0].strip(): item.split(':', 1)[1].strip() for item in s.split('\n') if item}


headers = format_s('''
	authority: m.amap.com
	method: GET
	path: /service/poi/tips.json?words=cuiyuanju&adcode=true&city=110000
	scheme: https
	accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
	accept-encoding: gzip, deflate, br
	accept-language: zh-CN,zh;q=0.9
	cache-control: no-cache
	pragma: no-cache
	sec-fetch-dest: document
	sec-fetch-mode: navigate
	sec-fetch-site: none
	sec-fetch-user: ?1
	upgrade-insecure-requests: 1
	user-agent: Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Mobile Safari/537.36''')


def cal_score(response, city_code, admin_name, x_source, y_source, address_source, name_source):

                         # 'address': 'G327(连 菏线)',
                  #   'adcode': '370831',
                  #   'ignore_district': '0',
                  #   'province_name': '山东省',
                  #   'district_name': '泗水县',
                  #   'datatype_spec': '0',
                  #   'city_name': '济宁市',
                  #   'datatype': '0',
                  #   'district': '山东省济宁市泗水县',s
                  #   'name': '福缘民宿',
                  #   'x': '117.513825',
                  #   'line_distance': '471872',
                  #   'rank': '12000000.575055',
                  #   'y': '35.622944',
                  #   'poiid': 'B0FFL2JIMW',
                  #   'category': '100200',
                  #   'taginfo': "<font color='#666666'>山东省</font>"
    a = JaroWinkler()
    # print(response)
    for x in response['tip_list']:

        mid_tip_list = x.get('tip', '')
        name = mid_tip_list.get('name', '')
        address = mid_tip_list.get('address', '')
        adcode = mid_tip_list.get('adcode', '')
        province = mid_tip_list.get('province', '')
        district = mid_tip_list.get('districe_name', '')
        province = mid_tip_list.get('province_name', '')
        city = mid_tip_list.get('city_name', '')
        x = mid_tip_list.get('x', '')
        y = mid_tip_list.get('y', '')
        poiid = mid_tip_list.get('poiid', '')
        city_list = admin_name.split('|')
        is_city_code = 0
        is_distance = 0

        try:
            if adcode == city_code or city.startswith(city_list[1]) or district.startswith(city_list[2]) or province.startswith(city_list[1]):
                is_city_code = 1
        except:
            is_city_code = 1

        if is_city_code:
            try:
                distance = get_distance(x, y, x_source, y_source)

                if distance <= 1000:

                    is_distance = 1
            except Exception as e:
                is_distance = 1

                # return {'ver_result':True,
                # 'id_':id_,
                # 'name':name,
                # 'address':address,
                # 'name_sim':name_sim,
                # 'addr_sim':addr_sim,
                # 'tel_sim':tel_sim,
                # 'phone':phone,
                # 'pointx':pointx,
                # 'ponty':pointy,
                # }

        if is_distance:
            if a.similarity(name, name_source) > 0.85:
                return {'ver_result': True,
                        'id_': poiid,
                        'name': name,
                        'address': address,
                        'pointx': x,
                        'pointy': y,
                        'name_sim': str(a.similarity(name, name_source)),
                        'addr_sim': str(a.similarity(address, address_source)),
                        'phone': '',
                        'tel_sim': '',
                        'distance': str(distance),
                        'ver_type': 'sana_box'
                        }
        elif a.similarity(name, name_source) > 0.85 and a.similarity(address, address_source) > 0.85:
            return {'ver_result': True,
                    'id_': poiid,
                    'name': name,
                    'address': address,
                    'pointx': x,
                    'pointy': y,
                    'name_sim': str(a.similarity(name, name_source)),
                    'addr_sim': str(a.similarity(address, address_source)),
                    'phone': '',
                    'tel_sim': '',
                    'ver_type': 'sana_box'
                    }


def req_api(url):

    while 1:
        try:
            response = requests.get(url)
            return response.json()
        except json.decoder.JSONDecodeError:

            return {'isSame': False, 'similarity': 0}

        except Exception as e:
            print(e)
            time.sleep(1)


def cal_api(response, city_code, admin_name, x_source, y_source, address_source, name_source):

    admin_name = admin_name.split('|')[1]
    for x in response['tip_list']:
        print(x)
        mid_tip_list = x.get('tip', '')
        name = mid_tip_list.get('name', '').replace('&', '、')
        address = mid_tip_list.get('address', '').replace('&', '、')
        adcode = mid_tip_list.get('adcode', '')
        province = mid_tip_list.get('province', '')
        district = mid_tip_list.get('districe_name', '')
        province = mid_tip_list.get('province_name', '')
        city = mid_tip_list.get('city_name', '')
        x = mid_tip_list.get('x', '')
        y = mid_tip_list.get('y', '')
        poiid = mid_tip_list.get('poiid', '')
        city_list = admin_name.split('|')

        url = f"http://192.168.32.80:8090/dpc/ipc/IpcImportTaskAction.do?operate=calPoiSimilary&sourcePoi=20200628FPCS00083791^_^{admin_name}^_^{name_source}^_^{address_source}^_^^_^^_^{x_source}^_^{y_source}&targetPoi=00293520160528144032^_^{city}^_^{name}^_^{address}^_^^_^^_^{x}^_^{y}"
        print(url)
        if poiid:
            end_result = req_api(url)
            if end_result['isSame']:
                return {'ver_result': True,
                        'id_': poiid,
                        'name': name,
                        'address': address,
                        'pointx': x,
                        'pointy': y,
                        'phone': '',
                        "similarty": str(end_result['similarty']),
                        'ver_type': 'sana_box'
                        }


def sana_search_box(city_code, name):

    if city_code:
        while 1:
            try:
                url = f'https://m.amap.com/service/poi/tips.json?words={name}&adcode=true&city={city_code}'
                ip = get_ip()
                print(url)
                response = requests.get(
                    url, headers=headers, timeout=3, proxies=ip)
                print(response.json())
                if response.json()['message'] == 'Not found.':

                    return None
                if response.json()['tip_list']:

                    # return cal_score(response.json(),city_code,admin_name,x_source,y_source,address_source,name)
                    # return
                    # cal_api(response.json(),city_code,admin_name,x_source,y_source,address_source,name)
                    return response.json()

            except Exception as e:

                print(e)


if __name__ == '__main__':
    city_code = '110101'
    name = '名创优品(东方新天地店)'
    admin_name = '北京市|北京市|东城区'
    #admin_name = '河北省|济宁市|丰润区'
    x_source = '116.41199'
    y_source = '39.90933'
    address_source = '东长安街１号东方新天地地下１层'

    print(sana_search_box(city_code, name, admin_name,
                          x_source, y_source, address_source))
