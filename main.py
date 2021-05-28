import hashlib

flag = 0

print("created by: ")
print(r"""
      .o.       ooo        ooooo ooo        ooooo       .o.       ooooooooo.   
     .888.      `88.       .888' `88.       .888'      .888.      `888   `Y88. 
    .8"888.      888b     d'888   888b     d'888      .8"888.      888   .d88' 
   .8' `888.     8 Y88. .P  888   8 Y88. .P  888     .8' `888.     888ooo88P'  
  .88ooo8888.    8  `888'   888   8  `888'   888    .88ooo8888.    888`88b.    
 .8'     `888.   8    Y     888   8    Y     888   .8'     `888.   888  `88b.  
o88o     o8888o o8o        o888o o8o        o888o o88o     o8888o o888o  o888o                                                                              
                                                                               """)

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
