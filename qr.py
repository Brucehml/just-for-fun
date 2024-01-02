import qrcode#引入模块
# 传入将要生成二维码的URL
text = input('')#输入内容
img = qrcode.make(text)
# 保存
img.save('test.png')
