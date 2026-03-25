#!/usr/bin/python3

# INET4031
# Winter Douglas
# 11/19/2024
# 3/25/2026

# Import modules:
# os = run system commands
# re = work with regular expressions
# sys = read input from stdin
import os
import re
import sys

def main():
    for line in sys.stdin:

        # Check if the line starts with "#" (comment line), used to skip comments
        match = re.match("^#",line)

        # Split the line into fields using ":" as the separator
        fields = line.strip().split(':')

        # Skip the line if it is a comment or does not have exactly 5 fields
        if match or len(fields) != 5:
            continue

        # Extract user info (username, password, and full name for /etc/passwd format)
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        # Split groups by comma to handle multiple group assignments
        groups = fields[4].split(',')

        # Inform user that account creation is starting
        print("==> Creating account for %s..." % (username))

        # Build command to create user with no password and set user info
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        # Run the command to create the user
        os.system(cmd)

        # Inform user that password is being set
        print("==> Setting the password for %s..." % (username))

        # Build command to set the user's password using passwd
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        # Run the command to set the password
        os.system(cmd)

        for group in groups:
            # If group is not "-", assign user to that group ("-" means no group)
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)

                # Run the command to add user to the group
                os.system(cmd)

if __name__ == '__main__':
    main()
