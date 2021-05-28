import hashlib

flag = 0

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

print("created by: yaah")
print(G+r"""
 ____   _    ____ ____     ____ ____      _    ____ _  __
|  _ \ / \  / ___/ ___|   / ___|  _ \    / \  / ___| |/ /
| |_) / _ \ \___ \___ \  | |   | |_) |  / _ \| |   | ' /
|  __/ ___ \ ___) |__) | | |___|  _ <  / ___ \ |___| . \
|_| /_/   \_\____/____/___\____|_| \_\/_/   \_\____|_|\_\
                     |_____|                                                                               """+W)
print('\n' + G + '[>]' + C + ' Created By : ' + R + '®YAAH™'+C)
print(G+"________________________________________________________"+W)
pass_hash = input("Enter md5 hash; ")

wordlist = input("File name: ")

try:
  pass_file = open (wordlist, "r")
except:
  print("File Not Found")
  quit()

for word in pass_file:

  enc_wrd = word.encode('utf-8')
  digest = hashlib.md5(enc_wrd.strip()).hexdigest()

  if digest == pass_hash:
    print("password found")
    print("password is" +word)
    flag = 1
    break

if flag == 0:
  print("password/passphrase is not in the list")
