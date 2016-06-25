# coding:utf-8
from elaphe import barcode
from PIL import Image

def get_barcode(info):
    #  生成二维码
    a = barcode('qrcode', info, options=dict(version=2, eclevel='H'), margin=10, data_mode='8bits')
    # options 中version表示生成二维码的内容密度，可以为1-40
    # eclevel 表示生成二维码图片质量，L，M（默认），Q,H
    # margin 表示边距
    # a.show()
    a.save("hello.png")
    # print dir(a)
if __name__ == '__main__':
    info = raw_input("input a string: ")
get_barcode(info)

# 简单二维码生成
# import qrcode
# img = qrcode.make('hello,qrcode1212')
# img.save('test.png');
