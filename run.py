if __name__ == "__main__":
    import uvicorn
    from src import config

    uvicorn.run(app="src.main:app", port=config.PORT, reload=True)
