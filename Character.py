import time
import random

class Skill:
    def __init__(self, name, cooldown,press_count,press_time):
        self.name = name
        self.cooldown = cooldown
        self.last_used_time = 0
        self.press_count = press_count
        self.press_time = press_time

    def is_ready(self, current_time):
        return current_time - self.last_used_time >= self.cooldown


allskills = {
    '默认': [
            Skill("x", 10,1,0.3),
            Skill("a", 10,1,0.3),
            Skill("s", 10,1,0.3),
            Skill("d", 10,1,0.3),
            Skill("f", 10,1,0.3),
            Skill("q", 10,1,0.3),
            Skill("w", 10,1,0.3),
            Skill("e", 10,1,0.3),
            Skill("r", 10,1,0.3),
            Skill("z", 10,1,0.3),
            Skill("v", 100,1,0.3),
            ],
    '武神': [
            Skill("x", 11, 1, 0.3),
            Skill("a", 8, 1, 0.3),
            Skill("s", 8, 1, 0.3),
            Skill("d", 14, 2, 0.3),
            Skill("f", 18, 1, 0.3),
            Skill("q", 8, 1, 0.3),
            Skill("w", 18, 1, 0.3),
            Skill("e", 14, 1, 0.3),
            Skill("r", 40, 1, 0.3),
            Skill("z", 30, 1, 0.3),
            Skill("v", 100, 1, 0.3),
           ],
    '爆刀': [
        Skill("a", 10, 3, 0.3),
        Skill("s", 5, 1, 0.1),
        Skill("d", 20, 1, 2.1),
        Skill("f", 24, 1, 2.1),
        Skill("q", 16, 1, 0.1),
        Skill("w", 15, 1, 0.1),
        Skill("e", 10, 1, 0.1),
        Skill("r", 15, 1, 0.1),
        Skill("z", 20, 1, 0.1),
        Skill("v", 100, 1, 0.1),
    ],
    '赤子': [
        Skill("a", 9, 3, 0.3),
        Skill("s", 14, 1, 0.3),
        Skill("d", 24, 1, 2.1),
        Skill("f", 36, 1, 2.1),
        Skill("q", 8, 2, 0.3),
        Skill("w", 25, 1, 0.3),
        Skill("e", 30, 1, 0.3),
        Skill("r", 25, 1, 0.3),
        Skill("v", 100, 1, 0.3),
    ],
    '红督': [
        Skill("a", 10, 1, 0.3),
        Skill("s", 30, 1, 2.3),
        Skill("d", 24, 1, 0.3),
        Skill("f", 30, 1, 2.3),
        Skill("q", 8, 1, 0.3),
        Skill("w", 18, 1, 2.3),
        Skill("e", 16, 2, 0.3),
        Skill("r", 20, 1, 0.3),
        Skill("z", 30, 1, 0.3),
        Skill("v", 100, 1, 0.3),
    ],
    '墨灵': [
        Skill("a", 16, 1, 0.3),
        Skill("s", 24, 1, 0.3),
        Skill("d", 30, 1, 0.3),
        Skill("f", 27, 1, 0.3),
        Skill("q", 24, 1, 0.3),
        Skill("w", 24, 1, 0.3),
        Skill("e", 30, 1, 0.3),
        Skill("r", 25, 1, 0.3),
        Skill("x", 30, 1, 0.3),
        Skill("v", 100, 1, 0.3),
    ],
    '黑狂': [
        Skill("a", 16, 1, 0.3),
        Skill("s", 24, 1, 0.3),
        Skill("d", 30, 1, 0.3),
        Skill("f", 27, 1, 0.3),
        Skill("q", 24, 1, 0.3),
        Skill("w", 24, 1, 0.3),
        Skill("e", 30, 1, 0.3),
        Skill("r", 25, 1, 0.3),
        Skill("x", 30, 1, 0.3),
        Skill("v", 100, 1, 0.3),
    ],
    '伞萝': [
        Skill("a", 27, 1, 0.3),
        Skill("s", 27, 1, 0.3),
        Skill("d", 20, 1, 0.3),
        Skill("f", 18, 2, 0.3),
        Skill("q", 14, 1, 0.3),
        Skill("w", 30, 1, 0.3),
        Skill("e", 7, 1, 0.3),
        Skill("r", 7, 1, 0.3),
        Skill("z", 30, 1, 0.3),
        Skill("v", 100, 1, 0.3),
    ],
    '召唤': [
        Skill("a", 24, 1, 0.3),
        Skill("s", 45, 1, 0.3),
        Skill("d", 30, 1, 2.3),
        Skill("f", 30, 2, 0.3),
        Skill("q", 20, 1, 0.3),
        Skill("w", 14, 1, 0.3),
        Skill("e", 24, 1, 0.3),
        Skill("r", 30, 1, 0.3),
        Skill("z", 15, 1, 0.3),
        Skill("v", 100, 1, 0.3),
    ],
    '手枪手': [
        Skill("a", 10, 1, 0.3),
        Skill("s", 24, 1, 1.8),
        Skill("d", 16, 1, 2.3),
        Skill("f", 18, 2, 0.3),
        Skill("q", 8, 1, 0.3),
        Skill("w", 20, 1, 0.3),
        Skill("e", 12, 2, 0.3),
        Skill("r", 6, 1, 0.3),
        Skill("v", 100, 1, 0.3),
    ],
    '环流': [
        Skill("a", 14, 1, 0.3),
        Skill("s", 22, 1, 0.3),
        Skill("d", 24, 1, 2.3),
        Skill("f", 28, 2, 0.3),
        Skill("q", 10, 1, 0.3),
        Skill("w", 18, 1, 0.3),
        Skill("e", 24, 1, 0.3),
        Skill("r", 16, 1, 0.3),
        Skill("v", 100, 1, 0.3),
    ],
    '大枪': [
        Skill("a", 24, 1, 3.3),
        Skill("s", 20, 1, 2.0),
        Skill("d", 20, 1, 2.0),
        Skill("f", 10, 1, 0.3),
        Skill("q", 5, 1, 0.3),
        Skill("w", 8, 1, 0.3),
        Skill("e", 40, 1, 0.3),
        Skill("r", 27, 1, 2.0),
        Skill("v", 100, 1, 0.3),
    ],
    '气功': [
        Skill("a", 24, 1, 0.3),
        Skill("s", 20, 1, 0.3),
        Skill("d", 16, 1, 0.3),
        Skill("f", 30, 1, 0.3),
        Skill("q", 12, 1, 0.3),
        Skill("w", 20, 1, 0.3),
        Skill("e", 8, 3, 0.3),
        Skill("r", 16, 1, 0.3),
        Skill("v", 100, 1, 0.3),
    ],
    '枪术': [
        Skill("a", 18, 1, 0.3),
        Skill("s", 20, 3, 0.3),
        Skill("d", 30, 1, 0.3),
        Skill("f", 24, 3, 0.3),
        Skill("q", 10, 1, 0.3),
        Skill("w", 10, 1, 0.3),
        Skill("e", 10, 1, 0.3),
        Skill("r", 15, 1, 0.3),
        Skill("v", 100, 1, 3.3),
    ],
    '霸拳': [
        Skill("a", 5, 1, 0.3),
        Skill("s", 16, 1, 0.3),
        Skill("d", 18, 1, 0.3),
        Skill("f", 16, 2, 0.5),
        Skill("q", 8, 1, 0.3),
        Skill("w", 10, 1, 0.3),
        Skill("e", 24, 1, 0.3),
        Skill("r", 16, 1, 2.3),
        Skill("v", 100, 1, 3.3),
    ],
    '大锤': [
        Skill("a", 18, 1, 2.8),
        Skill("s", 30, 2, 0.5),
        Skill("d", 24, 1, 0.3),
        Skill("f", 30, 1, 0.3),
        Skill("q", 5, 1, 0.3),
        Skill("w", 12, 1, 0.3),
        Skill("e", 10, 1, 0.3),
        Skill("r", 30, 1, 0.3),
        Skill("v", 100, 1, 3.3),
    ],
    '鹰眼': [
        Skill("a", 10, 1, 0.3),
        Skill("s", 12, 1, 0.3),
        Skill("d", 30, 1, 1.8),
        Skill("f", 24, 1, 0.8),
        Skill("q", 18, 1, 0.3),
        Skill("w", 12, 1, 0.3),
        Skill("e", 20, 1, 0.3),
        Skill("r", 20, 1, 0.3),
        Skill("z", 10, 1, 0.3),
        Skill("v", 100, 1, 3.3),
    ],
    '圣骑': [
        Skill("a", 12, 1, 0.8),
        Skill("s", 18, 2, 0.8),
        Skill("d", 27, 1, 0.8),
        Skill("f", 36, 1, 0.8),
        Skill("q", 18, 1, 0.8),
        Skill("w", 24, 1, 0.8),
        Skill("e", 27, 1, 0.8),
        Skill("r", 30, 1, 0.8),
        Skill("z", 50, 1, 0.8),
        Skill("v", 100, 1, 0.8),
    ],
    '诗人': [
        Skill("a", 18, 2, 0.8),
        Skill("s", 30, 1, 0.8),
        Skill("d", 30, 1, 0.8),
        Skill("f", 24, 1, 0.8),
        Skill("q", 24, 1, 0.8),
        Skill("w", 16, 1, 0.8),
        Skill("e", 24, 1, 0.8),
        Skill("r", 12, 1, 0.8),
        Skill("x", 50, 1, 0.8),
        Skill("v", 100, 1, 0.8),
    ],
}


