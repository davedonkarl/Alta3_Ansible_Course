#!/usr/bin/env python3
import shutil
import os

# Calling shutil.move(source, destination) will move the file or folder at the path source to the path destination and will return a string of the absolute path of the new location. If destination points to a folder, the source file gets moved into destination and keeps its current filename.
shutil.move('raynor.obj', 'ceph_storage/')

# If there had been a raynor.obj file already in the destination folder ~/home/student/mycode/ceph_storage/ it would have been overwritten. Since it’s easy to accidentally overwrite files in this way, you should take some care when using move().

# Prompt the user for a new name for the kerrigan.obj file.
xname = input('What is the new name for kerrigan.obj? ')

# Rename the current kerrigan.obj file.
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
