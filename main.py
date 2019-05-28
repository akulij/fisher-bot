import vk_api
import time
import random
import json
from vkcoinapi import *
#import sqlite3


frazes = [". Повезёт в следующий раз!",". Попытка не пытка:)"]
token = "51a0f4676238c9c6ce3953b85de84c2278c2575237908bbcde5fb2688ee226a75e3c1daabd97a0688f401"
vk = vk_api.VkApi(token=token)
vk._auth_token()
coin = VKCoin(key = ',CpRlqItl5pQtOXUWrcBH60x58]gy9WtU#qov=_Po*EQgUlB2e', merchantId = 514689451)
coin.setShopName('FishCoin')
balancebyid = []
#lastpay=2000000000
bingo=14
now='zero'
ozerofish = ["karas","karp","lenok","amur","korop"]
# riverfish = []

# print(coin.getTransactions(1))

# pid = open('payids.json', 'r')
# pidtr = json.loads('{'+pid.read()+'}')
# pid.close()

# def usedpay(payld):
   # uspay = open('payids.json', 'a')
   # uspay.write(',"'+str(payld)+'"')
   # uspay.close()



a = open('users.json', 'r')
user = json.loads('{'+a.read()+'}')
a.close()

lpay = open('lastpayid.txt','r')
lastpay = int(lpay.read())
lpay.close()
print(lastpay)
lastpay = lastpay + 1


def upformtop():
 global listtop
 toper = open("toplist.txt","r")
 listtop = toper.read()
 toper.close()
def updatedb():
   with open("users.json", "w") as wfile:
      json.dump(user, wfile)
   with open("users.json", "r") as rfile:
      wehbndbd=rfile.read()
   with open("users.json", "w") as wowfile:
      wowfile.write(wehbndbd[1:-1])
def updatefromdb():
   a = open('users.json', 'r')
   user = json.loads('{'+a.read()+'}')
   a.close()

def updatelp():
   lip = open('lastpayid.txt','w')
   lip.write(str(lastpay))
   lip.close()



def profile(vkc,fc):
    if user[str(id)]["donater"]:
       donater=" ✅куплен!"
    else:
       donater=" ❌ не куплен!"
    return "👤Привет, "+str(vk.method("users.get", {'user_ids': id})[0]['first_name'])+" "+str(vk.method("users.get", {'user_ids': id})[0]['last_name'])+'''!
    Выбери пункт.'''
	# 💶 Монеты VKC:'''+str(vkc)+'''
	# 🀄 FishCoin:'''+str(fc)+'''
    # 🔝 Премиум донат:'''+donater #+vkc(id)
    h=0
def blnce(vkc,fc):
   return '''💶 Монеты VKC:'''+str(vkc)+'''
   🀄 FishCoin:'''+str(fc)+'''
   Выбери, что собираешься сделать с балансом:'''



def useradd(number):
   print('started creating profile to id '+str(number))
   usradd = open('users.json', 'a')
   usradd.write(',"'+str(number)+'":{"fc":100000,"vkc":1000,"fishrod":0, "sudak":0, "chuka":0, "lech":0, "yorsh":0, "som":0, "karas":0, "karp":0, "lenok":0, "amur":0, "korop":0, "semga":0, "krasnoperka":0, "treska":0, "koluga":0, "paltus":0, "losos":0, "osetr":0, "forel":0, "kambala":0, "akula":0, "fish":0, "rodhealht":0, "bonusused":0, "now":"zero","donater":0}')
   usradd.close()
   a = open('users.json', 'r')
   userid = json.loads('{'+a.read()+'}')
   user = userid
   a.close()
   print(user)

def withdraw(idl):
   money = (user[str(idl)]["vkc"])*1000
   coin.sendPayment(idl, money)
   user[str(idl)]["vkc"] = 0
   updatedb()

def vkc(idl):
	exec('idv='+idl)
	return idv
def editvk(idf, var):
    filen=idf+'.txt'
    f = open(filen,'w')
    f.write(var)
    f.close()

def getvk(idf):
    filen=str(idf)+'.txt'
    f = open(filen,'r')
    fi = f.read()
    f.close()
    return fi
def vkcout(idl):
	#print(idl)
	#print(balancebyid[idl])
	#if balancebyid[idl]>0:
	print('Send to ',idl)
	coin.sendPayment(idl, 1000)#amount)
	print('sended')
	#return "Весь баланс выведен успешно!"
	#else:
	#	print('no money!')
	#	return "Ошибка, недостаточно средств"
	h=0
def upurl():
	lastpay=lastpay-1
	return 'пополнять сюда: '+coin.getPaymentURL(1000, lastpay)
def balance(name, value):
    print(id539339322)
    dmain='id'+str(name)
    print(id539339322)
    exec(dmain+'='+dmain+'+value')
    print(id539339322)
def vkctofc(idl,amvkc,amfc):
   if user[str(idl)]['vkc'] >= amvkc:
      user[str(idl)]['vkc'] = user[str(idl)]['vkc'] - amvkc
      user[str(idl)]['fc'] = user[str(idl)]['fc'] + amfc
      updatedb()
      return 'Переведено успешно!\n'
   else:
      return 'Ошибка! На балансе Недостаточно VKCoin.\n'

def fctovkc(idl,amfc,amvkc):
   if user[str(idl)]['fc'] >= amfc:
      user[str(idl)]['fc'] = user[str(idl)]['fc'] - amfc
      user[str(idl)]['vkc'] = user[str(idl)]['vkc'] + amvkc
      updatedb()
      return 'Переведено успешно!\n'
   else:
      return 'Ошибка! На балансе недостаточно FishCoin.\n'

