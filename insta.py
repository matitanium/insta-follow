import requests
import time
headers = {
    'authority': 'www.instagram.com',
    'method': 'POST',
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR2W6VqWYBc-K2p-G7gPDh9J68D7p0vSd98h9XU9I97KJxV7',
    'x-instagram-ajax': '3fc885d05fce',
    'x-requested-with': 'XMLHttpRequest'
}
session = requests.Session()
session.headers = {'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36", 'Referer': 'https://www.instagram.com/'}
username = input("enter yor username: ")
password = input("enter yor pass: ")


resp = session.get("https://www.instagram.com/")
session.headers.update({'x-csrftoken': resp.cookies['csrftoken']})
login_data = {'username': username, 'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:' + password}
login_resp = session.post('https://www.instagram.com/accounts/login/ajax/', data=login_data)
if login_resp.json()['authenticated']:
    print("Logged in")
else:
    print("Login Failed")
session.headers.update({'x-csrftoken': login_resp.cookies['csrftoken']})
session.headers.update({'cookie': 'sessionid='+login_resp.cookies['sessionid']})
session.headers.update(headers)


def unfollow():
    requests.post("https://www.instagram.com/web/friendships/"+id+"/unfollow/", headers=session.headers)


def follow():
    requests.post("https://www.instagram.com/web/friendships/"+id+"/follow/", headers=session.headers)
    





ids = "cristiano"
url_id = ('https://www.instagram.com/'+ids+'/?__a=1')
req_id = session.get(url_id).json()
id = str(req_id['graphql']['user']['id'])
try:
    while True:
        time.sleep(3)
        print("follow " + id)
        follow()
        time.sleep(7)
        print("unfollow"+ id)
        unfollow()
except:
    print("end ...")
# while True:
#     follow()
#     time.sleep(5)
#     unfollow()
#     time.sleep(3)