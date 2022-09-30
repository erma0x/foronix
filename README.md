# Foronix

![](foronix.jpeg)

## Description
Telegram chat scanner for new messages containing eth addresses.
1. scan the telegram selected chats or groups. 
2. save each ETH address with a timestamp in the file addresses.txt.

Example of a saved ETH address:

`0x00000000219ab540356cbb839cbe05303d7705fa , 2021-12-08 17:09:35+00:00`


## Installation
1. Upgrade pip
``` python3 -m pip install --upgrade pip ```


2. Install telethon
```python3 -m pip install --upgrade telethon ```

3. Change telegram api credential into _main.py_ with your, if you don't have it create one API with **my.telegram.org**

## How to run
```python3 foronix.py```

