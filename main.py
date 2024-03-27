import time
import random
import pyautogui
import 方舟模板def
import math

import 方舟模板执行


class Skill:
    def __init__(self, name, cooldown):
        self.name = name
        self.cooldown = cooldown
        self.last_used_time = 0

    def is_ready(self, current_time):
        return current_time - self.last_used_time >= self.cooldown

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.位置 = [0, 0]

    def is_alive(self):
        return self.health > 0

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} attacks {other.name} for {self.attack_power} damage.")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} heals for {amount} health points.")





class Monster(Character):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)


class Player(Character):
    def __init__(self, name, health, attack_power,character_class):
        super().__init__(name, health, attack_power)
        self.level = 1
        self.气息 = 10000
        self.钓点坐标 = [500,500]
        self.上个目标距离 = 1080

        self.character_class = character_class

        if character_class == "武神":
            self.skills = [
                # ... 添加更多技能
                Skill("x", 11),
                Skill("a", 8),
                Skill("s", 8),
                Skill("d", 14),
                Skill("f", 18),
                Skill("q", 8),
                Skill("w", 18),
                Skill("e", 14),
                Skill("r", 40),
                Skill("z", 30),
                Skill("v", 100),
            ]
        elif character_class == "红督":
            self.skills = [
                # ... 添加更多技能
                Skill("c", 11),
                Skill("a", 10),
                Skill("s", 30),
                Skill("d", 24),
                Skill("f", 30),
                Skill("q", 8),
                Skill("w", 18),
                Skill("e", 16),
                Skill("r", 20),
                Skill("z", 30),
                Skill("v", 100),
            ]
        elif character_class == "墨灵":
            self.skills = [
                # ... 添加更多技能
                Skill("a", 16),
                Skill("s", 24),
                Skill("d", 30),
                Skill("f", 27),
                Skill("q", 16),
                Skill("w", 36),
                Skill("e", 24),
                Skill("r", 14),
                Skill("x", 30),
                Skill("v", 100),
            ]
        elif character_class == "黑狂":
            self.skills = [
                # ... 添加更多技能
                Skill("a", 14),
                Skill("s", 18),
                Skill("d", 36),
                Skill("f", 24),
                Skill("q", 12),
                Skill("w", 24),
                Skill("e", 24),
                Skill("r", 30),
                Skill("z", 30),
                Skill("v", 100),
            ]
        elif character_class == "圣骑":
            self.skills = [
                # ... 添加更多技能
                Skill("a", 14),
                Skill("s", 18),
                Skill("d", 36),
                Skill("f", 24),
                Skill("q", 12),
                Skill("w", 24),
                Skill("e", 24),
                Skill("r", 30),
                Skill("z", 30),
                Skill("v", 100),
            ]
        self.current_time = 0

    def update(self):
        # 更新当前时间
        self.current_time = time.time()

    def use_available_skill(self):
        self.update()
        for skill in self.skills:
            if skill.is_ready(self.current_time):
                skill.last_used_time = self.current_time
                #print(f"Using skill: {skill.name}")
                return skill.name
        print("No skills are available.")
        return "c"
    def use_random_available_skill(self):
        self.update()
        for i in range(len(self.skills)):
            skill = random.choice(self.skills)
            if skill.is_ready(self.current_time):
                skill.last_used_time = self.current_time
                #print(f"Using skill: {skill.name}")
                return skill.name
        print("No skills are available.")
        return "c"

    def level_up(self):
        self.level += 1
        self.health += 10
        self.attack_power += 5
        print(f"{self.name} has leveled up to level {self.level}!")

    def 有气息(self):
        return self.气息 > 0
    def 就位确认(self):# 这里找图，找浮标，找技能栏
        print(f"{self.钓点坐标}检查当前状态，是否是待命中，还是已经下钩，技能栏是否在生活样栏")

        if 方舟模板def.查找指定图片([800, 800, 280, 280],['resources/demo/042.png'],['resources/1080/poplavok.png']):
            print("已经就位")
            return True
        else:
            #pyautogui.press('e', interval=random.uniform(0.1, 0.5))
            return False
    def 投掷钓线(self):
        pyautogui.moveTo(self.钓点坐标[0], self.钓点坐标[1])
        pyautogui.press('e', interval=random.uniform(0.1, 0.5))

        print(f"{self.name} 投掷钓线")
        # 获取当前时间戳
        current_timestamp = time.time()
        time.sleep(6)
        while not 等待上钩():
            time.sleep(0.3)  # 每秒检查一次条件
            if time.time()-current_timestamp>20:
                print(f"{self.name} 过了15秒后钓鱼失败了")
                return False
        return True

    def 收线取鱼(self):
        self.气息 -= 60
        print("收线取鱼")
        pyautogui.press('e', interval=random.uniform(0.1, 0.5))

    def 寻找目标(self,other):# 找怪物的图片  返回坐标
        other.位置 = 方舟模板def.查找指定图片返回最佳点([0, 0, 1920, 1080], ['resources/demo/033.png', 'resources/demo/046.png', 'resources/demo/060.png'])
        if other.位置:
            other.位置 = (other.位置[0] + 30, other.位置[1] + 100)  # 找到的点在血条上，要偏移到身体上
        return other.位置

    def 移动到目标(self,other):

        NowTargetDistance = 方舟模板def.和目标的距离(960,540,other.位置[0],other.位置[1])
        if NowTargetDistance < 300: #
            print("可攻击范围肉")
            return True
        else:
            print(f"移动到目标 {other.name}{other.位置} 距离{NowTargetDistance}!")
            方舟模板def.向目标移动(other.位置)
        # 结束一轮，要重新找怪了
        return False

    def 攻击目标(self,other):
        pyautogui.moveTo(other.位置[0], other.位置[1], duration=random.uniform(0.1, 0.2))
        pyautogui.press(self.use_random_available_skill(), interval=random.uniform(0.3, 0.6))
        print("正在攻击")

    def 搜索小地图(self,other):
        other.位置 = 方舟模板def.查找指定图片返回最佳点([1596, 40, 294, 256], ['resources/demo/031.png','resources/demo/053.png', 'resources/demo/037.png', 'resources/demo/059.png', 'resources/demo/058.png'])
        return other.位置

    def 搜索小地图2(self,other):
        other.位置,template_size = 方舟模板def.查找指定图片返回最佳点2([1596, 40, 294, 256], ['resources/demo/068.png','resources/demo/067.png','resources/demo/065.png','resources/demo/059.png','resources/demo/051.png','resources/demo/058.png','resources/demo/053.png', 'resources/demo/031.png'])
        if other.位置:
            other.位置 = (other.位置[0] + template_size[0]//2, other.位置[1] + template_size[1]//2)
        return other.位置

    def 搜索小地图采集物(self,other):
        other.位置,template_size = 方舟模板def.查找指定图片返回最佳点2([1596, 40, 294, 256], ['resources/demo/029.png'])
        if other.位置:
            other.位置 = (other.位置[0] + template_size[0]//2, other.位置[1] + template_size[1]//2)
        return other.位置

    def 移动到小地图目标(self, other):
        other.位置 = 方舟模板def.calculate_point_b((960, 540), (960 + (other.位置[0] - 147), 540 + (other.位置[1] - 128)), 359) # 按照小地图中心点的方向到目标的方向 在 屏幕中进行369单位的延申

        方舟模板def.向目标移动不减半(other.位置)

    def 搜索各种按钮(self,other):

        位置 = 方舟模板def.查找图片返回图片名([0, 0, 1920, 1080],['resources/demo/010.png', 'resources/demo/020.png', 'resources/demo/021.png', 'resources/demo/022.png', 'resources/demo/023.png', 'resources/demo/024.png', 'resources/demo/026.png', 'resources/demo/054.png'])
        if not 位置:return False
        if 位置 == 'resources/demo/010.png':  # 组队确认
            pyautogui.moveTo(x=1695 + random.randint(-15, 15), y=887 + random.randint(-15, 15), duration=random.uniform(0.2, 0.3))
            pyautogui.click()
        elif 位置 == 'resources/demo/020.png':  # 地牢确认
            pyautogui.moveTo(x=920 + random.randint(-15, 15), y=650 + random.randint(-15, 15), duration=random.uniform(0.2, 0.3))
            pyautogui.click()
        elif 位置 == 'resources/demo/021.png':  # 下一空间确认```
            pyautogui.moveTo(x=918 + random.randint(-15, 15), y=648 + random.randint(-15, 15), duration=random.uniform(0.2, 0.3))
            pyautogui.click()
        elif 位置 == 'resources/demo/022.png':  # 星辰确认
            pyautogui.moveTo(x=919 + random.randint(-15, 15), y=671 + random.randint(-15, 15), duration=random.uniform(0.2, 0.3))
            pyautogui.click()
        elif 位置 == 'resources/demo/023.png':  # 复活确认 ```
            pyautogui.moveTo(x=1379 + random.randint(-15, 15), y=425 + random.randint(-15, 15), duration=random.uniform(0.2, 0.3))
            pyautogui.click()
        elif 位置 == 'resources/demo/024.png':  # 地牢结束点击
            pyautogui.moveTo(x=964 + random.randint(-15, 15), y=960 + random.randint(-15, 15), duration=random.uniform(0.2, 0.3))
            pyautogui.click()
        elif 位置 == 'resources/demo/026.png':  # 星辰结束确认ESC
            pyautogui.press('esc', interval=random.uniform(0.1, 0.5))
        elif 位置 == 'resources/demo/054.png':  # 地牢结束点击
            pyautogui.moveTo(x=964 + random.randint(-15, 15), y=960 + random.randint(-15, 15), duration=random.uniform(0.2, 0.3))
            pyautogui.click()

        return True

    def 搜索图片后仅移动(self,other):
        other.位置 = 方舟模板def.查找指定图片返回最佳点([0, 0, 1920, 1080], ['resources/demo/061.png','resources/demo/062.png'])
        if other.位置:
            other.位置 = (other.位置[0] + 30, other.位置[1] + 100)  # 找到的点在血条上，要偏移到身体上
            方舟模板def.向目标移动(other.位置)
        return other.位置

    def 试验搜索小地图(self):
        DiscoveredImg = 方舟模板def.试验查找小地图指定图片([1596, 40, 294, 256],方舟模板执行.image_list2)
        if DiscoveredImg:
            #['resources/demo/068.png', 0.7, 按下某键, [参数1]，[参数2]],
            DiscoveredImg[2](DiscoveredImg[3],DiscoveredImg[4])
        return DiscoveredImg

    def 试验搜索全屏(self):
        DiscoveredImg = 方舟模板def.试验查找全屏指定图片([0, 0, 1920, 1080],方舟模板执行.image_list3)
        if DiscoveredImg:
            # image_name, image_scale, image_offset, image_method,max_loc,template_size
            # 想当去 方舟模板执行.点击目标(xy,offset)
            #['resources/demo/068.png', 0.7, 按下某键, [参数1]，[参数2]],
            DiscoveredImg[2](DiscoveredImg[3],DiscoveredImg[4])
        return DiscoveredImg

def fight(player, monster):
    while player.is_alive() and monster.is_alive():
        player.attack(monster)
        if monster.is_alive():
            monster.attack(player)
        else:
            print(f"{monster.name} has been defeated!")
            # 升级逻辑
            if player.level < 5:
                player.level_up()
        time.sleep(3)
def 开始战斗(player, monster):
    次数 =0
    while player.is_alive() and monster.is_alive():

        if player.寻找目标(monster):
            #注意 要先找屏幕血条，再找小地图，都是要找多个结果，因为可能同时有很多血条，小地图也可能有多个红点，要找最近的
            if player.移动到目标(monster):# 目标位置保存在 monster.位置
                player.攻击目标(monster)
            次数 = 0
        elif player.搜索图片后仅移动(monster) and 次数 > 2:
            print("找到下一个传送门")

        elif player.搜索各种按钮(monster) and 次数 > 6:
            time.sleep(random.uniform(2.5, 3.5))
            #print(f"没找到目标")


        elif player.搜索小地图(monster) and 次数 > 8:
            player.移动到小地图目标(monster)

        elif 次数 > 10:
            x,y = random.randint(860, 1060), random.randint(440, 640)
            pyautogui.click(x, y, clicks=1, button='right')
        else:
            次数+=1
        time.sleep(0.3)

def 开始过图(player, monster):

    if player.搜索图片后仅移动(monster):
        print("找到下一个传送门")

    elif player.搜索各种按钮(monster):
        time.sleep(random.uniform(2.5, 3.5))
        # print(f"没找到目标")
    elif player.搜索小地图(monster):
        player.移动到小地图目标(monster)
    time.sleep(0.3)

def 开始采集(player, monster):
    if player.搜索小地图采集物(monster):
        player.移动到小地图目标(monster)
        NowTargetDistance = math.sqrt((monster.位置[0] - 960) ** 2 + (monster.位置[1] - 540) ** 2)
        if player.上个目标距离 > NowTargetDistance: # 连续 并且 越来越近
            pyautogui.press('g')
        player.上个目标距离 = NowTargetDistance
#-----
def 开始试验(player, monster):

    if player.试验搜索全屏():
        return True
    elif player.试验搜索小地图():
        return True
    else:
        time.sleep(2)

#————————————————————————————
def 地牢查看小地图(player, monster):
    if player.搜索小地图2(monster):
        player.移动到小地图目标(monster)
        NowTargetDistance = math.sqrt((monster.位置[0] - 960) ** 2 + (monster.位置[1] - 540) ** 2)
        if player.上个目标距离 > NowTargetDistance: # 连续 并且 越来越近
            pyautogui.press('g')
        player.上个目标距离 = NowTargetDistance
    time.sleep(1)

def 钓鱼(player,fish):
    if player.就位确认():
        print("就位确认成功")

        # 获取当前时间戳
        current_timestamp = time.time()
        可换鱼杆 = True
        while player.有气息():

            if player.投掷钓线():
                print('成功')
                player.收线取鱼()
                current_timestamp = time.time()
            else:
                print("失败")

            if time.time()-current_timestamp>50 and 可换鱼杆:  # 换鱼杆
                print(f"过了60秒超时超时,气息耗尽也许")
                pyautogui.press('i')
                time.sleep(2)
                pyautogui.moveTo(1835, 765, duration=0.3)
                time.sleep(2)
                pyautogui.click(button='right')
                time.sleep(2)
                pyautogui.press('i')
                可换鱼杆 = False
            if time.time() - current_timestamp > 150: # 回选角色界面

                pyautogui.press('esc')
                time.sleep(2)
                pyautogui.moveTo(1252, 727, duration=0.3)
                time.sleep(2)
                pyautogui.click()
                time.sleep(2)
                pyautogui.press('enter')

            if time.time() - current_timestamp >300:  # 退游戏
                pyautogui.press('esc')
                time.sleep(25)
                pyautogui.press('esc')
                time.sleep(2)
                pyautogui.press('enter')
                print("GameOver")
                exit()
            time.sleep(random.uniform(6.5, 7.5))
    else:
        print("就位确认失败")
        time.sleep(3)

def 等待上钩(): # 这里找图，！上钩的图
    if 方舟模板def.查找指定图片([930, 455, 70, 77], ['resources/1080/bang.png'],['resources/1080/poplavok.png']):#930 455 1000 532
        print("鱼上钩了!")
        return True
    else:
        print("鱼没上钩.")
        return False

def main():
    choice = input("1打怪，2钓鱼，3不打怪，4地牢过图，5采集，6拿def当变量：")
    if choice == '1':
        choice = "打怪"
        choice2 = input("你的职业是：")
        player = Player("英雄", 500, 10, choice2)
        monster = Monster("哥布林", 300, 5)
        print(f"{choice}{choice2}进入游戏")
        time.sleep(3)  # 切到游戏里
        while player.is_alive():
            开始战斗(player, monster)
            if not monster.is_alive():
                # 游戏胜利
                print(f"Congratulations, {player.name}! You have won the game!")
                break

    elif choice == '2':
        choice = "钓鱼"
        player = Player("英雄", 500, 10, "黑狂")
        monster = Monster("哥布林", 300, 5)
        fish = Monster("鱼", 10000, 5)
        print(f"{choice} 进入游戏")
        time.sleep(3)  # 切到游戏里
        player.钓点坐标 = pyautogui.position()
        while player.有气息():
            钓鱼(player, fish)

    elif choice == '3':
        choice = "不打怪"
        player = Player("英雄", 500, 10, "武神")
        monster = Monster("哥布林", 300, 5)
        print(f"{choice}进入游戏")
        time.sleep(3)  # 切到游戏里
        while player.is_alive():
            开始过图(player, monster)
            if not monster.is_alive():
                # 游戏胜利
                print(f"Congratulations, {player.name}! You have won the game!")
                break

    elif choice == '4':
        choice = "地牢过图"
        player = Player("英雄", 500, 10, "武神")
        monster = Monster("哥布林", 300, 5)
        print(f"{choice}进入游戏")
        time.sleep(3)  # 切到游戏里
        while player.is_alive():
            地牢查看小地图(player, monster)
            if not monster.is_alive():
                # 游戏胜利
                print(f"Congratulations, {player.name}! You have won the game!")
                break

    elif choice == '5':
        choice = "采集"
        player = Player("英雄", 500, 10, "武神")
        monster = Monster("哥布林", 300, 5)
        print(f"{choice} 模式 进入游戏")
        time.sleep(3)  # 切到游戏里
        while player.is_alive():
            开始采集(player, monster)
            if not monster.is_alive():
                # 游戏胜利
                print(f"Congratulations, {player.name}! You have won the game!")
                break

    elif choice == '6':
        choice = "拿def当变量"
        player = Player("英雄", 500, 10, "武神")
        monster = Monster("哥布林", 300, 5)
        print(f"{choice} 模式 进入游戏")
        time.sleep(3)  # 切到游戏里
        while player.is_alive():
            开始试验(player, monster)
            if not monster.is_alive():
                # 游戏胜利
                print(f"Congratulations, {player.name}! You have won the game!")
                break




    print("Welcome to the RPG game! You are the hero.")
    while player.is_alive():
        fight(player, monster)
        if not monster.is_alive():
            # 游戏胜利
            print(f"Congratulations, {player.name}! You have won the game!")
            break


if __name__ == "__main__":
    main()