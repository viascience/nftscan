import binascii
import requests


# Main logic to call the multiple algorithms
def malware_review(algorithm, image_name, services):
    info = []
    malware = 0
    port = 5000
    services.remove("scanner")
    if algorithm == 'all':

        for service in services:   
            response = requests.get(f'http://{service}:{port}', params={"image":image_name})
            if "malware" not in response.json():
                raise Exception(response.json()["info"])
            malware = malware + response.json()["malware"]
            
            info.append({
                "service": service, 
                "stdout": response.json()["info"]
                })
         
        malware = True if malware > 0 else False    

    else:
        
        if algorithm in services:
            response = requests.get(f'http://{algorithm}:{port}', params={"image":image_name})
            malware = response.json()["malware"]
            
            info.append({
                "service": algorithm, 
                "stdout": response.json()["info"]
                })
        else:
            raise Exception("Service not available")
                
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
