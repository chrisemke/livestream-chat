from websockets.exceptions import ConnectionClosedOK

from .schemas import ChatSchema


class WebSocketManager:
    def __init__(self):
        self.connections = []

    async def connect(self, websocket):
        await websocket.accept()
        self.connections.append(websocket)

    def disconnect(self, websocket):
        self.connections.remove(websocket)

    async def broadcast(self, message: ChatSchema):
        for con in self.connections:
            try:
                await con.send_json(message)
            except ConnectionClosedOK:
                self.disconnect(con)


ws_manager = WebSocketManager()
