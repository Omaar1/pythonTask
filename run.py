import Nmapper
import myBanner
import makeAchoice
import directoryWatcher
import ipsSimulate
import webScrapper
import logParser


myBanner.displayBanner()
print("\nchooose ur favourite attack :\n")
nmapList = ["1. Nmap ", "2. Directory watcher " ,"3. IPS simulate ","4. WebScrapper","5. LogParser"]
inp = makeAchoice.makeAchoice(nmapList, 5)

if inp == 1:
	Nmapper.run()
if inp == 2:
	directoryWatcher.run()
if inp == 3:
	ipsSimulate.run() 
if inp == 4:
	webScrapper.run() 
if inp == 5:
	logParser.run() 

