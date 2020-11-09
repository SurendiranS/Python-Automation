from os import system

def banner():
    system("clear;tput setaf 1; tput cup 3 15;tput bold;tput rev")
    print("Python Automation")
    system("tput sgr0;tput bold;tput cup 5 15 ; ");
    print("Docker Automation")
    system("tput cup 7 0;tput sgr0")


def main():

    banner()
    print("""
        1.  To Check docker Images 
        2.  To Launch docker container
        3.  To Stop docker container
        4.  To Start the Stopped Container
        5.  To Pull docker image from docker-hub
        6.  To Create DockerFile
        7.  To Delete all running docker containers

        99.  Back...""")
    system("tput bold;tput cup 50 0")
    d = int(input("Enter your choice [1-7]: "))
    system("tput sgr0");
    
    banner()
    if d == 1:
        print("docker images")
        system("docker images")
    elif d == 2:
        name = input("Enter Name\t\t:   ")
        image = input("Enter the image name\t:   ")
        system("docker run -itd --name {0} {1}".format(name,image))
        system("espeak-ng 'Successfully launched conatiner' ")
    elif d == 3:
        name = input("Enter name of running container\t: ")
        system("docker stop {}".format(name))
        system("espeak-ng 'Conatiner Stopped' ")
    elif d == 4:
        name = input("Enter name of running container\t: ")
        system("docker start {}".format(name))
        system("espeak-ng 'Conatiner Started' ")
    elif d == 5:
        img = input("Enter the image to pullll\t:   ")
        system("docker pulll {}".format(img))
        system("espeak-ng 'Imaged downloaded' ")
    elif d == 6:
        print("update soon")
    elif d == 7:
        system("systemctl status docker")
    elif d == 99:
        return
    else:
        print("Wrong Choice...")
    system("tput bold; tput cup 50 0")
    input("Enter Enter key to exit.. ")

# main()
