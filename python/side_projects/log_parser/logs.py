import re
import tabulate

# ids.log created with https://github.com/cruikshank25/Security-Log-Generator


ts_pttrn = re.compile(r"\b\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\b", re.IGNORECASE)
logger_name_pttrn = re.compile(r' - (\w+_\d+) - ')
sev_pttrn = re.compile(r' - (low|medium|high)_severity - ')
protocol_pttrn = re.compile(r' - (ICMP|TCP|TFTP|HTTPS|UDP|DNS|FTP|HTTP|SNMP) - ')
port_pttrn = re.compile(r'\b(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d+)\b')
flags_pttrn = re.compile(r' - (SYN|ACK|RST|URG|FIN|PSH) - ')
desc_pttrn = re.compile(r' - (SYN|ACK|RST|URG|FIN|PSH) - (.+)')

file_path = "ids.log"
with open(file_path, 'r') as f:
	ts_data = []
	lname_data = []
	sev_data = []
	proto_data = []
	src_ip_data = []
	src_port_data = []
	dest_ip_data = []
	dest_port_data = []
	flags_data = []
	desc_data = []

	for _ in f:

		ts_parts = ts_pttrn.findall(_.strip())
		lname_parts = logger_name_pttrn.findall(_.strip())
		sev_parts = sev_pttrn.findall(_.strip())
		proto_parts = protocol_pttrn.findall(_.strip())

		ts_data.append(ts_parts)
		lname_data.append(lname_parts)
		sev_data.append(sev_parts)
		proto_data.append(proto_parts)

		ip_port_match = port_pttrn.findall(_.strip())
		if len(ip_port_match) >= 2:
			src_ip, src_port = ip_port_match[0]
			dest_ip, dest_port = ip_port_match[1]
			src_ip_data.append(src_ip)
			src_port_data.append(src_port)
			dest_ip_data.append(dest_ip)
			dest_port_data.append(dest_port)
		else:
			src_ip_data.append(None)
			src_port_data.append(None)
			dest_ip_data.append(None)
			dest_port_data.append(None)

		flags_match = flags_pttrn.search(_.strip())
		if flags_match:
			flags = flags_match.group(1)
			flags_data.append(flags)
		else:
			flags_data.append(None)

		desc_match = desc_pttrn.search(_.strip())
		if desc_match:
			desc = desc_match.group(2)
			desc_data.append(desc)
		else:
			desc_data.append(None)

data = []

for _ in range(len(ts_data)):
    data.append([
        ts_data[_][0] if ts_data[_] else '',
        lname_data[_][0] if lname_data[_] else '',
        sev_data[_][0] if sev_data[_] else '',
        proto_data[_][0] if proto_data[_] else '',
        f"{src_ip_data[_]}:{src_port_data[_]}" if src_ip_data[_] else '',
        f"{dest_ip_data[_]}:{dest_port_data[_]}" if dest_ip_data[_] else '',
        flags_data[_] if flags_data[_] else '',
        desc_data[_] if desc_data[_] else ''
    ])

headers = ['Timestamp', 'Logger Name', 'Severity', 'Protocol', 'Source IP:Port', 'Destination IP:Port', 'Flags', 'Description']

print(tabulate(data, headers=headers, tablefmt='grid'))

"""print(ts_data)    
print('\n', lname_data)
print('\n', sev_data)
print('\n', proto_data)
print('\n', src_ip_data)
print('\n', src_port_data)
print('\n', dest_ip_data)
print('\n', dest_port_data)
print('\n', flags_data)
print('\n', desc_data)"""

