import argparse
import re
import os

class Plugboard:
    def __init__(self, connections):
        self.wiring = self.decodePlugboard(connections)
    
    def getWiring(self):
        return self.wiring
    
    # Taking in the string of letter pairs and decoding
    # them into the numerical mapping of the characters
    def decodePlugboard(self,connections):
        if connections==None or connections=="":
            return self.IdentityPlugboard()
        
        pairings=re.split("[^a-zA-z]",connections)
        mapping=self.identityPlugboard()
        pluggedChars=[]
        
        # First, check for if the number of pairings
        # is greater than 13 (the max amount possible)
        if len(pairings)>=13:
            print("Too many pairings detected!")
            return self.IdentityPlugboard()
        
        # Now to check if the number of chars in each pairing
        # is equal to 2. If there is one that isn't, we return
        # the identity plugboard.
        for pair in pairings:
            if len(pair)!=2:
                return self.IdentityPlugboard()
            
            # Else, force uppercase and convert to ascii
            c1=ord(str(pair[0]).upper())-65
            c2=ord(str(pair[1]).upper())-65
            
            # Check if either of our characters already have a plug.
            if c1 in pluggedChars or c2 in pluggedChars:
                return self.IdentityPlugboard()
            
            # Else, append.
            pluggedChars.append(c1)
            pluggedChars.append(c2)
            
            # Now, update the mapping.
            mapping[c1]=c2
            mapping[c2]=c1
            
        # Return the completed mapping
        return mapping
    
    # Now, the identity plugboard.
    def IdentityPlugboard(self):
        mapping=[]
        for i in range(26):
            mapping.append(i)
        return mapping
    
    # Finding all plugboard letters that do not have a plug in them
    def getUnpluggedChars(self,connections):
        unplugged_chars=[]
        for i in range(26):
            unplugged_chars.append(i)
        
        if "" in connections:
            return unplugged_chars
        
        pairings=re.split("[^a-zA-z]",connections)
        
        for pair in pairings:
            c1=ord(str(pair[0]).upper())-65
            c2=ord(str(pair[0]).upper())-65
            unplugged_chars.remove(c1)
            unplugged_chars.remove(c2)
        return unplugged_chars
    
    # Method for returning the wiring
    def forward(self,c):
        return chr((self.wiring[ord(c)-65])+65)

def create_plugboard(connections):
    return Plugboard(connections)

class Reflector:
    def __init__(self,encoding):
        self.fWiring=self.decodeWiring(encode)
    
    def decodeWiring(self,wiring):
        dwires=[]
        for char in wiring:
            dwires.append(char)
        return dwires
    def forward(self,c):
        return self.fWiring[ord(c)-65]

# Function for creating a reflector
def create_reflector(name):
    ref_list = {
        # Commercial Enigma A,B
        "IC": Reflector("DMTWSILRUYQNKFEJCAZBPGXOHV"),
        "IIC": Reflector("HQZGPJTMOBLNCIFDYAWVEUSRKX"),
        "IIIC": Reflector("UQNTLSZFMREHDPXKIBVYGJCWOA"),
        # Regular M3 Reflectors
        "B": Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT"),
        "C": Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL"),
        # Kriegsmarine M4 "Thin" Reflectors
        "Bthin": Reflector("ENKQAUYWJICOPBLMDXZVFTHRGS"),
        "Cthin": Reflector("RDOBJNTKVEHMLFCWZAXGYIPSUQ"),
        # Default "Identity" Reflector
        "Identity": Reflector("ZYXWVUTSRQPONMLKJIHGFEDCBA")
    }
    return ref_list.get(name, "Identity")

