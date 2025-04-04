from pyfiglet import Figlet
figlet = Figlet()
import random
import sys
if len(sys.argv) == 1 :
    figlet.setFont(font=random.choice(figlet.getFonts()))
    s=input('')
    print(figlet.renderText(s)) 

elif sys.argv[2] in figlet.getFonts() and len(sys.argv) == 3 and sys.argv[1] == "-f" or sys.argv[1] == "--font":
    figlet.setFont(font=sys.argv[2])
    s=input('')
    print(figlet.renderText(s))

else:
    sys.exit
    print("error")