#!/usr/bin/python
import os
import time
source = ['"D:\pythonUpload\code"']
target_dir = 'D:\\pythonUpload\\backup'
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
comment = input('Enter a comment -->')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ','_')+'zip'
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory',today)
zip_command = "zip -qr {0} {1}".format(target,' '.join(source))

if os.system(zip_command) == 0:
    print('Successful backup to',target)
else:
    print('Backup FAILED')
