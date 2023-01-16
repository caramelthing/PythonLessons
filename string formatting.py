ip_address1 = "10.0.0.0/8"
ip_address2 = "172.16.0.0/12"
ip_address3 = "192.168.0.0/16"
ip_address4 = "1.2.3.4"
octet = ip_address4.split('.')
#i guess the point of this is .split method returns a list..

print("*" * 80)
print("{a:<20} {b:^20} {c:>20}".format(c=ip_address1, b=ip_address2, a=ip_address3))
print("{:10}{:10}{:10}{:10}".format(octet[1],octet[2],octet[3],octet[0]))
print("{:10}{:10}{:10}{:10}".format(*octet))