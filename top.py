import json
import time
import vk_api
token = "51a0f4676238c9c6ce3953b85de84c2278c2575237908bbcde5fb2688ee226a75e3c1daabd97a0688f401"
vk = vk_api.VkApi(token=token)
vk._auth_token()
# k = {
    # "347639": {
        # "fc": 7980123,
        # "vkc": 1000000,
        # "fishrod": 3,
        # "fish": 1
    # },
    # "34896586": {
        # "fc": 100000,
        # "vkc": 1000,
        # "fishrod": 0,
        # "fish": 178
    # },
    # "9836531": {
        # "fc": 20000000,
        # "vkc": 10000000.0,
        # "fishrod": 0,
        # "fish": 334
    # }}
def get_bn(data):
    bn = max(data.values(), key=lambda x: x[sortby])
    return list(data.keys())[list(data.values()).index(bn)]
while True:
 f = open('users.json','r')
 user = f.read()
 usr = json.loads('{'+user+'}')
 f.close()
 sortby='fish'





 top1 = get_bn(usr)
 print(top1)
 top1name = str(vk.method("users.get", {'user_ids': top1})[0]['first_name'])+" "+str(vk.method("users.get", {'user_ids': top1})[0]['last_name'])
 top1fish = usr[str(top1)]["fish"]
 usr[str(top1)][sortby] = 0
 top1x = "[id"+top1+"|"+str(top1name)+"]"
 
 
 
 top2 = get_bn(usr)
 print(top2)
 top1name = str(vk.method("users.get", {'user_ids': top2})[0]['first_name'])+" "+str(vk.method("users.get", {'user_ids': top2})[0]['last_name'])
 top2fish = usr[str(top2)]["fish"]
 usr[str(top2)][sortby] = 0
 top2x = "[id"+top1+"|"+str(top1name)+"]"
 
 
 top3 = get_bn(usr)
 top3fish = usr[str(top3)]["fish"]
 print(top3)
 top1name = str(vk.method("users.get", {'user_ids': top3})[0]['first_name'])+" "+str(vk.method("users.get", {'user_ids': top3})[0]['last_name'])
 usr[str(top3)][sortby] = 0
 top3x = "[id"+top1+"|"+str(top1name)+"]"
 
 
 
 
 print('e')
 topel ='Cамые лучшие рыбаки:\n1 место: '+top1x+" Рыб: "+str(top1fish)+'\n2 место: '+top2x+" Рыб: "+str(top2fish)+'\n3 место: '+top3x+" Рыб: "+str(top3fish)+'\nТоп 1 даётся 6% банка, топ 2 3% банка, а топ 3 даётся 1,5% банка!\nПопробуй и ты попасть в топ!'
 print('q')
# topin = open("toplist.txt", "w")
# topal.write(topel)
# topal.close()

 a = open('toplist.txt','w')
 a.write(topel)
 a.close()
 time.sleep(5)
