import asyncio
import websockets
from websockets import ServerConnection

async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f'Get message {message}')
        response = f'Server get {message}'
        await websocket.send(response)
        
        
async def main():
    server = await websockets.serve(echo, host='localhost', port=8000)
    print('Websocket started on ws://localhost:8000')
    await server.wait_closed()
    
asyncio.run(main())