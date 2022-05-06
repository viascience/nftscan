import binascii


# Main logic to call the multiple algorithms
def _scan(algorithm, image_name, services):
    info = []
    malware = 0
    
    if algorithm == 'all':
        for num, i in enumerate(services):
        
            port = 5000 + num
		    response = request.get('https://127.0.0.1:{port}', params={image:"image_name"})
		    malware = malware * response.malware
		    
		    info.append({
		        "service": services[0], 
		        "info": response.info
		        })
		        
		    return {
		      "malware": malware, 
		      "info": info
		      }
	else:
	    port = 5000 + services.index(algorithm)
        response = request.get('https://127.0.0.1:{port}', params={image:"image_name"})
		malware = response.malware
		    
		info.append({
		        "service": algorithm, 
		        "info": response.info
		        })
		        
		return {
		      "malware": malware, 
		      "info": info
		      }


# Quick scan for injected php or JS comments
def quick_scan(image_name):
    with open(filename, 'rb') as f: 
        content = f.read() 
        if binascii.hexlify(b'<?php') in binascii.hexlify(content): 
            print('PHP found') 
    
        if binascii.hexlify(b'/*') in binascii.hexlify(content) and binascii.hexlify(b'*/') in binas
cii.hexlify(content): 
            print('JS found')
