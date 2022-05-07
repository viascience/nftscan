import binascii


# Main logic to call the multiple algorithms
def _scan(algorithm, image_name, services):
    info = []
    malware = 0
    port = 5000
    
    if algorithm == 'all':

        for service in services:        
            response = request.get('http://service:{port}', params={image:"image_name"})
            malware = malware + response.malware
            
            info.append({
                "service": services, 
                "info": response.info
                })
         
        malware = True if malware > 0 else False    

    else:
        
        if algorithm in services:
            response = request.get('https://algorithm:{port}', params={image:"image_name"})
            malware = response.malware
            
            info.append({
                "service": algorithm, 
                "info": response.info
                })
        else:
            raise Except("Service not available")
                
    return {
        "malware": malware, 
        "info": info
        }


# Quick scan for injected php or JS comments
#def quick_scan(image_name):
#    with open(filename, 'rb') as f: 
#        content = f.read() 
#        if binascii.hexlify(b'<?php') in binascii.hexlify(content): 
#            print('PHP found') 
    
#        if binascii.hexlify(b'/*') in binascii.hexlify(content) and binascii.hexlify(b'*/') in binas
#cii.hexlify(content): 
#            print('JS found')
