# demo for gstreamer
# @Xin 26/04/2026 
# usage: gst-lauch-1.0 -v videotestsrc pattern=snow ! videorate ! "video/x-raw,width=640,height=480,framerate=60/1" ! x264enc tune=zelolatency bitrate=12000000 speed-preset=superfast ! h264parse ! rtph264pay pt=96 ! udpsink port=5000 host=$HOST

import subprocess 

cmd = (
    'gst-launch-1.0 -v videotestsrc pattern=snow ! videorate ! '
    '"video/x-raw,width=640,height=480,framerate=60/1" ! '
    'x264enc tune=zerolatency bitrate=12000 speed-preset=superfast ! '
    'h264parse ! rtph264pay pt=96 ! '
    'udpsink port=5000 host=127.0.0.1'
)
print(cmd)
subprocess.run(cmd, shell=True)