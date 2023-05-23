#Scraping currency exchange rate from Bank.uz
import json
from datetime import datetime
import time
from bs4 import BeautifulSoup
import aiohttp
import asyncio
from fake_useragent import UserAgent

async def get_currency_exchange():
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random
    }

    async with aiohttp.ClientSession() as session:
        response = await session.get(url="https://bank.uz/currency", headers=headers)
        soup = BeautifulSoup(await response.text(), 'lxml')


        currency_rate_content = soup.find_all("div", id="best_USD")
        currency_dict = {}
        for currency_r in currency_rate_content:
            currency_name = 'USD'
            currency_purchase = [item.text.strip() for item in currency_r.find(class_='bc-inner-block-left').find_all(class_='bc-inner-block-left-texts')]

            currency_sale = [item1.text.strip() for item1 in currency_r.find(class_='bc-inner-blocks-right').find_all(class_='bc-inner-block-left-texts')]
            currency_url = "https://bank.uz/currency"


            currency_dict={
                'currency_name': currency_name,
                'currency_purchase': currency_purchase,
                'currency_sale': currency_sale,
                'currency_url':  currency_url
            }
        print(currency_dict)
        #currency_purchase = soup.find(class_='bc-inner-blocks-right').find_all(class_='bc-inner-block-left-texts')

        #print(currency_purchase.text.strip())
        #for i in currency_purchase:
        #    print(i.text.strip())
    #print(currency_rate_content)
    with open('dollar_exchange_rate.json', 'w', encoding='utf-8') as file:
        json.dump(currency_dict, file, indent=4, ensure_ascii=False)



async def main():
    await get_currency_exchange()




asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(get_currency_exchange())
if __name__ == '__main__':
    asyncio.run(main())
