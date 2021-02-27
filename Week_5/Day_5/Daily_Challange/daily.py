# Using the modules requests and time create a function that returns how long a webpage takes to load (how long it takes for a complete response to a request)
# Test your code with multiple sites

import requests
import time

url1 = 'https://www.google.com'
url2 = 'https://github.com/'

url1_start = time.process_time()
response = requests.get(url1)
url1_stop = time.process_time()
url1_total = url1_stop - url1_start
print(f'Google total return time: {url1_final}')

url2_start = time.process_time()
response = requests.get(url2)
url2_stop = time.process_time()
url2_total = url2_stop - url2_start
print(f'Github total return time: {url2_total}')
