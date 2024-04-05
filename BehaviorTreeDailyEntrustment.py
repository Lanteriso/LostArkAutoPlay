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

def 接取任务():
    pyautogui.hotkey('alt','j')
    time.sleep(3)
    FindedImg = myfunction.试验查找指定图片([0, 0, 1920, 1080], [['resources/DailyEntrustment/ysdyw.png', 0.7, myfunction.click_on_position, [[923, 23], 'left']], ])
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
                FindedImg = myfunction.试验查找指定图片([0, 0, 1920, 1080], [['resources/DailyEntrustment/ysdyw8.png', 0.7, myfunction.click_on_position,[[22, 1], 'left']], ])
                if FindedImg:
                    FindedImg[2](FindedImg[3], FindedImg[4])
                    time.sleep(1)
                    pyautogui.press('enter')
                    time.sleep(15)
                    return True
    time.sleep(5)
def 运行状态(player):
    print(player.状态,player.character_class)
    if player.character_class == "默认":
        if 接取任务():
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



