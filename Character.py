import time
import random
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