def selfinfo(idl):
   idl = str(idl)
   return '''Количество рыб: 
Судак: '''+str(user[idl]["sudak"])+'''
Щука: '''+str(user[idl]["chuka"])+'''
Лещь: '''+str(user[idl]["lech"])+'''
Ёрш: '''+str(user[idl]["yorsh"])+'''
Сом: '''+str(user[idl]["som"])+'''
Карась: '''+str(user[idl]["karas"])+'''
Карп: '''+str(user[idl]["karp"])+'''
Ленок: '''+str(user[idl]["lenok"])+'''
Амур: '''+str(user[idl]["amur"])+'''
Короп: '''+str(user[idl]["korop"])+'''
Всего: '''+str(user[idl]["sudak"]+user[idl]["chuka"]+user[idl]["lech"]+user[idl]["yorsh"]+user[idl]["som"]+user[idl]["karas"]+user[idl]["karp"]+user[idl]["lenok"]+user[idl]["amur"]+user[idl]["korop"])#+user[idl]["semga"]+user[idl]["krasnoperka"]+user[idl]["treska"]+user[idl]["koluga"]+user[idl]["paltus"]+user[idl]["losos"]+user[idl]["osetr"]+user[idl]["forel"]+user[idl]["kambala"]+user[idl]["akula"])
# Семга: '''+str(user[idl]["semga"])+'''
# Краснопёрка: '''+str(user[idl]["krasnoperka"])+'''
# Треска: '''+str(user[idl]["treska"])+'''
# Колуга: '''+str(user[idl]["koluga"])+'''
# Пальтус: '''+str(user[idl]["paltus"])+'''
# Лосось: '''+str(user[idl]["losos"])+'''
# Осётр: '''+str(user[idl]["osetr"])+'''
# Форель: '''+str(user[idl]["forel"])+'''
# Камбала: '''+str(user[idl]["kambala"])+'''
# Акула: '''+str(user[idl]["akula"])+'''
   h=0
# def topup():
   # tpup = open('toplist.txt','r')
def buyrod(idl, lvl, cost):
   if user[str(idl)]["fc"]>=cost:
      user[str(idl)]['fishrod'] = lvl
      user[str(idl)]["fc"] = user[str(idl)]["fc"] - cost
      if lvl == 1:
         user[str(idl)]["rodhealht"]=100
      updatedb()
      return "Удочка lvl "+str(lvl)+" кулена!"
   else:
      return "Ошибка! Недостаточно FC!"

def reprod(idl):
   if user[str(idl)]["fc"]>=500000:
      user[str(idl)]["fc"] = user[str(idl)]["fc"] - 500000
      user[str(idl)]["rodhealht"] = 100
      return "Починено!"
   else:
      return "Недостаточно FC!"
def fishsell(idl):
   idlk = str(idl)
   man = user[str(idl)]
   user[str(idl)]["sudak"]=0
   user[str(idl)]["chuka"]=0
   user[str(idl)]["lech"]=0
   user[str(idl)]["yorsh"]=0
   user[str(idl)]["som"]=0
   user[str(idl)]["karas"]=0
   user[str(idl)]["karp"]=0
   user[str(idl)]["lenok"]=0
   user[str(idl)]["amur"]=0
   user[str(idl)]["korop"]=0
   cost = int(user[idlk]["sudak"]*50100+user[idlk]["chuka"]*50000+user[idlk]["lech"]*50100+user[idlk]["yorsh"]*50000+user[idlk]["som"]*50500+user[idlk]["karas"]*50100+user[idlk]["karp"]*50000+user[idlk]["lenok"]*50100+user[idlk]["amur"]*50000+user[idlk]["korop"]*50500)
   updatedb()
   return cost
def inventory(idl):
   if user[str(idl)]["fishrod"]==0:
      return "Нету удочки"
   else:
      return "Удочка lvl "+str(user[str(idl)]["fishrod"])
def updatefish(idl):
   idlk = str(idl)
   user[idlk]["fish"] = user[idlk]["sudak"]+user[idlk]["chuka"]+user[idlk]["lech"]+user[idlk]["yorsh"]+user[idlk]["som"]+user[idlk]["karas"]+user[idlk]["karp"]+user[idlk]["lenok"]+user[idlk]["amur"]+user[idlk]["korop"]
   updatedb()

#keyboard zone start
def mkbutton(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }
menu = {
    "one_time": False,
    "buttons": [

    [mkbutton(label="🎣 Рыбалка", color="positive")],
	[mkbutton(label="🛒 Магазин", color="positive"),mkbutton(label="🏟 Рынок", color="negative")],#primary(blue) positive(green) negative(red) or default(grey)
	[mkbutton(label="🐡 Склад", color="primary"),mkbutton(label="📦 Инвентарь", color="primary")],
	# [mkbutton(label="🗺 Локации", color="primary"),mkbutton(label="💰 Баланс", color="positive"),mkbutton(label="🎁 Бонус", color="primary")],
	[mkbutton(label="💰 Баланс", color="positive"),mkbutton(label="🎁 Бонус", color="primary")],
	#[mkbutton(label="Игры", color="primary"),mkbutton(label="Донат", color="positive"),mkbutton(label="Контейнеры", color="primary")],
	[mkbutton(label="🏝 Статистика 🏝", color="default")]]
}
back = {
    "one_time": False,
    "buttons": [

    [mkbutton(label="Вернуться", color="positive")]]
}
balance = {
    "one_time": False,
    "buttons": [

    [mkbutton(label="Обмен VKCoin на FCoin", color="positive"),mkbutton(label="Внести VKCoin", color="primary")],
    [mkbutton(label="Обмен FCoin на VKCoin", color="negative"),mkbutton(label="Вывод VKCoin", color="default")],
    [mkbutton(label="🔙 Назад", color="default")]]
}

