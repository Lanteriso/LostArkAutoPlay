import time

import pyautogui
import random
import 方舟模板def
import myfunction


image_list3 = [
    ['resources/DailyEntrustment/ysdyw.png', 0.7, myfunction.click_on_position, [[923, 23], 'left']],  # 同意和拒绝
]


def RunBehaviorTree(player, monster):
    while 1:
        运行状态(player)

def RunBehaviorTree2(player, monster):
    while 1:
        淘气的妖精任务(player)

def 阴森的夜雾():
    pyautogui.press('f5')
    pyautogui.moveTo(1695, 320, duration=random.uniform(0.2, 0.3))
    pyautogui.click()
    time.sleep(1)
    FindedImg = myfunction.试验查找指定图片([0, 0, 1920, 1080], [['resources/DailyEntrustment/ysdyw1.png', 0.7, myfunction.click_on_position, [[467, 10], 'left']], ])
    if FindedImg:
        FindedImg[2](FindedImg[3], FindedImg[4])
        time.sleep(1)
        pyautogui.press('enter')

        return True

    time.sleep(5)

def 完成阴森的夜雾():
    FindedImg = myfunction.试验查找指定图片([0, 0, 1920, 1080], [['resources/DailyEntrustment/ysdyw2.png', 0.7, myfunction.click_on_position, [[70, 10], 'left']], ])
    if FindedImg:
        FindedImg[2](FindedImg[3], FindedImg[4])
        time.sleep(1)
        pyautogui.press('8')
        FindedImg = myfunction.试验查找指定图片([0, 0, 1920, 1080], [['resources/DailyEntrustment/ysdyw3.png', 0.7, myfunction.click_on_position, [[70, 13], 'left']], ])
        if FindedImg:
            FindedImg[2](FindedImg[3], FindedImg[4])
            return True

def 接取任务(Entrustment):
    pyautogui.hotkey('alt','j')
    time.sleep(2)
    FindedImg = myfunction.试验查找指定图片([0, 0, 1920, 1080], [[Entrustment, 0.8, myfunction.click_on_position, [[923, 23], 'left']], ])
    if FindedImg:
        print(FindedImg)
        FindedImg[2](FindedImg[3], FindedImg[4])
        time.sleep(1)
        pyautogui.hotkey('alt', 'j')
        return True

def 换号中():
    FindedImg = myfunction.试验查找指定图片([0, 0, 1920, 1080], [['resources/DailyEntrustment/ysdyw7.png', 0.7, None, [[0, 0], 'left']], ])
    if not FindedImg:
        pyautogui.press('esc')
        time.sleep(1)
        FindedImg = myfunction.试验查找指定图片([0, 0, 1920, 1080], [['resources/DailyEntrustment/ysdyw4.png', 0.7, myfunction.click_on_position, [[68, 11], 'left']], ])
        if FindedImg:
            FindedImg[2](FindedImg[3], FindedImg[4])
            time.sleep(1)
            FindedImg = myfunction.试验查找指定图片([0, 0, 1920, 1080], [['resources/DailyEntrustment/ysdyw5.png', 0.7, myfunction.click_on_position, [[283, 10], 'left']], ])
            if FindedImg:
                print(FindedImg)
                if FindedImg[4][0][0] > 1100:
                    if FindedImg[4][0][1] > 444:
                        exit()
                    else:
                        pyautogui.moveTo(713, 525)
                        time.sleep(random.uniform(1.0, 2.0))
                        pyautogui.click()
                else:
                    FindedImg[2](FindedImg[3], FindedImg[4])
                time.sleep(1)
                FindedImg = myfunction.试验查找指定图片([0, 0, 1920, 1080], [['resources/DailyEntrustment/ysdyw8.png', 0.7, myfunction.click_on_position,[[22, 11], 'left']], ])
                if FindedImg:
                    FindedImg[2](FindedImg[3], FindedImg[4])
                    FindedImg[2](FindedImg[3], FindedImg[4])
                    time.sleep(1)
                    pyautogui.press('enter')
                    time.sleep(15)
                    return True
    time.sleep(5)

def 传送(Entrustment):
    pyautogui.moveTo(1695, 320, duration=random.uniform(0.2, 0.3))
    pyautogui.click()
    time.sleep(1)
    FindedImg = myfunction.试验查找指定图片([0, 0, 1920, 1080], [[Entrustment, 0.8, myfunction.click_on_position, [[467, 10], 'left']], ])
    if FindedImg:
        FindedImg[2](FindedImg[3], FindedImg[4])
        time.sleep(1)
        pyautogui.press('enter')

        return True
    time.sleep(5)

def 做任务(Entrustment):
    FindedImg = myfunction.试验查找指定图片([0, 0, 1920, 1080], [[Entrustment, 0.6, myfunction.click_on_position, [[25, 200], 'right']], ])
    if FindedImg:
        print('1111111')
        pyautogui.press('g')
    time.sleep(3)

def 运行状态(player):
    print(player.状态,player.character_class)
    if player.character_class == "默认":
        if 接取任务('resources/DailyEntrustment/ysdyw.png'):
            player.character_class = "任务中"
    elif player.character_class == "任务中":
        if 阴森的夜雾():
            player.character_class = "任务完成"
    elif player.character_class == "任务完成":
        if 完成阴森的夜雾():
            player.character_class = "换号中"
    elif player.character_class == "换号中":
        if 换号中():
            player.character_class = "默认"


def 淘气的妖精任务(player):
    print(player.状态)
    if player.状态 == "待命中":
        if 接取任务('resources/DailyEntrustment/tqdyj.png'):
            #player.character_class = "传送中"
            player.状态 = "任务中"
    elif player.状态 == "传送中":
        if 传送('resources/DailyEntrustment/tqdyj2.png'):
            player.状态 = "任务中"
    elif player.状态 == "任务中":
        if 做任务('resources/DailyEntrustment/tqdyj3.png'):
            player.状态 = "任务完成"



