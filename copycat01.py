#!/usr/bin/env python3
import shutil
import os
# Let's force our Python program to 'start' in the home user directory, which for us will be /home/student/mycode/. This is made possible by calling os.chdir(). This will allow the user to run the program from any location on the system and our script still always start at /home/student/mycode/
print(os.getcwdb())
os.chdir('/home/student/Alta3_Ansible_Course/')
print(os.getcwdb())
# Calling shutil.copy(source, destination) will copy the file at the path source to the folder at the path destination (both source and destination are strings). If destination is a filename it will be used as the new name of the copied file. This function returns a string of the path of the copied file.
shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')

# The shutil.copy() will copy a single file, whereas shutil.copytree() will copy an entire folder and every folder and file contained in it. Calling shutil.copytree(source, destination) will copy the folder at the path source along with all of its files and subfolders to the folder at the path destination. The source and destination parameters are both strings. The function returns a string of the path of the copied folder.
shutil.copytree('5g_research/', '5g_research_backup/')
# The shutil.copytree() call creates a new folder named 5g_research_backup with the same content as the original folder. You have now safely backed up your 5g research! Huzzah!
