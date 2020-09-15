import socket as s 
hostn = s.gethostname()
IP = s.gethostbyname(hostn)
print("IP Address is " + IP)
