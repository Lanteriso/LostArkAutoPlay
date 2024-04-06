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
    ['resources/dungeon/012.png', 0.7, myfunction.小地图点击某点,[[10,15],339,'柱子']],  # 柱子
    ['resources/dungeon/013.png', 0.7, myfunction.小地图点击某点,[[10,15],339,'柱子']],  # 柱子
    ['resources/dungeon/015.png', 0.7, myfunction.小地图点击某点,[[15,12],339,'命运碎片']],  # 命运碎片
    ['resources/demo/032.png', 0.7, myfunction.小地图点击某点, [[11, 14], 339,'传送门']],  # 传送门
    ['resources/demo/053.png', 0.7, myfunction.小地图点击某点, [[14, 16], 339,'传送门']],  # 传送门
    ['resources/demo/058.png', 0.7, myfunction.小地图点击某点, [[15, 17], 339,'传送门']],  # 传送门
    ['resources/demo/031.png', 0.7, myfunction.小地图移动攻击某点, [[13, 13], 339,'BOSS']],  # BOSS

]
image_list1 = [
    ['resources/dungeon/014.png', 0.7, myfunction.click_on_position,[[42, 60], 'right']],  # 命运碎片
    ['resources/demo/074.png', 0.7, myfunction.press_key,['g',1]],  # 传送门按键
    ['resources/demo/061.png', 0.7, myfunction.click_on_position,[[238, 242], 'right']],  # 传送门图片
    ['resources/demo/063.png', 0.7, myfunction.移动并攻击,[[32,160],'right','地图柱子']],  # 柱子
    ['resources/demo/033.png', 0.7, myfunction.移动并攻击,[[41,180],'right','小怪血条']],  # 小怪血条
]

image_list2 = [
    ['resources/demo/030.png', 0.7, myfunction.小地图移动攻击某点, [[6, 6], 339,'小怪']],  # 小怪
]

image_list3 = [
    # 图片地址，模板匹配参数，对应方法,[要反回到方法的参数用数组的方式表示，不同的方法返回不同的参数，但都是一个数组]
    # 前3个参数是固定的，弟4参数是一个数组
    ['resources/demo/074.png', 0.7, myfunction.press_key,['g',1]],  # 进入传送门
    # ... 添加其他图片的信息和对应的方法
    # ['resources/demo/071.png', 0.7, 点击某点,[[252,250],'left']],  # 地牢确认

    ['resources/demo/020.png', 0.7, myfunction.click_on_position, [[150, 241], 'left']],  # 地牢确认
    # ... 添加其他图片的信息和对应的方法
    ['resources/demo/021.png', 0.7, myfunction.click_on_position, [[150, 244], 'left']],  # 地牢移动下一空间

    ['resources/demo/022.png', 0.7, myfunction.click_on_position, [[150, 253], 'left']],  # 星辰确认
    ['resources/demo/023.png', 0.7, myfunction.click_on_position, [[127, 119], 'left']],  # 复活确认
    #['resources/demo/024.png', 0.7, myfunction.click_on_position, [[355, 630], 'left']],    # 地牢结束点击
    ['resources/demo/026.png', 0.7, myfunction.click_on_position, [[65, 11], 'left']],  # 星辰结束确认ESC
    ['resources/demo/054.png', 0.7, myfunction.click_on_position, [[70, 236], 'left']],  # 地牢结束点击
    ['resources/demo/073.png', 0.7, myfunction.click_on_position, [[52, 18], 'left']],  # 同意和拒绝
]

image_list4 = [
    ['resources/characterclass/ws.png', 0.8, None, [[0, 0], '武神']],
    ['resources/characterclass/sq.png', 0.8, None, [[0, 0], '圣骑']],
    ['resources/characterclass/sr.png', 0.8, None, [[0, 0], '诗人']],
    ['resources/characterclass/hy.png', 0.8, None, [[0, 0], '伞萝']],
    ['resources/characterclass/qss.png', 0.8, None, [[0, 0], '枪术士']],
    ['resources/characterclass/kzs.png', 0.8, None, [[0, 0], '狂战士']],
    ['resources/characterclass/lmr.png', 0.8, None, [[0, 0], '猎魔人']],
    ['resources/characterclass/qpds.png', 0.8, None, [[0, 0], '枪炮大师']],
    ['resources/characterclass/bq.png', 0.8, None, [[0, 0], '霸拳']],
    ['resources/characterclass/ml.png', 0.8, None, [[0, 0], '墨灵']],
    ['resources/characterclass/yy.png', 0.8, None, [[0, 0], '鹰眼']],
    ['resources/characterclass/ysws.png', 0.8, None, [[0, 0], '元素巫师']],
    ['resources/characterclass/hmz.png', 0.8, None, [[0, 0], '毁灭者']],
    ['resources/characterclass/emlr.png', 0.8, None, [[0, 0], '恶魔利刃']],
    ['resources/characterclass/kpds.png', 0.8, None, [[0, 0], '卡牌大师']],
]

