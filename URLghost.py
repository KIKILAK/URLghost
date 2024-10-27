import socket
import gdshortener
import requests
from discordwebhook import Discord

title = r"""

     /\  ____ _____________.____            .__                    __   
    / / |    |   \______   \    |      ____ |  |__   ____  _______/  |_ 
   / /  |    |   /|       _/    |     / ___\|  |  \ /  _ \/  ___/\   __\
  / /   |    |  / |    |   \    |___ / /_/  >   Y  (  <_> )___ \  |  |  
 / /    |______/  |____|_  /_______ \\___  /|___|  /\____/____  > |__|  
 \/                      \/        \/_____/      \/           \/        

"""
print(title)

print("Hide any URL, make it unrecognizable")
print("Enjoy obfuscating!")
print("do not use this program for malicious purpose")
print("TIP : see URL examples to see how your URLs would look like using the methods below.")
print("=" * 100)
print("--------(Select an URl obfuscation metod.)--------")
print("\n")
print("1.- normal obfuscation")
print("2.- URL shortener")
print("3.- Access to the website via IP adress")
print("4.- hex encode obfuscation")
print("5.- Shorten and obfuscate URL")
print("6.- Access via IP and obfuscate")
print("7.- Hex encode and obfuscate")
print("8.- obfuscation with a #")
print("9.- obfuscation with a ?")
print("\n")
print("-------------(More Options)-------------")
print("\n")

print("99.- URL examples")
print("11.- actual version")
print("12.- send ideas")
print("00.- leave")
print("\n")

selection = input("--------(-🌐-)[@]/[Select an option] : ")

if selection == '1':
    print("\n")
    print("--------(Normal URL obfuscation)--------")
    print("\n")
    normal_url_obfuscation_legitimate_url = input("--------(-🌐-)[@normal-obfuscation]/[paste the legitimate URL, example: https://youtube.com] : ")
    normal_url_obfuscation_malicious_url = input("--------(-🌐-)[@normal-obfuscation]/[paste the malicious domain, example: devil.com, malicious.or/fsyThY] : ")
    print("\n")
    print("Obfuscated URL : " + normal_url_obfuscation_legitimate_url + "@" + normal_url_obfuscation_malicious_url)
    quit()
elif selection == '2':
    print("\n")
    print("--------(URL shortener)--------")
    print("\n")
    url_to_short = input("--------(-🌐-)[@URL-Shortener]/[paste the URL to shorten, example: https://devil.com, https://malicious.or/fsyThY] : ")
    s = gdshortener.ISGDShortener()
    print("Shortened url : ")
    shortened_url = s.shorten(url_to_short)
    print(shortened_url)
    print("\n")
elif selection == '3':
    print("--------(IP obfuscation)--------")
    print('\n')
    web_to_convert = input("--------(-🌐-)[@IP-obfuscation]/[paste the domain name] : ")
    print("\n")
    print("IP : " + socket.gethostbyname(web_to_convert) + "paste the IP adress in web browser")
elif selection == '4':
    print("--------(Hex obfuscation)--------")
    malicious_url_hex =  input("--------(-🌐-)[@hex-obfuscation]/[paste the malicious domain, example: devil.com, malicious.or/fsyThY] : ")
    hex_encoded = ''.join('%{:02x}'.format(ord(c)) for c in malicious_url_hex)
    print(hex_encoded)
elif selection == '5':
    print("\n")
    print("--------(URL shortener and obfuscation)--------")
    print("\n")
    url_to_short_2 = input("--------(-🌐-)[@URL-Shortener]/[paste the domain to shorten, example: devil.com, malicious.or/fsyThY] : ")
    legit_url_7 = input("--------(-🌐-)[@URL-Shortener]/[paste the domain to obfuscate, example: legit.lol] : ")
    s = gdshortener.ISGDShortener()
    test = requests.get("https://is.gd/create.php?format=simple&url=" + url_to_short_2).text
    print(legit_url_7 + "@" + test)
    print("\n")
elif selection == '6':
    print("\n")
    print("--------(Normal URL obfuscation and IP)--------")
    print("\n")
    ip_and_obfuscation_legitimate_url = input("--------(-🌐-)[@normal-obfuscation-and-ip]/[paste the legitimate URL, example: https://youtube.com] : ")
    ip_and_obfuscation_malicious = input("--------(-🌐-)[@normal-obfuscation-and-ip]/[paste the malicious domain, example: devil.com, malicious.or/fsyThY] : ")
    print("\n")
    malicious_url_to_ip = socket.gethostbyname(ip_and_obfuscation_malicious)
    print(ip_and_obfuscation_legitimate_url + "@" + malicious_url_to_ip)
elif selection == '7':
    print()
    malicious_url_hex =  input("--------(-🌐-)[@hex-obfuscation]/[paste the malicious domain, example: devil.com, malicious.or/fsyThY] : ")
    legit_url_hex =  input("--------(-🌐-)[@hex-obfuscation]/[paste the legitimate URL, example: https://youtube.com] : ")
    hex_encoded = ''.join('%{:02x}'.format(ord(c)) for c in malicious_url_hex)
    print(legit_url_hex + "@" + hex_encoded)

elif selection == '8':
    print("\n")
    print("--------(URL obfuscation with #)--------")
    print("\n")
    legitimate_url_ = input("--------(-🌐-)[@obfuscation with #]/[paste the legitimate URL, example: https://youtube.com] : ") 
    malicius_domain_ = input("--------(-🌐-)[@obfuscation with #]/[paste the malicious domain, example: devil.com, malicious.or/fsyThY] : ")
    print(legitimate_url_ + "#" + malicius_domain_)

elif selection == '9':
    print("\n")
    print("--------(URL obfuscation with #)--------")
    print("\n")
    legitimate = input("--------(-🌐-)[@obfuscation with ?]/[paste the legitimate URL, example: https://youtube.com] : ")
    malicious = input("--------(-🌐-)[@obfuscation with #]/[paste the malicious URL, example: http://devil.com, https://malicious.or/fsyThY] : ")
    print("\n")
    print("Obfuscated URL : " + legitimate + "?" + malicious)
elif selection == '99':
    print("---------------(:examples:)---------------")
    print("1.- normal obfuscation : youtube.com@phishing.com")
    print("2.- URL shortener : youtube.com -----> is.gd/ihhHx")
    print("3.- Access via IP Address : youtube.com -----> 142.250.179.142")
    print("4.- Hex encode obfuscation : youtube.com ------> %79%6f%75%74%75%62%65%2e%63%6f%6d")
    print("5.- Shorten and obfuscate URL : website-with-virus.com ----> realdomain.com@is.gd/iHKbFG")
    print("6.- Access via IP Adress and obfuscate : -----> virus-website.bad --------> realdomain.com@123.456.789.10")
    print("7.- Hex encode and obfuscate : killerwebsite.kill -----> realdomain.com@%79%6f%75%74%75%62%65%2e%63%6f%6d")
    print("8.- obfuscation with a # : youtube.com#phishing.com")
    print("9.- obfuscation with a ? : youtube.com?malicious.com")
    print("\n")
    print("These are some example of how your obfuscated URLs would look like.")
elif selection == '00':
    print("Exiting the program...")
    quit()
elif selection == '11':
    print("1.0.0")
elif selection == '12':
    url_webhook = Discord(url="removed_temporally")
    print("\n")
    suggest = input("--------(-🌐-)[Enter your suggestion (bugs, obfuscation methods, suggestions, etc) :) ] : ")
    url_webhook.post(content=suggest)
elif selection == 'xx':
    print("using all options")
else:
    print("[!] Invalid option, QUITTING!")
