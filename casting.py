

def main():
	print('HELLO, my name is Doris and i can encrypt and decrypt messages.')
	message = input("what is the message you have to send/recive: ") 
	while True:
		try:
			shift = int(input("how much would you like to shift by: "))
		except ValueError:
			continue
		if shift:
			while True:
				try:
					men = int(input('would you like...\n1.encrypt\n2,decrypt\n please understand i only know numbers\n'))
				except ValueError:
					continue
				if men:
					if men == 1:
						print('sending you to endrypt')
						en(message, shift)
						break
					elif men == 2:
						print('sending you to decrypt')
						de(message, shift)
						break
					else:
						print('my sensors do not understand, try again')
				else:
					break

def en(message, shift):
	#option = input("")

	encoded= ''
	f = open('encrypt.txt','w')	

	'''for i in range(len(message)):
		  tempv = ord(message[i])
		  tempv = tempv + shift
		  tempv = chr(tempv) 
		  encoded.append(tempv)

	for q in range(len(encoded)):
		print(encoded[q],end='')'''
		
	for n in range(len(message)):
		if message[n].isalpha():
			if message[n].islower():
				num = ord(message[n])+shift
				if num > ord('z'):
					num -= 26
					print(f'new value: {num}')
					encoded += chr(num)
				else:
					encoded += chr(num)

			elif message[n].upper():
				num = ord(message[n])+shift
				if num > ord('Z'):
					num -= 26
					encoded = encoded + chr(num)
				else:
					encoded += chr(num)
			
		elif ord(message[n]) == 32:
			encoded += ' '
			
		else:
			encoded += message[n]

	print("\n","message encoded by {} shifts".format(shift))

	print(encoded)
	print('message has been written to encrypt.txt, its there becouse it secret')
	f.write(encoded)

	f.close()


def de(message, shift):
	encoded = ''
	f = open('encrypt.txt','w')	
	
	for n in range(len(message)):
		if message[n].isalpha():
			if message[n].islower():
				num = ord(message[n])-shift
				if num > ord('z'):
					num += 26
					print(f'new value: {num}')
					encoded += chr(num)
				else:
					encoded += chr(num)

			elif message[n].upper():
				num = ord(message[n])-shift
				if num > ord('Z'):
					num += 26
					encoded = encoded + chr(num)
				else:
					encoded += chr(num)
			
		elif ord(message[n]) == 32:
			encoded += ' '
			
		else:
			encoded += message[n]

	f.write(encoded)
	print('message has been written to encrypt.txt, its there becouse it secret')
	f.close()

def fileREAD():
	message = ''
	file = open('message.txt','r')
	message += file.readline()
	shift = int(input('Enter shift: '))
	file.close()
	de(message, shift)
#abc()
#ascii()

#cipher()

if __name__ == "__main__":
	main()