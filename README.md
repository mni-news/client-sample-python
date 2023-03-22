# MNI Client Sample - Python


## Install Dependencies

This uses Python 3.

    pip install -r requirements.txt

## News API Sample [example.py](example.py)

### Run

    #run with
    python example.py <host> <user> <pass>
    
    #example
    python example.py apis-test.marketnews.com  my_user XXXXXXX

### Code

A main entry point is in [example.py](example.py).


## Instant Answers API Sample [example_instant_answers.py](example_instant_answers.py)

### Run

    #run with
    python example_instant_answers.py  <user> <pass>
    
    #example
    python example_instant_answers.py my_user XXXXXXX

### Example message from instant answers websocket

```json
[   
    {
        "instantAnswersSeriesId":1,
        "instantAnswersInstanceId":"159-1-20230322",
        "display":"FOMC Instant Answers",
        "state":"PUBLISHED",
        "questions":[
            {
                "answerType":"YES_NO_NA",
                "questionId":"159-13",
                "questionText":"1. Did most or more participants say it likely would be appropriate to slow the pace of hikes \"soon\" or at the next meeting?",
                "answer":{
                    "numericValue":1.0,
                    "textValue":"Yes"
                }
            },{
                "answerType":"YES_NO_NA",
                "questionId":"159-14",
                "questionText":"2. Did several or more participants mention the need to monitor any unwarranted loosening of financial conditions?",
                "answer":{
                    "numericValue":1.0,"textValue":"Yes"
                }
            },{
                "answerType":"YES_NO_NA",
                "questionId":"159-15",
                "questionText":"3. Did several or more participants anticipate the need to continue to tighten policy even if there is a moderation in inflation?",
                "answer":{
                    "numericValue":1.0,
                    "textValue":"Yes"
                }
            },{
                "answerType":"YES_NO_NA",
                "questionId":"159-16",
                "questionText":"4. Did several or more participants say a recession is now likely?",
                "answer":{
                    "numericValue":1.0,
                    "textValue":"Yes"
                }
            }
        ]
    }
]

```

### Code


A main entry point for instant answers is in [example_instant_answers.py](example_instant_answers.py).

A minimal STOMP frame decoder is in [frame.py](frame.py).

This uses the Python [websocket client](https://pypi.org/project/websocket-client/)