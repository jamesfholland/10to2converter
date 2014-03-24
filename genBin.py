#Author: James Holland
#License: MIT (see LICENSE file)

import sys

class Number:
    def __init__(self, value):
        self.value = int(value)
        print "Converting "+str(self.value)+" to binary formats.\n"
        self.mag = getMagnitude(abs(self.value))
        self.sign = getSign(self.value)
        self.onesComp = get1sComplement(self.mag,self.sign)
        self.twosComp = get2sComplement(self.mag,self.sign)
        print "Conversion for "+str(self.value)+" completed.\n"
        

def main():
    with open("numList.txt") as fi:
        numbers = fi.readlines()
    decVal = []

    for i in numbers:
        decVal.append(Number(i))

def getMagnitude(decin):
    print "Calculating binary magnitude"
    binStr = ""
    dec = decin
    while dec > 0:
        remainder = dec % 2
        newdec = dec // 2
        print ""+str(dec) +"/2="+str(newdec)+" with a remainder of "+str(remainder)
        dec = newdec
        binStr = str(remainder) + binStr
    print "The magnitude of "+str(decin)+" is "+binStr
    print ""
    return binStr

def getSign(decin):
    if decin < 0:
        print str(decin)+" is negative so the MSB is 1\n"
        return "1"
    else:
        print str(decin)+" is positive so the MSB is 0\n"
        return "0"

def get1sComplement(mag,sign):
    if sign == "0":
        print "Because the number is positive the 1's complement is '0' followed by the magnitude"
        print "0"+mag
        return "0"+mag
    else:
        print "Because the number is negative the 1's complement is '1' followed by the magnitude inverted. EG 101 -> 010"
        print "1"+getInvertedMag(mag)
        return "1"+getInvertedMag(mag)

def get2sComplement(mag,sign):
    if sign == "0":
        print "Because the number is positive the 2's complement is '0' followed by the magnitude"
        print "0"+mag
        return "0"+mag
    else:
        print "Because the number is negative the 2's complement is '1' followed by the magnitude inverted plus 1. EG 101 -> 010"
        print "1"+add1(getInvertedMag(mag))
        return "1"+add1(getInvertedMag(mag))

def add1(invMag):
    #Convert bin to array
    bitarray = []
    bitStr = ""
    for bit in invMag:
        bitarray.append(bit)
    carry = "1"
    for i in range(len(bitarray)):
        size = len(bitarray)-1
        #print size, i
        curbit = size - i
        if carry == "1" and bitarray[curbit] == "1":
            bitarray[curbit] = "0"
        elif carry == "1":
            bitarray[curbit] = "1"
            carry = "0"
        bitStr = bitarray[curbit] + bitStr
    return bitStr

        
        
def getInvertedMag(mag):
    inverted = ""
    for bit in mag:
        if bit == "1":
            inverted = inverted + "0"
        else:
            inverted = inverted + "1"
    return str(inverted)


if __name__ == "__main__":
        main()
