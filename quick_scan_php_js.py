import binascii

filename = "test_JackSparrow"
filename = "test.php.jpg"

with open(filename, 'rb') as f: 
    content = f.read() 
    if binascii.hexlify(b'<?php') in binascii.hexlify(content): 
        print('PHP found') 
    
    if binascii.hexlify(b'/*') in binascii.hexlify(content) and binascii.hexlify(b'*/') in binas
cii.hexlify(content): 
        print('JS found')
