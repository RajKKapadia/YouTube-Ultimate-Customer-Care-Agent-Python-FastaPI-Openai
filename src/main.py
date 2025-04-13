import json

from fastapi import FastAPI, HTTPException, Request, Response, status, BackgroundTasks

from src import logging
from src.utils import process_message

app = FastAPI()

logger = logging.getLogger(__name__)


@app.get("/", status_code=status.HTTP_200_OK)
async def handle_get_home():
    return {"message": "Working okay!"}


@app.get("/webhook")
async def verify_webhook(request: Request):
    """
    Verify webhook endpoint for WhatsApp.
    This endpoint is used by Meta to verify the webhook URL during setup.
    """
    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    logger.info(mode, token, challenge)

    if mode and token:
        if mode == "subscribe" and token == "abcdefgh12345678":
            logger.info("Webhook verified successfully")
            return Response(content=challenge, media_type="text/plain")
        else:
            logger.warning("Webhook verification failed")
            raise HTTPException(status_code=403, detail="Verification failed")

    return {"status": "error", "message": "Invalid verification request"}


@app.post("/webhook")
async def receive_webhook(request: Request, background_tasks: BackgroundTasks):
    """
    Receive webhook notifications from WhatsApp.
    This endpoint processes incoming messages and events from WhatsApp.
    """
    body = await request.body()

    try:
        logger.info(f"Webhook received: {body}")
        data = json.loads(body)

        # Process messages in the background
        background_tasks.add_task(process_message, data)

        return Response(content="EVENT_RECEIVED", media_type="text/plain")
    except json.JSONDecodeError:
        logger.error("Invalid JSON in webhook request")
        raise HTTPException(status_code=400, detail="Invalid JSON")
    except Exception as e:
        logger.error(f"Error processing webhook: {e}")
        raise HTTPException(status_code=500, detail=str(e))