class Rotor:
    def __init__(self, name, wiring, rPos, nPos, rRing):
        self.name = name
        self.fWiring = self.decode(wiring)
        self.bWiring = self.iDecode(wiring)
        self.rPos = int(rPos)
        self.nPos = int(nPos)
        self.rRing = int(rRing)
    
    # Returns rotor wheel number
    def getName(self):
        return self.name
    
    # Returns current position of rotor
    def getPos(self):
        return self.rPos
    
    def getRingSetting(self):
        return slef.rRing
    
    def decode(self,wiring):
        dWires=[]
        for char in wiring:
            dWires.append(char)
        return dWires
    
    def idecode(self,wiring):
        NEW_MAPPING = ['']*26
        for char in wiring:
            CUR_POS_ARR = self.fWiring.index(char)
            MAP_LET_NUM = ord(char)-65
            NEW_MAP[MAP_LET_NUM]=chr(CUR_POS_ARR+65)
        return NEW_MAP
    
    def encipher(self,k,wire_map,rtrA):
        k=ord(k)-65
        aOffset=k-rtrA.rPos
        bInput=aOffset+self.rPos
        map_inp=bInput-self.rRing
        map_inp_cons=(map_inp+26)%26
        map_out=wire_map[map_int_cons]
        map_out_chr=ord(map_out)-65
        map_out=map_out_chr+self.rRing
        map_out_cons=(map_out+26)%26
        return chr(map_out_cons+65)
    
    def forward(self,c,rtrA):
        return self.encipher(c,self.fWiring,rtrA)
    
    def backward(self,c,rtrA):
        return self.encipher(c,self.bWiring,rtrA)
    
    def is_at_notch(self):
        if self.name=="VI" or self.name=="VII" or self.name=="VIII":
            return self.rPos==12 or self.rPos==25
        else:
            return self.nPos==self.rPos
    
    def turnover(self):
        self.rPos = (self.rPos + 1)%26

