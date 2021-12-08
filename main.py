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
# Those are just examples USE YOUR OWN! 
api_id = 12526799
api_hash = "c5br4r3y95t5dcd8225e3f6eb5c1b500" 

# use full phone number including + and country code 
phone = "+111111111111"
username = "@my_username"

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
