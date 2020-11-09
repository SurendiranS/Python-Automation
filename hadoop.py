from os import system


def banner():
    system("clear;tput setaf 1; tput cup 3 15;tput bold;tput rev")
    print("Python Automation")
    system("tput sgr0;tput bold;tput cup 5 15 ; ")
    print("Hadoop Automation")
    system("tput cup 7 0;tput sgr0")


def main():
    banner()
    print("""
    1.  Configure NameNode 
    2.  Configure Datanode
    3.  Configure Client

    99.  Back... """)  
    system("tput bold;tput cup 50 0")
    h = int(input("Enter your choice [1-3]: "))
    system("tput sgr0");

    banner()
    if h == 1:
        print("Configuring NameNode")
        print("\n\n")
        ip = input("Enter the IP of Namenode\t: ")
        print("Install java-jdk and hadoop software")
        system("ssh {} rpm -ivh  jdk-8u171-linux-x64.rpm hadoop-1.2.1-1.x86_64.rpm  --force".format(ip))
        print("Successfully installed all required softwares")
        print("\n\n")
        print("Configure HDFS file")
        system("ssh {} rm /etc/hadoop/hdfs-site.xml".format(ip))
        system("scp /hadoop/namenode/hdfs-site.xml {}:/etc/hadoop".format(ip))
        print("\n\n")
        print("Configure core file")
        system("ssh {} rm /etc/hadoop/core-site.xml".format(ip))
        system("scp /hadoop/namenode/core-site.xml {}:/etc/hadoop".format(ip))
        print("\n\n")
        print("Setting up dir for Connecting with datanodes")
        system("ssh {} mkdir /nn".format(ip))
        print("Directory successfully created")
        print("\n\n")
        print("Format the Namenode")
        print("hadoop namenode -format")
        system("ssh {} hadoop namenode -format".format(ip))
        print("Successfully formated the Namenode")
        print("\n\n")
        print("Start the Namenode")
        print("hadoop-daemon.sh start namenode")
        system("ssh {} hadoop-daemon.sh start namenode".format(ip))
        print("\n\n")
        print("Status of Namenode")
        print("jps")
        system("ssh {} jps".format(ip))
        print("Running Succesfully")
        print("\n\n")
    
    elif h == 2:
        print("Configuring Datanode")
        print("\n\n")
        ip = input("Enter the IP of Datanode\t:")
        print("Install java-jdk and hadoop software")
        system("ssh {} rpm -ivh  jdk-8u171-linux-x64.rpm hadoop-1.2.1-1.x86_64.rpm  --force".format(ip))
        print("Successfully installed all required softwares")
        print("\n\n")
        print("Configure HDFS file")
        system("ssh {} rm /etc/hadoop/hdfs-site.xml".format(ip))
        system("scp /hadoop/datanode/hdfs-site.xml {}:/etc/hadoop".format(ip))
        print("\n\n")
        print("Configure core file")
        system("ssh {} rm /etc/hadoop/core-site.xml".format(ip))
        system("scp /hadoop/datanode/core-site.xml {}:/etc/hadoop".format(ip))
        print("\n\n")
        print("Setting up dir for datanode")
        system("ssh {} mkdir /dn1".format(ip))
        print("Directory successfully created")
        print("\n\n")
        print("Start the Datanode")
        print("hadoop-daemon.sh start datanode")
        system("ssh {} hadoop-daemon.sh start datanode".format(ip))
        print("\n\n")
        print("Status of Datanode")
        print("jps")
        system("ssh {} jps".format(ip))
        print("Running Succesfully")
        print("\n\n")
    
    elif h == 3:
        print("Configuring Client")
        ip = input("Enter the IP of Client\t: ")
        print("Install java-jdk and hadoop software")
        system("ssh {} rpm -ivh  jdk-8u171-linux-x64.rpm hadoop-1.2.1-1.x86_64.rpm  --force".format(ip))
        print("Successfully installed all required softwares")
        print("\n\n")
        print("Configure HDFS file")
        system("ssh {} rm /etc/hadoop/hdfs-site.xml".format(ip))
        system("scp /hadoop/client/hdfs-site.xml {}:/etc/hadoop".format(ip))
        print("\n\n")
        print("Configure core file")
        system("ssh {} rm /etc/hadoop/core-site.xml".format(ip))
        system("scp /hadoop/client/core-site.xml {}:/etc/hadoop".format(ip))
        print("Configured successfully")
        print("\n\n")
    elif h == 99:
        return
    else:
        print("Wrong Choice...")
    system("tput bold; tput cup 50 0")
    input("Enter Enter key to exit.. ")

# main()
