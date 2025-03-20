#!/usr/bin/python3

# INET4031
# Nick
# 03/20/25
# 03/20/25

# To handle input/output, regular expressions, and system commands, respectively, import the os, re, and sys modules.
import os
import re
import sys

#YOUR CODE SHOULD HAVE NONE OF THE INSTRUCTORS COMMENTS REMAINING WHEN YOU ARE FINISHED
#PLEASE REPLACE INSTRUCTOR "PROMPTS" WITH COMMENTS OF YOUR OWN

def main():
    for line in sys.stdin:

        #The regular expression looks for a comment, which is usually indicated by a '#' at the beginning of the line.
        #If it's a comment, the matched line will be in the match variable; if not, it will be None.
        match = re.match("^#",line)

        print("The contents of the match variable were: ",match)
        #Remove any leading or trailing whitespace and split the line by ':'; save the segments in 'fields'.
        fields = line.strip().split(':')

        print("Length of fields was: ", len(fields))
        #Skip this line if it has fewer than five fields or is a comment (beginning with '#'). Only legitimate lines in the right format (user data) are processed thanks to this logic.
        if match or len(fields) != 5:
            continue

        #Retrieve the GECOS data, username, and password from the fields.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #Print a notification that the process of creating a user account is underway.
        print("==> Creating account for %s..." % (username))
        #Get the command ready to create the user with the given username and GECOS data.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #To really create the user account, run the command (uncomment this line to perform the command).
        #The first time you run the code...what should you do here?  If uncommented - what will the os.system(cmd) statemetn attempt to do?
        #print cmd
        os.system(cmd)

        #Print a message with the user account's password setup.
        print("==> Setting the password for %s..." % (username))
        #Use sudo and echo to get the command ready to set the user's password.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #Set the user's password by running the command (uncomment this line to perform the program).
        #The first time you run the code...what should you do here?  If uncommented - what will the os.system(cmd) statemetn attempt to do?

        #print cmd
        os.system(cmd)

        for group in groups:
            #Verify that the group does not contain '-'. The user should be added to this group if it isn't '-'.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                os.system(cmd)

if __name__ == '__main__':
    main()
