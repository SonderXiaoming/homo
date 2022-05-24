from .dict import dictnum
from hoshino import Service
from hoshino.typing import CQEvent

sv = Service(
    name="114514",  # 功能名
    visible=True,  # 可见性
    enable_on_default=True,  # 默认启用
    bundle="娱乐",  # 分组归类
    help_="发送【恶臭化+数字】即可将数字以114514来表示",  # 帮助说明
)

def start(num):
    output = ""
    numbackup = num #输入数字备份
    needchangenum = []
    restnum = []
    class caculate():
        def __init__(self,num,output):
            self.num = num
            self.output = output
        def chufa(self):
            numafter = self.num/114514
            return int(numafter)
        def output1(self):
            if self.num > 114514:
                self.output = self.output+"114514*"
                return self.output
            else:
                return self.output+f"{changenum(int(self.num))[int(self.num)]}"

    def fenjie(num,output):#分解成114514*
        list1 = []
        while 1:
            list1.append(num)
            a = caculate(num,output)
            num = int(a.chufa())
            output = a.output1()
            if num == 0:
                return list1[-1],eval(output),output
    #分解成****+****的形式
    def addit(num,output):
        nextnum,usednum,output = fenjie(num,output)
        needchangenum.append(nextnum)
        num = numbackup - usednum
        return num,output,needchangenum

    while 1:
        num,output,needchangenum = addit(num,output)
        if num == 0:
            break
        output = output + "+"
    print(output)
    return output


def changenum(num):
    listkeys = list(dictnum.keys())
    numbackup = num
    data = "("
    while not num == 0:
        for i in listkeys:
            if num - i > 0:
                data = data+dictnum[i]+"+"
                num = num - i
                break
            if num - i == 0:
                data = data+dictnum[i]
                num = 0
                break
    data = data + ")"
    dictover = {numbackup:data}
    return dictover

@sv.on_prefix(("恶臭化"))
async def homo(bot, ev: CQEvent):
    text = ev.message.extract_plain_text().strip()
    try: 
        num = int(text)
        if num == 0:
            msg = "(1-1)*4514"
        elif abs(num) == 114514:
            msg = "这么恶臭的数字无法再恶臭下去了"
        elif num > 0:
            msg = start(num)
        elif num < 0:
            msg = str(start(abs(num)))
            msg = "-"+msg         
        await bot.send(ev,msg)
    except:
        await bot.send(ev, "你肯定输入了一些奇怪的东西，爬爬")