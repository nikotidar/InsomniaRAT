Insomnia RAT developed by Hari Patel (hari.p.221221@gmail.com) (github.com/Hari-P-22121)

Insomnia RAT is a P2P Remote Administrator Tool for OSX. The client and host both require OSX operating system. 

This does not require extra dependencies to be installed. 

When the software launches, there are total 3 options. 

1) Build Stub

This allows you to build software that will be run by the client's machine. After the client executes the software, the host will have remote access. The port must be from 1024 to 65535. Also, a hostname/IP must be provided. 

2) Listen on port

This allows the host to listen on any port from 1024 to 65535. The host would listen on the port the client is reverse connecting on. Once a connection is established, the attacker will be given commands that they can use on the client's computer. NOTE: There can only be one connection at a time. If 2 computers are both reverse connecting on the same port at the same time, then there may be problems. 

3) Exit

Exit the software. 
