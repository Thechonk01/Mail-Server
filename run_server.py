from server.smtp_server import start_smtp_server

if __name__ == '__main__':
    start_smtp_server()
    # Keep the server running
    try:
        import asyncio
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        pass
