#! /usr/bin/env python
ip1 = '1.2.3.4'
ip2 = '1.3.4.5'

ip1_list = ip1.split( '.' )
ip2_list = ip2.split( '.' )

curr_offset = -1
for i in range( len(ip1_list) ):
	if ip1_list[i] < ip2_list[i]:
		curr_offset = i
		break

ip_num_min = 0
ip_num_max = 255

ip_num_1st = int( ip1_list[0] )
ip_num_2nd = int( ip1_list[1] )
ip_num_3rd = int( ip1_list[2] )
ip_num_4th = int( ip1_list[3] )

while True:
	curr_ip = str(ip_num_1st) + '.' + str(ip_num_2nd) + '.' + str(ip_num_3rd) + '.' + str(ip_num_4th)
	if curr_ip > ip2:
		break

	# scan operation
	print curr_ip

	if ip_num_4th >= ip_num_max:
		if ip_num_3rd >= ip_num_max:
			if ip_num_2nd >= ip_num_max:
				if ip_num_1st >= ip_num_max:
					raise Exception( 'IP overflow' )
				else:
					ip_num_1st += 1
					ip_num_2nd = ip_num_min
					ip_num_3rd = ip_num_min
					ip_num_4th = ip_num_min
			else:
				ip_num_2nd += 1
				ip_num_3rd = ip_num_min
				ip_num_4th = ip_num_min
		else:
			ip_num_4th = ip_num_min
			ip_num_3rd += 1
	else:
		ip_num_4th += 1
