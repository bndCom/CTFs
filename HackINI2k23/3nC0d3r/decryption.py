#------------------first part----------------------
flagEncFile = open("flag_encoded", "r")
flagEnc = flagEncFile.read()
#the binary file after first encryption part ----------------------
flagBin = open("binary" , "w")
#--------------------------------------------------

zeroList = ['A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H']
oneList = ['I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'P' , 'Q']
binary = ""
for i in range(len(flagEnc)):
    if flagEnc[i] in zeroList :
        #find position of caracter in the list ----------------------
        position = zeroList.index(flagEnc[i])
        #find repetion of 0 or 1 in binary file --------------
        repeat = position + 1
        binary += '0'*repeat
    elif flagEnc[i] in oneList :
        repeat = oneList.index(flagEnc[i]) + 1
        binary += '1'*repeat   
flagBin.write(binary)
flagBin.close()
flagEncFile.close()
#----------------------second part--------------------------

flagBin = open("binary" , "r")
flag = open("flag" , "wb")
while True:
    byte = flagBin.read(8)
    if not byte:
        break
    #converting '0' and '1' digits to bytes -------------------
    newByte = int(byte , 2).to_bytes(1, 'big')
    flag.write(newByte)

flag.close()
flagBin.close()