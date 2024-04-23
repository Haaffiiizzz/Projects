import urllib3
import io


url = "https://eclass.srv.ualberta.ca/portal/"

web = urllib3.request("GET", url, preload_content= False)
web.auto_close = False


with open("HTML", "w") as file:
    for line in io.TextIOWrapper(web):
        file.write(line)
