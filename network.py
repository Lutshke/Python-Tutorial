"To request a website we use the request module"

import requests

# there are a few methods how to interact with websites
# if your using a api look into the documentation to know which method to use ["get", "post", "delete", "put"]

r = requests.get("google.de") #this sends a request to google

# we can now access informations about that website with the variable "r"

r.status_code # this will show the status code of the website
r.content # will show the source of the html
r.text # this will output all visible text