shop = {
    "one_time": False,
    "buttons": [

    [mkbutton(label="🎣 Удочки", color="primary"),mkbutton(label="Починка", color="primary")],
	# [mkbutton(label="🎏 Снасти", color="primary"),mkbutton(label="🕸 Сетка", color="negative")],
	# [mkbutton(label="🍿 Прикормка", color="negative"),mkbutton(label="🕸 Сетка", color="negative")],
    [mkbutton(label="🔙 Назад", color="default")]]
}
fishrod = {
    "one_time": False,
    "buttons": [

    [mkbutton(label="Удочка lvl1 (шанс ловли 12%) Цена:500кFC", color="primary")],
    [mkbutton(label="Удочка lvl2 (шанс 17%) Цена:1ккFC", color="primary")],
    [mkbutton(label="Удочка lvl3 (шанс 25%) Цена:2.5ккFC", color="primary")],
    [mkbutton(label="Удочка lvl4 (шанс 34%) Цена:3.3ккFC", color="primary")],
    [mkbutton(label="Удочка lvl5 (шанс 42%) Цена:4ккFC", color="primary")],
    [mkbutton(label="Удочка lvl6 (шанс 54%) Цена:5ккFC", color="primary")],
    [mkbutton(label="Удочка lvl7 (шанс 62%) Цена:10ккFC", color="primary")],
    [mkbutton(label="🔙 Назад", color="default")]]
}
chosewater = {
    "one_time": False,
    "buttons": [

    [mkbutton(label="🐟 Речка", color="primary")],
    # [mkbutton(label="🐠 Озеро", color="primary")],
    # [mkbutton(label="🐬 Море", color="primary")],
    # [mkbutton(label="🦈 Океан", color="primary")],
    [mkbutton(label="🔙 Назад", color="default")]]
}
river = {
    "one_time": False,
    "buttons": [

    [mkbutton(label="1", color="primary",payload=random.randint(1, 100)),mkbutton(label="2", color="primary",payload=random.randint(1, 100)),mkbutton(label="3", color="primary",payload=random.randint(1, 100))],
    [mkbutton(label="4", color="primary",payload=random.randint(1, 100)),mkbutton(label="5", color="primary",payload=random.randint(1, 100)),mkbutton(label="6", color="primary",payload=random.randint(1, 100))],
    [mkbutton(label="7", color="primary",payload=random.randint(1, 100)),mkbutton(label="8", color="primary",payload=random.randint(1, 100)),mkbutton(label="9", color="primary",payload=random.randint(1, 100))]]
}#3*3
ozero = {
    "one_time": False,
    "buttons": [

    [mkbutton(label="1", color="primary",payload=random.randint(1, 100)),mkbutton(label="2", color="primary",payload=random.randint(1, 100)),mkbutton(label="3", color="primary",payload=random.randint(1, 100)),mkbutton(label="4", color="primary",payload=random.randint(1, 2))],
    [mkbutton(label="5", color="primary",payload=random.randint(1, 100)),mkbutton(label="6", color="primary",payload=random.randint(1, 100)),mkbutton(label="7", color="primary",payload=random.randint(1, 100)),mkbutton(label="8", color="primary",payload=random.randint(1, 2))],
    [mkbutton(label="9", color="primary",payload=random.randint(1, 100)),mkbutton(label="10", color="primary",payload=random.randint(1, 100)),mkbutton(label="11", color="primary",payload=random.randint(1, 100)),mkbutton(label="12", color="primary",payload=random.randint(1, 2))],
    # [mkbutton(label="13", color="primary",payload=random.randint(1, 100)),mkbutton(label="14", color="primary",payload=random.randint(1, 100)),mkbutton(label="15", color="primary",payload=random.randint(1, 100)),mkbutton(label="16", color="primary",payload=random.randint(1, 2))]
    ]
}#4*4
more = {
    "one_time": False,
    "buttons": [

    [mkbutton(label="1", color="primary",payload=random.randint(1, 2)),mkbutton(label="2", color="primary",payload=random.randint(1, 2)),mkbutton(label="3", color="primary",payload=random.randint(1, 2)),mkbutton(label="4", color="primary",payload=random.randint(1, 2))],
    [mkbutton(label="5", color="primary",payload=random.randint(1, 2)),mkbutton(label="6", color="primary",payload=random.randint(1, 2)),mkbutton(label="7", color="primary",payload=random.randint(1, 2)),mkbutton(label="8", color="primary",payload=random.randint(1, 2))],
    [mkbutton(label="9", color="primary",payload=random.randint(1, 2)),mkbutton(label="10", color="primary",payload=random.randint(1, 2)),mkbutton(label="11", color="primary",payload=random.randint(1, 2)),mkbutton(label="12", color="primary",payload=random.randint(1, 2))],
    [mkbutton(label="13", color="primary",payload=random.randint(1, 2)),mkbutton(label="14", color="primary",payload=random.randint(1, 2)),mkbutton(label="15", color="primary",payload=random.randint(1, 2)),mkbutton(label="16", color="primary",payload=random.randint(1, 2))],
    [mkbutton(label="17", color="primary",payload=random.randint(1, 2)),mkbutton(label="18", color="primary",payload=random.randint(1, 2)),mkbutton(label="19", color="primary",payload=random.randint(1, 2)),mkbutton(label="20", color="primary",payload=random.randint(1, 2))],
    [mkbutton(label="21", color="primary",payload=random.randint(1, 2)),mkbutton(label="22", color="primary",payload=random.randint(1, 2)),mkbutton(label="23", color="primary",payload=random.randint(1, 2)),mkbutton(label="24", color="primary",payload=random.randint(1, 2))],]
}#6*4 error
ocean = {
    "one_time": False,
    "buttons": [

    [mkbutton(label="1", color="primary",payload=random.randint(1, 2)),mkbutton(label="2", color="primary",payload=random.randint(1, 2)),mkbutton(label="3", color="primary",payload=random.randint(1, 2)),mkbutton(label="4", color="primary",payload=random.randint(1, 2))],
    [mkbutton(label="5", color="primary",payload=random.randint(1, 2)),mkbutton(label="6", color="primary",payload=random.randint(1, 2)),mkbutton(label="7", color="primary",payload=random.randint(1, 2)),mkbutton(label="8", color="primary",payload=random.randint(1, 2))],
    [mkbutton(label="9", color="primary",payload=random.randint(1, 2)),mkbutton(label="10", color="primary",payload=random.randint(1, 2)),mkbutton(label="11", color="primary",payload=random.randint(1, 2)),mkbutton(label="12", color="primary",payload=random.randint(1, 2))],
    [mkbutton(label="13", color="primary",payload=random.randint(1, 2)),mkbutton(label="14", color="primary",payload=random.randint(1, 2)),mkbutton(label="15", color="primary",payload=random.randint(1, 2)),mkbutton(label="16", color="primary",payload=random.randint(1, 2))],
    [mkbutton(label="17", color="primary",payload=random.randint(1, 2)),mkbutton(label="18", color="primary",payload=random.randint(1, 2)),mkbutton(label="19", color="primary",payload=random.randint(1, 2)),mkbutton(label="20", color="primary",payload=random.randint(1, 2))],
    [mkbutton(label="21", color="primary",payload=random.randint(1, 2)),mkbutton(label="22", color="primary",payload=random.randint(1, 2)),mkbutton(label="23", color="primary",payload=random.randint(1, 2)),mkbutton(label="24", color="primary",payload=random.randint(1, 2))],]
}#9*4
vkcfc = {
    "one_time": False,
    "buttons": [

    [mkbutton(label="Обмен 1VKC на 2FC", color="primary")],
    [mkbutton(label="Обмен 10VKC на 20FC", color="primary")],
    [mkbutton(label="Обмен 1кVKC на 2кFC", color="primary")],
    [mkbutton(label="Обмен 100кVKC на 200кFC", color="primary")],
    [mkbutton(label="Обмен 1ккVKC на 2ккFC", color="primary")],
    [mkbutton(label="Обмен 10ккVKC на 20ккFC", color="primary")],
    [mkbutton(label="Обмен 100ккVKC на 200ккFC", color="primary")],
    [mkbutton(label="🔙 назад", color="default")]]
}
fcvkc = {
    "one_time": False,
    "buttons": [

    [mkbutton(label="Обмен 2FC на 1VKC", color="primary")],
    [mkbutton(label="Обмен 20FC на 10VKC", color="primary")],
    [mkbutton(label="Обмен 200FC на 100VKC", color="primary")],
    [mkbutton(label="Обмен 20кFC на 10кVKC", color="primary")],
    [mkbutton(label="Обмен 200кFC на 100кVKC", color="primary")],
    [mkbutton(label="Обмен 2ккFC на 1ккVKC", color="primary")],
    [mkbutton(label="Обмен 20ккFC на 10ккVKC", color="primary")],
    [mkbutton(label="Обмен 200ккFC на 100ккVKC", color="primary")],
    [mkbutton(label="🔙 назад", color="default")]]
}
statistic = {
    "one_time": False,
    "buttons": [

    [mkbutton(label="Лучшие рыбаки", color="positive")],
    [mkbutton(label="🔙 Назад", color="default")]]
}
repair = {
    "one_time": False,
    "buttons": [

    [mkbutton(label="Починить (500кFC)", color="positive")],
    [mkbutton(label="Вернуться", color="default")]]
}
splace = {
    "one_time": False,
    "buttons": [

    [mkbutton(label="Продать", color="positive")],
    [mkbutton(label="🔙 Назад", color="default")]]
}
#keyboard zone end



