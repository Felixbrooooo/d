powershell -Command "$code = @'
import json
import base64

SECRET_KEY = 'LEAK123'
TARGET_FILE = 'MtxShit.json'

try:
    with open(TARGET_FILE, 'r', encoding='utf-8') as f:
        MY_SECRET_DATA = json.load(f)

    json_str = json.dumps(MY_SECRET_DATA, separators=(',', ':'))
    scrambled = ''.join(chr(ord(c) ^ ord(SECRET_KEY[i % len(SECRET_KEY)])) for i, c in enumerate(json_str))
    safe_string = base64.b64encode(scrambled.encode('utf-8')).decode('utf-8')

    final_json_structure = {'data': safe_string}
    with open(TARGET_FILE, 'w', encoding='utf-8') as f:
        json.dump(final_json_structure, f)

    print(f'Success! {TARGET_FILE} is now fully scrambled.')
except FileNotFoundError:
    print(f'Error: Could not find the file {TARGET_FILE} in Downloads.')
except json.JSONDecodeError:
    print('Error: Your JSON file has a syntax typo and cannot be read.')
'@; [System.IO.File]::WriteAllText('auto_scramble.py', $code)"

