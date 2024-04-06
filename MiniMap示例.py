import numpy
import pyautogui
import time
import math
import random
import numpy as np

from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement
import cv2
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#https://www.hyjaer.com/python/655/  自动寻路


def calculate_point_b(o,a, distance):
    # 计算从原点 O 到点 A 的向量
    dx = a[0]-o[0]
    dy = a[1]-o[1]

    # 单位化向量
    vector_length = math.sqrt(dx ** 2 + dy ** 2)
    unit_dx = dx / vector_length
    unit_dy = dy / vector_length

    # 计算延伸向量
    extension_vector = (unit_dx * distance, unit_dy * distance)

    # 计算点 B 的坐标
    b = (a[0] + extension_vector[0], a[1] + extension_vector[1])

    return b

def GetHeroLocation():
    # 读取大图像
    base_img = cv2.imread('resources/MiniMap/fnzq.png', 0)

    # 读取模板图像
    template_img = pyautogui.screenshot(region=(1596, 40, 294, 256))
    template_img = cv2.cvtColor(numpy.array(template_img), 0)
    template_img = cv2.cvtColor(template_img, cv2.COLOR_BGR2GRAY)
    # ------------------------------------------------------------------------------
    template_img = cv2.resize(template_img, None, fx=0.58, fy=0.58, interpolation=cv2.INTER_LINEAR)
    # python 模板匹配

    # 如果图像是四通道或更多通道，需要转换为三通道
    if len(base_img.shape) >= 3:
        if base_img.shape[2] > 3:
            base_img = cv2.cvtColor(base_img, cv2.COLOR_BGRA2BGR)
    if len(template_img.shape) >= 3:
        if template_img.shape[2] > 3:
            template_img = cv2.cvtColor(template_img, cv2.COLOR_BGRA2BGR)

    # 确保模板图像不是空的
    if template_img is None:
        print("模板图像未找到，请检查路径")
        exit()

    template_img = cv2.resize(template_img, None, fx=1, fy=1, interpolation=cv2.INTER_LINEAR)
    # 获取模板图像的大小
    template_size = template_img.shape[::-1]

    # 使用cv2.TM_CCOEFF_NORMED进行归一化相关匹配
    result = cv2.matchTemplate(base_img, template_img,
                               cv2.TM_CCOEFF_NORMED)  # TM_CCOEFF_NORMED 0.45 TM_CCOEFF 0.7 TM_CCORR 10000  TM_CCORR_NORMED 0.9false  TM_SQDIFF 0.8false   TM_SQDIFF_NORMED 1false
    # 找到匹配结果中的最大值
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    w, h = template_size
    return round(max_loc[0] + w / 2), round(max_loc[1] + h / 2)

def GetAnImageOfTheScreen(ScreenX1,ScreenY1,ScreenX2,ScreenY2):
    Screen_img = pyautogui.screenshot(region=(ScreenX1,ScreenY1,ScreenX2,ScreenY2))
    Screen_img = cv2.cvtColor(numpy.array(Screen_img), 0)
    Screen_img = cv2.cvtColor(Screen_img, cv2.COLOR_BGR2GRAY)
    return Screen_img


def waitForSwitchToLostArk():
    print("5秒内请切换至命运方舟")
    time.sleep(5)


