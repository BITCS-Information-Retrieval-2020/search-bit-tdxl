### 通过pip安装
pip install search_utils-1.0.0.tar.gz

#### get_suggestion()
**请求参数：**

|参数名称|类型|描述|是否必填|
|:-------|:---|:----|:----|
|keyword|str|搜索关键字| 是|

**响应示例：**

```
[{
    value: "Audrey Acken article"
},
{
    value: "Audrey Acken"
}]
```

#### search()
**请求参数：**

|参数名称|类型|描述|是否必填|
|:-------|:---|:----|:----|
|query|str|搜索关键字| 是|
|theme|str|搜索主题	| 否|
|page|str|页码| 否|
|order|str|排序| 否|
|year|str|年份| 否|



**响应示例：**

```
{
  "code": 1, 
  "data": [
    {
      "abstract": "With the COVID-19 pandemic raging world-wide since the beginning of the 2020 decade, the need for monitoring systems to track relevant information on social media is vitally important. This paper describes our submission to the WNUT-2020 Task 2: Identification of informative COVID-19 English Tweets. We investigate the effectiveness for a variety of classification models, and found that domain-specific pre-trained BERT models lead to the best performance. On top of this, we attempt a variety of ensembling strategies, but these attempts did not lead to further improvements. Our final best model, the standalone CT-BERT model, proved to be highly competitive, leading to a shared first place in the shared task. Our results emphasize the importance of domain and task-related pre-training.", 
      "author": "Lilei,Hanmeimei", 
      "dataset_url": "http://39.96.43.48/static/dadataset/W18-0516.Datasets.zip", 
      "keyword_in_video_time": "00:2:58", 
      "pdf": "http://39.96.43.48/static/pdf/2020.wnut-1.47.pdf", 
      "publish_month": "June", 
      "publish_year": "2018", 
      "publusher": "Association for Computational Linguistics", 
      "titile": "Pace English", 
      "video": "http://39.96.43.48/static/video/123.mp4"
    }, 
    {
      "abstract": "With the COVID-19 pandemic raging world-wide since the beginning of the 2020 decade, the need for monitoring systems to track relevant information on social media is vitally important. This paper describes our submission to the WNUT-2020 Task 2: Identification of informative COVID-19 English Tweets. We investigate the effectiveness for a variety of classification models, and found that domain-specific pre-trained BERT models lead to the best performance. On top of this, we attempt a variety of ensembling strategies, but these attempts did not lead to further improvements. Our final best model, the standalone CT-BERT model, proved to be highly competitive, leading to a shared first place in the shared task. Our results emphasize the importance of domain and task-related pre-training.", 
      "author": "Lilei,Hanmeimei", 
      "dataset_url": "http://39.96.43.48/static/dadataset/W18-0516.Datasets.zip", 
      "keyword_in_video_time": "00:2:58", 
      "pdf": "", 
      "publish_month": "June", 
      "publish_year": "2018", 
      "publusher": "Association for Computational Linguistics", 
      "titile": "Pace English", 
      "video": ""
    }
  "total": 2
  ]
}
```