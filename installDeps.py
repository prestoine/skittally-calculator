import os

print("starting install...")
if os.name == "nt":
  os.system("pip install tk")
else:
  os.system("pip install tk --break-system-packages")
print("done!")
