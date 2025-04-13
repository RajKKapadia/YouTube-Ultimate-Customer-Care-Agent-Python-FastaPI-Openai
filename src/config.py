import os

from dotenv import load_dotenv, find_dotenv
from openai import AsyncOpenAI

from src import logging

load_dotenv(find_dotenv())

logger = logging.getLogger(__name__)


WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
WHATSAPP_API_URL = os.getenv("WHATSAPP_API_URL", "https://graph.facebook.com/v22.0")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MONGODB_URL = os.getenv("MONGODB_URL")

VECTOR_STORE_ID = "vs_67fa34bc79648191a32eaaf87683017b"

if not all(
    [WHATSAPP_TOKEN, VERIFY_TOKEN, OPENAI_API_KEY, PHONE_NUMBER_ID, MONGODB_URL]
):
    logger.error("Missing required environment variables")
    raise ValueError("Please set all required environment variables")


async_client = AsyncOpenAI(api_key=OPENAI_API_KEY)