def RunBehaviorTree(player, monster):
    if 进入地牢(player):
        开始战斗(player)

def RunBehaviorTree2(player, monster):
    # player.状态 = '星辰护卫中'
    while 1:
        运行状态(player)

def RunBehaviorTree3(player, monster):
    # player.状态 = '星辰护卫中'
    while 1:
        运行状态(player)

def 进入地牢(player):

    # if not 在地牢中():
    FindedImg0 = 方舟模板def.试验查找全屏指定图片([0, 0, 1920, 1080], [['resources/dungeon/007.png', 0.7, None, [[0, 0], 'left']], ])
    if not FindedImg0:  # 在星辰里
        pyautogui.hotkey('alt','q')
        time.sleep(1)
    else:
        FindedImg0 = 方舟模板def.试验查找全屏指定图片([0, 0, 1920, 1080], [['resources/dungeon/010.png', 0.7, myfunction.click_on_position, [[37, 12], 'left']], ])
        if FindedImg0:
            FindedImg0[2](FindedImg0[3], FindedImg0[4])
            time.sleep(1)
        else:
            return True# 已经在地牢里了，准备战斗
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
        FindedImg0 = 方舟模板def.试验查找全屏指定图片([0, 0, 1920, 1080],[['resources/dungeon/011.png', 0.7, None, [[86, 18], 'left']], ])
        if FindedImg0:
            pyautogui.press('esc')
            time.sleep(1)
            pyautogui.press('esc')
            player.状态 = "换人中"
        FindedImg3 = 方舟模板def.试验查找全屏指定图片([0, 0, 1920, 1080], [['resources/dungeon/003.png', 0.7, myfunction.click_on_position, [[54, 15], 'left']], ])
        if FindedImg3:
            FindedImg3[2](FindedImg3[3], FindedImg3[4])
            time.sleep(1)
        return FindedImg3


def 开始战斗(player):
    # 小地图
    FindedImg = myfunction.试验查找指定图片([1596, 40, 294, 256], image_list)
    if FindedImg:
        if FindedImg[2](FindedImg[3], FindedImg[4]):
            player.攻击目标2()
    else:
        FindedImg1 = myfunction.试验查找指定图片([0, 0, 1920, 1080], image_list1)
        if FindedImg1:
            if FindedImg1[2](FindedImg1[3], FindedImg1[4]):
                player.攻击目标2()
            if FindedImg1[0] == 'resources/dungeon/014.png':
                pyautogui.press('g')
        else:
            FindedImg2 = myfunction.试验查找指定图片([1596, 40, 294, 256], image_list2)
            if FindedImg2:
                if FindedImg2[2](FindedImg2[3], FindedImg2[4]):
                    player.攻击目标2()
            else:
                FindedImg3 = myfunction.试验查找指定图片([0, 0, 1920, 1080], image_list3)
                if FindedImg3:
                    FindedImg3[2](FindedImg3[3], FindedImg3[4])
                    if FindedImg3[0] == 'resources/demo/054.png':
                        player.状态 = "待命中"

                else:
                    time.sleep(2)
                    x, y = random.randint(860, 1060), random.randint(440, 640)
                    pyautogui.click(x, y, clicks=1, button='right')
                    player.攻击目标2()
                    screenshot = pyautogui.screenshot(region=(808, 962, 1, 1))
                    r,g,b = screenshot.getpixel((0, 0))
                    if all(abs(c1 - c2) <= 20 for c1, c2 in zip((r,g,b), (20,20,20))):
                        pyautogui.press('f1')
                        time.sleep(0.3)


def 开始换人(player):
    time.sleep(3)
    FindedImg = 方舟模板def.试验查找全屏指定图片([0, 0, 1920, 1080], [['resources/dungeon/008.png', 0.7, myfunction.click_on_position, [[111, 136], 'left']], ])
    return FindedImg

def 查看职业(player):
    pyautogui.press('p')
    time.sleep(3)
    FindedImg = 方舟模板def.试验查找全屏指定图片([0, 0, 1920, 1080],image_list4)
    if FindedImg:
        print(FindedImg)
        player.SetCharacterSkill(FindedImg[3][1])
        pyautogui.press('p')

def 运行状态(player):
    print(player.状态,player.character_class)
    if player.character_class == "默认":
        查看职业(player)
    elif player.状态 == "待命中":
        if 进入地牢(player):
            player.状态 = "战斗中"
    elif player.状态 == "战斗中":
        开始战斗(player)
    elif player.状态 == "换人中":
        if 开始换人(player):
            player.状态 = "待命中"

