import os

main()
def banner():
    os.system("clear")
    if int(choice) == 4:
        print("""
        \n
            Press 1 : To Check docker Images 
            Press 2 : To Launch docker container
            Press 3 : To Stop docker container
            Press 4 : To Start the Stopped Container
            Press 5 : To Pull docker image from docker-hub
            Press 6 : To Create DockerFile
            Press 7 : To Delete all running docker containers

            Press 99 : Exit!
        
        
        """)
def main():
    while True:
        banner()

        d = int(input("Enter your need:  "))
        if d == 1:
            print("docker images")
            os.system("docker images")
        elif d == 2:
            name = input("Enter Name:   ")
            image = input("Enter the image name:   ")
            os.system("docker run -itd --name {0} {1}".format(name,image))
            os.system("espeak-ng 'Successfully launched conatiner' ")
        elif d == 3:
            name = input("Enter name of running container: ")
            os.system("docker stop {}".format(name))
            os.system("espeak-ng 'Conatiner Stopped' ")
        elif d == 4:
            name = input("Enter name of running container: ")
            os.system("docker start {}".format(name))
            os.system("espeak-ng 'Conatiner Started' ")
        elif d == 5:
            img = input("Enter the image to pull:   ")
            os.system("docker pulll {}".format(img))
            os.system("espeak-ng 'Imaged downloaded' ")
        elif d == 6:
            print("update soon")
        elif d == 7:
            os.system("systemctl status docker")

        else:
            exit()

