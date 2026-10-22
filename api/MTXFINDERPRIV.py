import json
import base64

SECRET_KEY = "LEAK123"

def load_obfuscated_json(filepath):
    # Read the valid JSON structure
    with open(filepath, "r", encoding="utf-8") as f:
        outer_data = json.load(f)
    
    # Extract the encrypted string block
    safe_string = outer_data["data"]
    
    # Reverse the base64 and XOR cipher
    scrambled = base64.b64decode(safe_string.encode('utf-8')).decode('utf-8')
    original_json_str = "".join(chr(ord(c) ^ ord(SECRET_KEY[i % len(SECRET_KEY)])) for i, c in enumerate(scrambled))
    
    # Parse back to your dictionary
    return json.loads(original_json_str)

# Load it safely in your app
my_data = load_obfuscated_json("MtxShit.json")
