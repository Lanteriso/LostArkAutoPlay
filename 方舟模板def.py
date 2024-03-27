import cv2
import numpy as np
import time
import pyautogui
import numpy
import math

def 修改模板大小(inimg,insize):
    # 修改模板图像大小为新的宽度和高度
    resized_inimg = cv2.resize(inimg, None, fx=insize, fy=insize, interpolation=cv2.INTER_LINEAR)
    return resized_inimg
def 转换颜色空间(inimg):
    # 颜色空间转换示例
    # 将BGR图像转换为灰度图像
    '''
    cv2.COLOR_BGR2GRAY
    用于将BGR三通道图像转换为单通道灰度图像。
    cv2.COLOR_BGR2HSV
    将BGR图像转换为HSV（色调、饱和度、明度）颜色模型，这种颜色空间在很多颜色检测和追踪任务中非常有用。
    cv2.COLOR_HSV2BGR
    则相反，将HSV图像转换回BGR。
    cv2.COLOR_BGR2RGB
    将BGR顺序的图像转换为符合大多数其他图形库所使用的RGB顺序。
    '''
    out_img = cv2.cvtColor(inimg, cv2.COLOR_BGR2GRAY)
    return out_img

def 高斯滤波器(inimg):
    # 应用高斯滤波器进行平滑处理
    sigma = 0.5  # 高斯核的标准差
    img_filtered = cv2.GaussianBlur(inimg, (5, 5), sigma)
    return img_filtered

def 边缘检测(inimg):
    # 应用Canny边缘检测器
    return cv2.Canny(inimg, threshold1=100, threshold2=200)

def 特征提取(inimg):
    return

def find_closest_point(points, target):
    """
    从points数组中找到最接近target点的坐标。

    参数:
    points -- 二维坐标数组，形状为 (n, 2)
    target -- 目标点，形状为 (2,)

    返回:
    closest_point -- 最接近target的点的坐标
    """
    # 计算每个点与目标点之间的距离
    distances = np.sqrt(((points - target) ** 2).sum(axis=1))

    # 找到最小距离的索引
    closest_index = np.argmin(distances)

    # 返回最接近的点
    closest_point = points[closest_index]
    return closest_point
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
def GetAnImageOfTheScreen(ScreenX1,ScreenY1,ScreenX2,ScreenY2):
    Screen_img = pyautogui.screenshot(region=(ScreenX1,ScreenY1,ScreenX2,ScreenY2))
    Screen_img = cv2.cvtColor(numpy.array(Screen_img), 0)
    Screen_img = cv2.cvtColor(Screen_img, cv2.COLOR_BGR2GRAY)
    return Screen_img

def TheImageTemplateMatches(img1,img2,):
    # 读取大图像
    base_img = img1
    # 读取模板图像
    template_img = cv2.imread(img2, 0)

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
        return False

    template_img = cv2.resize(template_img, None, fx=1, fy=1, interpolation=cv2.INTER_LINEAR)
    # 获取模板图像的大小
    template_size = template_img.shape[::-1]

    # 使用cv2.TM_CCOEFF_NORMED进行归一化相关匹配
    result = cv2.matchTemplate(base_img, template_img, cv2.TM_CCOEFF_NORMED)

    #loc = numpy.where(result >= 0.65)

    # 找到匹配结果中的最大值
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(img2,max_val)
    if max_val < 0.66:
        return False #没找到图片
    else:
        return True #找到图片
def 查找指定图片(Screenxy,templatepath,templatepath2):# 屏幕范围，白名单，黑名单

    imgbase = GetAnImageOfTheScreen(Screenxy[0],Screenxy[1],Screenxy[2],Screenxy[3])
    for i in templatepath:
        if not TheImageTemplateMatches(imgbase, i):
            return False  # 如果有张图没找到，就返回False

    for i in templatepath2:
        if TheImageTemplateMatches(imgbase, i):
            return False  # 如果有张图找到了，就返回False
    return True  # 组队确认



