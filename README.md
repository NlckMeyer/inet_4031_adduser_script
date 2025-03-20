# INET4031 Add Users Script and User List

## Program Description

Automating the process of adding users to a system is the aim of this Python script. To establish user accounts, set passwords, and allocate users to the proper groups, an administrator would typically manually run commands like adduser. This procedure can be laborious and prone to mistakes, particularly when handling a big user base. This script automates the procedure, which speeds it up and reduces the likelihood of errors. By receiving input from a file and progressively running the required instructions, the script automates the use of the same fundamental operations (adduser, passwd, and adduser for group assignment) that are normally done manually.

## Program User Operation

The user must first prepare an input file and then execute the Python script in order to use this software. In accordance with the guidelines given in the input file, the script will read the user data, generate user accounts, assign passwords, and group the users into the appropriate categories. For efficiency, the process is automated.

### Input File Format
A list of users and the information that goes with them should be included in the input file. A colon (:) should be used to divide each field, and each line should reflect a distinct user account. The following is the input format:

You have two options if you want to skip a line: either leave it blank or designate it as a comment by prefixing it with the # symbol. The script will disregard lines that include fewer than five fields or that begin with a #.

Simply leave the group and additional_group columns set to - if you do not want a new user to be added to any groups. This instructs the script to create the user and not add them to any groups.

### Command Excuction
You must first make sure the Python script is executable before you can launch the application.
  ./create-users.py < createusers.input
  
The list of users to be added is included in the input file createusers.input, which is sent to the Python script by this command when it executes.

### "Dry Run"
By changing the script to output the commands it would execute rather than actually running them, you may do a "dry run" to see what the script will do without really making any modifications. This enables you to confirm the accuracy of the user information and group assignments prior to creating accounts.

This capability can be manually enabled in the present implementation by enclosing the commands being performed in a simple print statement. The user should make sure that the os.system(cmd) commands are disabled and that the print statements are not commented out if they wish to test the script first. In this manner, the expected commands will be displayed by the script without being executed.
