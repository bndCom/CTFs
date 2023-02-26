flagEncFile = open("flag_encoded", "r")
flagEnc = flagEncFile.read()
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
#----------------------------------------------------

flagBin = open("binary" , "r")
flag = open("flagDec" , "wb")
while True:
    byte = flagBin.read(8)
    if not byte:
        break
    newByte = int(byte , 2).to_bytes(1, 'big')
    flag.write(newByte)

flag.close()
flagBin.close()








# Defining BinarytoDecimal() function
# def BinaryToDecimal(binary):
        
#     binary1 = binary
#     decimal, i, n = 0, 0, 0
#     while(binary != 0):
#         dec = binary % 10
#         decimal = decimal + dec * pow(2, i)
#         binary = binary//10
#         i += 1
#     return (decimal) 

#----------------------------------------------------

# def binToStr(binary):
#     flagDec = ""
#     while true:
#         byte = 

    # for i in range(0 , len(binary) - 8 , 8):
    #     byte = binary[i:i+8]
    #     byte = int(byte)
    #     dec = BinaryToDecimal(byte)
    #     carac = chr(dec)
    #     string += carac
#     return string



# bin = creatBinary(flagEnc)
# flagFile = binToStr(bin)
# open("trueFlag.gif" , "w").write(flagFile)

