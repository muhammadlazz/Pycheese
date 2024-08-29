import os           # Untuk mendeklarasikan fungsi OS
import requests     # Mendeklarasikan fungsi request


# Daftar fungsi fitur yang terdapat di aplikasi
# 1 : Mendetect IP tersebut berada diwilayah mana
def iptrack(ip): # definisi dari fitur ip track dan variabel ip
    try:  # mencoba run code yang berada di line setelah 'try'
        response = requests.get(f"http://ipinfo.io/{ip}/json")  # membuat request ke API ipinfo 
        data = response.json()  # merespon dengan mengembalikan data dengan format json
        
        if 'bogon' in data:  # mengecek apakah ip tersebut private atau tidak
            print(f"The IP {ip} is a bogon (private or reserved IP address).")
        else:  # jika tidak, maka akan ditampilkan data kota, wilayah, negara
            city = data.get('city', 'Unknown')
            region = data.get('region', 'Unknown')
            country = data.get('country', 'Unknown')  # jika tidak ada data yang terbaca maka unknown
            print(f"IP from {ip} is located in {city}, {region}, {country}")
    except Exception as e:  # jika kode 'try' tidak jalan, maka except yang berjalan dan disimpan di variabel e
        print(f"Could not perform Geo-IP lookup for IP {ip}: {e}")


# 2 : Menganalisis log file yang terdapat pattern atau pola mencurigakan
def logfile_analyzer(file_path):  # definisi dari fitur log file analyzer
    suspicious_patterns = ["Failed login", "error", "unauthorized access"]  # mendeklarasikan pattern yang mencurigakan
    try:
        with open(file_path, 'r') as file:  # membuka file dan dalam mode read
            logs = file.readlines()  # membaca semua baris dalam file log tersebut
        
        for log in logs:  # looping untuk menampilkan pola yang mencurigakan
            if any(pattern in log for pattern in suspicious_patterns):  #  any untuk mengecek apakah ada pola yang sudah dideklarasikan di 'suspicious_patterns'
                print(f"Suspicious log entry: {log.strip()}")  # strip untuk menghapus spasi depan dan belakang
    except FileNotFoundError:  # jika file tidak ditemukan di fungsi with open, maka akan berjalan except ini
        print(f"Log file {file_path} not found.")
    except Exception as e:
        print(f"Error reading log file {file_path}: {e}")


# 3 : Mengecek domain / website tersebut rentan terhadap clickjacking / tidak (X-Frame Options) 
def check_vul(domain):  # definisi dari fitur vulnerable check web
  headers = requests.get(domain).headers  # request http ke domain yang diinputkan. kemudian headers untuk mengambil info header dari respon http

  if 'X-Frame-Options' in headers:  # mengecek apakah header 'X-frame options' terdapat pada header domain yang diinputkan
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
            logfile_analyzer(file_path)
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


main_menu()