import os
import getpass
os.system("tput setaf 5")
print("\t\t\tWelcome to my menu")
os.system("tput setaf 3")

passwd=getpass.getpass("Enter ur password:")
if passwd != "arth":
	print("password incorrect")
	exit()

while True:
	print("""		Select ur choice:
\n1.RAM check\n2.Harddisk storage check\n3.CPU status\n4.Disk space storage\n5.List all the files and directories\n6.Hadoop\n7.AWS\n8.To exit """)


	os.system("tput setaf 4")
	ch = input("Select ur choice : ")
	if int(ch)==1:
        	os.system("free -m")
	elif int(ch) == 2:
		os.system("fdisk -l")
	elif int(ch) == 3:
		os.system("lscpu")
	elif int(ch) == 4:
		os.system("df -h")
	elif int(ch) == 5:
		os.system("ls -l")
		print()
		print('1. Create a new file')
		print('2. Create a new directory')
		print('3. Remove a file or directory')
		print('4. Access file or directory')
		print('5. No function to perform or Exit')
		d = (int)(input("Enter ur choice: "))
		if(d == 5):
		    print('EXITING FUNCTION')
		    os.system('clear')
		    continue
		else:
		    print('Enter the file name ')
		    file = input()
		    if(d == 1):
		        os.system("touch {}".format(file))
		    elif(d == 2):
		        os.system("mkdir {}".format(file))
		    elif(d==3):
		        os.system("rm -r {}".format(file))
		    elif(d == 4):
                	os.system("cd {}".format(file))
	elif int(ch) == 6:
		print("""  \n\n 1.Namenode \n 2.Datanode \n 3.Back""")
		os.system("tput setaf 7")
		r=input("Enter ur choice :")
		if int(r)==1:
			print("""\n 1.Install jdk and hadoop \n 2.Create a file \n 3.Configure Namenode  \n 4.Disable firewall \n 5.Start namenode \n 6.jps \n 7.dfsadmin-report \n 8.Back""")
			os.system("tput setaf 4")
			a=input("Enter ur choice: ")
			if int(a) == 1:
				os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm")
				os.system("cd /etc/hadoop/")
			elif int(a) == 2:
				os.system("mkdir /nn")
			elif int(a) == 3:
				os.system("cd /etc/hadoop/")
				print(""" \n 1.Setup hdfs-site.xml \n 2.Setup core-site.xml""")
				e = input("Enter ur choice :")
				if int(e) == 1:
					os.system("vi hdfs-site.xml")
				if int (e) == 2:
					os.system("vi core-site.xml")		
			elif int(a) == 4:
				os.system("cd /etc/hadoop/")
				os.system("systemctl stop firewalld")
				print("stoping firewall.....")
			elif int(a) == 5:
				os.system("cd /etc/hadoop/")
				os.system("hadoop-daemon.sh   start namenode")
			elif int(a) == 6:
				os.system("cd /etc/hadoop/")
				os.system("jps")
			elif int(a) == 7:
				os.system("cd /etc/hadoop/")
				os.system("hadoop dfsadmin -report")
			elif int(a) == 8:
				os.system("exit()")
				


		elif int(r)==2:
			print("""\n 1.Install jdk and hadoop \n 2.Configure Datanode  \n 3.Disable firewall \n 4.Start Datanode \n 5.jps \n 6.Back """)
			a=input("Enter ur choice: ")
			if int(a) == 1:
				os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm")
				os.system("cd /etc/hadoop/")
			elif int(a) == 2:
				os.system("cd /etc/hadoop/")
				print(""" \n 1.Setup hdfs-site.xml \n 2.Setup core-site.xml""")
				e = input("Enter ur choice :")
				if int(e) == 1:
					os.system("vi hdfs-site.xml")
				if int (e) == 2:
					os.system("vi core-site.xml")		
			elif int(a) == 3:
				os.system("cd /etc/hadoop/")
				os.system("systemctl stop firewalld")
				print("stoping firewall.....")
			elif int(a) == 4:
				os.system("cd /etc/hadoop/")
				os.system("hadoop-daemon.sh   start datanode")
			elif int(a) == 5:
				os.system("cd /etc/hadoop/")
				os.system("jps")
	elif int(ch) == 7:
		
		print("""  \n		         1.create key pair \n 			 2.create security group \n 			 3.create ingress rule\n			 4.create instances \n			 5.create volume \n 			 6.Attach volume \n			 7.create bucket \n 			 8.to upload files to bucket \n			 9.create cloudfront\n			 10.AWS configure\n			 11.to exit \n""")

		r=input("enter ur choice :")

		if int(r)==1:
			kn=input("enter key name\n")
			os.system("aws ec2 create-key-pair --key-name {}".format(kn))
			

		elif int(r)==2:
				
			os.system("aws ec2 create-security-group --group-name {} --description {}".format(input("enter group name\n"),input("enter group description\n")))
		elif int(r)==3:
			os.system("aws ec2 authorize-group-ingress --protocol {} --group-id {} --cidr 0.0.0.0/0".format(input("enter protocol\n"),input("enter security group id\n")))
		elif int(r)==4:
			os.system("aws ec2 run-instances --image-id {} --instance-type {} --key-name {} --security-group-ids {} --count 1 --subnet-id {}".format(input("enter image id\n"),input("enter instance type\n"),input("enter key name\n"),input("enter security group id\n"),input("enter subnet id\n")))
		elif int(r)==5:
			os.system("aws ec2 create-volume --availability-zone {} --volume-type {} --size {}".format(input("enter availability zone \n"),input("enter volume type \n"),input("enter size \n")))
		elif int(r)==6:
			os.system("aws ec2 attach-volume --instance-id {} --volume-id {} --device {}".format(input("enter instance id\n"),input("enter volume id \n"),input("enetr device name \n")))
		elif int(r)==7:
			os.system("aws s3api create-bucket --bucket {} --create-bucket-configuration LocationConstraint=ap-south-1 --acl {}".format(input("enter unique name of bucket \n"),input("enter readable view i.e acl\n")))
		elif int(r)==8:
			os.system("aws s3 cp {} s3://{} --acl {}".format(input("enter location of file\n"),input("enter bucket name\n"),input("enter readable view i.e acl")))
		elif int(r)==9:
			os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazon.com".format(input("enter bucket name")))
		elif int(r)==10:
			os.system("aws configure")
							

	else:
		print('Exiting....')		
		exit()