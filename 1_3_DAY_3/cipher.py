# ceaser cipher
import string

alphabet = string.ascii_lowercase
print(alphabet)
list1 = []
for i in alphabet:
    list1.append(i)

print(list1)

text = str(input("enter the text which you want to encrypt:")).lower()
shift = int(input("enter the shift of character you want to perform"))

def encrypt_fun(normal_text, shift_num):
    cipher_text = ""
    for i in normal_text:
        shifted = alphabet.index(i) + shift_num
        cipher_text += alphabet[shifted]

    print(cipher_text)

c_text=input("enter the cipher text you get from the encryption:").lower()
def decrypt_fun(cipher_text, shift_num):
    normal_text = ""
    for i in cipher_text:
        shifted = alphabet.index(i) - shift_num
        normal_text += alphabet[shifted]

    print(normal_text)

encrypt_fun(normal_text=text, shift_num=shift)
decrypt_fun(cipher_text=c_text, shift_num=shift)