def create_rotor(name, rPos, rRing):
    # Bodged Case Switch that returns a Rotor Object depending on which of the 9
    # available rotors is wanted, and will set it's initial Ring Position (rPos), 
    # the Notch Position (nPos) and the Ring Setting (rRing)
    rotor_list = {
        "I": Rotor("I", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", rPos, 16, rRing),
        "II": Rotor("II", "AJDKSIRUXBLHWTMCQGZNPYFVOE", rPos, 4, rRing),
        "III": Rotor("III", "BDFHJLCPRTXVZNYEIWGAKMUSQO", rPos, 21, rRing),
        "IV": Rotor("IV", "ESOVPZJAYQUIRHXLNFTGKDCMWB", rPos, 9, rRing),
        "V": Rotor("V", "VZBRGITYUPSDNHLXAWMJQOFECK", rPos, 25, rRing),
        # Rotor's 6, 7 and 8 all use 2 notch position, at 12 (M) and 25 (Z)
        "VI": Rotor("VI", "JPGVOUMFYQBENHZRDKASXLICTW", rPos, 0, rRing),
        "VII": Rotor("VII", "NZJHGRCXMYSWBOUFAIVLPEKQDT", rPos, 0, rRing),
        "VIII": Rotor("VIII", "FKQHTLXOCBJSPDZRAMEWNIUYGV", rPos, 0, rRing),
        # Default Return
        "Identity": Rotor("Identity", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", rPos, 0, rRing)
    }
    return rotor_list.get(name, "Identity")

class Enigma():
    def __init__(self,rotors,ringPos,ringSet,reflector,plugboard):
        self.lRotor = create_rotor(rotors[0],ringPos[0],ringSet[0])
        self.mRotor = create_rotor(rotors[1],ringPos[1],ringSet[1])
        self.rRotor = create_rotor(rotors[2],ringPos[2],ringSet[2])
        
        self.reflector = create_reflector(reflector)
        self.plugboard = create_plugboard(plugboard)
        self.etw = create_rotor("Identity",0,0)
        
        def rotate(self):
            if self.rRotor.is_at_notch():
                if self.mRotor.is_at_notch():
                    self.mRotor.turnover()
                    self.lRotor.turnover()
                self.mRotor.turnover()
            self.rRotor.turnover()
        
        def encipher(self,c):
            self.rotate()
            plug_out=self.plugboard.forward(c)
            
            # Pass the plain text through the rotors left to right.
            c1 = self.rRotor.forward(plug_out,self.etw)
            c2 = self.mRotor.forward(c1,self.rRotor)
            c3 = self.lRotor.forward(c2,self.mRotor)
            
            rotor_out = self.etw.forward(c3,self.lRotor)
            
            # New character is now reflected
            c4 = self.reflector.forward(rotor_out)
            
            # Back through the rotors
            c5 = self.lRotor.backward(c4,self.etw)
            c6 = self.mRotor.backward(c5,self.lRotor)
            c7 = self.rRotor.backward(c6,self.mRotor)
            rotor_out = self.etw.backward(c7,self.rRotor)
            
            # Finally, we pass it through the plugboard
            c8 = self.plugboard.forward(rotor_out)
            
            # Return the enciphered character.
            return c8
        
        def encrypt(self,pText):
            pText = self.sanitize_input(pText)
            cText = ""
            for c in pText:
                cText += self.encipher(c)
            spaced_ctext = ""
            count = 0
            for c in cText:
                count+=1
                spaced_cText += c
                if count%5==0:
                    spaced_cText+=" "
            return spaced_cText
        
        def sanitize_input(self,pText):
            pText = pText.upper()
            pText = pText.strip()
            pText = pText.replace(" ","")
            pText = pText.replace("."," STOP")
            
            any_non_cap = re.findall("[^A-Z]",pText)
            if len(any_non_cap)!=0:
                print("Plaintext contains non-alphabetical characters.")
                print("Removing all non-alphabetical characters...")
                for i in any_non_cap:
                    pText = pText.replace(i,"")
            print("Sanitized input: "+pText)
            return pText
        
        def get_rotor_positions(self):
            positions = {
                self.rRotor.getName(): self.rRotor.getPos(),
                self.mRotor.getName(): self.mRotor.getPos(),
                self.lRotor.getName(): self.lRotor.getPos(),
            }
            return postions

def main():
    # Create the argument parser to handle user input
    parser = argparse.ArgumentParser(description="Encrypts a text file using an implementation of the Enigma Machine")
    
    # Adding the positional arguments needed to create the Enigma machine
    parser.add_argument("Rotors", help="""Select which 3 rotors, left to right, you want to be used. Given as a string of Roman Numerals: "I II III" """)
    parser.add_argument("rPos", help="""Choose the Rotor's initial rotor position. Given as a string: "B X K" """)
    parser.add_argument("rSet", help="""Setting the Ring Position of each Rotor. Given as a string: " V G T" """)
    parser.add_argument("Reflector", help="""Choosing the reflector. Given as a string: "B" """)
    parser.add_argument("Plugboard", help="""Setting Plugboard Wiring, with a max of 13 pairs. Given as a string of pairs: "AF HV ZI QF" """)
    
    # Positional Arguments
    parser.add_argument("-rf", "--readfile", nargs="?", const="", help="Reads in Cipher Text from a specified file, or plaintext.txt if no file is specified")
    parser.add_argument("-wf", "--writefile", nargs="?", const="", help="Writes the output of the machine to a specified file, or to ciphertext.txt if on file is specified")
    # Parsing Arguments into the program
    args = parser.parse_args()
    
    # Create an instance of the Enigma machine
    enig = Enigma(re.split("[a-zA-z]",args.Rotors),split_chars(args.rPos),split_chars(args.rSet),args.Reflector,args.Plugbaord)
    
    # Checking if the user wanted to read the plaintext from a file
    if args.readfile == "":
        print("No plaintext file specified, attempting to read from plaintext.txt")
        pText = getpText('plaintext.txt')
        if pText == "":
            print("Nothing found in plaintext.txt!")
    
    elif args.readfile != None:
        if os.path.exists(args.readfile):
            pText = getpText(args.readfile)
    
    print("Plaintext is: "+pText)
    cText = enig.encrypt(pText)
    print("Encrypted Plaintext!")
    
    if args.writefile == "":
        print("No output file specified, attempting to write to ciphertext.txt...")
        if writecText(cText,'ciphertext.txt'):
            print("Written ciphertext to: "+"ciphertext.txt")
        else:
            print("Error writing file")
    
    # Checking if the user wanted to write output to a file
    elif args.writefile != None:
        if writecText(cText,args.writefile):
            print("Written ciphertext to: "+str(args.writefile))
        else:
            pritn("Error writing to: "+str(args.writefile))

def getpText(pTextPath):
    try:
        pText = open(pTextPath,"r")
        pTextContents = pText.read()
        pText.close()
    except FileNotFoundError:
        print("File " + pTextPath + " not found. Please try again. :(")
    return pTextContents

def writecText(cText, cTextPath):
    with open(cTextPath, "w") as pTextFile:
        pTextFile.write(cText)
    return True

def split_chars(rPos):
    split = re.split("[^a-zA-Z]",rPos)
    for i in range(len(split)):
        split[i] = ord(split[i])-65
    return split

main()
