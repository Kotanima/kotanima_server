

curl -X POST -d '{"username": "$DJ_KAA_USER","password": "$DJ_KAA_PW"}' -H 'Content-Type: application/json'  http://127.0.0.1:8000/api/auth/token/login/

REGISTER NEW USER:
curl -X POST http://127.0.0.1:8000/auth/users/ --data 'username=&password='

LOGIN:
curl -X POST http://127.0.0.1:8000/api/auth/token/login/ --data 'username=&password='


https://github.com/miki725/django-url-filter
http://127.0.0.1:8000/reddit_posts/?limit=1&title__contains!=ass&sub_name=ecchi
http://127.0.0.1:8000/reddit_posts/?limit=2&id__in=1,2,3,4,5
http://127.0.0.1:8000/reddit_posts/?limit=4&title__icontains!=original&created_utc__lt=1359779200
http://127.0.0.1:8000/reddit_posts/?limit=1&sub_name=ecchi
http://127.0.0.1:8000/reddit_posts/?limit=20&&sub_name__in=awwnime,fantasymoe,awenime


import requests

# https://djoser.readthedocs.io/en/latest/sample_usage.html
mytoken = ""
MY_PK = 39430
# myurl = "http://localhost:8000/auth/users/me"
# myurl = f"http://localhost:8000/reddit_posts/update-partial/{MY_PK}"
myurl = f"http://localhost:8000/edit_reddit_posts/{MY_PK}/"
# A get request (json example):
response = requests.patch(myurl, headers={'Authorization': 'Token {}'.format(mytoken)}, data={"dislike": True})
# data = response.json()
