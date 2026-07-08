# INET4031 Add Users Script and User List

## Program Description

Normally if you want to add a user on Linux, you'd manually run `adduser` to make the account, `passwd` to set their password, and `adduser <user> <group>` for each group they need. That's fine for one user, but annoying if you have a whole list of people to add.

This script automates all of that. It reads a list of users from a file and runs those same commands for each one:

1. `adduser --disabled-password --gecos '<Full Name>' <username>` – creates the account
2. `passwd <username>` (with sudo) – sets their password
3. `adduser <username> <group>` – adds them to whatever groups they need

So instead of typing all that out by hand for every user, you just run the script once against a file.

## Program User Operation

The script reads the user list from stdin, one line per user, and does the three steps above for each one. It also has a dry-run mode built in so you can check what it's going to do before it actually does it.

### Input File Format

Each line = one user, 5 fields separated by colons:

```
username:password:LastName:FirstName:groups
```

Example:
```
user04:pass04:Last04:First04:group01
user06:pass06:Last06:First06:group01,group02
```

- Want to skip a line? Put a `#` at the start of it, script ignores it.
- Don't want the user in any groups? Use `-` instead of a group name.
- If a line doesn't have exactly 5 fields (like a typo or missing field), it just gets skipped automatically.

### Command Execution

Make it executable first:
```
chmod +x create-users.py
```

Then run it against your input file:
```
./create-users.py < create-users.input
```

It'll go line by line and print out what it's doing as it creates accounts, sets passwords, and adds groups.

### "Dry Run"

By default it's a dry run — it just prints the commands instead of actually running them, so you can check everything looks right first.

If you actually want it to create the accounts for real, you have to go into the script and uncomment the `os.system(cmd)` lines. Do the dry run first though, so you're not creating a bunch of broken accounts if the input file's messed up.
