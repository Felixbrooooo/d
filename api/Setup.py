import json
import base64

SECRET_KEY = "LEAKED123"
TARGET_FILE = "MtxShit.json"  # <-- Change this to your actual JSON filename

try:
    # 1. Load your original giant JSON data automatically from your file
    with open(TARGET_FILE, "r", encoding="utf-8") as f:
        MY_SECRET_DATA = json.load(f)

    # 2. Turn it into a compact text string
    json_str = json.dumps(MY_SECRET_DATA, separators=(',', ':'))

    # 3. Scramble the text characters
    scrambled = "".join(chr(ord(c) ^ ord(SECRET_KEY[i % len(SECRET_KEY)])) for i, c in enumerate(json_str))

    # 4. Turn it into clean gibberish text
    safe_string = base64.b64encode(scrambled.encode('utf-8')).decode('utf-8')

    # 5. Overwrite the file with the new scrambled format
    final_json_structure = {"data": safe_string}
    with open(TARGET_FILE, "w", encoding="utf-8") as f:
        json.dump(final_json_structure, f)

    print(f"Success! {TARGET_FILE} is now fully scrambled and ready.")

except FileNotFoundError:
    print(f"Error: Could not find the file '{TARGET_FILE}'. Make sure it's in this folder!")

