import socket
import gdshortener
import requests
from kcolors import Colors
import time
import pyperclip
import random
from titles import *
import os


# global

black = Colors.BLACK
red = Colors.RED
green = Colors.GREEN
blue = Colors.BLUE
purple = Colors.PURPLE
yellow = Colors.YELLOW
bold = Colors.BOLD
underline = Colors.UNDERLINE
faint = Colors.FAINT
italic = Colors.ITALIC
cyan = Colors.CYAN
bblack = Colors.BBLACK
bblue = Colors.BBLUE
bcyan = Colors.BCYAN
bgreen = Colors.BGREEN
bpurple = Colors.BPURPLE
bred = Colors.BRED
crossed = Colors.CROSSED
end = Colors.END

def main():

    while True:
        import public_ip as ip

        # title
        all_titles = [title1, title2, title3, title4, title5, title6, title7, title8, title9, title10]
        title = random.choice(all_titles)
        all_colors = [black, red, purple]
        title_color = random.choice(all_colors)
        print(f"{title_color}{title}{end}")

        print(f"{red}-{end}" * 65)
        print(f"{bblue}Hide any URL, make it unrecognizable | IP : {ip.get()} | Ver: 2{end}")
        print(f"{red}-{end}" * 65)
        print("\n")
        print(f"\t\t1.- normal obfuscation")
        print(f"\t\t2.- URL shortener")
        print(f"\t\t3.- Access via IP adress")
        print(f"\t\t4.- hex encode obfuscation")
        print(f"\t\t5.- Shorten and obfuscate URL")
        print(f"\t\t6.- Access via IP and obfuscate")
        print(f"\t\t7.- Hex encode and obfuscate")
        print(f"\t\t8.- obfuscation with '#'")
        print(f"\t\t9.- obfuscation with '?'")
        print(f"\t\t10.- Examples/Use all")
        print("\n")
        print("\t\t" + "-" * 20)
        print("\t\t99.- Exit")
        print("\t\t" + "-" * 20)
        print("\n")
        selection = input(f"{red}|--------{end}{bblue}({end}{red}-{end}🕵️‍♂️{red}-{end}{bblue}){end}{bblue}/{end}{red}[{end}{yellow}GhostURL{end}{red}]{end}{bblue}/{end}{red}[{end}{purple}Select an option{end}{red}]{end} {green}${end} ")
        if selection == '1':
            print("\n")
            print("\t\t--------(Normal URL obfuscation)--------")
            print("\n")
            nomal_url_ob1 = input(f"{red}|--------{end}{bblue}({end}{red}-{end}🕵️‍♂️{red}-{end}{bblue}){end}{bblue}/{end}{red}[{end}{yellow}GhostURL{end}{red}]{end}{bblue}/{end}{red}[{end}{purple}Paste the fake URL :  {end}{red}]{end} {green}${end} ")
            normal_url_ob2 = input(f"{red}|--------{end}{bblue}({end}{red}-{end}🕵️‍♂️{red}-{end}{bblue}){end}{bblue}/{end}{red}[{end}{yellow}GhostURL{end}{red}]{end}{bblue}/{end}{red}[{end}{purple}Paste the real domain{end}{red}]{end} {green}${end} ")
            print("\n")
            normal_obfuscation = nomal_url_ob1 + "@" +normal_url_ob2
            print(f"[+] Obfuscated URL : {normal_obfuscation}")
            pyperclip.copy(normal_obfuscation)
            print("[+] Copied to Clipboard!")
            print("\n")
            time.sleep(3)

        elif selection == '2':
            print("\n")
            print("\t\t--------(URL Shortener)--------")
            print("\n")
            url_to_short = input(f"{red}|--------{end}{bblue}({end}{red}-{end}🕵️‍♂️{red}-{end}{bblue}){end}{bblue}/{end}{red}[{end}{yellow}GhostURL{end}{red}]{end}{bblue}/{end}{red}[{end}{purple}Paste the URL to Short{end}{red}]{end} {green}${end} ")
            gd_short = gdshortener.ISGDShortener()
            shortened_url = gd_short.shorten(url_to_short)
            print(f"[+] New URL : {shortened_url}")
            pyperclip.copy(shortened_url)
            print(f"[+] Copied to ClipBoard!")
            print("\n")
            time.sleep(3)

        elif selection == '3':
            print("\n")
            print("\t\t--------(IP Obfuscation)--------")
            print("\n")
            url_to_ip = input(f"{red}|--------{end}{bblue}({end}{red}-{end}🕵️‍♂️{red}-{end}{bblue}){end}{bblue}/{end}{red}[{end}{yellow}GhostURL{end}{red}]{end}{bblue}/{end}{red}[{end}{purple}Paste the Domain{end}{red}]{end} {green}${end} ")
            ip_convert = socket.gethostbyname(url_to_ip)
            print(f"[+] IP : {ip_convert}, paste the IP Address in your browser")
            pyperclip.copy(ip_convert)
            print(f"[+] Copied to ClipBoard!")
            print("\n")
            time.sleep(3)
        
        elif selection == '4':
            print("\n")
            print("--------(Hex obfuscation)--------")
            malicious_url_hex =  input(f"{red}|--------{end}{bblue}({end}{red}-{end}🕵️‍♂️{red}-{end}{bblue}){end}{bblue}/{end}{red}[{end}{yellow}GhostURL{end}{red}]{end}{bblue}/{end}{red}[{end}{purple}Paste the URL{end}{red}]{end} {green}${end} ")
            hex_encoded = ''.join('%{:02x}'.format(ord(c)) for c in malicious_url_hex)
            print(f"[+] Obfuscated URL : {hex_encoded}")
            pyperclip.copy(hex_encoded)
            print(f"[+] Copied to ClipBoard!")
            print("\n")
            time.sleep(3)

        elif selection == '5':
            print("\n")
            print("\t\t--------(URL shortener and obfuscation)--------")
            print("\n")
            short_and_ob = input(f"{red}|--------{end}{bblue}({end}{red}-{end}🕵️‍♂️{red}-{end}{bblue}){end}{bblue}/{end}{red}[{end}{yellow}GhostURL{end}{red}]{end}{bblue}/{end}{red}[{end}{purple}Paste the URL to short{end}{red}]{end} {green}${end} ")
            legit_url_short_and_ob = input(f"{red}|--------{end}{bblue}({end}{red}-{end}🕵️‍♂️{red}-{end}{bblue}){end}{bblue}/{end}{red}[{end}{yellow}GhostURL{end}{red}]{end}{bblue}/{end}{red}[{end}{purple}Paste the Fake domain{end}{red}]{end} {green}${end} ")
            gdrequest_short_and_ob = requests.get("https://is.gd/create.php?format=simple&url=" + short_and_ob).text
            final_url_ob_short = legit_url_short_and_ob + "@" + gdrequest_short_and_ob
            print(f"[+] New URL : {final_url_ob_short}")
            pyperclip.copy(final_url_ob_short)
            print(f"[+] URL copied to ClipBoard!")
            print(f"[!] TIP : remove the https:// from the url and put it on the start of the URL")
            print("\n")
            time.sleep(3)

        elif selection == '6':

            print("\n")
            print("\t\t--------(Normal URL obfuscation and IP)--------")
            print("\n")
            ip_and_obfuscation_legitimate_url = input(f"{red}|--------{end}{bblue}({end}{red}-{end}🕵️‍♂️{red}-{end}{bblue}){end}{bblue}/{end}{red}[{end}{yellow}GhostURL{end}{red}]{end}{bblue}/{end}{red}[{end}{purple}Paste the URL to hide{end}{red}]{end} {green}${end} ")
            ip_and_obfuscation_malicious = input(f"{red}|--------{end}{bblue}({end}{red}-{end}🕵️‍♂️{red}-{end}{bblue}){end}{bblue}/{end}{red}[{end}{yellow}GhostURL{end}{red}]{end}{bblue}/{end}{red}[{end}{purple}Paste the Real Domain{end}{red}]{end} {green}${end} ")
            print("\n")
            malicious_url_to_ip = socket.gethostbyname(ip_and_obfuscation_malicious)
            ip_ob2 = ip_and_obfuscation_legitimate_url + "@" + malicious_url_to_ip
            print(f"[+] New URL : {ip_ob2}")
            pyperclip.copy(ip_ob2)
            print(f"[+] URL copied to ClipBoard!")
            print("\n")
            time.sleep(3)

        elif selection == '7':
            print("\n")
            print("\t\t--------(Hex and Obfuscation)--------")
            malicious_url_hex =  input(f"{red}|--------{end}{bblue}({end}{red}-{end}🕵️‍♂️{red}-{end}{bblue}){end}{bblue}/{end}{red}[{end}{yellow}GhostURL{end}{red}]{end}{bblue}/{end}{red}[{end}{purple}Paste the URL To hide{end}{red}]{end} {green}${end} ")
            legit_url_hex =  input(f"{red}|--------{end}{bblue}({end}{red}-{end}🕵️‍♂️{red}-{end}{bblue}){end}{bblue}/{end}{red}[{end}{yellow}GhostURL{end}{red}]{end}{bblue}/{end}{red}[{end}{purple}Paste the Fake Domain{end}{red}]{end} {green}${end} ")
            hex_encoded = ''.join('%{:02x}'.format(ord(c)) for c in malicious_url_hex)
            ob_and_hex_url = legit_url_hex + "@" + hex_encoded
            print(f"[+] New URL : {ob_and_hex_url}")
            pyperclip.copy(ob_and_hex_url)
            print(f"[+] Copied to ClipBoard!")
            print("\n")
            time.sleep(3)

        elif selection == '8':
            print("\n")
            print("\t\t--------(URL obfuscation with #)--------")
            print("\n")
            legitimate_url_ = input(f"{red}|--------{end}{bblue}({end}{red}-{end}🕵️‍♂️{red}-{end}{bblue}){end}{bblue}/{end}{red}[{end}{yellow}GhostURL{end}{red}]{end}{bblue}/{end}{red}[{end}{purple}Paste the Fake Domain{end}{red}]{end} {green}${end} ") 
            malicius_domain_ = input(f"{red}|--------{end}{bblue}({end}{red}-{end}🕵️‍♂️{red}-{end}{bblue}){end}{bblue}/{end}{red}[{end}{yellow}GhostURL{end}{red}]{end}{bblue}/{end}{red}[{end}{purple}Paste the URL to hide{end}{red}]{end} {green}${end} ")
            hasht_ob = legitimate_url_ + "#" + malicius_domain_
            print(f"[+] New URL : {hasht_ob}")
            pyperclip.copy(hasht_ob)
            print(f"[+] Copied To ClipBoard!")
            print("\n")
            time.sleep(3)

        elif selection == '9':

            print("\n")
            print("\t\t--------(URL obfuscation with ?)--------")
            print("\n")
            legitimate = input(f"{red}|--------{end}{bblue}({end}{red}-{end}🕵️‍♂️{red}-{end}{bblue}){end}{bblue}/{end}{red}[{end}{yellow}GhostURL{end}{red}]{end}{bblue}/{end}{red}[{end}{purple}Paste the Fake URL{end}{red}]{end} {green}${end} ") 
            malicious = input(f"{red}|--------{end}{bblue}({end}{red}-{end}🕵️‍♂️{red}-{end}{bblue}){end}{bblue}/{end}{red}[{end}{yellow}GhostURL{end}{red}]{end}{bblue}/{end}{red}[{end}{purple}Paste the URL to hide{end}{red}]{end} {green}${end} ") 
            print("\n")
            interr_ob = legitimate + "?" + malicious
            print(f"[+] New URL : {interr_ob}")
            pyperclip.copy(interr_ob)
            print(f"[+] Copied to ClipBoard!")
            print("\n")
            time.sleep(3)

        elif selection == '10':
            print("\n\n[+] Using All Options...\n\n")
            url = input("[ Enter the URL to hide, ex: iplogger.org] > ")
            url2 = input("[ Enter the Fake URL, ex: youtube.com ] > ")
            print("\n")
            obs = url2 + "@" + url
            print(f"[-] Normal Obfuscation : " + obs)

            gd = requests.get("https://is.gd/create.php?format=simple&url=" + url).text
            print(f"[-] URL Shortener (the url to hide shortened) : {gd}" )

            ip = socket.gethostbyname(url)
            print(f"[-] Access Via IP address (the ip of the url to hide): {ip}")

            hexe = ''.join('%{:02x}'.format(ord(c)) for c in url)
            print(f"[-] Hex Encoded (the URL to hide) : {hexe}")

            gdrequest_short_and_ob = requests.get("https://is.gd/create.php?format=simple&url=" + url).text
            final_url_ob_short = url2 + "@" + gdrequest_short_and_ob
            print(f"[-] Short and Obfuscate : {final_url_ob_short}")


            
            malicious_url_to_ip = socket.gethostbyname(url)
            ip_ob2 = url2 + "@" + malicious_url_to_ip
            print(f"[-] Access Via IP and Obfuscate : {ip_ob2}")


            hex_encoded = ''.join('%{:02x}'.format(ord(c)) for c in url)
            ob_and_hex_url = url2 + "@" + hex_encoded
            print(f"[-] Hex and Obfuscate : {ob_and_hex_url}")

            hasht_ob = url2 + "#" + url
            print(f"[+] Obfuscation with '#' : {hasht_ob}")


            interr_ob = url2 + "?" + url
            print(f"[+] Obfuscation with '?' : {interr_ob}")


        elif selection == '99':
            print("\n\n[!] Exiting the program...")
            break

        
        else:
            print("\n\n[x] Invalid Option!\n")
            time.sleep(1)

        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")





if __name__ == '__main__':
    main()
