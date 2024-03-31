import time
import random
import pyautogui
import 方舟模板def
import math
import BehaviorTreePlayer
import 方舟模板执行

#git clone https://github.com/Lanteriso/LostArkAutoPlay.git

class Skill:
    def __init__(self, name, cooldown,press_count,press_time):
        self.name = name
        self.cooldown = cooldown
        self.last_used_time = 0
        self.press_count = press_count
        self.press_time = press_time

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
        self.气息 = 100000
        self.钓点坐标 = [500,500]
        self.上个目标距离 = 1080
        self.状态 = '待命中'

        self.character_class = character_class

        if character_class == "武神":
            self.skills = [
                Skill("f1", 23, 1, 0.1),
                Skill("x", 11,1,0.1),
                Skill("a", 8,1,0.1),
                Skill("s", 8,1,0.1),
                Skill("d", 14,2,0.1),
                Skill("f", 18,1,0.1),
                Skill("q", 8,1,0.1),
                Skill("w", 18,1,0.1),
                Skill("e", 14,1,0.1),
                Skill("r", 40,1,0.1),
                Skill("z", 30,1,0.1),
                Skill("v", 100,1,0.1),
            ]
        elif character_class == "爆刀":
            self.skills = [
                Skill("a", 10,3,0.3),
                Skill("s", 5,1,0.1),
                Skill("d", 20,1,2.1),
                Skill("f", 24,1,2.1),
                Skill("q", 16,1,0.1),
                Skill("w", 15,1,0.1),
                Skill("e", 10,1,0.1),
                Skill("r", 15,1,0.1),
                Skill("z", 20,1,0.1),
                Skill("v", 100,1,0.1),
            ]
        elif character_class == "赤子":
            self.skills = [
                Skill("a", 9,3,0.3),
                Skill("s", 14,1,0.1),
                Skill("d", 24,1,2.1),
                Skill("f", 36,1,2.1),
                Skill("q", 8,2,0.3),
                Skill("w", 25,1,0.1),
                Skill("e", 30,1,0.1),
                Skill("r", 25,1,0.1),
                Skill("v", 100,1,0.1),
            ]
        elif character_class == "红督":
            self.skills = [
                # ... 添加更多技能
                Skill("f1", 20,1,0.3),
                Skill("a", 10,1,0.3),
                Skill("s", 30,1,2.3),
                Skill("d", 24,1,0.3),
                Skill("f", 30,1,2.3),
                Skill("q", 8,1,0.3),
                Skill("w", 18,1,2.3),
                Skill("e", 16,2,0.3),
                Skill("r", 20,1,0.3),
                Skill("z", 30,1,0.3),
                Skill("v", 100,1,0.3),
            ]
        elif character_class == "墨灵":
            self.skills = [
                # ... 添加更多技能
                Skill("a", 16,1,0.3),
                Skill("s", 24,1,0.3),
                Skill("d", 30,1,0.3),
                Skill("f", 27,1,0.3),
                Skill("q", 16,1,0.3),
                Skill("w", 36,1,0.3),
                Skill("e", 24,1,0.3),
                Skill("r", 14,1,0.3),
                Skill("x", 30,1,0.3),
                Skill("v", 100,1,0.3),
            ]
        elif character_class == "黑狂":
            self.skills = [
                # ... 添加更多技能
                Skill("a", 14,1,0.3),
                Skill("s", 18,2,0.3),
                Skill("d", 36,1,0.3),
                Skill("f", 24,2,0.3),
                Skill("q", 12,1,0.3),
                Skill("w", 24,1,0.3),
                Skill("e", 24,3,0.3),
                Skill("r", 30,1,0.3),
                Skill("z", 30,1,0.3),
                Skill("v", 100,1,0.3),
            ]
        elif character_class == "圣骑":
            self.skills = [
                # ... 添加更多技能
                Skill("a", 14,1,0.3),
                Skill("s", 18,1,0.3),
                Skill("d", 36,1,0.3),
                Skill("f", 24,1,0.3),
                Skill("q", 12,1,0.3),
                Skill("w", 24,1,0.3),
                Skill("e", 24,1,0.3),
                Skill("r", 30,1,0.3),
                Skill("z", 30,1,0.3),
                Skill("v", 100,1,0.3),
            ]
        elif character_class == "伞萝":
            self.skills = [
                # ... 添加更多技能
                Skill("f1", 27, 1, 0.3),
                Skill("a", 27,1,0.3),
                Skill("s", 27,1,0.3),
                Skill("d", 20,1,0.3),
                Skill("f", 18,2,0.3),
                Skill("q", 14,1,0.3),
                Skill("w", 30,1,0.3),
                Skill("e", 7,1,0.3),
                Skill("r", 7,1,0.3),
                Skill("z", 30,1,0.3),
                Skill("v", 100,1,0.3),
            ]
        elif character_class == "召唤":
            self.skills = [
                # ... 添加更多技能
                Skill("f1", 27, 1, 0.3),
                Skill("a", 24,1,0.3),
                Skill("s", 45,1,0.3),
                Skill("d", 30,1,2.3),
                Skill("f", 30,2,0.3),
                Skill("q", 20,1,0.3),
                Skill("w", 14,1,0.3),
                Skill("e", 24,1,0.3),
                Skill("r", 30,1,0.3),
                Skill("z", 15,1,0.3),
                Skill("v", 100,1,0.3),
            ]
        elif character_class == "手枪手":
            self.skills = [
                # ... 添加更多技能
                Skill("f1", 27, 1, 0.3),
                Skill("a", 10,1,0.3),
                Skill("s", 24,1,1.8),
                Skill("d", 16,1,2.3),
                Skill("f", 18,2,0.3),
                Skill("q", 8,1,0.3),
                Skill("w", 20,1,0.3),
                Skill("e", 12,2,0.3),
                Skill("r", 6,1,0.3),
                Skill("v", 100,1,0.3),
            ]
        elif character_class == "环流":
            self.skills = [
                # ... 添加更多技能
                Skill("f1", 27, 1, 0.3),
                Skill("a", 14,1,0.3),
                Skill("s", 22,1,0.3),
                Skill("d", 24,1,2.3),
                Skill("f", 28,2,0.3),
                Skill("q", 10,1,0.3),
                Skill("w", 18,1,0.3),
                Skill("e", 24,1,0.3),
                Skill("r", 16,1,0.3),
                Skill("v", 100,1,0.3),
            ]
        elif character_class == "大枪":
            self.skills = [
                # ... 添加更多技能
                Skill("f1", 27, 1, 0.3),
                Skill("a", 24,1,3.3),
                Skill("s", 20,1,2.0),
                Skill("d", 20,1,2.0),
                Skill("f", 10,1,0.3),
                Skill("q", 5,1,0.3),
                Skill("w", 12,1,0.3),
                Skill("e", 40,1,0.3),
                Skill("r", 27,1,2.0),
                Skill("v", 100,1,0.3),
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

    def use_random_available_skill2(self):
        self.update()
        for i in range(len(self.skills)):
            skill = random.choice(self.skills)
            if skill.is_ready(self.current_time):
                skill.last_used_time = self.current_time
                #print(f"Using skill: {skill.name}")
                return [skill.name,skill.cooldown,skill.press_count,skill.press_time]
        print("No skills are available.")
        return ["c",1,1,0.1]

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

    def 可以撒网(self):

        # 获取当前时间戳
        current_timestamp = time.time()
        while not 等待可撒网():
            time.sleep(0.1)  # 每秒检查一次条件
            if time.time()-current_timestamp>6:
                print(f"{self.name} 过了6秒后不可以撒网1")
                return False
        return True

    def 开始撒网(self):
        print("开始撒网")
        time.sleep(2)
        pyautogui.moveTo(self.钓点坐标[0], self.钓点坐标[1])
        pyautogui.press('d', interval=random.uniform(0.1, 0.5))

        # 获取当前时间戳
        current_timestamp = time.time()
        time.sleep(3)
        while not 撒网游戏成功2():
            if time.time()-current_timestamp>18:
                print(f"{self.name} 过了15秒后钓鱼失败了")
                return False
        return True


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

    def 攻击目标2(self):
        skills = self.use_random_available_skill2()

        for i in range(skills[2]):
            pyautogui.keyDown(skills[0])
            time.sleep(skills[3])
            pyautogui.keyUp(skills[0])

        print(f"正在攻击 {skills}")

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

def 开始战斗2(player, monster):
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

def 钓鱼撒网(player,fish):
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

                if player.可以撒网():
                    player.开始撒网()


            else:
                time.sleep(random.uniform(6.5, 7.5))
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

    else:
        print("就位确认失败")
        time.sleep(3)


def 等待可撒网():
    DiscoveredImg = 方舟模板def.试验查找全屏指定图片([0, 0, 1920, 1080], [['resources/demo/079.png', 0.7, 撒网游戏开始, [[0, 0], 'space']], ])
    return DiscoveredImg

def 等待上钩(): # 这里找图，！上钩的图
    if 方舟模板def.查找指定图片([930, 455, 70, 77], ['resources/1080/bang.png'],['resources/1080/poplavok.png']):#930 455 1000 532
        print("鱼上钩了!")
        return True
    else:
        print("鱼没上钩.")
        return False

def 撒网游戏成功():
    DiscoveredImg = 方舟模板def.试验查找全屏指定图片([500, 120, 20, 430], [['resources/1080/perfectZone.png', 0.65, 撒网游戏开始, [[0, 0], 'space']],])
    DiscoveredImg2 = 方舟模板def.试验查找全屏指定图片([516, 120, 44, 430], [['resources/1080/movingArrow.png', 0.65, 撒网游戏开始, [[0, 0], 'space']], ])

    if DiscoveredImg and DiscoveredImg2:
        print('12345', DiscoveredImg[4][0][1], DiscoveredImg2[4][0][1])
        if DiscoveredImg[4][0][1] - 18 < DiscoveredImg2[4][0][1]:  # 第一张图片的y轴和第二张的对比
            pyautogui.press('space')
            pyautogui.press('space')
    return False

def 撒网游戏成功2():
    # 读取图像
    time.sleep(0.085)
    screenshot = pyautogui.screenshot(region=(0, 0, 1920, 1080))
    for i in range(120, 550):
        pixel1 = screenshot.getpixel((510, i))
        pixel2 = screenshot.getpixel((539, i))
        if [pixel1[0], pixel1[1], pixel1[2]] == [229, 86, 8]:
            pyautogui.press('space')
            break
        if [pixel2[0], pixel2[1], pixel2[2]] == [156, 0, 0]:
            break
    return False
def 撒网游戏开始(pairs1,pairs2):
    print('11')

def 自动地牢开始(player, monster):
    BehaviorTreePlayer.RunBehaviorTree(player, monster)

def 自动地牢开始2(player, monster):
    BehaviorTreePlayer.RunBehaviorTree2(player, monster)

def main():
    choice = input("1打怪，2钓鱼，3不打怪，4地牢过图，5采集，6拿def当变量，7钓鱼S：")
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

    elif choice == '7':
        choice = "钓鱼2"
        player = Player("英雄", 500, 10, "黑狂")
        monster = Monster("哥布林", 300, 5)
        fish = Monster("鱼", 10000, 5)
        print(f"{choice} 进入游戏")
        time.sleep(3)  # 切到游戏里
        player.钓点坐标 = pyautogui.position()
        while player.有气息():
            钓鱼撒网(player, fish)

    elif choice == '8':
        choice = "自动地牢"
        choice2 = input("你的职业是：")
        player = Player("英雄", 500, 10, choice2)
        monster = Monster("哥布林", 300, 5)
        print(f"{choice} 模式 进入游戏")
        time.sleep(3)  # 切到游戏里
        while player.is_alive():
            自动地牢开始(player, monster)
            if not monster.is_alive():
                # 游戏胜利
                print(f"Congratulations, {player.name}! You have won the game!")
                break

    elif choice == '9':
        choice = "自动地牢"
        choice2 = input("你的职业是：")
        player = Player("英雄", 500, 10, choice2)
        monster = Monster("哥布林", 300, 5)
        print(f"{choice} 模式 进入游戏")
        time.sleep(3)  # 切到游戏里
        while player.is_alive():
            自动地牢开始2(player, monster)
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