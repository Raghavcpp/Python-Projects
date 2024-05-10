import webbrowser as wb
import os
from dotenv import load_dotenv, dotenv_values 
load_dotenv() 

def workautoWEB():
    Chrome_path = os.getenv('chromePath') + ' %s'
    URLS = ("stackoverflow.com",
            "github.com/Raghavcpp",
            "gmail.com",
            "google.com",
            "youtube.com")
    for url in URLS:
        wb.get(Chrome_path).open(url)

def workauto():
    app_path= os.getenv("appPath")
    os.startfile(app_path)
# workautoWEB()
workauto()