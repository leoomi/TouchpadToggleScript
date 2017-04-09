import os
from gi.repository import Notify
Notify.init ("Touchpad")

id = os.popen("xinput --list --id-only 'ETPS/2 Elantech Touchpad'").read()

if(os.path.isfile("/tmp/touchpad")):
   f = open("/tmp/touchpad", "r+")
else:
   os.system("echo \"on\" >> /tmp/touchpad")


if('on' in f.read()):
    os.system("xinput -disable " + id)
    f.seek(0)
    f.write("off")
    notification=Notify.Notification.new("Touchpad: Off")
else:
    os.system("xinput -enable " + id)
    f.seek(0)
    f.write("on")
    notification=Notify.Notification.new("Touchpad: On")

notification.show ()
f.truncate()    
f.seek(0)
print(f.read())
f.close()
