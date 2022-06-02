import random


AsciiArt = [r"""
```
							 ____
					 __,-~~/~    `---.
				   _/_,---(      ,    )
			   __ /        <    /   )  \___
- ------===;;;'====------------------===;;;===----- -  -
				  \/  ~"~"~"~"~"~\~"~)~"/
				  (_ (   \  (     >    \)
				   \_( _ <         >_>'
					  ~ `-i' ::>|--"
						  I;|.|.|
						 <|i::|i|`.
						(` ^'"`-' ")
```
""",
r"""
```
		  _ ._  _ , _ ._
		(_ ' ( `  )_  .__)
	  ( (  (    )   `)  ) _)
	 (__ (_   (_ . _) _) ,__)
		 `~~`\ ' . /`~~`
			  ;   ;
			  /   \
_____________/_ __ \_____________
```
""",
r"""
```
	 _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \\._                   _./  
	`` --. . , ; .--'''       
		  | |   |             
	   .-=||  | |=-.   
	   `-=#$%&%$#=-'   
		  | ;  :|     
 _____.,-#%&$@%#&#~,._____
```
""",
r"""
```
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠙⢿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣦⡀⠙⢿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣶⣦⣀⠙⢿⣦⡀⠙⢿⣿⣿⣿⣿⣿⣷⡄⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣷⣄⠙⢿⣦⡀⠙⢿⣿⣿⡿⠋⠀⠀
⠀⠀⠀⠀⣠⣴⣿⣿⣿⠿⢻⣿⣿⣿⣿⣿⣿⣿⣧⡀⠙⠛⠂⠀⠙⠋⠀⠀⠀⠀
⠀⠀⠀⢸⣿⣿⣿⡿⠁⠀⣠⣿⣿⠋⠙⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣇⠘⣿⣿⣿⣿⣷⣾⣏⣉⣿⣀⣀⢸⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣧⡈⢻⣿⣿⡿⠋⠉⠛⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣷⣄⠙⢿⣿⣷⣦⣤⣽⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢻⣿⣿⣿⣷⣄⠙⠻⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⠿⣿⣿⣿⣿⣦⣄⡉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
```
""",
"""
```

##    ## ##     ## ##    ## ######## ########  
###   ## ##     ## ##   ##  ##       ##     ## 
####  ## ##     ## ##  ##   ##       ##     ## 
## ## ## ##     ## #####    ######   ##     ## 
##  #### ##     ## ##  ##   ##       ##     ## 
##   ### ##     ## ##   ##  ##       ##     ## 
##    ##  #######  ##    ## ######## ########  

```
""",
r"""
```
  █████▒█    ██  ▄████▄   ██ ▄█▀▓█████ ▓█████▄ 
▓██   ▒ ██  ▓██▒▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▒██▀ ██▌
▒████ ░▓██  ▒██░▒▓█    ▄ ▓███▄░ ▒███   ░██   █▌
░▓█▒  ░▓▓█  ░██░▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ░▓█▄   ▌
░▒█░   ▒▒█████▓ ▒ ▓███▀ ░▒██▒ █▄░▒████▒░▒████▓ 
 ▒ ░   ░▒▓▒ ▒ ▒ ░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░ ▒▒▓  ▒ 
 ░     ░░▒░ ░ ░   ░  ▒   ░ ░▒ ▒░ ░ ░  ░ ░ ▒  ▒ 
 ░ ░    ░░░ ░ ░ ░        ░ ░░ ░    ░    ░ ░  ░ 
		  ░     ░ ░      ░  ░      ░  ░   ░    
				░                       ░      
```
""",
r"""
```
 ███▄    █  █    ██  ██ ▄█▀▓█████ ▓█████▄ 
 ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ▒██▀ ██▌
▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███   ░██   █▌
▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ ░▓█▄   ▌
▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒░▒████▓ 
░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░ ▒▒▓  ▒ 
░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░ ░ ▒  ▒ 
   ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░    ░ ░  ░ 
		 ░    ░     ░  ░      ░  ░   ░    
								   ░      
```
""",
r"""
```
 ██▀███   ██▓ ██▓███  
▓██ ▒ ██▒▓██▒▓██░  ██▒
▓██ ░▄█ ▒▒██▒▓██░ ██▓▒
▒██▀▀█▄  ░██░▒██▄█▓▒ ▒
░██▓ ▒██▒░██░▒██▒ ░  ░
░ ▒▓ ░▒▓░░▓  ▒▓▒░ ░  ░
  ░▒ ░ ▒░ ▒ ░░▒ ░     
  ░░   ░  ▒ ░░░       
   ░      ░           
					  
```
"""]

