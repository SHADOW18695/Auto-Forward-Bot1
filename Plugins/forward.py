import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import asyncio
from pyrogram import filters
from bot import channelforward
from config import Config 


@channelforward.on_message(filters.channel)
async def forward(c, m):
    # Forwarding the messages to the channel
    try:
        AS_COPY = True  # Set to True if you want to copy the message, or False if you want to forward without making a copy
        for id in Config.CHANNEL:
            from_channel, to_channel = id.split(":")
            if m.chat.id == int(from_channel):
                if AS_COPY:
                    await m.copy(chat_id=int(to_channel))
                else:
                    await m.forward(chat_id=int(to_channel))
                logger.info("Forwarded a message from", from_channel, "to", to_channel)
                await asyncio.sleep(1)
    except Exception as e:
        logger.exception(e)
