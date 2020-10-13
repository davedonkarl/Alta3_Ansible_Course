#!/usr/bin/env python3
## Moving files with SFTP

## import paramiko so we can talk SSH
import paramiko
import os

## where to connect to
t = paramiko.Transport("10.10.2.3", 22) ## IP and port

## how to connect (see other labs on using id_rsa private/public keypairs)
t.connect(username="bender", password="alta3")

## Make an sftp connection object
sftp = paramiko.SFTPClient.from_transport(t)

## iterate across the files within directory
for x in os.listdir("/home/student/Alta3_Ansible_Course/filestocopy/"): # iterate on directory contents
  if not os.path.isdir("/home/student/Alta3_Ansible_Course/filestocopy/"+x): # filter everything that is NOT a directory
    sftp.put("/home/student/Alta3_Ansible_Course/filestocopy/"+x, "/tmp/"+x) # move file to target location

## close the connection
sftp.close() # close the connection

"""
CUSTOMIZATION REQUEST 01 - Edit the script so that it queries the user for the machine to connect to (ask for input) as well as the password and username to use. After the code completes, the script should repeat until the user indicates they are done.

CUSTOMIZATION REQUEST 02 - Add general exception handling to the script. On an error, always attempt to close the connection and print out an message indicating some kind of connection error occured.

CUSTOMIZATION REQUEST 03 - Create a function, movethemfiles(), that is passed sftp as a value. Within this function place the logic found under the comment 'iterate across the files within directory'

CUSTOMIZATION REQUEST 04 - Collect additional input from the user to determine where on the target host the files should be placed. Ensure the target location exists before moving the files.
"""
