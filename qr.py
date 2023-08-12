import qrcode
# 传入将要生成二维码的URL
text = input('')
img = qrcode.make(text)
# 保存
img.save('test.png')