def TheImageTemplateMatches2(img1,img2,):
    # 读取大图像
    base_img = img1
    # 读取模板图像
    template_img = cv2.imread(img2, 0)

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
        return False

    # 设置模板图像的缩放
    #template_img = cv2.resize(template_img, None, fx=1, fy=1, interpolation=cv2.INTER_LINEAR)

    # 获取模板图像的大小
    #template_size = template_img.shape[::-1]

    # 获取模板图像的宽度和高度
    w, h = template_img.shape[::-1]



    # 使用cv2.TM_CCOEFF_NORMED进行归一化相关匹配
    result = cv2.matchTemplate(base_img, template_img, cv2.TM_CCOEFF_NORMED)

    # 找到所有匹配位置
    #locations = list(zip(*np.where(result >= 0.7)[::-1]))

    # 找到匹配结果中的最大值
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    '''
    # 检查是否找到了匹配点
    if max_val > 0.8 and 测试开关:  # 这里的阈值根据实际情况调整
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(img1, top_left, bottom_right, 255, 2)
        print("Best match found at location:", top_left)
        # 显示结果
        cv2.imshow('Matching Result', img1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        
        print("No match found")
    '''


    if max_val > 0.8:
        print(img2,max_val)
        return max_loc # 找到图片
    else:
        return []  # 没找到图片



    if len(locations) > 0  and 测试开关: # 测试  1打开，0关闭  多个点找离中心最近的点
        # 如果找到的匹配点太多，可以选择只保留得分最高的几个
        locations = sorted(locations, key=lambda x: result[x[1], x[0]], reverse=True)[:5]

        # 在源图像上绘制所有匹配位置的矩形框
        for pt in locations:
            cv2.rectangle(img1, pt, (pt[0] + w, pt[1] + h), (255, 255, 0), 2)

        # 示例使用
        points = np.array(locations)
        print(points)
        target = np.array([960, 540])  # 指定的目标点

        closest = find_closest_point(points, target)#查找离target最近的点
        print("最接近的点是:", closest)

        # 显示结果图像
        cv2.imshow('All Matches', img1)
        cv2.waitKey(0)

    #return locations


def TheImageTemplateMatches3(img1, img2, ):
    # 读取大图像
    base_img = img1
    # 读取模板图像
    template_img = cv2.imread(img2, 0)

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
        return False

    # 设置模板图像的缩放
    # template_img = cv2.resize(template_img, None, fx=1, fy=1, interpolation=cv2.INTER_LINEAR)

    # 获取模板图像的大小
    template_size = template_img.shape[::-1]

    # 获取模板图像的宽度和高度
    w, h = template_img.shape[::-1]

    # 使用cv2.TM_CCOEFF_NORMED进行归一化相关匹配
    result = cv2.matchTemplate(base_img, template_img, cv2.TM_CCOEFF_NORMED)

    # 找到所有匹配位置
    # locations = list(zip(*np.where(result >= 0.7)[::-1]))

    # 找到匹配结果中的最大值
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    '''
    # 检查是否找到了匹配点
    if max_val > 0.8 and 测试开关:  # 这里的阈值根据实际情况调整
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(img1, top_left, bottom_right, 255, 2)
        print("Best match found at location:", top_left)
        # 显示结果
        cv2.imshow('Matching Result', img1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:

        print("No match found")
    '''

    if max_val > 0.7:
        print(img2, max_val)
        return max_loc,template_size  # 找到图片
    else:
        return [],template_size  # 没找到图片

    if len(locations) > 0 and 测试开关:  # 测试  1打开，0关闭  多个点找离中心最近的点
        # 如果找到的匹配点太多，可以选择只保留得分最高的几个
        locations = sorted(locations, key=lambda x: result[x[1], x[0]], reverse=True)[:5]

        # 在源图像上绘制所有匹配位置的矩形框
        for pt in locations:
            cv2.rectangle(img1, pt, (pt[0] + w, pt[1] + h), (255, 255, 0), 2)

        # 示例使用
        points = np.array(locations)
        print(points)
        target = np.array([960, 540])  # 指定的目标点

        closest = find_closest_point(points, target)  # 查找离target最近的点
        print("最接近的点是:", closest)

        # 显示结果图像
        cv2.imshow('All Matches', img1)
        cv2.waitKey(0)

    # return locations

