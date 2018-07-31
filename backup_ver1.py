import os
import time

# 1. 需要备份的文件与目录将被指定在一个列表中。
source = 'D:\\pythonUpload\\code'
#2. 备份文件必须存储在一个主备份目录中
target_dir='D:\\pythonUpload\\backup'
# 3. 备份文件将打包压缩成 zip 文件。
# 4. zip 压缩文件的文件名由当前日期与时间构成。
target=target_dir+os.sep+time.strftime('%Y%m%d%H%M%S')+'.zip'
# 如果目标目录还不存在，则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
# 5. 我们使用 zip 命令将文件打包成 zip 格式
zip_command='zip -r {0} {1}'.format(target,''.join(source))
# 运行备份
print('zip command is:')
print(zip_command)
if os.system(zip_command)==0:
    print('Successful backup to',target)
else:
    print('Backup FAILED')


'''
这个地方有点蛋疼，必须装GnuWin32，必须在系统变量添加path，目录定位到gnuwin32根目录的bin目录，
然后程序才能运行成功，因为windows系统本身不支持linux压缩命令
'''