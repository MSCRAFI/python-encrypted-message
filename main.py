# Using random to create random text and num
import random
import random as r
def main():
 alphaChars=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 randomChars=[]
 randomNum=random.randint(3,3)
 # print(randomNum)
 for i in range(randomNum):
  randomChars.append(r.choice(alphaChars))
 randomWrd="".join(randomChars)
 # Giving choice of encode or decode
 getChoice=input("Do you want to Encode or Decode.\n1. Code\n2. Decode\n>> ")
 if int(getChoice)==1:
  # Getting text using input for code
  txt=input("Enter a text to encode it:\n>> ")
  # Using split to seperate the words from sentence
  split_wrd=txt.lower().split()
  # Reversing the words
  reverse_splt_wrd=["".join(reversed(word)) for word in split_wrd]
  # Adding random words on reversed words
  for i in range(len(reverse_splt_wrd)):
   reverse_splt_wrd[i]=randomWrd+reverse_splt_wrd[i]+randomWrd
  print("Below is your encoded words:")
  print(">>"," ".join(reverse_splt_wrd))
  # Choice for continue this program
  conProgram=input("Do you want to continue this program? Enter 'Y' or 'N':\n>> ")
  if conProgram=="Y" or conProgram=="y":
   main()
  elif conProgram=="N" or conProgram=="n":
   exit()
  else:
   print("Invalid value. Please enter 'Y' or 'N'.")
 elif int(getChoice)==2:
  # Getting text using input for decode
  txt=input("Enter a text to decode it:\n>> ")
  # Using split to seperate the words from sentence
  split_wrd=txt.lower().split()
  # Adding random words on reversed words
  for i in range(len(split_wrd)):
   split_wrd[i]=split_wrd[i].replace(split_wrd[i][:3],"")
  # Reversing the words
  reverse_splt_wrd=["".join(reversed(word)) for word in split_wrd]
  print("Below is your decoded words:")
  print(">>"," ".join(reverse_splt_wrd))
  # Choice for continue this program
  conProgram=input("Do you want to continue this program? Enter 'Y' or 'N':\n>> ")
  if conProgram=="Y" or conProgram=="y":
   main()
  elif conProgram=="N" or conProgram=="n":
   exit()
  else:
   print("Invalid value. Please enter 'Y' or 'N'.")
 else:
  print("Invalid Choice. Please choose between 1 or 2.")
  main()
main()