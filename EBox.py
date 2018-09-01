
class EBox:
    ''' The EBox class encrypts or decrypts string based on the users request.
        The mode tells EBox to encrypt or decrypt; the level determines how hard
        the encryption algorithm should be; the position is an integer which
        determines the next position in the password we will use; the password
        is a string which is used in the Viginère algorithm; and number of
        characters is an integer which tells us how many characters have been
        encrypted or decrypted since the last reset.
    '''
    
    alphabet = "ABCDEFGHIIJKLMNOPQRSTUVWXZ0123456789"
    
    def __init__(self):
        self.mode = "encrypt"
        self.level = 0
        self.pos = 0
        self.password = ""
        self.numChars = 0
        self.offset = 0
        self._debug = False

    def set_password(self, password=""):
    ''' This method sets the password that will be used.'''
        self.password = password
        self.pos = 0

    def reset(self, mode, level):
    ''' This method sets number of characters to 0, and takes in the new mode and
    level. Also sets position to 0.'''
        self.numChars = 0
        self.mode = mode
        slef.level = level
        self.pos = 0

    def _cryptChar(self, char):
    ''' This is an instance method that encrypts or decrypts one character using
    the next letter of the password; this is called by encrypt() and decrypt().
    It uses self.mode and self.level and self.pos.'''
        pass

    def _clean_line(string):
    ''' This is a class method that preprocesses a string: it removes any
    character except what is in the alphabet. It also uppercases the string.'''
        newString = ""
        for char in string:
            if char in alphabet:
                newString += char
        return newString

    def encrypt(self, line):
    ''' This method encrypts one line using the given password and level.
    If the mode is not "encrypt" then it raises an exception.'''
        if self.mode != "encrypt":
            raise Exception("Mode must be encrypt")
        line.replace("  ","").upper()
        cleanLine = EBox._clean_line(line)
        cryptLine = ""
        for char in cleanLine:
            cryptLine += self._cryptChar(char)
            numChars += 1
        return cryptLine

    def decrypt(self, line):
    ''' This method decrypts one line using the given password and level.
    If the mode is not "decrypt" then it raises an exception.'''
        if self.mode != "decrypt":
            raise Exception("Mode must be decrypt")
        pass

    def get_status(self):
    ''' This method returns a tuple: (mode, level, password length, position,
                number of characters encrypted or decrypted since last reset)'''
        status = (self.mode, self.level, len(self.password),
                  self.position, self.numChars)        
        return status

    def restart(self):
    ''' This method restarts the encryption machine by setting position and number
    of characters to 0. This is necessary whenever you encrypt/decrypt a file.'''
        self.pos = 0
        self.numChars = 0
        pass
    
