# 📚 Books to Scrape – Web Scraping Project

## Overview
This project scrapes book data from the publicly available website **Books to Scrape**, a site designed for practicing web scraping techniques.

The goal of the project is to demonstrate end-to-end web scraping skills using Python, including:
- Navigating multi-page listings
- Extracting structured and semi-structured data
- Following links to scrape detailed item-level information
- Preparing analysis-ready datasets

---

## Objectives
- Scrape all books listed on the website (50 pages)
- Extract both **summary-level** and **detail-level** information
- Preserve raw scraped data
- Produce a cleaned dataset suitable for analysis and visualisation

---

## Data Collected
For each book, the following attributes are extracted:

- **Title**
- **Genre**
- **Price (GBP)**
- **Rating**
- **In Stock** (textual availability)
- **Number Available** (numeric stock count)
- **Product description**
- **UPC (Universal Product Code)**
- **Product page URL**

---

## Tools & Libraries
- **Python**
- **Requests**
- **BeautifulSoup (bs4)**
- **Pandas**

---


---

## How It Works
1. The script iterates through all catalogue pages on the website.
2. Basic book information is scraped from listing pages.
3. Each individual book page is accessed to extract detailed metadata.
4. Raw scraped data is stored without modification.
5. A cleaned version of the dataset is produced with:
   - Standardised column names
   - Numeric ratings
   - Numeric prices
   - Parsed stock availability

---

## Output Data
- **Raw dataset**: Preserves the original scraped values.
- **Cleaned dataset**: Analysis-ready version with cleaned and typed fields.

> *Both datasets are included to demonstrate a simple but realistic data preparation pipeline.*

---

## Notes & Limitations
- This project is intended for **educational and portfolio purposes only**.
- The target website explicitly allows scraping.
- Request throttling and retry logic are not implemented.
- Due to file size, CSV previews may not fully render in GitHub’s interface; files can be downloaded directly for inspection.

---

## Possible Improvements
- Refactor code into reusable functions
- Add request retries and rate limiting
- Implement logging
- Perform exploratory data analysis and visualisation

---

## Author
**Ritvika Kedia**
