from os import system
import linux
import hadoop
import aws
import docker
import machineLearning

# Banner 
system("clear;tput setaf 1; tput cup 3 15;tput bold;tput rev");
print("Python Automation")
system("tput sgr0;tput bold;tput cup 5 17 ; ");
print("Main Menu")
system("tput sgr0");


#main menu
print('''
	1.  Basic Linux command Automation
	2.  Hadoop Automation
	3.  AWS-CLI Automation
	4.  Docker Automation
	5.  Machine Learning''')

system("tput bold")
print("\n\n\nEnter your choice [1-5] : ",end='')

choice = int(input())
if choice == 1:
	linux.main()
elif choice == 2:
	hadoop.main()
elif choice == 3:
	aws.main()
elif choice == 4:
	docker.main()
elif choice == 5:
	machineLearning.main()
