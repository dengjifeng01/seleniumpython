# coding=utf-8
from ShowapiRequest import ShowapiRequest
r = ShowapiRequest("http://route.showapi.com/184-1", "62626", "d61950be50dc4dbd9969f741b8e730f5")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addFilePara("image", "E:/1234.png") #文件上传时设置
res = r.post()
text = res.json()["showapi_res_body"]["Result"]
print(text)