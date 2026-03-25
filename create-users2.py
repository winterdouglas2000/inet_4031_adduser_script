#!/usr/bin/env python3

import os
import re
import sys

def main():

    # Ask user for dry-run mode
    choice = input("Run in dry-run mode? (Y/N): ").strip().upper()
    dry_run = (choice == "Y")

    for line in sys.stdin:

        # Check for comment lines
        match = re.match("^#", line)

        # Split fields
        fields = line.strip().split(':')

        # Handle invalid lines
        if match or len(fields) != 5:
            if dry_run:
                if match:
                    print("Skipping comment line")
                else:
                    print("Error: invalid line (not 5 fields)")
            continue

        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])
        groups = fields[4].split(',')

        print("==> Creating account for %s..." % username)
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        if dry_run:
            print(cmd)
        else:
            os.system(cmd)

        print("==> Setting the password for %s..." % username)
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        if dry_run:
            print(cmd)
        else:
            os.system(cmd)

        for group in groups:
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)

                if dry_run:
                    print(cmd)
                else:
                    os.system(cmd)

if __name__ == '__main__':
    main()
