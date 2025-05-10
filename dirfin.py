#!/usr/bin/env python3

import requests
import sys

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

def discover_directories(target_url, wordlist_file):
    with open(wordlist_file, "r") as wf:
        for line in wf:
            word = line.strip()
            test_url = target_url + "/" + word
            response = request(test_url)
            if response:
                print("[+] Discovered URL --> " + test_url)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <target_url> <wordlist_file>")
        sys.exit()

    target_url = sys.argv[1]
    wordlist_file = sys.argv[2]
    discover_directories(target_url, wordlist_file)
