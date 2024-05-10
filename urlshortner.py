import pyshorteners

url = input("Enter the URL : \n")
print("URL After Shortening :\n",pyshorteners.Shortener().tinyurl.short(url))