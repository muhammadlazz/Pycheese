import os           # Untuk mendeklarasikan fungsi OS
import requests     # 

# Daftar fungsi fitur yang terdapat di aplikasi
# 1 : Mendetect IP tersebut berada diwilayah mana
def iptrack(ip):
    try:
        response = requests.get(f"http://ipinfo.io/{ip}/json")
        data = response.json()
        
        if 'bogon' in data:
            print(f"The IP {ip} is a bogon (private or reserved IP address).")
        else:
            city = data.get('city', 'Unknown')
            region = data.get('region', 'Unknown')
            country = data.get('country', 'Unknown')
            print(f"IP from {ip} is located in {city}, {region}, {country}")
    except Exception as e:
        print(f"Could not perform Geo-IP lookup for IP {ip}: {e}")
    

# 2 : Menganalisis log file yang terdapat pattern atau pola mencurigakan
def analyze_log_file(file_path):
    suspicious_patterns = ["Failed login", "error", "unauthorized access"]
    try:
        with open(file_path, 'r') as file:
            logs = file.readlines()
        
        for log in logs:
            if any(pattern in log for pattern in suspicious_patterns):
                print(f"Suspicious log entry: {log.strip()}")
    except FileNotFoundError:
        print(f"Log file {file_path} not found.")
    except Exception as e:
        print(f"Error reading log file {file_path}: {e}")

# 3 : Mengecek domain / website tersebut rentan terhadap serangan / tidak (X-Frame Options)
def check_vul(domain):
  headers = requests.get(domain).headers

  if 'X-Frame-Options' in headers:
    print(domain + f"  -->  THE WEBSITE IS NOT VULNERABLE")
  else:
    print(domain + f"  -->  THE WEBSITE IS VULNERABLE")


# Disini fungsi menu yang akan ditampilkan terlebih dahulu
os.system("cls")
def main_menu():
    while True:
        os.system("cls")
        print("\n")
        print(""" 
   ▄███████▄ ▄██   ▄    ▄████████    ▄█    █▄       ▄████████    ▄████████    ▄████████    ▄████████ 
  ███    ███ ███   ██▄ ███    ███   ███    ███     ███    ███   ███    ███   ███    ███   ███    ███ 
  ███    ███ ███▄▄▄███ ███    █▀    ███    ███     ███    █▀    ███    █▀    ███    █▀    ███    █▀  
  ███    ███ ▀▀▀▀▀▀███ ███         ▄███▄▄▄▄███▄▄  ▄███▄▄▄      ▄███▄▄▄       ███         ▄███▄▄▄     
▀█████████▀  ▄██   ███ ███        ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ▀▀███▀▀▀     ▀███████████ ▀▀███▀▀▀     
  ███        ███   ███ ███    █▄    ███    ███     ███    █▄    ███    █▄           ███   ███    █▄  
  ███        ███   ███ ███    ███   ███    ███     ███    ███   ███    ███    ▄█    ███   ███    ███ 
 ▄████▀       ▀█████▀  ████████▀    ███    █▀      ██████████   ██████████  ▄████████▀    ██████████""")
        print("\n")
        print("1. Where is the IP located ?")
        print("2. Log File Suspicious Analysis")
        print("3. Check Vulnerable Website (X-Frame)")
        respon = input("What you want to Run ?: ")

        if respon == '1':
            os.system("cls")
            ip_address = input("Enter IP address: ")
            iptrack(ip_address)
            choose = input("Back to menu ? Yes/No\n")
            if choose == 'Yes':
                main_menu()
            else:
                print("Thankyou For Using this App.")
                break
                    

        elif respon == '2':
            os.system("cls")
            file_path = input("Enter log file path: ")
            analyze_log_file(file_path)
            choose = input("Back to menu ? Yes/No\n")
            if choose == 'Yes':
                main_menu()
            else:
                print("Thankyou For Using this App.")
                break

        elif respon == '3':
            os.system("cls")
            domain = input("Enter domain for check: ")
            check_vul(domain)
            choose = input("Back to menu ? Yes/No\n")
            if choose == 'Yes':
                main_menu()
            else:
                print("Thankyou For Using this App.")
                break
            
        else:
            os.system("cls")
            print("Choose the right option only !")
            os.system("pause")
            os.system("cls")


# Mengembalikan user ke menu lagi
if __name__ == "__main__":
    main_menu()
