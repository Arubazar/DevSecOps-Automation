import json
import os
import requests
import paramiko
import getpass
import time

PORT = 22


def ssh_command(username, password, cmd, hostname, port=PORT):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_system_host_keys()
    ssh.connect(hostname, port, username=username, password=password)

    remote_conn = ssh.invoke_shell()

    remote_conn.send("set cli pager off\n")
    for items in cmd:
        remote_conn.send(items + "\n")
        time.sleep(10)
        output = remote_conn.recv(100000)
        print(output.decode())
    ssh.close()


def select_firewall(cmd):

    firewall_ip = int(input("Select the firewall(s)\n  1.SITE-1 & SITE-2\n  2.SITE-1\n  3.SITE-3\n  4.SITE-4\n  5.SITE-2 \nSelect --> "))

    if firewall_ip == 1:
        SITE-1_HOSTNAME = '10.35.25.50'
        print("\n##---------- Running on SITE-1 " + SITE-1_HOSTNAME + " ----------##\n")
        ssh_command(username, password, cmd, SITE-1_HOSTNAME)
        print("\n##---------- Completed on SITE-1 " + SITE-1_HOSTNAME + " ----------##\n")

        SITE-2_HOSTNAME = '10.55.26.50'
        print("\n##---------- Running on SITE-2 " + SITE-2_HOSTNAME + " ----------##\n")
        ssh_command(username, password, cmd, SITE-2_HOSTNAME)
        print("\n##---------- Completed on SITE-2 " + SITE-2_HOSTNAME + " ----------##\n")

    elif firewall_ip == 2:
        HOSTNAME = '10.35.25.50'
        print("\n##---------- Running on SITE-1 " + HOSTNAME + " ----------##\n")
        ssh_command(username, password, cmd, HOSTNAME)
        print("\n##---------- Completed on SITE-1 " + HOSTNAME + " ----------##\n")

    elif firewall_ip == 3:
        HOSTNAME = '10.30.225.30'
        print("\n##---------- Running on SITE-3 " + HOSTNAME + " ----------##\n")
        ssh_command(username, password, cmd, HOSTNAME)
        print("\n##---------- Completed on SITE-3 " + HOSTNAME + " ----------##\n")

    elif firewall_ip == 4:
        HOSTNAME = '10.140.224.4'
        print("\n##---------- Running on SITE-4 " + HOSTNAME + " ----------##\n")
        ssh_command(username, password, cmd, HOSTNAME)
        print("\n##---------- Completed on SITE-4 " + HOSTNAME + " ----------##\n")

    elif firewall_ip == 5:
        HOSTNAME = '10.55.26.50'
        print("\n##---------- Running on SITE-2 " + HOSTNAME + " ----------##\n")
        ssh_command(username, password, cmd, HOSTNAME)
        print("\n##---------- Completed on SITE-2 " + HOSTNAME + " ----------##\n")

    else:
        print("Sorry, Please select correct firewall.")
        exit()


if __name__ == '__main__':
    #username = input("Enter username: ")
    #password = input("Enter password: ")
    #username = "username"
    #password = "password"
    username = input("Enter username: ")
    password = getpass.getpass(prompt='Enter password : ')

    action_no = int(input("\nPlease select your action : \n  1. To show the session  \n  2. To clear the session \n  3. Any other command \nSelect --> " ))
    
    if action_no == 1:
        ips_to_clear = input("\nTo show the session, please enter the IPs (separated by comma ',') : ").split(",")
        cmd = []
        for ips in ips_to_clear:
            cmd.append("show session all filter source " + ips) 
        select_firewall(cmd) 

    elif action_no == 2:
        ips_to_clear = input("\nTo clear the session, please enter the IPs (separated by comma ',') : ").split(",")
        cmd = []
        for ips in ips_to_clear:
            cmd.append("clear session all filter source " + ips)
        select_firewall(cmd)

    elif action_no == 3:
        cmd = input("\nEnter your commands (use comma for multiple commands) : ").split(",")
        select_firewall(cmd)

    else:
        print("Sorry, Please select correct option.")
        exit()
