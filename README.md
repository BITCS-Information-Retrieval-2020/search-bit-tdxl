#  检索模块-TDXL

## 项目介绍
搭建一个学术论文的综合搜索引擎，用户可以检索到一篇论文的综合信息，不仅有pdf文件，还有oral视频，数据集，源代码等多模态信息。
本项目为检索模块,最终提供了url和pip安装python包两种检索方式


## TDXL小组分工
姓名 | 学号 | 分工 |
:-: | :-: | :-: |
王洪飞| 3520180030 |es环境及服务器运行环境搭建  |
 高佳蕊| 3520200005 | pdf转文本模块开发|
 冯昭凯| 5720202085 | mongo倒入es数据模块开发 |
刘君| 3520190034 |  es封装为url模块开发|
 刘旭冬| 3520190035 | es查询模块开发 |
 王大为| 3520190039 | url接口封装及pip打包 |
 纪校锋| 3120201030 | 视频转文本模块开发 |


## 数据处理
主要了爬虫组提供的两个网站数据：
	CrossMinds数据包含视频(部分)、pdf(部分)、摘要、标题、发布时间等字段
	ACL Anthology数据包含视频(部分)、pdf(部分)、数据集(部分)、摘要、标题、发布时间等字段

## 使用方法

- ### url方式
 	
 	##### 1.输入关键字提示


	接口详情 |   |
	:-: | :-: 
	地址 |`http://39.96.43.48/suggestion`
	请求方式|`GET`

	***

	##### url示例
	 http://39.96.43.48/suggestion?keyword=A

	***

	##### 请求参数

	字段 | 说明 | 类型 | 备注 | 是否必填
	:-: | :-: | :-: | :-: | :-:
	keyword | `搜索关键字` | `string` |  | `是`| 


	***

	#####响应示例



	```python
	[{
	    value: "Audrey Acken article"
	},
	{
	    value: "Audrey Acken"
	}]

	```

	##### 2.搜索接口

	接口详情 |   |
	:-: | :-: 
	地址 |`http://39.96.43.48/search`
	请求方式|`GET`

	***

	##### url示例
	 http://39.96.43.48/search?theme=author&query=uclanlp&page=1&order=1&year=2020

	***


	##### 请求参数

	字段 | 说明 | 类型 | 备注 | 是否必填
	:-: | :-: | :-: | :-: | :-:
	query | `搜索关键字` | `string` |  | `是`| 
	theme | `搜索主题` | `string` |  | `否`| 
	page | `页码` | `string` |  | `否`| 
	order | `排序` | `string` |  | `否`| 
	year | `检索年份` | `string` |  | `否`| 

	<details>
	<summary>响应示例详情
	</summary>

	
	```python
	{
	  "code": 1, 
	  "data": [
	    {
	      "abstract": "With the COVID-19 pandemic raging world-wide since the beginning of the 2020 decade, the need for monitoring systems to track relevant information on social media is vitally important. This paper describes our submission to the WNUT-2020 Task 2: Identification of informative COVID-19 English Tweets. We investigate the effectiveness for a variety of classification models, and found that domain-specific pre-trained BERT models lead to the best performance. On top of this, we attempt a variety of ensembling strategies, but these attempts did not lead to further improvements. Our final best model, the standalone CT-BERT model, proved to be highly competitive, leading to a shared first place in the shared task. Our results emphasize the importance of domain and task-related pre-training.", 
	      "author": "Lilei,Hanmeimei", 
	      "dataset_url": "http://39.96.43.48/static/dadataset/W18-0516.Datasets.zip", 
	      "keyword_in_video_time": "00:2:58", 
	      "pdf": "http://39.96.43.48/static/pdf/2020.wnut-1.47.pdf", 
	      "publish_at": "2018", 
	      "publisher": "Association for Computational Linguistics", 
	      "title": "Pace English", 
	      "video": "http://39.96.43.48/static/video/123.mp4"
	    }, 
	    {
	      "abstract": "With the COVID-19 pandemic raging world-wide since the beginning of the 2020 decade, the need for monitoring systems to track relevant information on social media is vitally important. This paper describes our submission to the WNUT-2020 Task 2: Identification of informative COVID-19 English Tweets. We investigate the effectiveness for a variety of classification models, and found that domain-specific pre-trained BERT models lead to the best performance. On top of this, we attempt a variety of ensembling strategies, but these attempts did not lead to further improvements. Our final best model, the standalone CT-BERT model, proved to be highly competitive, leading to a shared first place in the shared task. Our results emphasize the importance of domain and task-related pre-training.", 
	      "author": "Lilei,Hanmeimei", 
	      "dataset_url": "http://39.96.43.48/static/dadataset/W18-0516.Datasets.zip", 
	      "keyword_in_video_time": "00:2:58", 
	      "pdf": "", 
	      "publish_at": "2018", 
	      "publusher": "Association for Computational Linguistics", 
	      "titile": "Pace English", 
	      "video": ""
	    }
	  "total": 2
	  ]
	}
	```

