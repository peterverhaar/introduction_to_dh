# https://eur03.safelinks.protection.outlook.com/?url=https%3A%2F%2Ffilesender.surf.nl%2F%3Fs%3Ddownload%26token%3D262afbf5-db16-4e61-b275-05cca192fa14&data=05%7C01%7CP.A.F.Verhaar%40library.leidenuniv.nl%7C0c0b5c43f51c4f312cde08da6335ae69%7Cca2a7f76dbd74ec091086b3d524fb7c8%7C0%7C0%7C637931379465346283%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=zJMpQWlWIBPtrRfQHht7BWlV9JWGRuNGav8VpME0o%2F0%3D&reserved=0

urls_dict = { 'https://raw.githubusercontent.com/peterverhaar/python_tutorial/main/12%20Visualisation.ipynb':'12 Visualisation.ipynb',
 'https://raw.githubusercontent.com/peterverhaar/twitter_tutorial/main/Twitter.ipynb':'Twitter.ipynb' }

import requests

for link in urls_dict:
    response = requests.get(link)
    if response.status_code == 200:
        with open( urls_dict[link] , 'w' , encoding = 'utf8' ) as fh:
            fh.write( response.text )
        