class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

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

        self.character_class = character_class

        if character_class == "武神":
            self.skills = [
                # ... 添加更多技能
                Skill("x", 11,1,0.3),
                Skill("a", 8,1,0.3),
                Skill("s", 8,1,0.3),
                Skill("d", 14,1,0.3),
                Skill("f", 18,1,0.3),
                Skill("q", 8,1,0.3),
                Skill("w", 18,1,0.3),
                Skill("e", 14,1,0.3),
                Skill("r", 40,1,0.3),
                Skill("z", 30,1,0.3),
                Skill("v", 100,1,0.3),
            ]
        elif character_class == "红督":
            self.skills = [
                # ... 添加更多技能
                Skill("c", 11,1,0.3),
                Skill("a", 10,1,0.3),
                Skill("s", 30,1,0.3),
                Skill("d", 24,1,0.3),
                Skill("f", 30,1,0.3),
                Skill("q", 8,1,0.3),
                Skill("w", 18,1,0.3),
                Skill("e", 16,1,0.3),
                Skill("r", 20,1,0.3),
                Skill("z", 30,1,0.3),
                Skill("v", 100,1,0.3),
            ]

        self.current_time = 0
    def update(self):
        # 更新当前时间
        self.current_time = time.time()

    def use_random_available_skill(self):
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

class Skill:
    def __init__(self, name, cooldown,press_count,press_time):
        self.name = name
        self.cooldown = cooldown
        self.last_used_time = 0
        self.press_count = press_count
        self.press_time = press_time

    def is_ready(self, current_time):
        return current_time - self.last_used_time >= self.cooldown

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

def main():
    player = Player("Hero", 500, 10,'武神')
    monster = Monster("Goblin", 300, 5)

    print("Welcome to the RPG game! You are the hero.")
    while player.is_alive():
        fight(player, monster)
        if not monster.is_alive():
            # 游戏胜利
            print(f"Congratulations, {player.name}! You have won the game!")
            break


if __name__ == "__main__":
    main()