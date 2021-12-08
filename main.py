import asyncio
import logging
import re

from telethon.sync import TelegramClient, events
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import InputPeerEmpty
from telethon.events import StopPropagation, NewMessage

TEXT_PATTERN = '0x'
LENGHT_ADDRESS = 42 # prefix + address

group_name = 'Test'

# Use API id and API hash from my.telegram.org
api_id = 16524799
api_hash = "fdb94b3595455c8832553b6eb8c1b503"

# use full phone number including + and country code
phone = "+393271589163"
username = "@hydrogeek"

# create the client
client = TelegramClient(username, api_id, api_hash)

# create async function for scanning new messages on the group_name
@client.on(events.NewMessage(chats=group_name))
async def handler(event):   
    new_message = event.message.message
    date = str(event.message.date)
    

    for word in new_message.split():
        if TEXT_PATTERN in word and len(word)==LENGHT_ADDRESS:
            WRITE =str(word)+' , '+ date +'\n' 
            RECIVER_ADDRESS = word
            with open('addresses.txt','a+') as f:
                f.write(WRITE)
                print(' NEW address ',WRITE)
    


client.start()
print("Client created, connected with ",username)

with client:
    client.run_until_disconnected()
