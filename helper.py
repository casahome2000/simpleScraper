import requests

def keyword_search(page, keyword):
    pagetext = requests.get(page).text

    count = pagetext.count(keyword)
    if count > 0:
        msg = 'Page: %s has the keyword: %s ( %s times )' % (page, keyword, str(count))
        category = 'success'
        return msg, category
    else:
        msg = 'Page does NOT contain the keyword: %s.' % keyword
        category = 'danger'
        return msg, category


# print(keyword_search("https://www.airbnb.com/about/about-us", 'villa'))


#TODO: need to write out to CSV file
#TODO: migrate to asyncio for speed - http://compiletoi.net/fast-scraping-in-python-with-asyncio.html
#TODO: need to take in multiple websites and search keyword
#TODO: add method to take in multiple keywords
#TODO: add method to take in 'phrase' as keyword
#TODO: return count for number of occurance
#TODO: move / POST to dedicated Endpoint (Scraping as a Service)

