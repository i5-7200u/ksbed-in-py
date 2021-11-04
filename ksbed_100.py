import base64
print("KCS String Base64 Encoder/Decoder 1.0.0-^")
print("Islem secin / Choose a operation")
print("1-Encoding \n2-Decoding")
select = int(input())
if select == 1:
    print("Write the to be encoding string / Base64 ile kodlanacak yaziyi yazin")
    thestring = str(input())
    thebyte = str.encode(thestring, "utf-8")
    print(str(base64.b64encode(thebyte), "ASCII"))
elif select == 2:
    print("Write the to be decoding base64 string / Dekodlanacak Base64 ciktisini yazin")
    thebyte = base64.b64decode(str(input()))
    print(str(thebyte, "utf-8"))
else:
    print("Write the to be encoding string / Base64 ile kodlanacak yaziyi yazin")
    thestring = str(input())
    thebyte = str.encode(thestring, "utf-8")
    print(str(base64.b64encode(thebyte), "ASCII"))