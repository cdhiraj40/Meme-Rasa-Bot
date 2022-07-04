<h1 align="center">MEME Rasa Bot</h1>
<p align="center">A bot made for absolute fun. It can create memes.</a>.</p>

## 👇 Prerequisites

Before installation, please make sure you have already installed the following tool:

- [``pipenv``](https://pypi.org/project/pipenv/)  
```
pip install pipenv
```
We will use pipenv to easily manage and setup a working environment. 

## 🛠️ Installation Steps
Once you have cloned the project follow these steps to install:

- Initialize a virtual environment and install dependencies via **use pipenv**

```
cd Meme-Rasa-Bot
pipenv install
```

## 🧑‍💻 Training and Testing
- Train bot
```
rasa train
```
- Test bot on terminal
```
rasa shell
```
- start ``rasa server`` and test locally
```
rasa run --enable-api --port 5005
```
- start `actions` server
```
rasa run actions -p 5005
```
Once the server is up and running, test the bot directly via [``postman``](https://www.postman.com/)  
Here's a [blog to explore the ``rasa`` apis with postman](https://rasa.com/blog/explore-rasa-apis-with-postman/)

But here are some of the common apis to use:

1. Testing the bot  
**POST**: http://localhost:5005/webhooks/rest/webhook with the body
```
{
    "message": <your message>
}
```

2. Check rasa version  
**GET**: http://localhost:5005/version no body needed

You could also explore the [apis with postman via video](https://www.youtube.com/watch?v=usHTraJTPyQ&list=PL75e0qA87dlHogEVKnBJLhqyaZKDg2f0W).  
