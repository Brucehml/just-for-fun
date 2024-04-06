import random
import time
def intro():
    print("欢迎来到冒险游戏！")
    print("你是一名英勇的战士，现在身处在一个神秘的世界中。")
    print("你的目标是寻找神秘的魔法宝石，并打败邪恶的魔法师。")
    print("你的旅程刚刚开始，祝你好运！")
def player_command():
    command = input("请输入你的命令：").lower()
    if command in ["look", "examine"]:
        print("你环顾四周，发现了一枚金币和一把锋利的宝剑。")
    elif command.startswith("go"):
        print("你向前走了一段路，但并没有发现任何有用的东西。")
    elif command == "sleep":
        print("你打了一个盹，感觉舒服了一些。")
        time.sleep(3)
    else:
        print("你不知道你在说什么。")

def npc_dialogue():
    print("你遇到了一个NPC，请选择你想要的对话选项：")
    dialogue = input("1. 问路\n2. 购买物品\n3. 挑战\n")
    if dialogue == "1":
        print("他告诉你去北方就能找到魔法宝石。")
    elif dialogue == "2":
        print("你购买了一些恢复药剂和强化药剂。")
    elif dialogue == "3":
        print("你和他展开了激烈的战斗！")
        time.sleep(3)
        if random.choice([True, False]):
            print("你赢了，获得了一些经验值和金币。")
        else:
            print("你输了，失去了一些生命值。")

intro()
player_command()
npc_dialogue()
