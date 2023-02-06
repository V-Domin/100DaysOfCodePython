from datetime import datetime

now = datetime.now().time()
print(now.strftime("%X"))