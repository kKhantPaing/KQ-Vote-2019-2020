#encrypt Algo for qr
import qrcode
import hashlib as h
n=1
li=[]
while n<5:
    rollno="1A-"+str(n)
    roll=rollno.split("-")
    no=roll[1].encode("utf-8")
    encText=""
    rn=h.md5(rollno.encode("utf-8")).hexdigest()
    encText+=rn[:2]
    encText+=rn[21:23]
    encText+=h.md5(no).hexdigest()[30:]
    cT=rollno+"@gmail.com"+" "+encText
    #img = qrcode.make(cT)
    #img.save(rollno+'.png')
    print(cT)
    li.append(cT)
    n+=1
print("Done!")
