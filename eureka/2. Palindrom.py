


def checkPalindrome(word) :
        if word == " ":
            return True
        
        else:
            word = word.lower()
            word.replace(" ","")

            def letters(input):
                return ''.join(filter(str.isalpha,input))
            
            new = letters(word)

            rev = new[::-1]

            if rev == new:
                return True
            
            else:
                return False
