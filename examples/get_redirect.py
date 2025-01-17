"""Example script for testing redirection support of mrequest."""

import sys
import mrequests as requests


print("Running on platform:", sys.platform)

host = 'http://httpbin.org/'
base_url = host + "redirect/"

url = base_url + "1"
print("Requesting %s with default max_redirects ..." % url)
r = requests.get(url)
print("Status code:", r.status_code)
r.close()

url = base_url + "2"
print("Requesting %s with default max_redirects=2 ..." % url)
r = requests.get(url, max_redirects=2)
print("Status code:", r.status_code)
r.close()

# max_redirects defaults to 1, so this should raise a ValueError
print("Requesting %s with default max_redirects (should fail)..." % url)
try:
    r = requests.get(url)
except ValueError as exc:
    print("FAIL", exc)
else:
    r.close()

base_url = host + "absolute-redirect/"

url = base_url + "1"
print("Requesting %s with default max_redirects ..." % url)
r = requests.get(url)
print("Status code:", r.status_code)
r.close()

url = base_url + "2"
print("Requesting %s with default max_redirects=2 ..." % url)
r = requests.get(url, max_redirects=2)
print("Status code:", r.status_code)
r.close()

# max_redirects defaults to 1, so this should raise a ValueError
print("Requesting %s with default max_redirects (should fail)..." % url)
try:
    r = requests.get(url)
except ValueError as exc:
    print("FAIL", exc)
else:
    r.close()
