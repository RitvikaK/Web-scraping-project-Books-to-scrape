# ============================================================
# WEB SCRAPING PROJECT: Books to Scrape
# ============================================================

# ------------------------------------------------------------
# 1. Import required libraries
# ------------------------------------------------------------
import pandas as pd
import requests
from bs4 import BeautifulSoup

# ------------------------------------------------------------
# 2. Define base URL and storage container
# ------------------------------------------------------------
base_url = "http://books.toscrape.com"
all_books = []

# ------------------------------------------------------------
# 3. Loop through catalogue pages
#    The website contains 50 pages of books
# ------------------------------------------------------------
for page_num in range(1, 51):  # Pages 1 to 50
    url = f"{base_url}/catalogue/page-{page_num}.html"
    response = requests.get(url)

    # Parse HTML only if request is successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        # ----------------------------------------------------
        # 4. Loop through each book on the page
        # ----------------------------------------------------
        for book in soup.find_all(
            "li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3"
        ):
            # ------------------------------------------------
            # 5. Extract basic book information (list page)
            # ------------------------------------------------
            title = book.find("h3").find("a")["title"]
            price = book.find("p", class_="price_color").text
            rating = book.find("p", class_="star-rating")["class"][1]
            in_stock = (
                book.find("p", class_="instock availability")
                .text.strip()
            )

            # ------------------------------------------------
            # 6. Build individual book URL
            # ------------------------------------------------
            link = book.find("h3").find("a")
            book_url = base_url + "/catalogue/" + link["href"]

            # ------------------------------------------------
            # 7. Request individual book page
            # ------------------------------------------------
            book_response = requests.get(book_url)

            if book_response.status_code == 200:
                book_soup = BeautifulSoup(
                    book_response.content, "html.parser"
                )

                # --------------------------------------------
                # 8. Extract detailed book information
                # --------------------------------------------

                # UPC
                upc = (
                    book_soup.find("th", string="UPC")
                    .find_next("td")
                    .text
                )

                # Stock availability
                stock = (
                    book_soup.find("th", string="Availability")
                    .find_next("td")
                    .text.strip()
                )
               stock_availability=int(stock.split("(")[1].split(" ")[0])

                # Genre (from breadcrumb navigation)
                breadcrumb = book_soup.find(
                    "ul", class_="breadcrumb"
                )
                genre_link = breadcrumb.find_all("a")[2]
                genre = genre_link.text.strip()

                # Description (not all books have one)
                description_tag = book_soup.find(
                    "div", id="product_description"
                )
                if description_tag:
                    description = (
                        description_tag.find_next("p").text
                    )
                else:
                    description = "No description"

                # --------------------------------------------
                # 9. Store extracted data
                # --------------------------------------------
                book_data = {
                    "title": title,
                    "genre": genre,
                    "rating": rating,
                    "price": price,
                    "in_stock": in_stock,
                    "stock_availability":  stock_availability,
                    "description": description,
                    "url": book_url,
                    "upc": upc,
                }

                all_books.append(book_data)

# ------------------------------------------------------------
# 10. Convert to DataFrame (for analysis/export)
# ------------------------------------------------------------
all_books_df=pd.DataFrame(all_books)

# ------------------------------------------------------------
# 11. Clean and format dataset columns
# ------------------------------------------------------------

# Rename and capitalise column headers
all_books_cleaned_df = all_books_df.rename(columns={
    "title": "Title",
    "genre": "Genre",
    "rating": "Rating",
    "price": "Price (GBP)",
    "in_stock": "In Stock?",
    "stock_availability": "Stock Availability",
    "description": "Description",
    "url": "Product URL",
    "upc": "UPC"
})

# Convert rating from text to numeric
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}
all_books_cleaned_df["Rating"] = all_books_cleaned_df["Rating"].map(rating_map)

# Remove currency symbol and convert price to float
all_books_cleaned_df["Price (GBP)"] = (
    all_books_cleaned_df["Price (GBP)"]
    .str.replace("£", "", regex=False)
    .astype(float)
)

# ------------------------------------------------------------
# 12. Download tables into a csv file
# ------------------------------------------------------------

# For the original table before cleaning:
all_books_df.to_csv("books_to_scrape_original.csv", index=False)

# For the final cleaned table: 
all_books_cleaned_df.to_csv("books_to_scrape_cleaned.csv", index=False)
