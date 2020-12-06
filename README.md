# Wine_ETL



#### ![wine1](Images\wine1.jpg)

#### Extract:

We extracted the wine info from the following  websites:

https://chatham.bottleking.com

​          info extracted: name, country, region, state, varietal, price, description, merchant, address 

https://www.petrocksliquors.com/category_Wine

​          info extracted: name, country, region, sub_region, grape_varietal, bottle_price, sale_price, description, 		  address 

https://garyswine.com/api/v1/products/search.json

​		 info extracted : name, country, region, state, varietal, price, description, merchant, address, age, sku, 		 type, subtype



#### Transform:

**individual csv cleanup**:

Chatham data: already was part of the scraping code

Gary's wine data: dropped columns to match Chatham data, checked for duplicate

Petrocks data: renamed and dropped columns to match with others, checked for empty rows, checked for duplicates

**final clean up**:

loaded all CSVs, checked for data type, converted price column from an object to float type, appended all data 

#### Load:





---------------------------------------------------------------------------------------------------------------------------------------------------

##### All necessary steps to recreate your database when someone clones our repository:



**Step1-** run the following files (Scrapping and API calls (Chrome is needed))

brian_garyswine_json.ipynb

- ​	produces: garys_wine_real2.csv

petrockswine.ipynb

- ​	produces: petrocks_wine_final.csv

bottleking_scraper.ipynb

- ​	produces: chathambottlekingcleaned.csv

  

- 

**Step2-** run the following notebook:

Clean_up_CSV.ipynb

produces: Allwine.csv

**Step3-**