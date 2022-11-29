alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def number_in_range(asc,shift):
  while (asc+shift)>122:
    n = asc+shift-122+96
    if n > 96 and n<123:
      return n
    else:
      number_in_range(n,shift)

def decode_beyond(asc,shift):
  while (asc-shift)<97:
    n = asc-shift+122-96
    if n > 96 and n<123:
      return n
    else:
      number_in_range(n,shift)

def encode(msg,shift):
  ls=list(msg)
  encrypted_text=[]
  for item in ls:
    asc = ord(item)
    if asc in range(97,123):
      if asc+shift > 122:
        asc = number_in_range(asc,shift)
        encrypted_text.append(chr(asc))
      else:
        encrypted_text.append(chr(asc+shift))
    else: 
      encrypted_text.append(item)
  print('Encrypted text is -> ',''.join(encrypted_text))


def decode(msg,shift):
  ls=list(msg)
  encrypted_text=[]
  for item in ls:
    asc = ord(item)
    if asc in range(97,123):
      if asc-shift < 97:
        asc = decode_beyond(asc,shift)
        encrypted_text.append(chr(asc))
      else:
        encrypted_text.append(chr(asc-shift))
    else: 
      encrypted_text.append(item)
  print('Encrypted text is -> ',''.join(encrypted_text))
