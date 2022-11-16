#!/usr/bin/env python3

import os
import paramiko
from dotenv import load_dotenv

load_dotenv()

def download_csv():
	try:
	    os.mkdir(os.getenv('LOCAL_PATH'))
	except:
	    print(os.getenv('LOCAL_PATH') + "ALREADY EXIST")
	# download files
	transport = paramiko.Transport((os.getenv('REMOTE_IP'), 22))
	transport.connect(username=os.getenv('REMOTE_USERNAME'),
			  password=os.getenv('REMOTE_PASSWORD'))
	sftp = paramiko.SFTPClient.from_transport(transport)

	for file in sftp.listdir(path=os.getenv('REMOTE_PATH')):
		sftp.get(os.path.join(os.getenv('REMOTE_PATH'),file),
			 os.path.join(os.getenv('LOCAL_PATH'), file))

	sftp.close()
	transport.close()
