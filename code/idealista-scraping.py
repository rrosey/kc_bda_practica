

import scrapy
import json
from scrapy.crawler import CrawlerProcess


#https://www.milanuncios.com/datos-contacto/?usePhoneProxy=0&from=detail&id=316280106


class IdealistaSpider(scrapy.Spider):
    name = 'IdealistaSpider'
    start_urls = ['https://www.idealista.com/venta-locales/madrid-madrid/']
    

    def parse(self, response):
        global articles
        # Aqui scrapeamos los datos y los imprimimos a un fichero
        for article in response.css('article'):
            #if extract_text is not None:
            title_text = clean_text(article.css('div.item-info-container > a ::text').get())
            price_text = clean_text(article.css('span.item-price ::text').get())
            description_text = clean_text(article.css('div.item-description > p.ellipsis ::text').get())
            m2_text = clean_text(article.css('span.item-detail ::text').get())
            contact_text = clean_text(article.css('span.icon-phone ::text').get())
              
            # Print a un fichero
            if title_text is not None:
                print(f"{articles}: {title_text} {price_text} {m2_text} {contact_text}")
                print(f"{title_text};{price_text};{m2_text};{contact_text};{description_text}", file=filep)

            articles = articles + 1

            

        # Aqui hacemos crawling (con el follow)
        # For <a> elements there is a shortcut: response.follow uses their href attribute automatically
        for next_page in response.css('li.next a'):
            yield response.follow(next_page, self.parse)

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'DOWNLOAD_DELAY': 5
})

def clean_text(text):
    if text is not None:
        return text.strip().replace(';',' ').replace('\n',' ')
    else:
        return text

def main():
   
    process.crawl(IdealistaSpider)
    process.start()
    filep.close()

articles = 1
filep = open('.\idealista-locales.csv', 'w', encoding="utf-8")

if __name__ == "__main__":
    main()