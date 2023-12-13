
import requests

       url = "https://openlibrary.org/search.json"

       response = requests.get(url)

       data = response.json()
	print(data)
