import requests
from bs4 import BeautifulSoup
import time

class DomainLabel():
    '''
    Class to label domain names using the McAfee SmartFilter Internet / Webwasher URL Filter Database
    '''
    def __init__(self):
        # ====================
        # Set the configuration of a simulated browser
        self.headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5)',
                        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                        'Accept-Language' : 'en-US,en;q=0.9,de;q=0.8'
                    }
        self.base_url = 'http://www.trustedsource.org/sources/index.pl'
        # ==========
        r = requests.get(self.base_url, headers=self.headers)
        bs = BeautifulSoup(r.content, "html.parser")
        form = bs.find("form", {"class": "contactForm"})
        # ==========
        self.token1 = form.find("input", {'name': 'e'}).get('value')
        self.token2 = form.find("input", {'name': 'c'}).get('value')
        self.headers['Referer'] = self.base_url

    def lookup(self, url):
        payload = {'e': (None, self.token1),
                   'c': (None, self.token2),
                   'action': (None, 'checksingle'),
                   'product': (None, '01-ts'),
                   'url': (None, url)}

        r = requests.post('https://www.trustedsource.org/en/feedback/url', headers=self.headers, files=payload)
        bs = BeautifulSoup(r.content, "html.parser")
        #form = bs.find("form", { "class" : "contactForm" })
        table = bs.find("table", {"class": "result-table"})

        # ====================
        # When the database return 'None', sleep for 3 sec and retry (w/ new configurations)
        while table is None:
            print('-Retry-')
            del r
            time.sleep(3)
            # ==========
            self.update() # Update the configurations of the simulated browser
            payload = {'e': (None, self.token1),
                       'c': (None, self.token2),
                       'action': (None, 'checksingle'),
                       'product': (None, '01-ts'),
                       'url': (None, url)}
            r = requests.post('https://www.trustedsource.org/en/feedback/url', headers=self.headers, files=payload)
            bs = BeautifulSoup(r.content, "html.parser")
            table = bs.find("table", {"class": "result-table"})

        td = table.find_all('td')
        categorized = td[len(td)-3].text # Whether the given domain is categorized in the database
        category = td[len(td) - 2].text[2:] # The category of the given domain
        risk = td[len(td) - 1].text # Risk level

        return categorized, category, risk

    def update(self):
        '''
        Function to update the configurations of the simulated browser
        '''
        # ====================
        r = requests.get(self.base_url, headers=self.headers)
        bs = BeautifulSoup(r.content, "html.parser")
        form = bs.find("form", {"class": "contactForm"})
        # ==========
        self.token1 = form.find("input", {'name': 'e'}).get('value')
        self.token2 = form.find("input", {'name': 'c'}).get('value')
        self.headers['Referer'] = self.base_url
