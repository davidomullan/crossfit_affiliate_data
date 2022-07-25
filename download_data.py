#!/usr/bin/env python

# Description: Scrape data of CrossFit Affiliates (gyms) from crossfit.com
# Data: Name, Country, Address, Website, Org. Type, Effective Date, etc
# Output: .CSV file
# Created By: David O'Mullan
# Created On: 24 July 2022

import requests, json, csv

# Website: JSON list of (50) Crossfit Affiliate data object per page
start_URL = "https://www.crossfit.com/cf/find-a-box.php?page="
# URL can filter by: country, state, city, and org. type
# end_URL = "&country=&state=&city=&type=Commercial"

# Create/Open .CSV file to store affiliate data
data_file = open('data_file.csv', 'w+')
csv_writer = csv.writer(data_file)

# List of potential data points (not guarenteed for each affiliate)
keys = ["aid", "bad_standing", "address", "city", "zip", "country", "country_short_code", "kids", "name", "name_search", "active", "org_type", "show_on_map", "website", "effective_date", "ordernum", "ready_to_link", "status", "photo_version", "photo", "onramp_optin", "latlon", "full_state", "state_code"]

#Create Header Row in .CSV file
csv_writer.writerow(keys)

num_affiliate = 0
i = 1
# Iterate through 200 webpages with Affiliate Data (in JSON format)
# Iterate through affiliate date, set missing values to null
# Write affiliate data to .CSV file
print("Starting Webscraping... (~60sec)")
while i <= 200:

    r = requests.get(start_URL + str(i), allow_redirects=True)
#   r = requests.get(start_URL + str(i) + end_URL, allow_redirects=True)

    # List of Dictionaries; each Dictionary is an Affiliate
    affiliates = r.json()["affiliates"]

    for affiliate in affiliates:
        temp = dict()
        for key in keys:
            if key not in affiliate.keys():
                temp[key] = None
            else:
                temp[key] = affiliate[key]
        csv_writer.writerow(temp.values())
        num_affiliate += 1

    i+=1
    
print("Finished Webscraping!")
print("Number of Affiliates: " + str(num_affiliate))

data_file.close()
