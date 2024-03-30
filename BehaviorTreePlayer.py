import time

import pyautogui
import random
import 方舟模板def
import myfunction

image_list = [
    # 图片地址，模板匹配参数，偏移量，对应方法,延伸距离
    #['resources/demo/029.png', 0.7, 小地图点击某点,[[8,8],359]], # 小地图采集 偏移[8,8]   延长359
    # ... 添加其他图片的信息和对应的方法
    ['resources/demo/051.png', 0.7, myfunction.小地图点击某点,[[10,15],339,'柱子']],  # 柱子
    ['resources/demo/059.png', 0.7, myfunction.小地图点击某点,[[14,19],339,'柱子']],  # 柱子
    ['resources/demo/065.png', 0.7, myfunction.小地图点击某点,[[12,16],339,'柱子']],  # 柱子
    ['resources/demo/032.png', 0.7, myfunction.小地图点击某点, [[11, 14], 339,'传送门']],  # 传送门
    ['resources/demo/053.png', 0.7, myfunction.小地图点击某点, [[14, 16], 339,'传送门']],  # 传送门
    ['resources/demo/058.png', 0.7, myfunction.小地图点击某点, [[15, 17], 339,'传送门']],  # 传送门
    ['resources/demo/031.png', 0.7, myfunction.小地图移动攻击某点, [[13, 13], 339,'BOSS']],  # BOSS

]
image_list1 = [
    ['resources/demo/074.png', 0.7, myfunction.press_key,['g',1]],  # 传送门按键
    ['resources/demo/061.png', 0.7, myfunction.click_on_position,[[238, 242], 'right']],  # 传送门图片
    ['resources/demo/063.png', 0.7, myfunction.移动并攻击,[[32,160],'right','地图柱子']],  # 柱子
    ['resources/demo/033.png', 0.7, myfunction.移动并攻击,[[41,180],'right','小怪血条']],  # 小怪血条
]

image_list2 = [
    ['resources/demo/030.png', 0.7, myfunction.小地图移动攻击某点, [[6, 6], 339,'小怪']],  # 小怪
]
def RunBehaviorTree(player, monster):
    player.状态 = '星辰护卫中'
    开始战斗(player)
    if 进入地牢(player):
        开始战斗(player)


def 进入地牢(player):

    # if not 在地牢中():
    FindedImg0 = 方舟模板def.试验查找全屏指定图片([0, 0, 1920, 1080], [['resources/dungeon/007.png', 0.7, None, [[0, 0], 'left']], ])
    if not FindedImg0:  # 在星辰里
        pyautogui.hotkey('alt','q')
        time.sleep(1)
        FindedImg = 方舟模板def.试验查找全屏指定图片([0, 0, 1920, 1080], [['resources/dungeon/008.png', 0.7, myfunction.click_on_position, [[111, 136], 'left']], ])
        if FindedImg:
            FindedImg[2](FindedImg[3], FindedImg[4])
            time.sleep(1)
            FindedImg4 = 方舟模板def.试验查找全屏指定图片([0, 0, 1920, 1080], [['resources/dungeon/005.png', 0.7, myfunction.click_on_position, [[86, 18], 'left']], ])
            if FindedImg4:
                FindedImg4[2](FindedImg4[3], FindedImg4[4])
                time.sleep(1)
                FindedImg2 = 方舟模板def.试验查找全屏指定图片([0, 0, 1920, 1080], [['resources/dungeon/002.png', 0.7, myfunction.click_on_position, [[39, 10], 'left']], ])
                if FindedImg2:
                    FindedImg2[2](FindedImg2[3], FindedImg2[4])
                    time.sleep(1)
                    FindedImg3 = 方舟模板def.试验查找全屏指定图片([0, 0, 1920, 1080], [['resources/dungeon/003.png', 0.7, myfunction.click_on_position, [[54, 15], 'left']], ])
                    if FindedImg3:
                        FindedImg3[2](FindedImg3[3], FindedImg3[4])
                        time.sleep(1)
                        player.状态 = '星辰护卫中'
                    return FindedImg3
        return False  # 不在星辰 且 没成功进入星辰
    else:# 已经在星辰里
        player.状态 = '星辰护卫中'
        return True

def 开始战斗(player):

    while player.状态 == '星辰护卫中':
        # 小地图
        FindedImg = myfunction.试验查找小地图指定图片([1596, 40, 294, 256], image_list)
        if FindedImg:
            if FindedImg[2](FindedImg[3], FindedImg[4]):
                player.攻击目标2()
        else:
            FindedImg1 = myfunction.试验查找小地图指定图片([0, 0, 1920, 1080], image_list1)
            if FindedImg1:
                if FindedImg1[2](FindedImg1[3], FindedImg1[4]):
                    player.攻击目标2()
            else:
                FindedImg2 = myfunction.试验查找小地图指定图片([1596, 40, 294, 256], image_list2)
                if FindedImg2:
                    if FindedImg2[2](FindedImg2[3], FindedImg2[4]):
                        player.攻击目标2()
                else:
                    time.sleep(2)
                    x, y = random.randint(860, 1060), random.randint(440, 640)
                    pyautogui.click(x, y, clicks=1, button='right')
                    FindedImg3 =  方舟模板def.试验查找全屏指定图片([0, 0, 1920, 1080],[['resources/dungeon/009.png', 0.7, myfunction.click_on_position, [[70, 236], 'left']], ])
                    if FindedImg3:
                        FindedImg3[2](FindedImg3[3], FindedImg3[4])
                        player.状态 = '地牢结束'
                        exit()
