# -*- coding: utf-8 -*-
# markdown图片嵌入（部分浏览器可用）
# ![pic_name][ref_name]
# [ref_name]:data:image/png;base64,bs...

import base64

def img2bs(fn):
    '''
    将图片转化为base64编码并打印
    @param fn: 图片文件路径
    @return: base64字符串
    '''
    with open(fn,'rb') as f:
        bs = base64.b64encode( f.read() )
    return bs

def bs2img(bs,fn):
    '''
    将base64字符串转存为图片
    @param bs: base64字符串
    @param fn: 输出图片文件路径
    '''
    img = base64.b64decode(bs)
    with open(fn,'wb') as f:
        f.write(img)

if __name__ == '__main__':

    FILENAME = 'step3.png'
    
    bs = img2bs(FILENAME)
    print(bs)
    
    # bs2img(bs,'test.png')
