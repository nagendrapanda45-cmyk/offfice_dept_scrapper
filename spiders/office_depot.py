import scrapy
from office_depot_scraper.items import CrawledIndexItem, ScrappedProductItem
from datetime import datetime
import time

class OfficeDepotSpider(scrapy.Spider):
    name = "office_depot"
    allowed_domains = ["officedepot.com.mx"]
    start_urls = ["https://www.officedepot.com.mx/officedepot/en/Categor%C3%ADa/Todas/computo/laptops-y-macbook/c/04-039-0-0"]

    def parse(self, response):
        # Crawled Index Item
        index_item = CrawledIndexItem()
        index_item["product_url"] = response.url
        index_item["country"] = "Mexico"
        index_item["crawler_name"] = self.name
        index_item["currency"] = "MXN"
        index_item["domain_name"] = "officedepot.com.mx"
        index_item["http_status"] = response.status
        index_item["lang_code"] = "es-MX"
        index_item["lang_id"] = "es"
        index_item["pagination_url"] = response.url
        index_item["processed_date"] = datetime.now().strftime("%Y-%m-%d")
        index_item["retailer_id"] = "office_depot_mx"
        index_item["retailer_name"] = "Office Depot Mexico"
        index_item["scrap_datetime"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        index_item["scrap_timestamp"] = int(time.time())
        index_item["status"] = False
        yield index_item

        # Extract product links
        product_links = response.css("div.product-tile a.product-name::attr(href)").getall()
        for link in product_links:
            yield response.follow(link, callback=self.parse_product)

        # Handle pagination
        next_page = response.css("a.next::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_product(self, response):
        product_item = ScrappedProductItem()
        product_item["product_url"] = response.url
        product_item["brand"] = response.css("span.brand-name::text").get(default="").strip()
        product_item["breadcrumb"] = " > ".join(response.css("div.breadcrumb a::text").getall())
        product_item["category"] = "Laptops y Macbook"
        product_item["country"] = "Mexico"
        product_item["crawler_name"] = self.name
        product_item["currency"] = "MXN"
        product_item["description"] = response.css("div.product-description::text").get(default="").strip()
        product_item["display_technology"] = response.css("div.specs:contains('Pantalla')::text").get(default="").strip()
        product_item["domain_name"] = "officedepot.com.mx"
        product_item["ean"] = response.css("span.ean::text").get(default="").strip()
        product_item["graphics_card"] = response.css("div.specs:contains('Tarjeta gráfica')::text").get(default="").strip()
        product_item["http_status"] = response.status
        product_item["key_features"] = response.css("ul.key-features li::text").getall()
        product_item["lang_code"] = "es-MX"
        product_item["memory"] = response.css("div.specs:contains('Memoria')::text").get(default="").strip()
        product_item["mpn"] = response.css("span.mpn::text").get(default="").strip()
        product_item["operating_system"] = response.css("div.specs:contains('Sistema operativo')::text").get(default="").strip()
        product_item["pagination_url"] = self.start_urls[0]
        product_item["price"] = response.css("span.price::text").get(default="").strip()
        product_item["processed_date"] = datetime.now().strftime("%Y-%m-%d")
        product_item["processor_brand"] = response.css("div.specs:contains('Procesador')::text").get(default="").strip()
        product_item["processor_generation"] = response.css("div.specs:contains('Generación')::text").get(default="").strip()
        product_item["processor_model"] = response.css("div.specs:contains('Modelo procesador')::text").get(default="").strip()
        product_item["processor_number_cores"] = response.css("div.specs:contains('Núcleos')::text").get(default="").strip()
        product_item["processor_variant"] = response.css("div.specs:contains('Variante')::text").get(default="").strip()
        product_item["region"] = "LATAM"
        product_item["retailer_id"] = "office_depot_mx"
        product_item["retailer_name"] = "Office Depot Mexico"
        product_item["scrap_datetime"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        product_item["scrap_timestamp"] = int(time.time())
        product_item["sku"] = response.css("span.sku::text").get(default="").strip()
        product_item["status"] = True
        product_item["thunderbolt"] = response.css("div.specs:contains('Thunderbolt')::text").get(default="").strip()
        product_item["title"] = response.css("h1.product-title::text").get(default="").strip()
        product_item["wifi"] = response.css("div.specs:contains('Wi-Fi')::text").get(default="").strip()

        yield product_item