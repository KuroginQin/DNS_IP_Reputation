from modules.IP import *
import time
import os

# Demonstration to label a set of domains using the TALOS API (https://talosintelligence.com/)
# For each domain, give the domain category and risk level if it can be categorized by the API

# ====================
INPUT_PATH = 'data/IP_list.txt' # Path of the input IP list
RES_PATH = 'res/IP_labels.txt' # Path to save the IP reputation labels

# =====================
IP_set = set()
# Read the IPs that has been labelled
if os.path.exists(RES_PATH):
    f_IP_list = open(RES_PATH, 'r')
    for line in f_IP_list.readlines():
        record = line.strip().split(',')
        IP = record[0]
        #print('-Labelled IP %s' % (domain))
        IP_set.add(IP)
    f_IP_list.close()

# =====================
f_input = open(INPUT_PATH, 'r')
IP_cnt = 0 # Counter of labelled IPs
for line in f_input.readlines():
    # ==========
    IP = line.strip()
    if IP in IP_set:
        IP_cnt += 1
        continue
    rep_data = get_pkg(IP)
    if rep_data is None:
        print('-Record-#%d %s None' % (IP_cnt, IP))
        # ==========
        f_output = open(RES_PATH, 'a+')
        f_output.write('%s,None,None\n' % (IP))
        f_output.close()
        time.sleep(1)
        IP_cnt += 1
    else:
        IP_addr = rep_data['address'] # IP address
        email_rep = rep_data['email_reputation'] # Email reputation
        web_rep = rep_data['web_reputation'] # Web reputation
        print('-Record-#%d %s %s %s' % (IP_cnt, IP_addr, email_rep, web_rep))
        # ==========
        f_output = open(RES_PATH, 'a+')
        f_output.write('%s,%s,%s\n' % (IP_addr, email_rep, web_rep))
        f_output.close()
        time.sleep(1)
        IP_cnt += 1
f_input.close()
