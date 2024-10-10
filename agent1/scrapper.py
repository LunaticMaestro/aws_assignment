import requests
from lxml import html
from typing import List

def extract_all_li_text() -> List:
    '''Returns top 10 market gainers

    Potential problem, the link does not specifically set the region of finance reporting and hence can get for the region, where lambda is located.

    Returns:
        List of top 10 tickers
    '''
    url = "https://www.google.com/finance/markets/gainers?hl=en&gl=us"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }

    tickers: List = []

    # Send a GET request to the URL
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the content using lxml
        tree = html.fromstring(response.content)

        # Use XPath to extract all 'li' elements
        li_elements = tree.xpath('//li')

        # Extract and print text from each 'li' element
        for index, li in enumerate(li_elements):
            # Adjust the XPath to get the nested div from each li
            nested_divs = li.xpath('.//a/div/div/div[1]/div[1]/div/div')

            # Extract and print text from the nested div if it exists
            for div in nested_divs:
                text = div.text_content().strip()

                # append to list 
                tickers.append(text)

    else:
        print("Failed to retrieve data. Status code:", response.status_code, response.text)

    return tickers[:10] # can work even if None


if __name__ == "__main__":
    extract_all_li_text()