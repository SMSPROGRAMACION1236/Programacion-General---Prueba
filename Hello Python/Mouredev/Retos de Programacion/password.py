import random
import string

aledl2 =string.ascii_letters + string.digits

password = "".join(random.choice(aledl2))
for i in  range(10):
  password += random.choice(aledl2)
  print(password)
  if password.count== 8:
    break