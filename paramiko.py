#-*- coding:utf-8 -*-
import paramiko

s = paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.connect('ip address', 22, username='username', password='pass', timeout=4)

sftp = s.open_sftp()
sftp.put('/source/x.jpg', '/remote-source/x.jpg')
sft.close()