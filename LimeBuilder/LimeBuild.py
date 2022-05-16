import os
import time

print("""

▒█░░░ ░▀░ █▀▄▀█ █▀▀ ▒█▀▀█ █░░█ ░▀░ █░░ █▀▀▄ █▀▀ █▀▀█ 
▒█░░░ ▀█▀ █░▀░█ █▀▀ ▒█▀▀▄ █░░█ ▀█▀ █░░ █░░█ █▀▀ █▄▄▀ 
▒█▄▄█ ▀▀▀ ▀░░░▀ ▀▀▀ ▒█▄▄█ ░▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀░ ▀▀▀ ▀░▀▀""")
print("Wanna build an exe?\nInput - yes or no")
choose = input("Input: ")
if choose == "yes":
	requirements = input("Want to install all requirements?: ")
	if requirements == "yes":
		os.system("pip install pyinstaller")
		print("Now specify the path to the file...")
		cd = input("Input folder path: ")
		path = input("Input file name: ")
		time.sleep(3)
		os.system("cd " + cd)
		os.system ("pyinstaller -F " + path)
		print("Builded successfully!")
	elif requirements == "no":
		print("Now specify the path to the file...")
		cd = input("Input folder path: ")
		path = input("Input file name: ")
		time.sleep(3)
		os.system("cd " + cd)
		os.system ("pyinstaller -F " + path)
		print("Builded successfully!")
	else:
		exit(0)    
elif choose == "no":
	exit(0)

input()
