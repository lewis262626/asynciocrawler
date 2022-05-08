import logging
import time
import asyncio
import aiohttp
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

class AsyncWebCrawler:
    def __init__(self, initial_url, depth):
        self.initial_url = initial_url
        self.depth = depth
        self.seen_links = set() # use a set for easy uniqueness constraint
        self.url_queue = asyncio.Queue() #(url, current_depth)

    def crawl(self):
    # Create three worker tasks to process the queue concurrently.
    tasks = []
    for i in range(3):
        task = asyncio.create_task(self._crawl))
        tasks.append(task)

    # Wait until the queue is fully processed.
    started_at = time.monotonic()
    await queue.join()
    total_slept_for = time.monotonic() - started_at

    # Cancel our worker tasks.
    for task in tasks:
        task.cancel()
    # Wait until all worker tasks are cancelled.
    await asyncio.gather(*tasks, return_exceptions=True)

    print('====')
    print(f'3 workers slept in parallel for {total_slept_for:.2f} seconds')
    print(f'total expected sleep time: {total_sleep_time:.2f} seconds')

    async def _crawl(self):
        url_to_fetch, depth = await self.url_queue.get()
        if depth <= 0:
            queue.task_done()
        async with aiohttp.ClientSession() as session:
            async with session.get(url_to_fetch) as response:
                logger.debug(f"Status: {response.status"})
                if response.status >= 200 and response.status <= 299:
                    if response.headers["Content-Type"] == 'text/html':
                        urls = await self.parse_links(response.body)
                        logger.debug(f"Found {len(urls} urls on page
                                {url_to_fetch}")
                        urls_to_add = set(urls) - self.seen_links
                        self.url_queue.append(urls_to_add)
                        self.seen_links.nowait(links)

    async def parse_links(self, body):
        links = []
        for link in BeautifulSoup(body, parse_only=bs4.SoupStrainer('a')):
            if link.has_attr('href'):
                links.append(link)
        return links


