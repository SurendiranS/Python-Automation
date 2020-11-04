from os import system
import linux
import hadoop
import aws

system("clear;tput setaf 1; tput cup 3 15;tput bold;tput rev");
print("Python Automation")
system("tput sgr0;tput bold;tput cup 5 17 ; ");
print("Main Menu")
system("tput sgr0");
print('''
	1.  Basic Linux command Automation
	2.  Hadoop Automation
	3.  AWS-CLI Automation''')
system("tput bold")
print("\n\n\nEnter your choice [1-3] : ",end='')


choice = int(input())
if choice == 1:
	linux.main()
elif choice == 2:
	hadoop.main()
elif choice == 3:
	aws.main()


