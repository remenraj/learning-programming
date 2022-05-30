# The Requests module is a third-party module for downloading web pages and files.
# requests.get() returns a Response object.
# The raise_for_status() Response method will raise an exception if the download failed.
# You can save a downloaded file to your hard drive with calls to the iter_content() method.

import requests


# Download a web page
response = requests.get(url="https://www.python.org/")

# status codes:
# 100: Continue
# 200 - OK
# 301 - Moved Permanently
# 302 - Found
# 403 - Forbidden
# 404 - Not Found
# 500 - Internal Server Error
# 503 - Service Unavailable
print(response.status_code)

print(len(response.text))
print(response.text[:500])  # print first 500 characters

response.raise_for_status()  # raise exception if not 200


# # writing to a file
# with open("python.html", "wb") as file_object:  # wb = write binary
#     for chunk in response.iter_content(100000):
#         file_object.write(chunk)    # write 100000 bytes at a time