import base64
import os
import random
import string

p = "./data/"

chars_for_id = string.ascii_lowercase + string.ascii_uppercase + string.digits + "_"

files = os.listdir(p)

if 'run.sh' not in files:
    print(f"Forgot to make '{p}run.sh' file")

print("base64-ing files...")
baseded = {i: base64.b64encode(open(p+i, 'rb').read()).decode() for i in files}
ids = ''.join(random.choice(chars_for_id) for _ in range(20))

def create_file(fn, b) -> str:
    return f'echo {b} | base64 -d > /tmp/{ids}/{fn}'

print("creating shell script...")
sh = f"mkdir /tmp/{ids}\n"
for base in baseded:
    sh += create_file(base, baseded[base])+'\n'
sh += f"cd /tmp/{ids}\n"
sh += "bash run.sh\n"
sh += f"rm -rdf /tmp/{ids}"
print("saved to zipped.sh...")
with open("zipped.sh", 'w') as f:
    f.write(sh)