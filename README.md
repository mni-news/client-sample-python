# MNI Client Sample - Python


## Install Dependencies

This uses Python 3.

    pip install -r requirements.txt

## Run

    #run with
    python example.py <host> <user> <pass>
    
    #example
    python example.py apis-test.marketnews.com  my_user XXXXXXX

## Code

A main entry point is in [example.py](example.py).

A minimal STOMP frame decoder is in [frame.py](frame.py).

This uses the Python [websocket client](https://pypi.org/project/websocket-client/)
