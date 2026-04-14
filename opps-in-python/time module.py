#
import time
print(time.time())
print("__________")

##
import time
print(time.ctime(time.time()))
print("__________")

###
import time
print(time.localtime())
print("__________")

####
import time
print("start")
time.sleep(3)
print("end")
print("__________")

#####
import time
print(time.strftime("%D-%m-%y %h:%m:%S"))