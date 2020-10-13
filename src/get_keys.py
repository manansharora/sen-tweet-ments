#!/usr/bin/env python3

api = input("Enter your consumer API key\n")
print("\n")
secret = input("Enter your consumer secret API key\n")

with open("keys.txt", "w") as f:
	f.write(api + "\n" + secret)

f.close()
