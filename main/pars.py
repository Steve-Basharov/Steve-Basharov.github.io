from bs4 import BeautifulSoup
import requests as req
    
resp = req.get("https://www.youtube.com/watch?v=4U0xJrNCKvk&t=145s")
 
soup = BeautifulSoup(resp.text, 'lxml')

text = soup.title.text