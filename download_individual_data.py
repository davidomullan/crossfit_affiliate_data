#!/usr/bin/env python

# Description: Scrape data of CrossFit Affiliates (gyms) from crossfit.com
# Data: Name, Address, Phone, Website, etc
# Output: .CSV file
# Created By: David O'Mullan
# Created On: 24 July 2022

import requests, json, csv, time

# Website: JSON data for one (1) Crossfit Affiliate with Affiliate ID in URL
start_URL = "https://map.crossfit.com/getAffiliateInfo.php?aid="

# Create/Open .CSV file to store affiliate data
data_file = open('individual_data_file.csv', 'w+')
csv_writer = csv.writer(data_file)

# List of potential data points (not guarenteed for each affiliate)
keys = ["name", "website", "address", "city", "state", "zip", "country", "cfkids", "phone", "courses", "trainers"]

#Create Header Row in .CSV file
csv_writer.writerow(keys)

num_affiliate = 0

# Affiliate IDs were not assigned numerically, so IDs are significantly higher that active gym numbers (scrapping 40000 webpages is time consuming!)
# Recommend max_aid = 100 for sample set, 31000 to scrape all data.
max_aid = 100
i = 1

# Iterate through up to 31000 webpages with Crossfit Affiliate Data (JSON format)
# Ignore empty webpages (Disaffiliate gym data deleted)
# Iterate through affiliate date, set missing values to null
# Write data to .CSV file
start = time.time()
print("Start Webscraping...")
while i < max_aid:

    r = requests.get(start_URL + str(i), allow_redirects=True)

    # List of one (1) dictionary with affiliate data
    affiliate = r.json()
    
    if not (affiliate["name"]==None):
        num_affiliate += 1
        temp = dict()
        for key in keys:
            if key not in affiliate.keys():
                temp[key] = None
            else:
                temp[key] = affiliate[key]
        csv_writer.writerow(temp.values())
        
    i+=1

end = time.time()
print("Finished Webscraping!")
print("Time: " + str(end-start))
print("Number of Affiliates: " + str(num_affiliate))

data_file.close()
