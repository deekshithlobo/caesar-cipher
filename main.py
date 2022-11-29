from functions import encode, decode
while(True):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  if direction == 'encode':
    encode(text,shift)
  elif direction == 'decode':
    decode(text,shift)
  else:
    print('Invalid Input!')
  print("\n--------Press CTRL+C to stop--------\n")