import requests

# Function to get the reputation of a given IP address from talosintelligence.com

def get_pkg(search_string):
    """
    Download data from talosintelligence.com for the given IP
    Return tabbed data text
    """
    try: # Set the configurations of simulated browser & get the lookup results
        r_details = requests.get('https://talosintelligence.com/sb_api/query_lookup',
                             headers={
                                 'Referer': 'https://talosintelligence.com/reputation_center/lookup?search=%s' % search_string,
                                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
                             },
                             params={
                                 'query': '/api/v2/details/ip/',
                                 'query_entry': search_string
                             }).json()
    except:
        return None

    data = {
        'address': search_string,
        'hostname': r_details['hostname'] if 'hostname' in r_details else "nodata",
        'volume_change': r_details['daychange'] if 'daychange' in r_details else "nodata",
        'lastday_volume': r_details['daily_mag'] if 'daily_mag' in r_details else "nodata",
        'month_volume': r_details['monthly_mag'] if 'monthly_mag' in r_details else "nodata",
        'email_reputation': r_details['email_score_name'] if 'email_score_name' in r_details else "nodata",
        'web_reputation': r_details['web_score_name'] if 'web_score_name' in r_details else "nodata"
    }

    return data