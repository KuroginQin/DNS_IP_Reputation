from modules.Domain import *
import os

# Demonstration to label a set of domains using the McAfee API (https://www.trustedsource.org/sources/index.pl)
# For each domain, give the domain category and risk level if it can be categorized by the API

# ====================
DATA_PATH = 'data/domain_list.txt' # Path of the input domain list
RES_PATH = 'res/domain_labels.txt' # Path to save the domain labels

# ====================
requests.adapters.DEFAULT_RETRIES = 100
domain_set = set()
# Read the domains that has been labelled
if os.path.exists(RES_PATH):
    f_input = open(RES_PATH, 'r')
    for line in f_input.readlines():
        record = line.strip().split(',')
        domain = record[0]
        #print('-Labelled Domain %s' % (domain))
        domain_set.add(domain)
    f_input.close()

# =====================
domain_label = DomainLabel()
label_cnt = 0 # Counter of labelled domains
flag = False
# ==========
f_input = open(DATA_PATH, 'r')
for line in f_input.readlines():
    domain = line.strip()
    if domain in domain_set:
        label_cnt += 1
        continue
    # ==========
    categorized, category, risk = domain_label.lookup(domain)
    print('-Record-#%d %s %s %s %s' % (label_cnt, domain, categorized, category, risk))
    f_output = open(RES_PATH, 'a+')
    if categorized == 'URL not valid':
        f_output.write('%s,%s\n' % (domain, categorized))
    else:
        f_output.write('%s,%s,%s,%s\n' % (domain, categorized, category, risk))
    f_output.close()
    label_cnt += 1
    time.sleep(1) # Sleep for 1 sec

f_input.close()
