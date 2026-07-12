name = input("enter your real name")
gadget = input("enter your favourite gadget")
agentnumber = 7
missioncount = 15
height = 1.65
isactive = True

print("Name is",name)
print("gadget is",gadget)
print("agent number",agentnumber)

fn = name[0:3]
print(fn)
ln = name[-1:]
print(ln)
secret = fn + ln

print(secret)
rs = gadget[::-1]
print(rs)
code = fn + ln + rs
print(code)