#!/usr/bin/env python3

import os

log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs/db.log')

import logging; logging.basicConfig(filename=log_path, level=logging.INFO)
import asyncio
from conf.config import configs
from db.mysql import orm


@asyncio.coroutine
def init(loop):
    yield from orm.create_pool(loop=loop, **configs.db)

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

