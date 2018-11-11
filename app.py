from flask import Flask, render_template
app = Flask(__name__)

import urllib.request as req
import os
from PIL import Image
import glob
from flask import request

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/seizure')
def isGifSeizure():
    gifUrl = request.args.get('gif_url')
    name = "gifprod.gif"
    req.urlretrieve(gifUrl, name)
    return isSeizure(name)




def extractFrames(inGif, outFolder):
    frame = Image.open(inGif)
    nframes = 0
    average = 0
    spikes = []

    while frame:
        frame.save( '%s/%s-%s.gif' % (outFolder, os.path.basename(inGif), nframes ) , 'GIF')
        frameSaved = Image.open('%s/%s-%s.gif' % (outFolder, os.path.basename(inGif), nframes))
        print(frameSaved.filename)
        width, height = frameSaved.size

        average2 = averageFrame(frameSaved, width, height)

        if (average == 0):
            average = average2
            nframes += 1
            continue

        percentage = average2/average * 100

        print(average2)
        print(average)

        if (percentage > 90 and percentage < 110 or percentage == 0):
            spikes.append(False)
        else: 
            spikes.append(True)
        
        average = average2

        nframes += 1
        try:
            frame.seek( nframes )
        except EOFError:
            return (nframes, spikes)
            break
    return True

def averageFrame(frame, width, height):
    newFrame = frame.convert("RGB")

    counter = 0
    total = 0

    for j in range (0, width):
        for k in range(0, height):
            coordinate = x,y = j,k
            rgb = newFrame.getpixel(coordinate)
            total += rgb[0]+rgb[1]+rgb[2]
            counter += 1

    return total/counter

def isSeizure(gifName):
    output = "output"
    nframes, spikes = extractFrames(gifName, output)

    numSpikes = 0
    for spike in spikes:
        if (spike == True):
            numSpikes += 1

    files = glob.glob(output+'/*')
    for f in files:
        os.remove(f)

    print("Number of frames " + str(nframes))    
    print("Number of spikes: " + str(numSpikes))

    percentage = numSpikes/nframes * 100
    if (percentage <= 10):
        return False
    else:
        return True