import typing

def encryp_rot13(_str):
    '''
    Encrypts a string using ROT13
    
    :param _str: The input string.
    
    :returns: The string encrypted using ROT13
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM'
    
    if type(_str)!=str:
        return "Parameter [_str] must be a string."
    
    Rot13=''
    for i in _str:
        if i in alphabet:
            Rot13 += alphabet[alphabet.index(i) + 13]
        else:
            Rot13 += i
    return Rot13

def encryp_rotN(_str,N=13):
    '''
    Encrypts a string using ROT-N

    :param _str: The input string
    :param N:    What ROT function we are using. By default,
                 this is 13.
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXY'
    
    if type(_str)!=str:
        return "Parameter [_str] must be a string."
    if type(N)!=int:
        return "Parameter [N] must be an integer."
    if (N<1) or (N>25):
        return "Disallowed integer values detected."
    
    RotN=''
    for i in _str:
        if i in alphabet:
            RotN+=alphabet[alphabet.index(i)+N]
        else:
            RotN+=i
    return RotN

def decryp_rotN(_str,N=13):
    '''
    Decrypts a string using ROT-N

    :param _str: The input string to decrypt
    :param N:    What ROT function we decrypt with.
                 By default, this is 13.

    :returns: The decrypted string. Note that we could
              simply encrypt with ROT(26-N) to also
              decrypt the text.
    '''
    alphabet = 'ZYXWVUTSRQPONMLKJIHGFEDCBAZYXWVUTSRQPONMLKJIHGFEDCBzyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcb'
    
    if type(_str)!=str:
        return "Parameter [_str] must be a string."
    if type(N)!=int:
        return "Parameter [N] must be an integer."
    if (N<1) or (N>25):
        return "Disallowed integer values detected."
    
    RotN=''
    for i in _str:
        if i in alphabet:
            RotN+=alphabet[alphabet.index(i)+N]
        else:
            RotN+=i
    return RotN
