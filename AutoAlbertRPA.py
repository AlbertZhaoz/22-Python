import pyautogui
import time
import xlrd
import pyperclip
import os


# import pygame

# 定义鼠标事件

# pyautogui库其他用法 https://blog.csdn.net/qingfengxd1/article/details/108270159

# 判断所有的图片来源，如果存在则点击，不存在则不点击
def judgePicture(imgList):
    Exist = 1
    for img in imgList:
        location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
        if location is None:
            Exist = Exist | 0;
    if Exist != 1:
        return 0  # 不存在图片
    return 1  # 存在图片


def mouseClick(clickTimes, lOrR, img, reTry):
    if reTry == 1:
        while True:
            location = pyautogui.locateCenterOnScreen(img, confidence=0.8)
            if location is not None:
                pyautogui.click(location.x, location.y, clicks=clickTimes, interval=0.2, duration=0.2, button=lOrR)
                break
            else:
                # 此处将重试10次，10次后强制退出
                print("未找到我是脚本执行的结果匹配图片,查找10次，10次查找不到则退出")
                exitFlag = False
                count = 1
                while (count < 10):
                    location = pyautogui.locateCenterOnScreen(img, confidence=0.8)
                    count += 1
                    if location is None:
                        print("未找到匹配图片,0.1秒后重试")
                        print(img)
                        time.sleep(0.1)
                    else:
                        pyautogui.click(location.x, location.y, clicks=clickTimes, interval=0.2, duration=0.2,
                                        button=lOrR)
                        exitFlag = True
                        break
                    if count == 9:
                        exitFlag = True
                        break
            if exitFlag:
                break  # 跳出最外侧的For循环
    elif reTry == -1:
        while True:
            location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
            if location is not None:
                pyautogui.click(location.x, location.y, clicks=clickTimes, interval=0.2, duration=0.2, button=lOrR)
            time.sleep(0.1)
    elif reTry > 1:
        i = 1
        while i < reTry + 1:
            location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
            if location is not None:
                pyautogui.click(location.x, location.y, clicks=clickTimes, interval=0.2, duration=0.2, button=lOrR)
                print("重复")
                i += 1
            time.sleep(0.1)


# 数据检查
# cmdType.value  1.0 左键单击    2.0 左键双击  3.0 右键单击  4.0 输入  5.0 等待  6.0 滚轮
# ctype     空：0
#           字符串：1
#           数字：2
#           日期：3
#           布尔：4
#           error：5
def dataCheck(sheet1):
    checkCmd = True
    # 行数检查
    if sheet1.nrows < 2:
        print("没数据啊哥")
        checkCmd = False
    # 每行数据检查
    i = 1
    while i < sheet1.nrows:
        # 第1列 操作类型检查
        cmdType = sheet1.row(i)[0]
        if cmdType.ctype != 2 or (cmdType.value != 1.0 and cmdType.value != 2.0 and cmdType.value != 3.0
                                  and cmdType.value != 4.0 and cmdType.value != 5.0 and cmdType.value != 6.0):
            print('第', i + 1, "行,第1列数据有毛病")
            checkCmd = False
        # 第2列 内容检查
        cmdValue = sheet1.row(i)[1]
        # 读图点击类型指令，内容必须为字符串类型
        if cmdType.value == 1.0 or cmdType.value == 2.0 or cmdType.value == 3.0:
            if cmdValue.ctype != 1:
                print('第', i + 1, "行,第2列数据有毛病")
                checkCmd = False
        # 输入类型，内容不能为空
        if cmdType.value == 4.0:
            if cmdValue.ctype == 0:
                print('第', i + 1, "行,第2列数据有毛病")
                checkCmd = False
        # 等待类型，内容必须为数字
        if cmdType.value == 5.0:
            if cmdValue.ctype != 2:
                print('第', i + 1, "行,第2列数据有毛病")
                checkCmd = False
        # 滚轮事件，内容必须为数字
        if cmdType.value == 6.0:
            if cmdValue.ctype != 2:
                print('第', i + 1, "行,第2列数据有毛病")
                checkCmd = False
        i += 1
    return checkCmd


# 任务
def SendOnTime(img):
    i = 1
    picRootPath = os.path.abspath(os.path.join(os.getcwd(), "./")) + "\\albertpic\\"
    while i < sheetIndex.nrows:
        # 取本行指令的操作类型
        cmdType = sheetIndex.row(i)[0]
        if cmdType.value == 1.0:
            # 取图片名称
            sheetPath = sheetIndex.row(i)[1].value
            if ('|' in sheetIndex.row(i)[1].value):
                sheetPathList = sheetIndex.row(i)[1].value.split('|')
                for item in sheetPathList:
                    sheetPath = item
                    img = picRootPath + sheetPath
                    reTry = 1
                    if sheetIndex.row(i)[2].ctype == 2 and sheetIndex.row(i)[2].value != 0:
                        reTry = sheetIndex.row(i)[2].value
                    mouseClick(1, "left", img, reTry)
                    print("单击左键", img)
                    time.sleep(2)
                sheetPathList.clear()
            else:
                img = picRootPath + sheetPath
                reTry = 1
                if sheetIndex.row(i)[2].ctype == 2 and sheetIndex.row(i)[2].value != 0:
                    reTry = sheetIndex.row(i)[2].value
                mouseClick(1, "left", img, reTry)
                print("单击左键", img)
            print("单击左键执行完毕")
            # 2代表双击左键
        elif cmdType.value == 2.0:
            # 取图片名称
            img = picRootPath + sheetIndex.row(i)[1].value
            # 取重试次数
            reTry = 1
            if sheetIndex.row(i)[2].ctype == 2 and sheetIndex.row(i)[2].value != 0:
                reTry = sheetIndex.row(i)[2].value
            mouseClick(2, "left", img, reTry)
            print("双击左键", img)
        # 3代表右键
        elif cmdType.value == 3.0:
            # 取图片名称
            img = picRootPath + sheetIndex.row(i)[1].value
            # 取重试次数
            reTry = 1
            if sheetIndex.row(i)[2].ctype == 2 and sheetIndex.row(i)[2].value != 0:
                reTry = sheetIndex.row(i)[2].value
            mouseClick(1, "right", img, reTry)
            print("右键", img)
            # 4代表输入
        elif cmdType.value == 4.0:
            inputValue = sheetIndex.row(i)[1].value
            pyperclip.copy(inputValue)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.5)
            print("输入:", inputValue)
            # 5代表等待
        elif cmdType.value == 5.0:
            # 取图片名称
            waitTime = sheetIndex.row(i)[1].value
            time.sleep(waitTime)
            print("等待", waitTime, "秒")
        # 6代表滚轮
        elif cmdType.value == 6.0:
            # 取图片名称
            scroll = sheetIndex.row(i)[1].value
            pyautogui.scroll(int(scroll))
            print("滚轮滑动", int(scroll), "距离")
        i += 1


