

def video_to_text(video_url, video_id):
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
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    # post the audio to tencent cloud platform
    try:
        # <Your SecretId><Your SecretKey> of tencent cloud
        cred = credential.Credential(
            "AKID1w0sUvY1A4nQyJC5O1PXP43qMimcZNCY", "LWSHzeGgrmQNBk4MOiqiRu40at7TYNJg")
        # set http request
        httpProfile = HttpProfile()
        httpProfile.endpoint = "asr.tencentcloudapi.com"
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        clientProfile.signMethod = "TC3-HMAC-SHA256"
        client = asr_client.AsrClient(cred, "ap-beijing", clientProfile)

        # set params and create recognition task
        req = models.CreateRecTaskRequest()
        params = {"ChannelNum": 1, "ResTextFormat": 0, "SourceType": 0}
        req._deserialize(params)
        req.EngineModelType = "16k_en"
        req.Url = video_url
        resp = client.CreateRecTask(req)

        # set result query
        req = models.DescribeTaskStatusRequest()
        params = '{"TaskId":%s}' % resp.Data.TaskId
        req.from_json_string(params)

        # polling
        resp = client.DescribeTaskStatus(req)
        while resp.Data.Status != 2:
            print(111)
            if 'faild' in resp.Data.StatusStr:
                break
            print(222)
            print("video ID: " + str(video_id) + " is " +
                  resp.Data.StatusStr, flush=True)
            time.sleep(1)
            resp = client.DescribeTaskStatus(req)

        # process the result
        print("video ID: " + str(video_id) + " is " +
              resp.Data.StatusStr, flush=True)
        results = []
        lines = resp.Data.Result.split('\n')
        for line in lines:
            if len(line) < 1:
                continue
            time, text = line.split(']')[0][1:], line.split(']')[1][2:-1]
            result_dict = {}
            result_dict["time_start"], result_dict[
                "time_end"] = time.split(',')[0], time.split(',')[1]
            result_dict["text"] = text
            result_dict["vid"] = video_id
            results.append(result_dict)

        return results

    except TencentCloudSDKException as err:
        print(err)


# r = video_to_text("http://39.96.43.48/static/video/123.mp4",0)
# print(r)