def AiMoveTo(toX,toY):
    # 读取大图像
    base_img = cv2.imread("resources/MiniMap/fnzq.png", 0)
    # 读取模板图像
    template_img = GetAnImageOfTheScreen(1596,40,294,256)
    template_img = cv2.resize(template_img, None, fx=0.58, fy=0.58, interpolation=cv2.INTER_LINEAR)
    #------------------------------------------------------------------------------
    # 将图片转换为二值图
    ret, thresh = cv2.threshold(base_img, 127, 255, 0)

    # 获取图片的高度和宽度
    height, width = thresh.shape

    # 定义一个矩阵，用于存储图片中每个像素点的信息
    matrix = []

    # 遍历图片的每一个像素
    for i in range(height):
        row = []
        for j in range(width):
            # 获取像素的值
            pixel = thresh[i, j]
            # 判断像素值是否为 0，如果为 0，表示该像素为障碍物，否则为路径
            if pixel == 0:
                row.append(0)  # 0 表示障碍物
            else:
                row.append(1)  # 1 表示路径
        matrix.append(row)
    #------------------------------------------------------
    # python 模板匹配



    # 如果图像是四通道或更多通道，需要转换为三通道
    if len(base_img.shape)>=3:
        if base_img.shape[2] > 3:
            base_img = cv2.cvtColor(base_img, cv2.COLOR_BGRA2BGR)
    if len(template_img.shape)>=3:
        if template_img.shape[2] > 3:
            template_img = cv2.cvtColor(template_img, cv2.COLOR_BGRA2BGR)


    # 确保模板图像不是空的
    if template_img is None:
        print("模板图像未找到，请检查路径")
        exit()



    template_img = cv2.resize(template_img, None, fx=1, fy=1, interpolation=cv2.INTER_LINEAR)
    # 获取模板图像的大小
    template_size = template_img.shape[::-1]

    # 使用cv2.TM_CCOEFF_NORMED进行归一化相关匹配
    result = cv2.matchTemplate(base_img, template_img,cv2.TM_CCOEFF_NORMED)  # TM_CCOEFF_NORMED 0.45 TM_CCOEFF 0.7 TM_CCORR 10000  TM_CCORR_NORMED 0.9false  TM_SQDIFF 0.8false   TM_SQDIFF_NORMED 1false
    # 找到匹配结果中的最大值
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(min_val, '-----', max_val, '-----', min_loc, '-----', max_loc)

    # 为了找到最顶部的匹配结果，我们需要找到最大值的左上角
    top_left = max_loc

    # 标记匹配区域
    w, h = template_size
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(base_img, top_left, bottom_right, 255, 2)


    # 显示结果
    #cv2.imshow('Matching Result', base_img)
    #cv2.imshow('Matching Result2', template_img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    # ------------------------------------------------------
    # 1.创建一个网格，导入矩阵
    grid = Grid(matrix=matrix)

    # 2.创建开始和结束的点
    start = grid.node(round(top_left[0] + w / 2), round(top_left[1] + h / 2))
    # start = grid.node(233,233)
    end = grid.node(toX,toY)

    # 3.创建移动方法
    # finder = AStarFinder()
    # 对角线移动
    finder = AStarFinder(diagonal_movement=DiagonalMovement.always)

    # 4.使用finder查找路径
    path, runs = finder.find_path(start, end, grid)

    # ------------------------------------------------------

    counter = 0
    while True:
        if len(path) <= 0:return
        #路径坐标
        x2, y2, = path[counter]

        #角色坐标
        x1, y1 = GetHeroLocation()

        if math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)<10:
            print(counter,'到达',x1, y1,x2, y2)
            #time.sleep(0.1)
            counter += 5
        else:
            xy = calculate_point_b((960, 540), (960 + (x2 - x1), 540 + (y2 - y1)), 339)
            #pyautogui.moveTo(xy[0], min(xy[1], 950), duration=random.uniform(0.1, 0.2))
            pyautogui.click(xy[0], min(xy[1], 950),button='right')
            print(counter, '未到达', x1, y1, x2, y2)

            #pyautogui.click(960 + (x2 - x1)*30, 540 + (y2 - y1)*30, clicks=1, button='right')
            #print(counter,'未到达', x1, y1, x2, y2)
            #time.sleep(0.1)

        if counter > len(path):  # 假设我们想要在序列超过50时停止
            return True
        time.sleep(0.1)

def main():


    waitForSwitchToLostArk()
    AiMoveTo(218,179)


if __name__ == "__main__":
    main()