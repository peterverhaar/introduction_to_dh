urls_dict = { 'https://raw.githubusercontent.com/peterverhaar/python_tutorial/main/12%20Visualisation.ipynb':'12 Visualisation.ipynb',
 'https://raw.githubusercontent.com/peterverhaar/twitter_tutorial/main/Twitter.ipynb':'Twitter.ipynb'
            }

import requests

for link in urls_dict:
    response = requests.get(link)
    if response.status_code == 200:
        with open( urls_dict[link] , 'w' , encoding = 'utf8' ) as fh:
            fh.write( response.text )
        
