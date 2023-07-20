import asyncio

async def handle_echo(reader, writer):
    while True:
        data = await reader.read(100)
        if not data:
            break
        message = data.decode()
        addr = writer.get_extra_info('peername')
        print(f"received {message!r} from {addr!r}")
        writer.write(data)
        await writer.drain()

    print("connection closed")
    writer.close()

async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888
    )

    addr = server.sockets[0].getsockname()
    print(f'serving on {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
