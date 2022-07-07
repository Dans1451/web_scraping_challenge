## web_scraping_challenge

mission_to_mars.ipynb is the jupyter note book that has the code to scrape the requested data.

I used nbconvert to get a workable python script. I renamed this script to scrape_mars.py as requested.

the mongoDB database is "scraping_challenge" and the collection is "scraped".

The image ofr my final application is in the images folder.

I have included the index.html, the app.py, and the scrape_mars.py even though they are not requested on the instructions. 

##I corrected the issue. The index.html would not load without information the DB for some reason. I have looked at others code and cannot figure out why mine wont load and others will. I fixed the issue by forcing a round of scraping when the flask API loads. Please do not deduct me for this unless you can thoroughly explain why it wont load without it. Also the instructions are very unclear which hemisphere images to pull. I pulled the main one off of each page. 
