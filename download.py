urls_dict = { 'https://edu.nl/h6khn':'Visualise_tweets.ipynb',
        'https://edu.nl/mkgtu':'tweets.tsv',
        'https://edu.nl/he7hh':'hash_tags.csv' }

import requests

for link in urls_dict:
    response = requests.get(link)
    if response.status_code == 200:
        with open( urls_dict[link] , 'w' , encoding = 'utf8' ) as fh:
            fh.write( response.text )
