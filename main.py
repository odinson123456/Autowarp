from utils import *

pkg="com.google.android.youtube"
tools()
print("Tools Downloaded")

filename, title = downloadapk(pkg)
dat = patchdet()
print("Apks downloaded and Git details written")
logs = build(filename,pkg)
print("Build Done..")
wlogs(filename,title,logs)
print("Logs written")
