import sys 
import random
import hashlib
import hmac
import secrets
import unicodedata
if len(sys.argv)>3 and len(sys.argv)%2==0:
    print()
    print("Game\n ") 
    i=1
    s=len(sys.argv)
    print("Change the Number:")
    while i<s:
        print(i, ") ", sys.argv[i])
        i+=1
    def game():
            randomNumber=secrets.token_bytes(16)
            app=random.randint(1,s-1)
            h=hmac.new(str(randomNumber).encode("utf-8"),str(app).encode("utf-8"), hashlib.sha3_256).hexdigest()
            print("HMAC: ", h)
            x=int(input("Write the Number:\n> "))
            print("Key: " , randomNumber)
            if x>0 and x<s:
                print("Your choise is ", sys.argv[x]) 
                k=1
                while k<s:
                    if app==k:
                        cc=sys.argv[k]
                        print("Opponent choise is ", cc) 
                        v=sys.argv.index(cc)
                        if x<v:
                             if  v>(s-2)/2 and x<=(s-2)/2-(s-1-v):
                                print("You lose!\n")
                             else:
                                print("You win!\n")  
                        elif x>v:
                             if v>=1 and v<=(s-2)/2-(s-1-x) and x>=(s-2)/2+1:
                                 print("You win!\n") 
                             else:
                                 print("You lose!\n")
                        else:
                            print("Draw!\n") 
                                         
                    k+=1           
            else:
                print("Enter a number from 1 to ", s-1 ) 
                print()
  
    while 1==1:  
          game()


         
      
  
  