from Crypto.Cipher import AES
from base64 import b64encode, b64decode
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from colorama import init, Fore

class Crypt:
 
    def __init__(self, salt='SlTKeYOpHygTYkP3'):
        self.salt = salt.encode('utf8')
        self.enc_dec_method = 'utf-8'
 
    def encrypt(self, str_to_enc, str_key):
        try:
            aes_obj = AES.new(str_key, AES.MODE_CFB, self.salt)
            hx_enc = aes_obj.encrypt(str_to_enc.encode('utf8'))
            mret = b64encode(hx_enc).decode(self.enc_dec_method)
            return mret
        except ValueError as value_error:
            if value_error.args[0] == 'IV must be 16 bytes long':
                raise ValueError('Encryption Error: SALT must be 16 characters long')
            elif value_error.args[0] == 'AES key must be either 16, 24, or 32 bytes long':
                raise ValueError('Encryption Error: Encryption key must be either 16, 24, or 32 characters long')
            else:
                raise ValueError(value_error)
 
    def decrypt(self, enc_str, str_key):
        try:
            aes_obj = AES.new(str_key.encode('utf8'), AES.MODE_CFB, self.salt)
            str_tmp = b64decode(enc_str.encode(self.enc_dec_method))
            str_dec = aes_obj.decrypt(str_tmp)
            mret = str_dec.decode(self.enc_dec_method)
            return mret
        except ValueError as value_error:
            if value_error.args[0] == 'IV must be 16 bytes long':
                raise ValueError('Decryption Error: SALT must be 16 characters long')
            elif value_error.args[0] == 'AES key must be either 16, 24, or 32 bytes long':
                raise ValueError('Decryption Error: Encryption key must be either 16, 24, or 32 characters long')
            else:
                raise ValueError(value_error)

def consoleLog(message, print_success=True, print_time=True):
	if True:
		TIME = ''
		if print_time:
			TIME = f'[{time.strftime("%H:%M:%S", time.localtime())}] '
			TIME = Colorate.Horizontal(Colors.rainbow, TIME)
		if print_success:
			try:
				print(f'{TIME}{Colorate.Horizontal(Colors.yellow_to_red, message)}')
			except TypeError: # when there's a character that can't be logged with python print function.
				sys.stdout.buffer.write(f'{TIME}{Colorate.Horizontal(Colors.rainbow, message)}'.encode('utf8'))
		else:
			try:
				print(f'{TIME}{Fore.RED}{message}')
			except TypeError: # when there's a character that can't be logged with python print function.
				sys.stdout.buffer.write(f'{TIME}{Fore.RED}{message}'.encode('utf8'))