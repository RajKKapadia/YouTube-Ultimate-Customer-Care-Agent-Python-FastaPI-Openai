if __name__ == "__main__":
    import uvicorn

    port = 5000

    uvicorn.run(app="src.main:app", port=port, reload=True)
