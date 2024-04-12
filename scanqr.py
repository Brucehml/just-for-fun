import numpy as np
from PIL import Image
from pyzbar import pyzbar
import cv2
# 读取二维码信息
def OR_read(img):
    # 读取文件，转成数组
    im = np.array(img)
    py_decode = pyzbar.decode(im)
    if len(py_decode) != 0:
        return py_decode[0].data.decode("utf-8")
    else:
        return None
    # return pyzbar.decode(im)[0].data.decode("utf-8")
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
while cap.isOpened():
    ok, frame = cap.read()  # 读取一帧数据
    # if not ok:
    #     break
    a = OR_read(frame)
    if a != None:
        print(a)
    cv2.imshow("frame", frame)
    c = cv2.waitKey(10)
    if c & 0xFF == ord('q'):
        break

# 释放摄像头并销毁所有窗口
cap.release()
cv2.destroyAllWindows()
