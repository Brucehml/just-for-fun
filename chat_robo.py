import random

def greeting():
    return random.choice(["你好，我是聊天机器人。", "欢迎来跟我聊天！"])

def like():
    return random.choice(["我喜欢听音乐。", "我喜欢看电影。", "我喜欢健身。"])

def hobby():
    return random.choice(["你的业余爱好是什么？", "你喜欢做什么？"])

def good_bye():
    return random.choice(["再见，祝你有一个美好的一天。", "下次再聊！"])

while True:
    user_input = input("你好，有什么可以帮您？")
    if "你好" in user_input:
        print(greeting())
    elif "喜欢" in user_input:
        print(like())
    elif "爱好" in user_input:
        print(hobby())
    elif "再见" in user_input:
        print(good_bye())
        break
    else:
        print("抱歉，我不能理解你的语言。")
    #
