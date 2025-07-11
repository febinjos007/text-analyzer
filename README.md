
                        ████████ ███████ ██   ██ ████████                                  
                           ██    ██       ██ ██     ██                                     
                           ██    █████     ███      ██                                     
                           ██    ██       ██ ██     ██                                     
                           ██    ███████ ██   ██    ██                                     
                                                                   
                                                                   
         █████  ███    ██  █████  ██      ██    ██ ███████ ███████ ██████  
        ██   ██ ████   ██ ██   ██ ██       ██  ██     ███  ██      ██   ██ 
        ███████ ██ ██  ██ ███████ ██        ████     ███   █████   ██████  
        ██   ██ ██  ██ ██ ██   ██ ██         ██     ███    ██      ██   ██ 
        ██   ██ ██   ████ ██   ██ ███████    ██    ███████ ███████ ██   ██ 
                                                                   

                 
---
                                                                                                                    
                                                                                                                       
This is a FastApi application for analyzing Customer Feedback text


## API Reference

#### POST /analyze
Submits **free-form text** (e.g., customer feedback) to be analyzed.

```http
  POST /analyze
  Content-Type: text/plain
```
Send raw plain text in the body of the request.
```
curl -X POST http://localhost:8000/analyze \
     -H "Content-Type: text/plain" \
     --data "This is some free-form feedback text!"
```

Response 
```
{
  "word_count": 0,
  "most_common_words": [],
  "sentiment": positive, negative or neutral based on the sentence
}
```

#### GET /docs
Swagger page listing the endpoints. But since the post endpoint is using free-text input.
Swagger/OpenAPI doesn't render a form for text/plain by default, so you see no field.


#### POST /redoc
Read-only and fully responsive documentation page for the FastAPI API

## Sentiments
For this app we are using a small set of keywords to identify sentiments. Here is the list
| Positive  | Negative  |
|-----------------------------|-----------------------------|
| "great", "awesome", "excellent"<br>"good", "quick", "easy"<br>"fantastic", "amazing"       
| "bad", "poor", "slow", "terrible", "awful", "disappointing" |

## Requirements
| Package | Description |
| ------ | ------ |
| fastapi | Used to create backend REST APIs |
| uvicorn | Runs your FastAPI app, enabling async capabilities and hot-reloading |
| nltk | Useful for removing stop words |
| pydantic | Used by FastAPI to define and validate request/response models |


## Local deployment
uvicorn is used
Run following commands to start the app
Service runs in port 8000
```bash
  uvicorn src.main:app --reload
```
Note: `src.main` is used since the main.py file is under /src folder


## Testing
To make sure the service is working as expected, pytest is included in the app
Tests are under the /tests module. We can initiate the test using

```bash
  pytest --disable-warnings
```

## Authors

- [@febinjose](https://github.com/febinjos007)
