alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# def encrypt(original_text,shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter)+shift_amount
#         shifted_position = shifted_position % len(alphabet)  #this is  necessary because if we add 9 to 25 it will throw error despite of this
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encrypted text: {cipher_text}")
#
# encrypt("ram",3)
# def decrpyt(original_text,shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter)-shift_amount
#         shifted_position = shifted_position % len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the decrypted text: {cipher_text}")
#
# decrpyt("ram",3)

def cypher(original_text,shift_amount,encode_or_decode):
    cipher_text = ""
    if encode_or_decode == "encode":
        shift_amount *= -1
    for letter in original_text:

        if letter not in alphabet:
            cipher_text += letter
        else:

            shifted_position = alphabet.index(letter) - shift_amount
            shifted_position = shifted_position % len(alphabet)
            cipher_text += alphabet[shifted_position]

            print(f"Here is the {encode_or_decode}d text: {cipher_text}")


is_continue = True
while is_continue:
    text = input("Enter the text: ").lower()
    amount = int(input("Enter the amount: "))
    code = input("Enter what you want encode or decode: ")
    cypher(text, amount, code)

    ask = input ("Do you want to continue? (y/n):  \n").lower()
    if ask == "y":
        is_continue = True
    else:
        is_continue = False
