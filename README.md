# inet_4031_adduser_script

# INET4031 Add Users Script and User List
## Program Description

This program automates the process of creating user accounts on a Linux system. Instead of manually running multiple commands for each user, the script reads from an input file and creates users, sets their passwords, and assigns them to groups automatically.

Normally, a system administrator would need to run commands like adduser, passwd, and group assignment commands for each user. This script uses those same commands but automates them, saving time and reducing human error.

## Program User Operation

This program works by reading a list of users from an input file and processing each line. For every valid line, it creates a user, sets their password, and assigns them to any specified groups.

To use the program, the user must provide an input file and run the script from the terminal. The script will process each line one at a time and execute the necessary system commands.

## Input File Format

Each line in the input file must follow this format:

username:password:last:first:groups
username = the login name of the user
password = the user’s password
last = last name
first = first name
groups = comma-separated list of groups

Example:

user01:pass01:Last01:First01:group1,group2
Lines that start with # are treated as comments and are ignored
If a line does not have exactly 5 fields, it is skipped
If a user should not be added to any groups, use -

## Command Execution

To run the script, use:

python3 create-users.py < create-users.input

Or, if executable:

./create-users.py < create-users.input

To actually create users on the system, run with sudo:

sudo python3 create-users.py < create-users.input

This is required because creating users and modifying groups requires administrative privileges.

## "Dry Run"

A dry run allows the user to test the script without making any changes to the system.

In a dry run:

The script prints the commands that would be executed
No users are created
No changes are made

This is useful for checking that the input file and script logic are correct before running the commands for real.
