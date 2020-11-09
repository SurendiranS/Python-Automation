from os import system


def banner():
	system("clear;tput setaf 1; tput cup 3 15;tput bold;tput rev")
	print("Python Automation")
	system("tput sgr0;tput bold;tput cup 5 15 ; ")
	print("Linux Automation")
	system("tput cup 7 0;tput sgr0")


def main():
	banner()
	
	print('''
	1. Local system
	2. Remote system

	99. Back...''')
	system("tput bold;tput cup 50 0")
	print("Enter your choice [1-2]\t : ",end='')
	sys = int(input())

	if sys == 99:
		return 

	system("tput sgr0");

	banner()
	print('''
	1.  Get Network Interface Info
	2.  Ping
	3.  Start / Stop Firewall
	4.  Check Process
	5.  Shutdown / Reboot
	6.  Get Calender
	7.  Get Date
	8.  Get Calculator

	99.  To Exit.. ''')

	system("tput bold; tput cup 50 0")
	print("Enter your choice [1-8] : ",end='')
	choice = int(input())
	system("tput sgr0");

	banner()

	command = ""

	if choice == 99:
		return
	elif choice == 1:
		command = "ifconfig"
	elif choice == 2:
		temp = input("Enter the Address\t\t\t : ")
		command = "ping " + temp
	elif choice == 3:
		temp = input("Press 1 to start and 2 to stop : ")
		command = "systemctl stop firewalld" if temp == "2" else "systemctl start firewalld"
	elif choice == 4:
		command = "ps -a -u -x"
	elif choice == 5:
		temp = input("Press 1 to Reboot and 2 to Shutdown : ")
		command = "shutdown now" if choice == "2" else "reboot"
	elif choice == 6:
		command = "cal"
	elif choice == 7:
		command = "date"
	elif choice == 8:
		command = "bc"

	if sys == 1:
		system(command)
	else :
		ip = ""
		username = ""
		pas = ""
		ip = input("Enter Remote IP\t\t\t : ")
		username = input("Enter Username\t\t\t : ")
		temp  = input("\tPress 1 to use Password\n\tPress 2 to use key\nEnter Your choice\t\t : ")
		if temp == "1":
			system("ssh " + username+"@"+ip+" "+command)

		elif temp == "2":
			pas = input("Enter the location of key\t : ")
			banner()
			system("ssh " + username+"@"+ip+" -i "+pas+" " +command)

	system("tput bold; tput cup 50 0")
	input("Enter Enter key to exit..")

# main()

