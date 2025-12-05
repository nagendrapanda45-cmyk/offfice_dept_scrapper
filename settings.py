BOT_NAME = "office_depot_scraper"

SPIDER_MODULES = ["office_depot_scraper.spiders"]
NEWSPIDER_MODULE = "office_depot_scraper.spiders"

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    "office_depot_scraper.pipelines.MongoDBPipeline": 300,
}

MONGO_URI = "mongodb://localhost:27017"
MONGO_DATABASE = "office_depot"