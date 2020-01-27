import os
import re
import time
import socket
import subprocess
from makeAchoice import makeAchoice

IP_Port = {}


### port scanning ips using sockets  module ## 
def pscan(target, start=0, end=444):
    host = socket.gethostbyname(target)
    for port in range(start, end):
        scannerTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        status = scannerTCP.connect_ex((host, port))

        if not status:
            IP_Port[target].append(str(port))

        scannerTCP.close()



### filter "pingable" ips ### 
def IPFilter(UpHosts):
    filtered = []
    for ip in UpHosts:
        res = subprocess.Popen("ping -c 2 " + ip, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) 
        if "ttl" in str(res.stdout.read(), "utf-8"):
            filtered.append(ip)
    return filtered





def run():
    interface = input(" enter the interface you want to scan : ")
    res = subprocess.Popen("arp-scan --interface="+interface+" --localnet", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) 

    res = str(res.stdout.read(), "utf-8")
    #print(res)
    ips = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", res)
    UpHosts = list(set(ips))
    print("Scanning your network for up hosts.....")
    UpHosts_NoFireWall = IPFilter(UpHosts)




    if len(UpHosts_NoFireWall):
        print("Ping sweep complete! " + str(len(UpHosts_NoFireWall)) + " hosts found!\nInitiating port scanner.......")
        time.sleep(2)


        for ip in UpHosts_NoFireWall:  
            IP_Port[ip] = []
            print("Scanning " + ip + " ........")
            pscan(ip)

    
    print("\nScan Complete!!\nFeeding Results to Nmap....")
    print(IP_Port)
    nmapList = ["1. Save results to file", "2. Write results to screen"]
    inp = makeAchoice(nmapList, 2)


    for i in IP_Port:
        #print(IP_Port[i] )
        if not IP_Port[i]:
            continue
        print(f"\nScanning {i} ==================>")
        portS = ','.join(IP_Port[i])
        nmapCMD = "nmap -T4 -sV -p " + portS + " " + i
        res = os.popen(nmapCMD).read()
        ports = re.findall(r'\d+/tcp.+', res)
        
        if inp == 2:
            print("\n".join(ports))
        else:
            f = open("./Nmapper_IPScan.txt", "w")
            f.write("<<<<<< IP: " + i + " >>>>>>\n")
            f.write("\n".join(ports))
            f.write("\n-----------------------------DoNe-----------------------------\n")
