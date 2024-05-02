#导入包
from hyperlpr import *
#导入OpenCV库
import cv2
#读入图片
image = cv2.imread("13.jpg")
#识别结果
print(HyperLPR_plate_recognition(image))
#2024.4.21
#2024.5.2
