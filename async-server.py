async def handle_client(reader, writer):
    print(f'Got a connection; reader ID {id(reader)}, writer ID {id(writer)}')

    while True:
        request = (await reader.read(255)).decode('utf8')

        print(f'request = "{request}"')

        if not request.strip():
            print("\tEnding")
            break

        response = plsentence(request)
        writer.write(response.encode('utf8'))
        await writer.drain()
    writer.close()

loop = asyncio.get_event_loop()
print('Waiting for a connection')
loop.create_task(asyncio.start_server(handle_client, 'localhost', 6789))
loop.run_forever()