#messages
rivermsg = "Ты выбрал речку!\nПопади в нужную клетку и забери приз!"
ozeromsg = "Ты выбрал озеро!\nПопади в нужную клетку и забери приз!"
moremsg = "Ты выбрал море!\nПопади в нужную клетку и забери приз!"
oceanmsg = "Ты выбрал океан!\nПопади в нужную клетку и забери приз!"
#messages end



init=0
while True:
    # try:
        init=init+1
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        # print('msg')
        print(init)
        if init>4:
           init=0
           # topup()
        
        
        trs = coin.getTransactions(1)
        # if trs['response'][2]['payload']<lastpay:
                # print('///////using trs 2///////')
                # mid = trs['response'][2]['from_id']
                # user[str(mid)]['vkc'] = user[str(mid)]['vkc'] + (int(trs['response'][2]['amount']))/1000
                # updatedb()
                # updatelp()
                # vk.method("messages.send", {"peer_id": mid, "message": "Зачислено: "+str((int(trs['response'][2]['amount']))/1000)+" VKC", "random_id": random.randint(1, 2147483647)})

        # if trs['response'][1]['payload']<lastpay:
                # print('///////using trs 1///////')
                # mid = trs['response'][1]['from_id']
                # user[str(mid)]['vkc'] = user[str(mid)]['vkc'] + (int(trs['response'][1]['amount']))/1000
                # updatedb()
                # updatelp()
                # vk.method("messages.send", {"peer_id": mid, "message": "Зачислено: "+str((int(trs['response'][1]['amount']))/1000)+" VKC", "random_id": random.randint(1, 2147483647)})

        if trs['response'][0]['payload']<lastpay:
                print('///////using trs 0///////')
                mid = trs['response'][0]['from_id']
                user[str(mid)]['vkc'] = user[str(mid)]['vkc'] + (int(trs['response'][0]['amount']))/1000
                lastpay = trs['response'][0]['payload'] - 1
                updatedb()
                updatelp()
                vk.method("messages.send", {"peer_id": mid, "message": "Зачислено: "+str((int(trs['response'][0]['amount']))/1000)+" VKC", "random_id": random.randint(1, 2147483647)})

        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            print('///////do not using trs///////')
            updatefish(id)
            
            
            
            
            
            #trs = coin.getTransactions(1)
            # try:
               # wake = trs['response'][0]['payload']
               # somet = pidtr[str(wake)]
            # except Exception as E:
               # shortid = trs['response'][0]['from_id']
               # user[str(shortid)]["vkc"] = user[str(shortid)]["vkc"] + (int(trs['response'][0]['amount'])/1000)
               # print(user[str(shortid)]["vkc"])
               # usedpay(trs['response'][0]['payload'])
               # updatedb()
            # try:
               # wake = trs['response'][1]['payload']
               # somet = pidtr[str(wake)]
            # except Exception as E:
               # shortid = trs['response'][1]['from_id']
               # user[str(shortid)]["vkc"] = user[str(shortid)]["vkc"] + (int(trs['response'][1]['amount'])/1000)
               # print(user[str(shortid)]["vkc"])
               # usedpay(trs['response'][1]['payload'])
               # updatedb()
            # try:
               # wake = trs['response'][2]['payload']
               # somet = pidtr[str(wake)]
            # except Exception as E:
               # shortid = trs['response'][2]['from_id']
               # user[str(shortid)]["vkc"] = user[str(shortid)]["vkc"] + (int(trs['response'][2]['amount'])/1000)
               # print(user[str(shortid)]["vkc"])
               # usedpay(trs['response'][2]['payload'])
               # updatedb()
            # try:
               # wake = trs['response'][3]['payload']
               # somet = pidtr[str(wake)]
            # except Exception as E:
               # shortid = trs['response'][3]['from_id']
               # user[str(shortid)]["vkc"] = user[str(shortid)]["vkc"] + (int(trs['response'][3]['amount'])/1000)
               # print(user[str(shortid)]["vkc"])
               # usedpay(trs['response'][3]['payload'])
               # updatedb()
            # try:
               # wake = trs['response'][4]['payload']
               # somet = pidtr[str(wake)]
            # except Exception as E:
               # shortid = trs['response'][4]['from_id']
               # user[str(shortid)]["vkc"] = user[str(shortid)]["vkc"] + (int(trs['response'][4]['amount'])/1000)
               # print(user[str(shortid)]["vkc"])
               # usedpay(trs['response'][4]['payload'])
               # updatedb()
            
            
            try:
               vkcount = user[str(id)]["vkc"]
               fcount = user[str(id)]["fc"]
            except Exception as E:
               useradd(id)
               fa = open('users.json', 'r')
               user = json.loads('{'+fa.read()+'}')
               fa.close()
               vkcount = user[str(id)]["vkc"]
            vkcount = user[str(id)]["vkc"]
            fcount = user[str(id)]["fc"]
            print(str(messages))
            if id == 539339322 and body.lower() == "привет":
                vk.method("messages.send", {"peer_id": id, "message": "Привет!", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "📦 инвентарь":
                vk.method("messages.send", {"peer_id": id, "message": "У тебя в наличии:\n"+inventory(id), "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "🎁 бонус":
               if user[str(id)]["bonusused"]==0:
                  bonus = random.randint(1000,3000)
                  user[str(id)]["fc"] = user[str(id)]["fc"] + bonus
                  vk.method("messages.send", {"peer_id": id, "message": "Вы получили начальный бонус в размере "+str(bonus)+"FC", "random_id": random.randint(1, 2147483647)})
                  user[str(id)]["bonusused"]=1
               elif user[str(id)]["bonusused"]==1:
                  vk.method("messages.send", {"peer_id": id, "message": "Вы уже получили начальный бонус!", "random_id": random.randint(1, 2147483647)})
               else:
                  vk.method("messages.send", {"peer_id": id, "message": "Ошибка в начислении бонуса.", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "лучшие рыбаки":
                upformtop()
                vk.method("messages.send", {"peer_id": id, "message": listtop, "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "💰 баланс":
                vk.method("messages.send", {"peer_id": id, "message": blnce(vkcount,fcount), 'keyboard': str(json.dumps(balance, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "начать":
                vk.method("messages.send", {"peer_id": id, "message": profile(vkcount,fcount), 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "вернуться":
                vk.method("messages.send", {"peer_id": id, "message": profile(vkcount,fcount), 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "🔙 назад":
                vk.method("messages.send", {"peer_id": id, "message": profile(vkcount,fcount), 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
            #tabs 🏝 Статистика 🏝
            elif body.lower() == "🏝 статистика 🏝":
                updatefish(id)
                vk.method("messages.send", {"peer_id": id, "message": "Лучшие рыбаки мира, находятся в разделе 'лучшие рыбаки'\nА вот информация о тебе: "+selfinfo(id), 'keyboard': str(json.dumps(statistic, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "🐡 склад":
                #print(id+' entered in shop')
                vk.method("messages.send", {"peer_id": id, "message": selfinfo(id), 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "🏟 рынок":
                idlk=str(id)
                fishcost = str(user[idlk]["sudak"]*50100+user[idlk]["chuka"]*50000+user[idlk]["lech"]*50100+user[idlk]["yorsh"]*50000+user[idlk]["som"]*50500+user[idlk]["karas"]*50100+user[idlk]["karp"]*50000+user[idlk]["lenok"]*50100+user[idlk]["amur"]*50000+user[idlk]["korop"]*50500)
                #print(id+' entered in shop')
                vk.method("messages.send", {"peer_id": id, "message": "Это рынок! Здесь можно продавать рыбу!\nСейчас ты можешь продать всю свою рыбу за "+fishcost+"FC", 'keyboard': str(json.dumps(splace, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "продать":
                idlk=str(id)
                coster = str(user[idlk]["sudak"]*50100+user[idlk]["chuka"]*50000+user[idlk]["lech"]*50100+user[idlk]["yorsh"]*50000+user[idlk]["som"]*50500+user[idlk]["karas"]*50100+user[idlk]["karp"]*50000+user[idlk]["lenok"]*50100+user[idlk]["amur"]*50000+user[idlk]["korop"]*50500)
                # print(user[str(id)]["fc"])
                # print(coster)
                fishsell(id)
                user[str(id)]["fc"] = user[str(id)]["fc"] + int(coster)
                # print(user[str(id)]["fc"])
                updatedb()
                updatefish(id)
                vk.method("messages.send", {"peer_id": id, "message": "Вы продали всю рыбу на "+coster+"FC!", 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "🛒 магазин":
                vk.method("messages.send", {"peer_id": id, "message": "Здесь можно купить удки, снасти, сетки или корм для рыбалки", 'keyboard': str(json.dumps(shop, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "починка":
                #print(id+' entered in shop')
                vk.method("messages.send", {"peer_id": id, "message": "Здесь можно починить удочку, починка будет стоить 500кFC", 'keyboard': str(json.dumps(repair, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "починить (500кfc)":
                #print(id+' entered in shop')
                vk.method("messages.send", {"peer_id": id, "message": reprod(id), 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "🎣 удочки":
                #print(id+' entered in shop')
                vk.method("messages.send", {"peer_id": id, "message": "Удочка lvl 1 - это покупка удочки, а остальные, это лишь её улучшение.\nБаланс: "+str(fcount)+"FC", 'keyboard': str(json.dumps(fishrod, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "удочка lvl1 (шанс ловли 12%) цена:500кfc":
                #print(id+' entered in shop')
                vk.method("messages.send", {"peer_id": id, "message": buyrod(id, 1, 500000), 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                updatedb()
            elif body.lower() == "удочка lvl2 (шанс 17%) цена:1ккfc":
                if user[str(id)]["fishrod"]==1:
                   vk.method("messages.send", {"peer_id": id, "message": buyrod(id, 2, 1000000), 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                elif user[str(id)]["fishrod"]>2:
                   vk.method("messages.send", {"peer_id": id, "message": buyrod(id, 2, 1000000), 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                elif user[str(id)]["fishrod"]==2:
                   vk.method("messages.send", {"peer_id": id, "message": "У тебя уже удочка такого уровня!", 'keyboard': str(json.dumps(fishrod, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                else:
                   vk.method("messages.send", {"peer_id": id, "message": "Для покупки этой удочки у тебя должна быть удочка предыдущего уровня!", 'keyboard': str(json.dumps(fishrod, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                updatedb()
            elif body.lower() == "удочка lvl3 (шанс 25%) цена:2.5ккfc":
                if user[str(id)]["fishrod"]==2:
                   vk.method("messages.send", {"peer_id": id, "message": buyrod(id, 3, 2500000), 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                elif user[str(id)]["fishrod"]>3:
                   vk.method("messages.send", {"peer_id": id, "message": buyrod(id, 3, 2500000), 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                elif user[str(id)]["fishrod"]==3:
                   vk.method("messages.send", {"peer_id": id, "message": "У тебя уже удочка такого уровня!", 'keyboard': str(json.dumps(fishrod, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                else:
                   vk.method("messages.send", {"peer_id": id, "message": "Для покупки этой удочки у тебя должна быть удочка предыдущего уровня!", 'keyboard': str(json.dumps(fishrod, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                updatedb()
            elif body.lower() == "удочка lvl4 (шанс 34%) цена:3.3ккfc":
                if user[str(id)]["fishrod"]==3:
                   vk.method("messages.send", {"peer_id": id, "message": buyrod(id, 4, 3300000), 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                elif user[str(id)]["fishrod"]>4:
                   vk.method("messages.send", {"peer_id": id, "message": buyrod(id, 4, 3300000), 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                elif user[str(id)]["fishrod"]==4:
                   vk.method("messages.send", {"peer_id": id, "message": "У тебя уже удочка такого уровня!", 'keyboard': str(json.dumps(fishrod, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                else:
                   vk.method("messages.send", {"peer_id": id, "message": "Для покупки этой удочки у тебя должна быть удочка предыдущего уровня!", 'keyboard': str(json.dumps(fishrod, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                updatedb()
                # vk.method("messages.send", {"peer_id": id, "message": buyrod(id, 4, 3300000), 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "удочка lvl5 (шанс 42%) цена:4ккfc":
                if user[str(id)]["fishrod"]==4:
                   vk.method("messages.send", {"peer_id": id, "message": buyrod(id, 5, 4000000), 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                elif user[str(id)]["fishrod"]>5:
                   vk.method("messages.send", {"peer_id": id, "message": buyrod(id, 5, 4000000), 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                elif user[str(id)]["fishrod"]==5:
                   vk.method("messages.send", {"peer_id": id, "message": "У тебя уже удочка такого уровня!", 'keyboard': str(json.dumps(fishrod, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                else:
                   vk.method("messages.send", {"peer_id": id, "message": "Для покупки этой удочки у тебя должна быть удочка предыдущего уровня!", 'keyboard': str(json.dumps(fishrod, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                updatedb()
                # vk.method("messages.send", {"peer_id": id, "message": buyrod(id, 5, 4000000), 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "удочка lvl6 (шанс 54%) цена:5ккfc":
                if user[str(id)]["fishrod"]==5:
                   vk.method("messages.send", {"peer_id": id, "message": buyrod(id, 6, 5000000), 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                elif user[str(id)]["fishrod"]>6:
                   vk.method("messages.send", {"peer_id": id, "message": buyrod(id, 6, 5000000), 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                elif user[str(id)]["fishrod"]==6:
                   vk.method("messages.send", {"peer_id": id, "message": "У тебя уже удочка такого уровня!", 'keyboard': str(json.dumps(fishrod, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                else:
                   vk.method("messages.send", {"peer_id": id, "message": "Для покупки этой удочки у тебя должна быть удочка предыдущего уровня!", 'keyboard': str(json.dumps(fishrod, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                updatedb()
                # vk.method("messages.send", {"peer_id": id, "message": buyrod(id, 6, 5000000), 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "удочка lvl7 (шанс 62%) цена:10ккfc":
                if user[str(id)]["fishrod"]==6:
                   vk.method("messages.send", {"peer_id": id, "message": buyrod(id, 7, 10000000), 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                elif user[str(id)]["fishrod"]>7:
                   vk.method("messages.send", {"peer_id": id, "message": buyrod(id, 7, 10000000), 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                elif user[str(id)]["fishrod"]==7:
                   vk.method("messages.send", {"peer_id": id, "message": "У тебя уже удочка такого уровня!", 'keyboard': str(json.dumps(fishrod, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                else:
                   vk.method("messages.send", {"peer_id": id, "message": "Для покупки этой удочки у тебя должна быть удочка предыдущего уровня!", 'keyboard': str(json.dumps(fishrod, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                updatedb()
                # vk.method("messages.send", {"peer_id": id, "message": buyrod(id, 7, 10000000), 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "обмен vkcoin на fcoin":
                vk.method("messages.send", {"peer_id": id, "message": 'Выбери количество', 'keyboard': str(json.dumps(vkcfc, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "обмен fcoin на vkcoin":
                vk.method("messages.send", {"peer_id": id, "message": 'Выбери количество', 'keyboard': str(json.dumps(fcvkc, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
            elif body == "Обмен 10VKC на 20FC":
                vk.method("messages.send", {"peer_id": id, "message": vkctofc(id,10,20), "random_id": random.randint(1, 2147483647)})
                vkcount = user[str(id)]["vkc"]
                fcount = user[str(id)]["fc"]
                vk.method("messages.send", {"peer_id": id, "message": blnce(vkcount,fcount), "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "внести vkcoin":
                vk.method("messages.send", {"peer_id": id, "message": 'Пополняй сюда: '+coin.getPaymentURL(1000,payload=lastpay-1,free=True), 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                # lastpay=lastpay-1
            elif body.lower() == "вывод vkcoin":
                withdraw(id)
                vk.method("messages.send", {"peer_id": id, "message": 'Выведено успешно!\nОстаток VKC:0', 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "подарок":
                vkcout(id)
                vk.method("messages.send", {"peer_id": id, "message": "Подарок выдан!", 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "донат":
                #user[str(id)]["donater"]=0
                updatedb()
                vk.method("messages.send", {"peer_id": id, "message": "Для получения премиума, задонатьте 100 рублей сюда:https://www.donationalerts.com/r/kurort, написав в донате ссылку на свою страницу или свой id\n!!!Сылки отправлять без сокрашений (bit.ly vk.cc и т.д.), иначе донат не принимается!\nТакже не принимается донат на меньшую сумму, чем указано!", 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
            # elif body.lower() == "edstv8637tewvyjsts вбд":
                # updatedb()
                # vk.method("messages.send", {"peer_id": id, "message": 'Готово!', 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
            # elif body.lower() == "edstv8637tewvyjsts избд":
                # updatefromdb()
                # vk.method("messages.send", {"peer_id": id, "message": 'Готово!', 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "🎣 рыбалка":
                vk.method("messages.send", {"peer_id": id, "message": "Выбери место", 'keyboard': str(json.dumps(chosewater, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "🐟 речка":
                if user[str(id)]["rodhealht"]>=10:
                   user[str(id)]["now"] = "river"
                   vk.method("messages.send", {"peer_id": id, "message": rivermsg, 'keyboard': str(json.dumps(river, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                else:
                   vk.method("messages.send", {"peer_id": id, "message": "Почини свою удочку!", "random_id": random.randint(1, 2147483647)})
                now='river'
            elif body.lower() == "🐠 озеро":
                vk.method("messages.send", {"peer_id": id, "message": ozeromsg, 'keyboard': str(json.dumps(ozero, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                now='ozero'
            elif id == 539339322 and body.lower() == "🐬 море":
                vk.method("messages.send", {"peer_id": id, "message": moremsg, 'keyboard': str(json.dumps(more, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                now='more'
            elif id == 539339322 and body.lower() == "🦈 океан":
                vk.method("messages.send", {"peer_id": id, "message": oceanmsg, 'keyboard': str(json.dumps(ocean, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                now='ocean'
            elif body == "Обмен 1VKC на 2FC":
                vk.method("messages.send", {"peer_id": id, "message": vkctofc(id,1,2), "random_id": random.randint(1, 2147483647)})
                vkcount = user[str(id)]["vkc"]
                fcount = user[str(id)]["fc"]
                vk.method("messages.send", {"peer_id": id, "message": blnce(vkcount,fcount), "random_id": random.randint(1, 2147483647)})
            elif body == "Обмен 1кVKC на 2кFC":
                vk.method("messages.send", {"peer_id": id, "message": vkctofc(id,1000,2000), "random_id": random.randint(1, 2147483647)})
                vkcount = user[str(id)]["vkc"]
                fcount = user[str(id)]["fc"]
                vk.method("messages.send", {"peer_id": id, "message": blnce(vkcount,fcount), "random_id": random.randint(1, 2147483647)})
            elif body == "Обмен 100кVKC на 200кFC":
                vk.method("messages.send", {"peer_id": id, "message": vkctofc(id,100000,200000), "random_id": random.randint(1, 2147483647)})
                vkcount = user[str(id)]["vkc"]
                fcount = user[str(id)]["fc"]
                vk.method("messages.send", {"peer_id": id, "message": blnce(vkcount,fcount), "random_id": random.randint(1, 2147483647)})
            elif body == "Обмен 1ккVKC на 2ккFC":
                vk.method("messages.send", {"peer_id": id, "message": vkctofc(id,1000000,2000000), "random_id": random.randint(1, 2147483647)})
                vkcount = user[str(id)]["vkc"]
                fcount = user[str(id)]["fc"]
                vk.method("messages.send", {"peer_id": id, "message": blnce(vkcount,fcount), "random_id": random.randint(1, 2147483647)})
            elif body == "Обмен 10ккVKC на 20ккFC":
                vk.method("messages.send", {"peer_id": id, "message": vkctofc(id,10000000,20000000), "random_id": random.randint(1, 2147483647)})
                vkcount = user[str(id)]["vkc"]
                fcount = user[str(id)]["fc"]
                vk.method("messages.send", {"peer_id": id, "message": blnce(vkcount,fcount), "random_id": random.randint(1, 2147483647)}) #fctovkc
            elif body == "Обмен 100ккVKC на 200ккFC":
                vk.method("messages.send", {"peer_id": id, "message": vkctofc(id,100000000,200000000), "random_id": random.randint(1, 2147483647)})
                vkcount = user[str(id)]["vkc"]
                fcount = user[str(id)]["fc"]
                vk.method("messages.send", {"peer_id": id, "message": blnce(vkcount,fcount), "random_id": random.randint(1, 2147483647)}) #fctovkc
            
            elif body == "Обмен 2FC на 1VKC":
                vk.method("messages.send", {"peer_id": id, "message": fctovkc(id,2,1), "random_id": random.randint(1, 2147483647)})
                vkcount = user[str(id)]["vkc"]
                fcount = user[str(id)]["fc"]
                vk.method("messages.send", {"peer_id": id, "message": blnce(vkcount,fcount), "random_id": random.randint(1, 2147483647)}) #fctovkc
            elif body == "Обмен 20FC на 10VKC":
                vk.method("messages.send", {"peer_id": id, "message": fctovkc(id,20,10), "random_id": random.randint(1, 2147483647)})
                vkcount = user[str(id)]["vkc"]
                fcount = user[str(id)]["fc"]
                vk.method("messages.send", {"peer_id": id, "message": blnce(vkcount,fcount), "random_id": random.randint(1, 2147483647)}) #fctovkc
            elif body == "Обмен 200FC на 100VKC":
                vk.method("messages.send", {"peer_id": id, "message": fctovkc(id,200,100), "random_id": random.randint(1, 2147483647)})
                vkcount = user[str(id)]["vkc"]
                fcount = user[str(id)]["fc"]
                vk.method("messages.send", {"peer_id": id, "message": blnce(vkcount,fcount), "random_id": random.randint(1, 2147483647)}) #fctovkc
            elif body == "Обмен 20кFC на 10кVKC":
                vk.method("messages.send", {"peer_id": id, "message": fctovkc(id,20000,10000), "random_id": random.randint(1, 2147483647)})
                vkcount = user[str(id)]["vkc"]
                fcount = user[str(id)]["fc"]
                vk.method("messages.send", {"peer_id": id, "message": blnce(vkcount,fcount), "random_id": random.randint(1, 2147483647)}) #fctovkc
            elif body == "Обмен 200кFC на 100кVKC":
                vk.method("messages.send", {"peer_id": id, "message": fctovkc(id,200000,100000), "random_id": random.randint(1, 2147483647)})
                vkcount = user[str(id)]["vkc"]
                fcount = user[str(id)]["fc"]
                vk.method("messages.send", {"peer_id": id, "message": blnce(vkcount,fcount), "random_id": random.randint(1, 2147483647)}) #fctovkc
            elif body == "Обмен 2ккFC на 1ккVKC":
                vk.method("messages.send", {"peer_id": id, "message": fctovkc(id,2000000,1000000), "random_id": random.randint(1, 2147483647)})
                vkcount = user[str(id)]["vkc"]
                fcount = user[str(id)]["fc"]
                vk.method("messages.send", {"peer_id": id, "message": blnce(vkcount,fcount), "random_id": random.randint(1, 2147483647)}) #fctovkc
            elif body == "Обмен 20ккFC на 10ккVKC":
                vk.method("messages.send", {"peer_id": id, "message": fctovkc(id,20000000,10000000), "random_id": random.randint(1, 2147483647)})
                vkcount = user[str(id)]["vkc"]
                fcount = user[str(id)]["fc"]
                vk.method("messages.send", {"peer_id": id, "message": blnce(vkcount,fcount), "random_id": random.randint(1, 2147483647)}) #fctovkc
            elif body == "Обмен 200ккFC на 100ккVKC":
                vk.method("messages.send", {"peer_id": id, "message": fctovkc(id,200000000,100000000), "random_id": random.randint(1, 2147483647)})
                vkcount = user[str(id)]["vkc"]
                fcount = user[str(id)]["fc"]
                vk.method("messages.send", {"peer_id": id, "message": blnce(vkcount,fcount), "random_id": random.randint(1, 2147483647)}) #fctovkc
            else:
                print(messages)
                print('////')
                # if True:
                try:
                    win=0
                    print(messages["items"][0]["last_message"]["payload"])
                    payload = messages["items"][0]["last_message"]["payload"]
                    print('payload')
                    if True: #now=='river':
                        # if payload == '1':
                            # win=1
                    # elif now=='ozero':
                        chanse=0
                        if user[str(id)]['fishrod']==1:
                           chanse=chanse+12
                        elif user[str(id)]['fishrod']==2:
                           chanse=chanse+17
                        elif user[str(id)]['fishrod']==3:
                           chanse=chanse+25
                        elif user[str(id)]['fishrod']==4:
                           chanse=chanse+34
                        elif user[str(id)]['fishrod']==5:
                           chanse=chanse+42
                        elif user[str(id)]['fishrod']==6:
                           chanse=chanse+54
                        elif user[str(id)]['fishrod']==7:
                           chanse=chanse+62
                        elif user[str(id)]['fishrod']==0:
                           chanse=chanse+1
                        if chanse>=int(payload):
                           winfish = ozerofish[random.randint(0, 4)]
                           user[str(id)][winfish] = user[str(id)][winfish] + 1
                           user[str(id)]["rodhealht"] = user[str(id)]["rodhealht"] - 10
                           updatefish(id)
                           updatedb()
                           if winfish=="karas":
                              namefish = 'карася!'
                           elif winfish=="karp":
                              namefish = 'карпа!'
                           elif winfish=="lenok":
                              namefish = 'ленка!'
                           elif winfish=="amur":
                              namefish = 'амура!'
                           elif winfish=="korop":
                              namefish = 'коропа!'
                           vk.method("messages.send", {"peer_id": id, "message": "Ты поймал " + namefish, 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                           vk.method("messages.send", {"peer_id": id, "message": "Оставшаяся прочность твоей удочки: "+str(user[str(id)]["rodhealht"]), "random_id": random.randint(1, 2147483647)})
                        else:
                           if user[str(id)]["fishrod"]==0:
                              rodmsg=", так как ловил руками. Купи для этого удочку!"
                           else:
                              rodmsg = frazes[random.randint(0,1)]
                           vk.method("messages.send", {"peer_id": id, "message": "Ты ничего не поймал"+rodmsg, 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                        
                        # vk.method("messages.send", {"peer_id": id, "message": 'как ты сюда попал?', 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                    # elif now=='more':
                        # some=1
                        # vk.method("messages.send", {"peer_id": id, "message": 'как ты сюда попал?', 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                    # elif now=='ocean':
                        # some=1
                        # vk.method("messages.send", {"peer_id": id, "message": 'как ты сюда попал?', 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                    # else:
                        # some=1
                        # vk.method("messages.send", {"peer_id": id, "message": 'error', 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                    # if win==1:
                        # user[str(id)]["fc"]=user[str(id)]["fc"]+10000
                        # vk.method("messages.send", {"peer_id": id, "message": 'Ты выйграл!', 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                    # else:
                        # user[str(id)]["fc"]=user[str(id)]["fc"]-20000
                        # vk.method("messages.send", {"peer_id": id, "message": 'Ты проиграл!', 'keyboard': str(json.dumps(menu, ensure_ascii=False)), "random_id": random.randint(1, 2147483647)})
                except Exception as E:
                    vk.method("messages.send", {"peer_id": id, "message": "Я тебя не понимаю...", "random_id": random.randint(1, 2147483647)})

    # except Exception as E:
        # time.sleep(0.1)
        # print('Error')
