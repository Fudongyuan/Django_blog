import os
from io import BytesIO
from random import randint

from PIL import Image, ImageDraw, ImageFont

from blogs import settings


class Verifycode:
    def __init__(self,len):
        self.width = 100
        self.height = 35
        self.len = len   # 验证码长度
        self._code = ''   # 验证码字符串
        self.__pen = None  # 画笔

    @property
    def code(self):
        return self._code

    # 画验证码流程
    def output(self):
        # 1 创建画布
        im = Image.new('RGB',(self.width,self.height),self.__randcolor(90,200))
        self.__pen = ImageDraw.Draw(im)  # 产生画笔

        # 2 生成验证码字符串
        self.generateCode()

        # 3 画验证码
        self.__drawcode()

        # 4 画干扰点
        self.__drawpoint()
        # 5 画干扰线
        self.__drawline()
        # 6 返回验证码图片
        # im.save('vc.png','PNG')
        buf = BytesIO()
        im.save(buf,'png')
        res = buf.getvalue()
        buf.close()
        return res
    # 随机颜色
    def __randcolor(self,low,high):
        # 返回 RGB 随机的颜色
        return (randint(low,high),randint(low,high),randint(low,high))


    # 随机字符串
    def generateCode(self):
        num = ''
        for i in range(4):
            num += str(randint(0,9))
        self._code = num

    # 画验证码
    def __drawcode(self):
        # 字体路径
        path = os.path.join(settings.STATICFILES_DIRS[0],'font/Inkfree.ttf')
        # print(path)
        font1 = ImageFont.truetype(path,size=30,encoding='utf-8')

        # 一个字符的宽度
        width = (self.width - 20) / self.len
        # 字坐标起点
        for i in range(self.len):
            x = 10 + i * width
            y = randint(1,self.height - 30)
            self.__pen.text((x,y),self._code[i],font=font1,fill=self.__randcolor(0,100))

    def __drawpoint(self):
        # 干扰点的个数,随机坐标
        for i in range(400):
            x = randint(1,self.width - 1)
            y = randint(1,self.height - 1)
            self.__pen.point((x,y),fill=self.__randcolor(60,255))

    # 干扰线
    def __drawline(self):
        for i in range(5):
            # 起点坐标
            start = (randint(1,self.width-1),randint(1,self.height - 1))
            # 终点坐标
            end = (randint(1,self.width-1),randint(1,self.height - 1))
            self.__pen.line([start,end],fill = self.__randcolor(150,255))


if __name__ == '__main__':
    vc = Verifycode(4)
    print(vc.output())

