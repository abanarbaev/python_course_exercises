phrase="о не очкуй!" # очко!
plist=list(phrase)
print(phrase)
print(plist)
for i in range(4):
    plist.pop(1)
"""
plist.remove(" ")
plist.remove(" ")
plist.remove("н")
plist.remove("е")
"""
plist.remove("у")
plist.remove("й")
plist.extend([plist.pop(0),plist.pop(3)])
pli="".join(plist)
print(plist)
print(pli)
