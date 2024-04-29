import random
import pyautogui
import time
import math

# 延伸
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

# 假设你定义了一系列的方法
def method1(pairs1,pairs2):
    print("执行方法1")

def method2(xy):
    print("执行方法2")

def method10(xy):
    print("执行方法10")

def 点击目标(xy,offset):
    print("执行方法12")
    pyautogui.moveTo(xy[0]+offset[0] + random.randint(-10, 10), xy[1]+offset[1] + random.randint(-10, 10), duration=0.3)
    time.sleep(random.uniform(1.0, 2.0))
    pyautogui.click()

def 按下某键(pairs1,pairs2):# pairs1值是固定返回的，在image_list[3]定义，pairs2是动态返回的，比如找到图片的坐标
    print(f'按下某键{pairs1,pairs2}')
    # 模拟按下 'e' 键
    pyautogui.keyDown(pairs1[0])
    # 保持按下状态3秒钟
    time.sleep(pairs1[1])
    # 模拟释放 'e' 键
    pyautogui.keyUp(pairs1[0])

def 点击某点(pairs1,pairs2):
    print(f'点击某点{pairs1, pairs2}')
    pyautogui.moveTo(pairs2[0][0]+pairs1[0][0] + random.randint(-10, 10), pairs2[0][1]+pairs1[0][1] + random.randint(-10, 10), duration=0.3)
    time.sleep(random.uniform(1.0, 2.0))
    pyautogui.click(button = pairs1[1])

def 小地图点击某点(pairs1,pairs2):
    print(f'点击某点{pairs1, pairs2}')
    xy = calculate_point_b((960, 540), (960 + (pairs2[0][0] + pairs1[0][0] - 147), 540 + (pairs2[0][1] + pairs1[0][1] - 128)), pairs1[1])
    pyautogui.moveTo(xy, duration=random.uniform(0.2, 0.3))
    pyautogui.click(button='right')

def 小地图移动到目标(extended,xy,offset):
    print(f'小地图移动到目标{xy}')
    print(xy,xy[0] + offset[0],xy[1] + offset[1],offset)
    xy = calculate_point_b((960, 540), (960 + (xy[0] + offset[0] - 147), 540 + (xy[1] + offset[1] - 128)), extended)
    pyautogui.moveTo(xy, duration=random.uniform(0.2, 0.3))
    pyautogui.click(button='right')

# ... 为其他方法添加类似的函数定义

# 创建一个列表，其中包含图片的详细信息和对应的方法
image_list = [
    # 图片地址，模板匹配参数，偏移量，对应方法
    ['resources/demo/020.png', 0.7,[150,241], 点击目标],  # 地牢确认
    # ... 添加其他图片的信息和对应的方法
    ['resources/demo/021.png', 0.7, [150, 244], 点击目标],  # 下一空间确认
    ['resources/demo/022.png', 0.7, [150, 253], 点击目标],  # 星辰确认
    ['resources/demo/023.png', 0.7, [127, 119], 点击目标],  # 复活确认
    ['resources/demo/024.png', 0.7, [355, 629], 点击目标],  # 地牢结束点击
    ['resources/demo/026.png', 0.7, [65, 11], 点击目标],  # 星辰结束确认ESC
    ['resources/demo/054.png', 0.7, [70, 216], 点击目标],  # 地牢结束点击
    ['resources/demo/073.png', 0.7, [52, 18], 点击目标],  # 组队确认
]

# 小地图
image_list2 = [
    # 图片地址，模板匹配参数，偏移量，对应方法,延伸距离
    #['resources/demo/029.png', 0.7, 小地图点击某点,[[8,8],359]], # 小地图采集 偏移[8,8]   延长359
    # ... 添加其他图片的信息和对应的方法
    ['resources/demo/051.png', 0.7, 小地图点击某点,[[10,15],359]],  # 柱子
    ['resources/demo/059.png', 0.7, 小地图点击某点,[[14,19],359]],  # 柱子
    ['resources/demo/065.png', 0.7, 小地图点击某点,[[12,16],359]],  # 柱子
    ['resources/demo/032.png', 0.7, 小地图点击某点, [[11, 14], 359]],  # 传送门
    ['resources/demo/053.png', 0.7, 小地图点击某点, [[14, 16], 359]],  # 传送门
    ['resources/demo/058.png', 0.7, 小地图点击某点, [[15, 17], 359]],  # 传送门
]

# 找图
image_list3 = [
    # 图片地址，模板匹配参数，对应方法,[要反回到方法的参数用数组的方式表示，不同的方法返回不同的参数，但都是一个数组]
    # 前3个参数是固定的，弟4参数是一个数组
    ['resources/demo/074.png', 0.7, 按下某键,['g',1]],  # 进入传送门
    # ... 添加其他图片的信息和对应的方法
    # ['resources/demo/071.png', 0.7, 点击某点,[[252,250],'left']],  # 地牢确认

    ['resources/demo/020.png', 0.7, 点击某点, [[150, 241], 'left']],  # 地牢确认
    # ... 添加其他图片的信息和对应的方法
    ['resources/demo/021.png', 0.7, 点击某点, [[150, 244], 'left']],  # 地牢移动下一空间

    ['resources/demo/022.png', 0.7, 点击某点, [[150, 253], 'left']],  # 星辰确认
    ['resources/demo/023.png', 0.7, 点击某点, [[127, 119], 'left']],  # 复活确认
    ['resources/demo/024.png', 0.7, 点击某点, [[355, 630], 'left']],    # 地牢结束点击
    ['resources/demo/026.png', 0.7, 点击某点, [[65, 11], 'left']],  # 星辰结束确认ESC
    ['resources/demo/054.png', 0.7, 点击某点, [[70, 236], 'left']],  # 地牢结束点击
    ['resources/demo/073.png', 0.7, 点击某点, [[52, 18], 'left']],  # 地牢结束点击
]

image_list4 = [
    # 图片地址，模板匹配参数，对应方法,[要反回到方法的参数用数组的方式表示，不同的方法返回不同的参数，但都是一个数组]
    # 前3个参数是固定的，弟4参数是一个数组

    ['resources/demo/mzhddl.png', 0.7, 点击某点, [[0, 0], 'left']],  # 每周混沌地牢
    ['resources/demo/mzxchw.png', 0.7, 点击某点, [[0, 0], 'left']],  # 每周星辰护卫
]
