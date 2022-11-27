# import module
import csv
import requests
import pandas as pd
from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join
import streamlit as st


# user define function
# Scrape the data
HEADERS = ({'authority': 'www.amazon.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            # Requests sorts cookies= alphabetically
            # 'cookie': 'session-id=139-9978160-2094439; i18n-prefs=USD; sp-cdn="L5Z9:NL"; ubid-main=135-8743642-6494819; lc-main=en_US; session-id-time=2082787201l; skin=noskin; session-token="0mBt/h7EqXD6xGumzPUS7MFMSJ4PDbOZdIm9fNocUyWIxauBYfAYUDBiKYKqMLi8/ZSbgaDxJe+wnFIjV/ho3jHgwVS+4TmC/p+LHzuMFzWg6LpGEy6q6hMqT/17oaat1LmBo4oUhGRhZCOiogSEj8IZKi8iYF3JclE28ySVRcXD9O+U21hetfiCkg4DuUsjjhMLKqaDRUZW0OyUMqGOyg=="; csm-hit=tb:K0XD93VFTZP1BSV626R2+s-2QRMNXX0AAYYZSZF1X7S|1653824505514&t:1653824505514&adb:adblk_yes',
            'device-memory': '8',
            'downlink': '1.1',
            'dpr': '1',
            'ect': '4g',
            # 'referer': 'https://www.amazon.com/Cycling-Gloves-Bike-Men-Shock-Absorbing/dp/B08VRKTP28/ref=sr_1_8?crid=1ZZEV65PFSKTF&keywords=bike%2Bglove&qid=1653822777&sprefix=bike%2Bglove%2Caps%2C450&sr=8-8&th=1',
            'rtt': '150',
            'sec-ch-device-memory': '8',
            'sec-ch-dpr': '1',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-viewport-width': '1920',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
            'viewport-width': '1920', })


def getdata(url):
    r = requests.get(url, headers=HEADERS)
    return r.text


def html_code(url):
    # pass the url
    # into getdata function
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata, 'html.parser')
    return (soup)


def customer_review(url, limit=100):
    st.sidebar.info("Scraping the data from the url")

    url_review = url.split("/")[0] + "/" + \
                 url.split("/")[1] + "/" + \
                 url.split("/")[2] + "/" + \
                 url.split("/")[3] + "/" + \
                 "product-reviews/" + \
                 url.split("/")[5] + "/" + "ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews&sortBy=recent&pageNumber=1"
        
    data_str = ""

    while True:

        soup = html_code(url_review)
        all_reviews = soup.find_all("span", class_="a-size-base review-text review-text-content")

        for item in all_reviews:
            data_str = data_str + item.get_text()

        next_page = soup.find_all("li", class_="a-disabled a-last")
        if next_page:
            break

        else:
            temp_url = url_review.split("=")
            now = str(int(temp_url[-1]) + 1)
            temp_url[-1] = now
            url_review = ("=".join(temp_url))
            st.sidebar.write("🔗", f"page {int(now)-1} is being scraped")
        limit -= 1
        if limit == 0:
            break
    result = data_str.split("\n")

    rev_result = []
    for i in result:
        if i == "":
            pass
        else:
            rev_result.append(i)

    return rev_result


def get_review(url, limit=100):
    product_review = {}
    item_review = customer_review(url, limit)

    product_review["title"] = str(" ".join((url.split("/")[3]).split("-")))
    product_review["comments"] = str([str(row) for row in item_review if row != ""])
    product_review["url"] = url

    filename = "available-reviews/" + url.split("/")[3] + ".csv"
    pd.DataFrame(product_review, index=[0]).to_csv(filename, index=False)
    return product_review

def get_available_files():
    file_names = []
    for file in listdir("available-reviews"):
        if file.endswith(".csv"):
            file_names.append(file)
    return file_names