youtube = ['https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'https://www.youtube.com/watch?v=k4RMyGji1zc', 'https://www.youtube.com/watch?v=o6kKHm0UA50', 'https://www.youtube.com/watch?v=q8Rsdq3QCNM', 'https://www.youtube.com/watch?v=MnYNOfBFfHg', 'https://www.youtube.com/watch?v=MnYNOfBFfHg', 'https://www.youtube.com/watch?v=MmRj93zcEVs', 'https://www.youtube.com/watch?v=nCk1-mLNhBg', 'https://www.youtube.com/watch?v=UUa3O58D_Ts', 'https://www.youtube.com/watch?v=qJv3VdjhUCI', 'https://www.youtube.com/watch?v=67Nr4aiXzcY', 'https://www.youtube.com/watch?v=t0XjwoiDg5E']

discord_sv = ['https://discord.gg/F8eeqRh9aG', 'https://discord.gg/f7k3J8ZTRw']


settings = {"token":None,'user_id':None,"bot_status":"offline", 'prefix':None}

channel_names = ['☢️ 𝗙𝘂𝗰𝗸𝗲𝗱 𝗯𝘆 𝗔𝘆𝘂𝗹𝘆 ☢️', '☢️ 𝗥𝗜𝗣 𝗯𝘆 𝗔𝘆𝘂𝗹𝘆 ☢️', '☢️ 𝗙𝘂𝗰𝗸𝗲𝗱 𝗯𝘆 𝗔𝘆𝘂𝗹𝘆 ☢️', '☢️ 𝗡𝘂𝗸𝗲𝗱 𝗯𝘆 𝗔𝘆𝘂𝗹𝘆 ☢️', '☢️ 𝗥𝗜𝗣 𝗯𝘆 𝗔𝘆𝘂𝗹𝘆 ☢️','☢️ 𝗡𝘂𝗸𝗲𝗱 𝗯𝘆 𝗔𝘆𝘂𝗹𝘆 ☢️','☢️ 𝗙𝘂𝗰𝗸𝗲𝗱 𝗯𝘆 𝗔𝘆𝘂𝗹𝘆 ☢️']

message_spam = [f'@everyone \n☢️ 𝗡𝘂𝗸𝗲𝗱 𝗯𝘆 𝗔𝘆𝘂𝗹𝘆#𝟯𝟴𝟱𝟭 ☢️\n𝗗𝗶𝘀𝗰𝗼𝗿𝗱 𝗦𝗩: {random.choice(discord_sv)}\n𝗥𝗮𝗻𝗱𝗼𝗺 𝗩𝗶𝗱𝗲𝗼: {random.choice(youtube)}\n{random.choice(AsciiArt)}',f'@everyone \n☢️ 𝗥𝗜𝗣 𝗯𝘆 𝗔𝘆𝘂𝗹𝘆#𝟯𝟴𝟱𝟭 ☢️\n𝗗𝗶𝘀𝗰𝗼𝗿𝗱 𝗦𝗩: {random.choice(discord_sv)}\n𝗥𝗮𝗻𝗱𝗼𝗺 𝗩𝗶𝗱𝗲𝗼: {random.choice(youtube)}\n{random.choice(AsciiArt)}',f'@everyone \n☢️ 𝗙𝘂𝗰𝗸𝗲𝗱 𝗯𝘆 𝗔𝘆𝘂𝗹𝘆#𝟯𝟴𝟱𝟭 ☢️\n𝗗𝗶𝘀𝗰𝗼𝗿𝗱 𝗦𝗩: {random.choice(discord_sv)}\n𝗥𝗮𝗻𝗱𝗼𝗺 𝗩𝗶𝗱𝗲𝗼: {random.choice(youtube)}\n{random.choice(AsciiArt)}',f'@everyone \n☢️ 𝗡𝘂𝗸𝗲𝗱 𝗯𝘆 𝗔𝘆𝘂𝗹𝘆#𝟯𝟴𝟱𝟭 ☢️\n𝗗𝗶𝘀𝗰𝗼𝗿𝗱 𝗦𝗩: {random.choice(discord_sv)}\n𝗥𝗮𝗻𝗱𝗼𝗺 𝗩𝗶𝗱𝗲𝗼: {random.choice(youtube)}\n{random.choice(AsciiArt)}',f'@everyone \n☢️ 𝗥𝗜𝗣 𝗯𝘆 𝗔𝘆𝘂𝗹𝘆#𝟯𝟴𝟱𝟭 ☢️\n𝗗𝗶𝘀𝗰𝗼𝗿𝗱 𝗦𝗩: {random.choice(discord_sv)}\n𝗥𝗮𝗻𝗱𝗼𝗺 𝗩𝗶𝗱𝗲𝗼: {random.choice(youtube)}\n{random.choice(AsciiArt)}',f'@everyone \n☢️ 𝗙𝘂𝗰𝗸𝗲𝗱 𝗯𝘆 𝗔𝘆𝘂𝗹𝘆#𝟯𝟴𝟱𝟭 ☢️\n𝗗𝗶𝘀𝗰𝗼𝗿𝗱 𝗦𝗩: {random.choice(discord_sv)}\n𝗥𝗮𝗻𝗱𝗼𝗺 𝗩𝗶𝗱𝗲𝗼: {random.choice(youtube)}\n{random.choice(AsciiArt)}',f'@everyone \n☢️ 𝗡𝘂𝗸𝗲𝗱 𝗯𝘆 𝗔𝘆𝘂𝗹𝘆#𝟯𝟴𝟱𝟭 ☢️\n𝗗𝗶𝘀𝗰𝗼𝗿𝗱 𝗦𝗩: {random.choice(discord_sv)}\n𝗥𝗮𝗻𝗱𝗼𝗺 𝗩𝗶𝗱𝗲𝗼: {random.choice(youtube)}\n{random.choice(AsciiArt)}',f'@everyone \n☢️ 𝗥𝗜𝗣 𝗯𝘆 𝗔𝘆𝘂𝗹𝘆#𝟯𝟴𝟱𝟭 ☢️\n𝗗𝗶𝘀𝗰𝗼𝗿𝗱 𝗦𝗩: {random.choice(discord_sv)}\n𝗥𝗮𝗻𝗱𝗼𝗺 𝗩𝗶𝗱𝗲𝗼: {random.choice(youtube)}\n{random.choice(AsciiArt)}',f'@everyone \n☢️ 𝗙𝘂𝗰𝗸𝗲𝗱 𝗯𝘆 𝗔𝘆𝘂𝗹𝘆#𝟯𝟴𝟱𝟭 ☢️\n𝗗𝗶𝘀𝗰𝗼𝗿𝗱 𝗦𝗩: {random.choice(discord_sv)}\n𝗥𝗮𝗻𝗱𝗼𝗺 𝗩𝗶𝗱𝗲𝗼: {random.choice(youtube)}\n{random.choice(AsciiArt)}',f'@everyone \n☢️ 𝗡𝘂𝗸𝗲𝗱 𝗯𝘆 𝗔𝘆𝘂𝗹𝘆#𝟯𝟴𝟱𝟭 ☢️\n𝗗𝗶𝘀𝗰𝗼𝗿𝗱 𝗦𝗩: {random.choice(discord_sv)}\n𝗥𝗮𝗻𝗱𝗼𝗺 𝗩𝗶𝗱𝗲𝗼: {random.choice(youtube)}\n{random.choice(AsciiArt)}',f'@everyone \n☢️ 𝗥𝗜𝗣 𝗯𝘆 𝗔𝘆𝘂𝗹𝘆#𝟯𝟴𝟱𝟭 ☢️\n𝗗𝗶𝘀𝗰𝗼𝗿𝗱 𝗦𝗩: {random.choice(discord_sv)}\n𝗥𝗮𝗻𝗱𝗼𝗺 𝗩𝗶𝗱𝗲𝗼: {random.choice(youtube)}\n{random.choice(AsciiArt)}',f'@everyone \n☢️ 𝗙𝘂𝗰𝗸𝗲𝗱 𝗯𝘆 𝗔𝘆𝘂𝗹𝘆#𝟯𝟴𝟱𝟭 ☢️\n𝗗𝗶𝘀𝗰𝗼𝗿𝗱 𝗦𝗩: {random.choice(discord_sv)}\n𝗥𝗮𝗻𝗱𝗼𝗺 𝗩𝗶𝗱𝗲𝗼: {random.choice(youtube)}\n{random.choice(AsciiArt)}',f'@everyone \n☢️ 𝗡𝘂𝗸𝗲𝗱 𝗯𝘆 𝗔𝘆𝘂𝗹𝘆#𝟯𝟴𝟱𝟭 ☢️\n𝗗𝗶𝘀𝗰𝗼𝗿𝗱 𝗦𝗩: {random.choice(discord_sv)}\n𝗥𝗮𝗻𝗱𝗼𝗺 𝗩𝗶𝗱𝗲𝗼: {random.choice(youtube)}\n{random.choice(AsciiArt)}',f'@everyone \n☢️ 𝗥𝗜𝗣 𝗯𝘆 𝗔𝘆𝘂𝗹𝘆#𝟯𝟴𝟱𝟭 ☢️\n𝗗𝗶𝘀𝗰𝗼𝗿𝗱 𝗦𝗩: {random.choice(discord_sv)}\n𝗥𝗮𝗻𝗱𝗼𝗺 𝗩𝗶𝗱𝗲𝗼: {random.choice(youtube)}\n{random.choice(AsciiArt)}',f'@everyone \n☢️ 𝗙𝘂𝗰𝗸𝗲𝗱 𝗯𝘆 𝗔𝘆𝘂𝗹𝘆#𝟯𝟴𝟱𝟭 ☢️\n𝗗𝗶𝘀𝗰𝗼𝗿𝗱 𝗦𝗩: {random.choice(discord_sv)}\n𝗥𝗮𝗻𝗱𝗼𝗺 𝗩𝗶𝗱𝗲𝗼: {random.choice(youtube)}\n{random.choice(AsciiArt)}',]

webhook_names = ['☢️ 𝗙𝘂𝗰𝗸𝗲𝗱 𝗯𝘆 𝗔𝘆𝘂𝗹𝘆 ☢️', '☢️ 𝗥𝗜𝗣 𝗯𝘆 𝗔𝘆𝘂𝗹𝘆 ☢️','☢️ 𝗡𝘂𝗸𝗲𝗱 𝗯𝘆 𝗔𝘆𝘂𝗹𝘆 ☢️','Ayuly Here']