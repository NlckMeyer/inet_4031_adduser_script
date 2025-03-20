#!/usr/bin/python3

#INET4031
#Nick
#03/20/25
#03/20/25

#To handle input/output, regular expressions, and system commands, respectively, import the os, re, and sys modules.
import os
import re
import sys

#YOUR CODE SHOULD HAVE NONE OF THE INSTRUCTORS COMMENTS REMAINING WHEN YOU ARE FINISHED
#PLEASE REPLACE INSTRUCTOR "PROMPTS" WITH COMMENTS OF YOUR OWN

def main():
    #Ask the user if they want to run normally or in dry run mode.
    #Read from /dev/tty to ensure the prompt is interactive even when input is redirected.
    print("Would you like to run the code in 'dry-run' mode? (Y/N): ", end="", flush=True)
    with open('/dev/tty', 'r') as tty:
        dry_run = tty.readline().strip().upper()
    dry_run = dry_run == 'Y'  #Convert input to boolean (True for dry-run, False for normal execution)

    for line in sys.stdin:
        #The regular expression looks for a comment, which is usually indicated by a '#' at the beginning of the line.
        #If it's a comment, the matched line will be in the match variable; if not, it will be None.
        match = re.match("^#", line)

        print("The contents of the match variable were: ", match)
        #Remove any leading or trailing whitespace and split the line by ':'; save the segments in 'fields'.
        fields = line.strip().split(':')

        print("Length of fields was: ", len(fields))

        #Skip this line if it has fewer than five fields or is a comment (beginning with '#'). 
        #Only legitimate lines in the right format (user data) are processed thanks to this logic.
        if match or len(fields) != 5:
            if dry_run:
                #In dry-run mode, print messages for skipped lines (comments or invalid lines).
                if match:
                    print("==> Skipping line (comment):", line.strip())
                else:
                    print("==> Error: Line does not have enough fields:", line.strip())
            continue

        #Retrieve the data, username, and password from the fields.
        username = fields[0]
        password = fields[1]
        lastname = fields[2]
        firstname = fields[3]
        groups = fields[4].split(',')  # Split groups by comma

        #Construct the GECOS field using first name and last name.
        gecos = f"{firstname} {lastname},,,"

        #Print a notification that the process of creating a user account is underway.
        print("==> Creating account for %s..." % (username))

        #Get the command ready to create the user with the given username and GECOS data.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        #Execute the command or print it in dry-run mode.
        if dry_run:
            #In dry-run mode, print the command that would have been executed.
            print("==> Dry-run: Would execute command:", cmd)
        else:
            #In normal execution mode, execute the command to create the user.
            os.system(cmd)

        #Print a message with the user account's password setup.
        print("==> Setting the password for %s..." % (username))

        #Use sudo and echo to get the command ready to set the user's password.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        #Execute the command or print it in dry-run mode.
        if dry_run:
            #In dry-run mode, print the command that would have been executed.
            print("==> Dry-run: Would execute command:", cmd)
        else:
            #In normal execution mode, execute the command to set the password.
            os.system(cmd)

        #Process groups for the user.
        for group in groups:
            #Verify that the group does not contain '-'. The user should be added to this group if it isn't '-'.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)

                #Execute the command or print it in dry-run mode.
                if dry_run:
                    #In dry-run mode, print the command that would have been executed.
                    print("==> Dry-run: Would execute command:", cmd)
                else:
                    #In normal execution mode, execute the command to add the user to the group.
                    os.system(cmd)

if __name__ == '__main__':
    main()
