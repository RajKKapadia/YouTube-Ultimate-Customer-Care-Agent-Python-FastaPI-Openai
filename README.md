# WhatsApp Customer Care AI Agent

A FastAPI application that integrates with the WhatsApp API to provide automated customer service using OpenAI's GPT models.

## Features

- WhatsApp webhook integration
- Background message processing
- MongoDB database for message and user storage
- OpenAI GPT integration with context awareness
- Support for text, image, and document messages

## Requirements

- Python 3.8+
- FastAPI and Uvicorn
- MongoDB
- OpenAI API key
- WhatsApp Business API access

## Environment Variables

Create a `.env` file with the following variables:

```
WHATSAPP_TOKEN=your_whatsapp_token
WHATSAPP_API_URL=https://graph.facebook.com/v22.0
VERIFY_TOKEN=your_verification_token
PHONE_NUMBER_ID=your_phone_number_id
OPENAI_API_KEY=your_openai_api_key
MONGODB_URL=your_mongodb_connection_string
PORT=5000
```

## Installation

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

Start the server with:

```
python run.py
```

Or use Uvicorn directly:

```
uvicorn src.main:app --reload --port 5000
```

## API Endpoints

- `GET /`: Health check endpoint
- `GET /webhook`: WhatsApp webhook verification endpoint
- `POST /webhook`: WhatsApp webhook for receiving messages

## Architecture

- `src/main.py`: FastAPI application and API endpoints
- `src/config.py`: Configuration and environment variables
- `src/database.py`: MongoDB connection and database operations
- `src/utils.py`: Message processing and WhatsApp API integration

## Dependencies

See `requirements.txt` for a complete list of dependencies.