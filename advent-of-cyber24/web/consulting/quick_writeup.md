- The web app has login page, and the credentials are sent in JSON
- from the responses headers, the application is `Experss js`, so there is a possibility that it is running MongoDB, a payload as the following make it possible to bypass the login:
```json
{"username":{"$ne":null},"password":{"$ne":null}}
```
which is equivalent to `WHERE username IS NOT NULL AND password IS NOT NULL` which is always True;

- since login is not enough in this challenge, the credentials need to be revealed to access the other login page, and for this, the previous vulnerability `Blind NoSQL injection` to bruteforce username and password characters using **regex**.

this [script](solve.py) does the job