def 试验TheImageTemplateMatches(img1, templatelist, ):
    image_name, image_scale, image_offset, image_method = templatelist
    # 读取大图像
    base_img = img1
    # 读取模板图像
    template_img = cv2.imread(image_name, 0)

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
        return False

    # 设置模板图像的缩放
    # template_img = cv2.resize(template_img, None, fx=1, fy=1, interpolation=cv2.INTER_LINEAR)

    # 获取模板图像的大小
    template_size = template_img.shape[::-1]

    # 获取模板图像的宽度和高度
    w, h = template_img.shape[::-1]

    # 使用cv2.TM_CCOEFF_NORMED进行归一化相关匹配
    result = cv2.matchTemplate(base_img, template_img, cv2.TM_CCOEFF_NORMED)

    # 找到所有匹配位置
    # locations = list(zip(*np.where(result >= 0.7)[::-1]))

    # 找到匹配结果中的最大值
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    '''
    # 检查是否找到了匹配点
    if max_val > 0.8 and 测试开关:  # 这里的阈值根据实际情况调整
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(img1, top_left, bottom_right, 255, 2)
        print("Best match found at location:", top_left)
        # 显示结果
        cv2.imshow('Matching Result', img1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:

        print("No match found")
    '''

    if max_val > image_scale:

        return [image_name, image_scale, image_offset, image_method,max_loc,template_size]  # 找到图片
    else:
        return [] # 没找到图片

