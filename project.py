import socket as getIt
hostName = getIt.gethostname() # it gets the host name.
IP = getIt.gethostbyname(hostName) # it gets the ip from the host name.
print("IP Address is " + IP)