</details>
  


- ###pip安装包方式

		在文件目录使用 import search_utils 进行安装
		


	<details>
		<summary>源代码及使用示例
		</summary>

	
	```python
		import json
		import requests


		def _build_url_params(url, params):
		    url = url + '?'
		    for k, v in params.items():
		        url += '{}={}&'.format(k, v)
		    return url


		def get_suggestion(keyword):
		    url = "http://39.96.43.48/suggestion"
		    if not keyword:
		        return

		    params = {
		        'keyword': keyword
		    }
		    request_url = _build_url_params(url, params)
		    return requests.get(request_url, timeout=4).json()


		def search(query, theme=None, page=None, order=None, year=None):
		    url = "http://39.96.43.48/search"
		    if not query:
		        return

		    params = {
		        'query': query
		    }
		    if theme:
		        params['theme'] = theme
		    if page:
		        params['page'] = page
		    if order:
		        params['order'] = order
		    if year:
		        params['year'] = year
		    request_url = _build_url_params(url, params)
		    return requests.get(request_url, timeout=4).json()

		if __name__ == '__main__':
			# 搜索提示
		    print(get_suggestion("Audrey"))
		    theme = "author"
		    query = "uclanlp"
		    page = 1
		    order = 1
		    year = 2020
		    # 检索接口
		    print(search(query, theme=theme))

	```

</details>




## 其他模块简介

- ##### mongo倒入es
			
		利用pymongo和elasticsearch两个包将数据库实现对接，将以上及其他字段倒入es



	<details>
		<summary>源代码示例
		</summary>

	
	```python
		ES = ['127.0.0.1:9200']
		# 创建elasticsearch客户端
		es = Elasticsearch(
			ES,
			# 启动前嗅探es集群服务器
			sniff_on_start=True,
			# es集群服务器结点连接异常时是否刷新es节点信息
			sniff_on_connection_fail=True,
			# 每60秒刷新节点信息
			sniffer_timeout=60)
		def insert_es(id_,datas):
		name_list.append(datas['author'])
		es.create(index="search", doc_type="doc",
				  id=id_, ignore=[400, 409], body=datas)
		def mongo_to_es():
		datas= []
		i = 0
		myclient = pymongo.MongoClient("mongodb://localhost:27017/")
		mydb = myclient["crossmind"]
		mycol = mydb["crossmind"]
		x = mycol.find()
		for y in x:
				y.pop('_id')
				y['author'] = y['author']['name']
				y['description'] = ''.join([aa.replace('\n','') for aa in y["description"] ])
				pdf_list = pdf_to_text(y['pdf_path'].split('/')[-1])
				if pdf_list:
					y['pdf_text'] = ''.join([aa.replace('\n','') for aa in pdf_list ])
			insert_es(i,y)
			i += 1

	```

</details>





- ##### pdf转文本
		

		使用pdfminer将pdf转为pdf
		

	<details>
		<summary>源代码示例
		</summary>

	
	```python
		from pdfminer.pdfinterp import PDFPageInterpreter,PDFResourceManager
		from pdfminer.converter import TextConverter,PDFPageAggregator
		from pdfminer.layout import LAParams
		from pdfminer.pdfparser import PDFParser
		from pdfminer.pdfdocument import PDFDocument
		from pdfminer.pdfdevice import PDFDevice
		from pdfminer.pdfpage import PDFPage
		# 获取pdf文档
		fp = open('5ee96b86b1267e24b0ec2354.pdf','rb')
		# 创建一个与文档相关的解释器
		parser = PDFParser(fp)
		# pdf文档的对象，与解释器连接起来
		doc = PDFDocument(parser=parser)
		parser.set_document(doc=doc)
		# 如果是加密pdf，则输入密码
		# doc._initialize_password()
		# 创建pdf资源管理器
		resource = PDFResourceManager()
		# 参数分析器
		laparam=LAParams()
		# 创建一个聚合器
		device = PDFPageAggregator(resource,laparams=laparam)
		# 创建pdf页面解释器
		interpreter = PDFPageInterpreter(resource,device)
		# 获取页面的集合
		for page in PDFPage.get_pages(fp):
		    # 使用页面解释器来读取
		    interpreter.process_page(page)
		    # 使用聚合器来获取内容
		    layout = device.get_result()

	```

	</details>


