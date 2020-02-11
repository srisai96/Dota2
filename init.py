import requests

srisai = 233602455
anikt = 230940401
pabba = 249562073
strangers = [156459418]
pros = [162539779]

def player(account_id):
    URL = "https://api.opendota.com/api/players/{account_id}"
    URL_PARAM_DICT = {'account_id':account_id}
    r = requests.get(url=URL.format_map(URL_PARAM_DICT))
    return r

def win_loss(account_id):
    URL = "https://api.opendota.com/api/players/{account_id}/wl"
    URL_PARAM_DICT = {'account_id':account_id}
    r = requests.get(url=URL.format_map(URL_PARAM_DICT))
    return r

def get_live_game():
    URL =  "https://api.opendota.com/api/feed"
    r = requests.get(url= URL, params={'included_account_id':pros[0]})
    return r
def get_live():
    URL = "https://api.opendota.com/api/live"
    r = requests.get(url=URL)
    return r



player_data = get_live_game()
print(player_data.status_code, player_data.url)

# print(get_live().json()[0]['players'])
