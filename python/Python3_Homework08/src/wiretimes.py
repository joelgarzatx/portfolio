"""
wiretimes.py: reads a wireshark.bin data file dumped from pcap and lists the timestamp and microseconds offset for each packet.
"""
import datetime, os, struct
filename = r"V:\workspace\Python3_Homework08\src\wireshark.bin"

f = open(filename, "rb")

# read header
header = f.read(24)

magic_number,version_major,version_minor,thiszone,sigfigs,snaplen,network = struct.unpack("=IHHiIII", header)
print("Wireshark File Header")
print("magic_number:",hex(magic_number))
print("version_major:",hex(version_major)) 
print("version_minor:",hex(version_minor))
print("thiszone:",hex(thiszone))
print("sigfigs:",hex(sigfigs))
print("snaplen:",hex(snaplen))
print("network:",hex(network))

packet_count = 0
while True:
    packet_header = f.read(16)
    if not packet_header:
        break
    
    packet_count += 1    
    ts_sec, ts_usec, incl_len, orig_len = struct.unpack("=IIII", packet_header)
#    print("ts_sec", datetime.datetime.fromtimestamp(int(ts_sec)).strftime('%Y-%m-%d %H:%M:%S'))
#    print("ts_usec", ts_usec)
#    print("incl_len", hex(incl_len))
#    print("orig_len", hex(orig_len))

    print("Packet {0}: {1}, {2} microseconds".format(packet_count,datetime.datetime.fromtimestamp(int(ts_sec)).strftime('%Y-%m-%d %H:%M:%S'),ts_usec))
    packet_data = f.read(incl_len)
    
f.close()




