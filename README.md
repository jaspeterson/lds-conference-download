# Conference Download

This is a tool to download all LDS conference talks as text files. It's a python web scraper utilizing the BeautifulSoup library, written in python 3. For instructions on downloading this library, see their [documentation.](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

Note: The execution time is terrible because if too many requests are sent to [lds.org](https://www.lds.org/) too quickly, it won't serve the request. To counteract this, I added a function to create a random wait time of .1 to .5 seconds before requesting each talk page. Thus the horrible execution time. 