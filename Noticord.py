import asyncio, requests, time, os, discord, shutil, sys;

TOKEN = ""
NotificationChannelID = ""

def setTokenAndId(Token,ID):
    global TOKEN
    TOKEN = Token
    global NotificationChannelID
    NotificationChannelID = ID

def println():
    print();print("*************************************************");print()
    
def Notify(Content, ID = NotificationChannelID):
    async def Send(Content, Channel = ID): 
        try:
            await client.wait_until_ready()
            print(ID)
            message = await client.get_channel(Channel).send(Content);
            await client.close(); asyncio.set_event_loop(asyncio.new_event_loop());
            return True
        except Exception as e:
            print(e)
            print("Error occured")
            await client.close(); asyncio.set_event_loop(asyncio.new_event_loop());
            return None
    client = discord.Client()
    task = client.loop.create_task(Send(Content))
    client.run(TOKEN)
    if task.result() == None:
        time.sleep(10)
        return Notify(Content, ID)
    return task.result()

def NotifyInBox(Content, ID = NotificationChannelID):
    async def Send(Content, Channel = ID): 
        try:
            await client.wait_until_ready()
            message = await client.get_channel(Channel).send("#"*40+"\n"+str(Content)+"\n"+"#"*40);
            await client.close(); asyncio.set_event_loop(asyncio.new_event_loop());
            return True
        except Exception as e:
            print(e)
            print("Error occured")
            await client.close(); asyncio.set_event_loop(asyncio.new_event_loop());
            return None
    client = discord.Client()
    task = client.loop.create_task(Send(Content))
    client.run(TOKEN)
    if task.result() == None:
        time.sleep(10)
        return NotifyInBox(Content, ID)
    return task.result()

print(NotifyInBox("Hey"))