# 任务
def mainWork(img):
    i = 1
    picRootPath = os.path.abspath(os.path.join(os.getcwd(), "./")) + "\\albertpic\\"
    while i < sheet1.nrows:
        # 取本行指令的操作类型
        cmdType = sheet1.row(i)[0]
        if cmdType.value == 1.0:
            # 取图片名称
            sheetPath = sheet1.row(i)[1].value
            if ('|' in sheet1.row(i)[1].value):
                sheetPathList = sheet1.row(i)[1].value.split('|')
                for item in sheetPathList:
                    sheetPath = item
                    img = picRootPath + sheetPath
                    reTry = 1
                    if sheet1.row(i)[2].ctype == 2 and sheet1.row(i)[2].value != 0:
                        reTry = sheet1.row(i)[2].value
                    mouseClick(1, "left", img, reTry)
                    print("单击左键", img)
                    time.sleep(2)
                sheetPathList.clear()
            else:
                img = picRootPath + sheetPath
                reTry = 1
                if sheet1.row(i)[2].ctype == 2 and sheet1.row(i)[2].value != 0:
                    reTry = sheet1.row(i)[2].value
                mouseClick(1, "left", img, reTry)
                print("单击左键", img)
            print("单击左键执行完毕")
            # 2代表双击左键
        elif cmdType.value == 2.0:
            # 取图片名称
            img = picRootPath + sheet1.row(i)[1].value
            # 取重试次数
            reTry = 1
            if sheet1.row(i)[2].ctype == 2 and sheet1.row(i)[2].value != 0:
                reTry = sheet1.row(i)[2].value
            mouseClick(2, "left", img, reTry)
            print("双击左键", img)
        # 3代表右键
        elif cmdType.value == 3.0:
            # 取图片名称
            img = picRootPath + sheet1.row(i)[1].value
            # 取重试次数
            reTry = 1
            if sheet1.row(i)[2].ctype == 2 and sheet1.row(i)[2].value != 0:
                reTry = sheet1.row(i)[2].value
            mouseClick(1, "right", img, reTry)
            print("右键", img)
            # 4代表输入
        elif cmdType.value == 4.0:
            inputValue = sheet1.row(i)[1].value
            pyperclip.copy(inputValue)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.5)
            print("输入:", inputValue)
            # 5代表等待
        elif cmdType.value == 5.0:
            # 取图片名称
            waitTime = sheet1.row(i)[1].value
            time.sleep(waitTime)
            print("等待", waitTime, "秒")
        # 6代表滚轮
        elif cmdType.value == 6.0:
            # 取图片名称
            scroll = sheet1.row(i)[1].value
            pyautogui.scroll(int(scroll))
            print("滚轮滑动", int(scroll), "距离")
        i += 1


if __name__ == '__main__':
    file = 'cmd.xls'
    # 打开文件
    wb = xlrd.open_workbook(filename=file)
    # 通过索引获取表格sheet页
    sheet1 = wb.sheet_by_index(0)
    print('欢迎使用Albert Zhao-RPA~')
    # 数据检查
    checkCmd = dataCheck(sheet1)
    if checkCmd:
        key = input('Choose function: 1.Only One 2.While 3.SendMessOnTime\n')
        if key == '1':
            # 循环拿出每一行指令
            mainWork(sheet1)
        elif key == '2':
            while True:
                mainWork(sheet1)
                time.sleep(0.1)
                print("等待0.1秒")
        elif key == '3':
            timeList = ['06:30', '12:00', '22:30']  # 代表早、中、晚四个世间段 分别对应三张不同的sheet
            while True:
                now = time.strftime('%H:%M', time.localtime(time.time()))
                index = 2
                for ti in timeList:
                    if ti == now:
                        sheetIndex = wb.sheet_by_index(index)
                        # 数据检查
                        checkCmd = dataCheck(sheetIndex)
                        if checkCmd:
                            SendOnTime(sheetIndex)
                    index = index + 1
                    # pygame.mixer.init()
                    # pygame.mixer.music.load('D:\music\play.mp3')
                    # pygame.mixer.music.play()
                    # time.sleep(xxx)
                    # pygame.mixer.music.stop()
                time.sleep(50)
                print("等待50秒")
    else:
        print('输入有误或者已经退出!')
