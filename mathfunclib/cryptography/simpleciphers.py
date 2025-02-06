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

def upper_to_lower(_str):
    '''
    Returns the string with no uppercase letters.

    :param _str: The input string

    :returns: A string with no uppercase letters.

    If anything not really helpful except for being
    a helper function.
    '''
    UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
    
    if type(_str)!=str:
        return "Parameter [_str] must be a string."
    
    u_to_l=''
    for i in _str:
        if i in UPPERCASE_LETTERS:
            u_to_l+=LOWERCASE_LETTERS[UPPERCASE_LETTERS.index(i)]
        else:
            u_to_l+=i
    return u_to_l

def lower_to_upper(_str):
    '''
    Returns the string with no lowercase letters.

    :param _str: The input string.

    :returns: A string with no lowercase letters.

    Also not really that useful except for being
    a helper function.
    '''
    UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
    
    if type(_str)!=str:
        return "Parameter [_str] must be a string."
    
    l_to_u=''
    for i in _str:
        if i in LOWERCASE_LETTERS:
            l_to_u+=UPPERCASE_LETTERS[LOWERCASE_LETTERS.index(i)]
        else:
            l_to_u+=i
    return l_to_u

def char_count(_str,LETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'):
    '''
    Returns the count of each character of a string as a dict.

    :param _str: The input string.
    :param LETTERS: Optional, default is the capital English letters
                    followed by the lowercase English letters.
                    You can modify this if using this with index
                    of coincidence functions.

    :returns: The count of each character as a dict.
    '''
    if type(_str)!=str:
        return "Parameter [_str] must be a string."
    if type(LETTERS)!=str:
        return "Optional parameter [LETTERS] must be a string."
    
    d={}
    for i in LETTERS:
        d[i]=0
    for i in _str:
        if i in d:
            d[i]+=1
        else:
            continue
    return d
