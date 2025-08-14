import smtplib
from bs4 import BeautifulSoup
import requests
# import os
#from os.path import join, dirname
#from dotenv import load_dotenv

# URL = "https://appbrewery.github.io/instant_pot/"
URL = "https://www.amazon.com/ASUS-ROG-Strix-Gaming-Laptop/dp/B0CRDCXRK2?_encoding=UTF8&content-id=amzn1.sym.860dbf94-9f09-4ada-8615-32eb5ada253a&dib=eyJ2IjoiMSJ9.gJTc8SYDg-MUdo8YYdHG41HSfh_SN16T43ZldtulBXBLcGp-66ze3ljL7GPRWCBdofIWJvRJCH9nG9OsULO_fDGUXLGfd69FHBOAF2biYYbDMv_zQEJnB0z6nW3L94cY8pMw1XvLCogmvNL4RyDW-HXTOzSF8nu03K3wpCVCAjOgNfcEGhd3a1QTNaLQn1XsXcdAkYzcyYeDgLNDg2v-7__4_vtYDVc3pVKh9qyUGE-tl3fFfcLxKbtx8pZDvlNUz17YxA_q-ENgCiEc5OBje8AgKzdsSUeMR7yA9E9Xiq3VVk6cmg0_28-B7zEVMVIUEQJLGkT58rpl4Lz3Jp-olz9pd3sRxN7Nv6wHvQ1x4mc.hwexUJq5iKKVCA5vA6cpJKQ4QLXSnq9FachHojKs4gE&dib_tag=se&keywords=gaming&pd_rd_r=10a960ea-4ff6-4543-a2f1-0bb06f22e768&pd_rd_w=nv9V8&pd_rd_wg=anQ54&qid=1739611784&refinements=p_123%3A219979%7C247341&rnid=85457740011&s=electronics&sr=1-2&th=1"

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

response = requests.get(url = URL, headers=header)

soup = BeautifulSoup(response.content , "html.parser")

price = soup.find(class_="a-offscreen").get_text()

clear_price = price.split("$")[1]

float_price = float(clear_price)
print(float_price)

title = soup.find(id="productTitle").get_text().strip()
print(title)

Buy_Price = 1400

# dotenv_path = join(dirname("./security"), '.env')
# load_dotenv(dotenv_path)

# smtp_address = os.environ.get("SMTP_ADDRESS")
# email = os.environ.get("EMAIL")
# app_password = os.environ.get("APP_PASSWORD ")

smtp_address = "smtp.gmail.com"
email = ""
app_password = ""

if float_price <= Buy_Price:
    message = f"{title} is on sale for {price}!"

    with smtplib.SMTP(smtp_address, port=587) as connection:
        connection.starttls()
        result = connection.login(email, app_password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )
