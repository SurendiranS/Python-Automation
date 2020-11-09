import os

def banner():
    os.system("clear")
    if int(choice) == 3:
        print("""
        \n
            Press 1 : To create Key-pair
            Press 2 : To Create Security Group
            Press 3 : To Launch instance
            Press 4 : To create EBS volume
            Press 5 : To Attach EBS volume to running Instance
            Press 6 : To create S3 bucket
            Press 7 : To Delete all running instances

            Press 99 : Exit!
        
        
        """)
def main():
    while True:
        banner()
        a = int(input("What would you like to do on AWS [1-99]:    "))
        if a == 1:
            key = input("Enter your Key Name:     ")
            os.system("aws ec2 create-key-pair --key-name {}".format(key))
        elif a == 2:
            sec = input("Enter your Security Group Name:     ")
            os.system("aws ec2 create-security-group --description 'ALL traffic allowed' --group-name {}".format(sec))
        elif a == 3:
            ins = input("Enter your Instance type:     ")
            count = input("Number of instances:   ")
            keyn = input("Enter your key Name:  ")
            os.system("aws ec2 run-instances --security-group-ids sg-04922d3efb38dfb56 {0} --count {1} --image-id ami-0e306788ff2473b --key-name {}".format(ins,count,keyn))
        else:
            exit()
        
