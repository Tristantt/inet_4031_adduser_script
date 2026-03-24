#!/usr/bin/python3

# INET4031
# Your Name
# Date Created
# Date Last Modified
# 
# This script reads a colon-separated input file from stdin, 
# creates user accounts, sets passwords, and assigns groups.
# The script supports a dry-run mode where commands are printed 
# instead of executed for safe testing.

import os   # Execute system commands to create users, set passwords, and manage groups
import re   # Regular expressions for detecting comment lines in input
import sys  # Access stdin for reading the input file line by line

def main():
    # Read each line from the input file provided via stdin
    for line in sys.stdin:

        # Check if the line starts with a '#' character (comment line)
        # Lines starting with '#' are skipped
        match = re.match("^#", line)

        # Remove leading/trailing whitespace and split the line into fields by colon
        # Expected format: username:password:UID:FullName:groups
        fields = line.strip().split(':')

        # Skip line if it is a comment OR does not have exactly 5 fields
        if match or len(fields) != 5:
            continue

        # Extract user information from the fields
        username = fields[0]  # Username
        password = fields[1]  # Password
        # Full name formatted for the GECOS field used by adduser
        gecos = "%s %s,,," % (fields[3], fields[2])

        # Extract the list of groups (comma-separated) for this user
        groups = fields[4].split(',')

        # --- Create the user account ---
        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        # Dry-run: print command instead of executing
        print("DRY RUN: %s" % cmd)
        # Uncomment the next line to actually create the user
        # os.system(cmd)

        # --- Set the user password ---
        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        # Dry-run: print command instead of executing
        print("DRY RUN: %s" % cmd)
        # Uncomment the next line to actually set the password
        # os.system(cmd)

        # --- Assign user to additional groups ---
        for group in groups:
            # Skip placeholder '-' (no group) entries
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                # Dry-run: print command instead of executing
                print("DRY RUN: %s" % cmd)
                # Uncomment the next line to actually add user to the group
                # os.system(cmd)

if __name__ == '__main__':
    main()