import base64

with open("backdoor.py", "r") as f:
    code = f.read()

encoded_code = base64.b64encode(code.encode()).decode()
print(encoded_code)