- ##### 视频转文本

		使用tencentcloud-sdk-python讲视频转为文本并记录了每段话在视频出现的时间


	<details>
		<summary>源代码示例
		</summary>

	
	```python
	def video_to_text(video_url,video_id):
	    """
	    input:
	        video_url
	        video_id
	    output:
	        results 
	            format: [{time_start:xxx,time_end:xxx,text:xxx,vid:xxx},...]
	    """
	    from tencentcloud.common import credential
	    from tencentcloud.common.profile.client_profile import ClientProfile
	    from tencentcloud.common.profile.http_profile import HttpProfile
	    from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException 
	    from tencentcloud.asr.v20190614 import asr_client, models 
	    import base64
	    import io 
	    import time
	    import sys 
	    if sys.version_info[0] == 3:
	        sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
	    # post the audio to tencent cloud platform
	    try: 
	        # <Your SecretId><Your SecretKey> of tencent cloud
	        cred = credential.Credential("*****", "****") 
	        # set http request
	        httpProfile = HttpProfile()
	        httpProfile.endpoint = "asr.tencentcloudapi.com"
	        clientProfile = ClientProfile()
	        clientProfile.httpProfile = httpProfile
	        clientProfile.signMethod = "TC3-HMAC-SHA256"  
	        client = asr_client.AsrClient(cred, "ap-beijing", clientProfile) 
	        # set params and create recognition task
	        req = models.CreateRecTaskRequest()
	        params = {"ChannelNum":1,"ResTextFormat":0,"SourceType":0}
	        req._deserialize(params)
	        req.EngineModelType = "16k_en"
	        req.Url = video_url
	        resp = client.CreateRecTask(req)
	        # set result query
	        req = models.DescribeTaskStatusRequest()
	        params = '{"TaskId":%s}'%resp.Data.TaskId
	        req.from_json_string(params)
	        # polling
	        resp = client.DescribeTaskStatus(req)
	        while resp.Data.Status != 2:
	            print("video ID: "+str(video_id)+" is "+resp.Data.StatusStr,flush=True)
	            time.sleep(1)
	            resp = client.DescribeTaskStatus(req)
	        # process the result
	        print("video ID: "+str(video_id)+" is "+resp.Data.StatusStr,flush=True)
	        results = []
	        lines = resp.Data.Result.split('\n')
	        for line in lines:
	            if len(line) < 1:
	                continue
	            time, text = line.split(']')[0][1:], line.split(']')[1][2:-1]
	            result_dict = {} 
	            result_dict["time_start"], result_dict["time_end"] = time.split(',')[0], time.split(',')[1]
	            result_dict["text"] = text
	            result_dict["vid"] = video_id
	            results.append(result_dict)
	        return results
	    except TencentCloudSDKException as err: 
	        print(err) 
		r = video_to_text("http://39.96.43.48/static/video/123.mp4",0)
		print(r)

	```

</details>


- ##### es查询模块

		根据不同查询条件拼接成完整的查询语句


	<details>
		<summary>源代码示例
		</summary>

	
	```python
		def search_es(key_word, themes='', order='1', year='', page=1):
	    # 基础查询语句
	    query = {"query": {"bool": {"should": []}}}
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
	    # 如果有时间限制，添加时间查询
	    if year:
	        start_time, end_time = parse_year(year)
	        if start_time and end_time:
	            query["query"]["bool"]["must"] = [
	                {"range": {"published_at": {"gte": start_time, "lte": end_time}}}]
	        query["sort"] = {"published_at": {"order": "asc"}
	                         } if order == "1" else {"published_at": {"order": "desc"}}
	    # 分页 每页10条
	    query["size"] = 10
	    query["from"] = (page - 1) * 10
	    ret = es.search(body=query, index='ceshi3')
	    # print(ret['hits']['total'])
	    return ret['hits']['hits'],ret['hits']['total']
		if __name__ == '__main__':
		    theme = "adbtract"
		    order = "2"
		    year = "2020"
		    page = 1
		    key_word = 'HazyResearch'
		    search_es(key_word, theme, order, year, page)
	```

</details>
