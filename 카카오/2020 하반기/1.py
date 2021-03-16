import re
new_id = "...!@BaT#*..y.abcdefghijklm"
new_id = re.sub('\.\.+', '.', new_id)
print(new_id)
new_id = re.sub('[^a-z0-9-_.]', '', new_id)
print (new_id)
