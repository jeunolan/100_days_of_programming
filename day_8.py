#ceasar's cipher


'''
Author : Je Nolan 
6/13/2024



Program uses Ceaser Cypher.

Provides a header;

Ask the user if they want to encode or decode.
'''
#hello

'''
Encode function change message by shifting the alphabet letters over by the number requested 
i.e. 
The player asks for the message
then the player is asked for the shifted nuber
i.e.
if the message is "ABC" and the number shifted is 3 the new message becomes
DEF (A(0)-->D(3), B(1)-->E(4), and C(2)-->F(5))

'''


#logo

from secrets import choice


logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]




#ask for message to encode and number of shifts
#create a new function that will combine the other two

def cesear_code (text_message, num_shift,cipher_direction)
    cipher_message = ""
    if cipther_direction == "decode":
        num_shift *= -1 #this will make the direction go the opposite direction
    for letter in text_message:
        position = alphabet.index(letter)
        new_position = alphabet    

    print(f"Here is the {cipher_direction}d result, {cipher_message} ")

'''
def encode (text_message,num_shift):
    cipher_message = ""
    #take text_message paramenter and shit by the number allocated
    #in num_shift
    for letter in text_message:
        position = alphabet.index(letter)
        new_position = position+num_shift
        cipher_message += alphabet[new_position]
    print(cipher_message)

#ask for the message to decode and number of shifts
def decode(text_message, num_shift):
    cipher_message = ""
    for letter in text_message:
        position = alphabet.index(letter)
        new_position = position - num_shift 
        cipher_message += alphabet[new_position]
    print(cipher_message)
'''
print(logo)

end_of_program = False #initial variable assignment
#conduct a while statement that will continue the program until the player types no into the input box

#continue program until the player chooses the no option
while end_of_program == False:
    choice = input("Type 'encode' to encrypt, 'decode' to decrypt\n").lower()
    message = input("Type your message:\n")
    shift =int(input("Type the shift number:\n"))    
   #based upon choice call corresponding function 
    if choice == "encode":
        encode(message,shift)
    else:
        decode(message,shift)
    continue_choice = input("Type 'yes' if you want to go again. Otherwise type 'no'")
    if continue_choice == 'yes':
        continue
    else:
        end_of_program = True

    
