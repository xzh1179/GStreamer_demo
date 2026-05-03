# GStreamer demo

This is a small demo showing a basic video streaming pipeline using GStreamer.

The demo contains two scripts:

- `sender.py`: generates a test video source, encodes it in H.264, packetizes it as RTP, and sends it through UDP.
- `receiver.py`: receives the RTP/H.264 stream from UDP, depacketizes and decodes it, then displays the video in a window.

## Usage

Start the receiver in a terminal, and start the sender in another terminal

By default, the sender streams to `127.0.0.1` on UDP port `5000`, and the receiver listens on the same port.

## Pipeline overview

The sender pipeline is:

```text
videotestsrc -> videorate -> x264enc -> h264parse -> rtph264pay -> udpsink
```

The receiver pipeline is:

```text
udpsrc -> rtph264depay -> h264parse -> avdec_h264 -> videoconvert -> autovideosink
```

## Notes

This demo runs locally on the same machine. Therefore, it does not fully represent the behavior of a real network environment, where latency, packet loss, jitter, and bandwidth limitations may affect the video stream.
