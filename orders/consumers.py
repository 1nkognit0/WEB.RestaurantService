from channels.generic.websocket import AsyncWebsocketConsumer

import json

class OrderConsumer(AsyncWebsocketConsumer):
    groups = ["orders"]

    async def new_order(self, event):
        await self.send(text_data=json.dumps(event["data"]))
