ch = input("caracter:")
if ch.isalpha():
    if ch.isupper():
        print("Es letra mayúscula")
    else:
        print("Es letra minúscula")
elif ch.isdigit():
    print("Es número")
else:
    print("No es letra ni número")