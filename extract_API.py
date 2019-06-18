import requests

#url
url = 'https://api.data.gov/ed/collegescorecard/v1/schools?school.name=boston%20college&api_key=<insert_your_api_key_here'

#make get request and save in result object
result = requests.get(url)

#check status code [#200 is success]
result.status_code

#Headers
result.headers

#data in text form
result.text

#data in json form
result.json()

