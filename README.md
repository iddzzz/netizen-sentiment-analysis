# Netizen Thought Analysis
Thought analysis against a community (ahmadiyya community in Indonesia) in the social media in 2021.

## Project Overview
+ Analysing public opinion about the community to help the community prepare and improve future programs
+ Scraped 20k+ social media post samples from twitter using python and selenium
+ Extracted insights about the topics, sentiment, and tweets distribution throughout the year.

## Resources
**Python** version 3.9 \
**Packages:** pandas, selenium, langdetect, matplotlib, seaborn, json, tqdm, scikit-learn \
**Twitter Scraper Github:** https://github.com/iddzzz/twitter-scraper \
**Indonesian Stopwords:** https://github.com/stopwords-iso/stopwords-id

## Web Scraping
Scraped 15000+ tweets from twitter.com. With detail of:

+ Name
+ Username
+ Date
+ Reply to
+ Tweet content
+ Number of replies
+ Number of retweets
+ Number of likes

## Data Cleaning
Cleaned data for further analysis. I did the following tasks:
+ Removed advertisements
+ Removed tweets with languages other than Indonesian
+ Removed mentions and links
+ Transformed values each column into appropriate data type
+ Imputed null values

## Exploratory Data Analysis

### Tweets for one year

## Model Building
+ Optimized clustering model pipeline of Non-negative Matrix Factorization (NMF) and KMeans.

## Results
