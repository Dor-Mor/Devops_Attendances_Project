#!/usr/bin/env python3
import os
import pysftp
from stat import S_ISDIR, S_ISREG
from dotenv import load_dotenv

load_dotenv()

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
sftp = pysftp.Connection(os.getenv("REMOTE_IP"), username=os.getenv("REMOTE_USERNAME"),
                         password=os.getenv("REMOTE_PASSWORD"), cnopts=cnopts)


def get_r_portable(sftp, remotedir, localdir, preserve_mtime=False):
    for entry in sftp.listdir(remotedir):
        remotepath = remotedir + "/" + entry
        localpath = os.path.join(localdir, entry)
        mode = sftp.stat(remotepath).st_mode
        if S_ISDIR(mode):
            try:
                os.mkdir(localpath)
            except OSError:
                pass
            get_r_portable(sftp, remotepath, localpath, preserve_mtime)
        elif S_ISREG(mode):
            sftp.get(remotepath, localpath, preserve_mtime=preserve_mtime)


remote_path = os.getenv("REMOTE_PATH")
local_path = os.getenv("LOCAL_PATH")

get_r_portable(sftp, remote_path, local_path, preserve_mtime=False)
