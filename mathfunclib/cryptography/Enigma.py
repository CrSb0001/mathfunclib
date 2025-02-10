import re

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
