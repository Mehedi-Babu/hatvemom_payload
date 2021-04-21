#!/usr/bin/env python3

import os
import sys
import argparse

from core.payload import PayloadGenerator

parser = argparse.ArgumentParser()
parser.add_argument('--format', dest='format', help='Platform to generate for.')
parser.add_argument('--arch', dest='arch', help='Architecture to generate for.')
parser.add_argument('--shellcode', dest='shellcode', help='Shellcode to inject.')
parser.add_argument('-o', '--output', dest='output', help='File to output generated payload.')
args = parser.parse_args()

if __name__ == '__main__':
    if args.format and args.arch and args.shellcode:
        pg = PayloadGenerator()
        filename = args.output if args.output else 'a.out'

        if os.path.exists(args.shellcode):
            with open(args.shellcode, 'rb') as f:
                shellcode = f.read()
        else:
            print(f"[-] Shellcode file not found!")
            sys.exit(1)

        print(f"[i] Target format: {args.format}")
        print(f"[i] Target architecture: {args.arch}")

        print("[*] Generating payload...")
        payload = pg.generate(args.format, args.arch, shellcode)

        if payload is None:
            print(f"[-] Incorrect format or architecture specified!")
            sys.exit(2)

        print(f"[i] Final payload size: {str(len(payload))}")
        print(f"[*] Saving payload to {filename}...")
        with open(filename, 'wb') as f:
            f.write(payload)
        print(f"[+] Payload saved to {filename}!")
        sys.exit(1)
    else:
        print("[-] No format, architecture and shellcode specified!")

    print("[-] Failed to generate payload!")
    sys.exit(1)