def 试验小地图TheImageTemplateMatches(img1, templatelist, ):
    # image_name, image_scale, image_offset, image_method,image_extended = templatelist
    # 读取大图像
    base_img = img1
    # 读取模板图像
    template_img = cv2.imread(templatelist[0], 0)

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
        return False

    # 获取模板图像的大小
    template_size = template_img.shape[::-1]

    # 使用cv2.TM_CCOEFF_NORMED进行归一化相关匹配
    result = cv2.matchTemplate(base_img, template_img, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val > templatelist[1]:

        return [max_loc,template_size]  # 找到图片
    else:
        return [] # 没找到图片

def 试验全屏TheImageTemplateMatches(img1, templatelist, ):
    # #['resources/demo/068.png', 0.7, 按下某键, [参数1]，[参数2]] = templatelist
    # 读取大图像
    base_img = img1
    # 读取模板图像
    template_img = cv2.imread(templatelist[0], 0)

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
        return False

    # 获取模板图像的大小
    template_size = template_img.shape[::-1]

    # 使用cv2.TM_CCOEFF_NORMED进行归一化相关匹配
    result = cv2.matchTemplate(base_img, template_img, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val > templatelist[1]:

        return [[max_loc,template_size]]  # 找到图片
    else:
        return [] # 没找到图片

def 查找指定图片返回最佳点(Screenxy,templatepath):# 屏幕范围，白名单
    # 在很多血条模板中找，找到一张就返回True,相当于or，返回的是单个坐标,都没找到返回空数组
    imgbase = GetAnImageOfTheScreen(Screenxy[0],Screenxy[1],Screenxy[2],Screenxy[3])
    for i in templatepath:
        outTargetLocation = TheImageTemplateMatches2(imgbase, i)
        if outTargetLocation:
            return outTargetLocation
    return []

def 查找指定图片返回最佳点2(Screenxy,templatepath):# 屏幕范围，白名单
    # 在很多血条模板中找，找到一张就返回True,相当于or，返回的是单个坐标,都没找到返回空数组
    imgbase = GetAnImageOfTheScreen(Screenxy[0],Screenxy[1],Screenxy[2],Screenxy[3])
    for i in templatepath:
        outTargetLocation,template_size = TheImageTemplateMatches3(imgbase, i)
        if outTargetLocation:
            return outTargetLocation,template_size
    return [],template_size

def 试验查找指定图片(Screenxy,templatepath):# 屏幕范围，白名单
    # 在很多血条模板中找，找到一张就返回True,相当于or，返回的是单个坐标,都没找到返回空数组
    imgbase = GetAnImageOfTheScreen(Screenxy[0],Screenxy[1],Screenxy[2],Screenxy[3])
    for i in templatepath:
        outTarget = 试验TheImageTemplateMatches(imgbase, i)
        if outTarget:
            return outTarget
    return []

def 试验查找小地图指定图片(Screenxy,templatepath):# 屏幕范围，白名单
    # 在很多血条模板中找，找到一张就返回True,相当于or，返回的是单个坐标,都没找到返回空数组
    imgbase = GetAnImageOfTheScreen(Screenxy[0],Screenxy[1],Screenxy[2],Screenxy[3])
    for i in templatepath:
        outTarget = 试验全屏TheImageTemplateMatches(imgbase, i)
        if outTarget:
            return i+outTarget
    return []

def 试验查找全屏指定图片(Screenxy,templatepath):# 屏幕范围，白名单
    # 在很多血条模板中找，找到一张就返回True,相当于or，返回的是单个坐标,都没找到返回空数组
    imgbase = GetAnImageOfTheScreen(Screenxy[0],Screenxy[1],Screenxy[2],Screenxy[3])
    for i in templatepath:
        outTarget = 试验全屏TheImageTemplateMatches(imgbase, i)
        if outTarget:
            return i+outTarget
    return []

def 查找图片返回图片名(Screenxy,templatepath):
    imgbase = GetAnImageOfTheScreen(Screenxy[0],Screenxy[1],Screenxy[2],Screenxy[3])
    for i in templatepath:
        outTargetLocation = TheImageTemplateMatches2(imgbase, i)
        if outTargetLocation:
            return i
    return ""

def 向目标移动(xy):  # 因为有可能会移动到目标身后，所以//2，有时刚好
    pyautogui.moveTo((xy[0]+960)//2, (xy[1]+540)//2, duration=0.3)
    pyautogui.click(button='right')

def 向目标移动不减半(xy): #
    pyautogui.moveTo(xy, duration=0.3)
    pyautogui.click(button='right')

def 和目标的距离(x1,y1,x2,y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def gogogo():
    # 读取大图像和模板图像
    img = cv2.imread('resources/demo/028.png', 0)
    template = cv2.imread('resources/demo/029.png', 0)




    # 获取模板图像的宽度和高度
    w, h = template.shape[::-1]

    # 使用matchTemplate函数进行匹配
    res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)

    # 找到最大和最小值及其位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(min_val, max_val, min_loc, max_loc)
    # 使用阈值确定匹配区域
    threshold = 0.8
    loc = np.where( res >= threshold)

    # 绘制所有矩形框
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

    # 为了找到最顶部的匹配结果，我们需要找到最大值的左上角
    top_left = max_loc
    # 绘制最佳的矩形框
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(img, top_left, bottom_right, 255, 2)

    # 显示结果
    cv2.imshow('Detected',img)
    cv2.imshow('Detected2',template)
    cv2.imshow('Detected3',res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

测试开关 = 0
# 测试
while 测试开关 and 0:  # 查敌人血条
    ovidjvodj = 查找指定图片返回最佳点([0, 0, 1920, 1080], ['resources/demo/033.png', 'resources/demo/046.png'])
    if ovidjvodj:
        print(f'找到了{ovidjvodj}')
        exit()
    time.sleep(5)