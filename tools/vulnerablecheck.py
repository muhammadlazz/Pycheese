import requests

def check_vul(domain):
  headers = requests.get(domain).headers

  if 'X-Frame-Options' in headers:
    print(domain + f"  -->  THE WEBSITE IS NOT VULNERABLE")
  else:
    print(domain + f"  -->  THE WEBSITE IS VULNERABLE")