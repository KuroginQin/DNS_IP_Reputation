# Web Crawlers for Data Labelling of Malicious Domain Detection \& IP Reputation Evaluation

This repository provides two web crawlers to label domain names using the McAfee API (https://www.trustedsource.org/sources/index.pl) and IP reputation using the TALOS API (https://talosintelligence.com/), respectively.

### Citing
If you find this project useful for your research, please cite my paper.
```
@article{qin2024multi,
  title={Multi-Task DNS Security Analysis via High-Order Heterogeneous Graph Embedding},
  author={Qin, Meng},
  journal={arXiv preprint arXiv:2401.07410},
  year={2024}
}

```

### Requirements
* BeautifulSoup

### Usage
Descriptions of the demonstration code are as follows.

1. To label the categories of a set of domains, put the domain list in '**data/domain_list.txt**' and run '**demo_domain_label.py**'. The program will label the (1) category (e.g., Malicious Sites- Parked Domain) as well as (2) risk level (e.g., High Risk) of each domain (using the McAfee API) and save the results in '**res/domain_labels.txt**'. *When the program continuously outputs ''-Retry-'', please stop the program and wait for a moment. After the waiting, you can start the program again, which can automatically skip the domains already labeled and continue to label the rest domains.* 

2. To label the reputation of a set of IP addresses, put the IP list in '**data/IP_list.txt**' and run '**demo_IP_label.py**'. The program will label the (1) email reputation as well as (2) web reputation (with 3 levels of Poor, Neutral, and Good) and save the results in '**res/IP_labels.txt**'. *When the program continuously outputs ''None'', please stop the program and wait for a moment. After the waiting, you can start the program again, which can automatically skip the IPs already labeled and continue to label the rest IPs.*

3. An example domain name list (with 21,820 effective second-level domains) and an example IP list (with 67,751 IP addresses) are given in '**data/examples/example_domain_list.txt**' and '**data/examples/example_IP_list.txt**', repsectively. The corresponding labeled results are saved in '**res/examples/example_domain_labels.txt**' and '**res/examples/example_IP_labels.txt**', respectively.

If you have questions regarding this repository, you can contact the author via [mengqin_az@foxmail.com].
