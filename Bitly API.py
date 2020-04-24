import requests
import os

def get_shorten_link(link, token):
  url = "https://api-ssl.bitly.com/v4/bitlinks"
  headers = {
    "Authorization": f"Bearer {token}",
  }
  payload = {
    "long_url": link
  }
  response = requests.post(url, json=payload, headers=headers)
  response.raise_for_status()

  answer = response.json()
  return answer['id']

def count_clicks(token, bitlink):
  url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary"
  headers = {
    "Authorization": f"Bearer {token}",
  }
  response = requests.get(url, headers=headers)
  return response.json()
  
if __name__=='__main__':
  link = input("Please, enter your link: ")
  token = os.getenv("TOKEN")

  if link.startswith('bit.ly'):
    try:
      clicks = count_clicks(token, link)
      print(f'Total ckicks = {clicks["total_clicks"]}')
    except requests.exceptions.HTTPError:
      print("Error")
  else:
    try:
      bitlink = get_shorten_link(link, token)
      print(f'Битлинк {bitlink}')
    except requests.exceptions.HTTPError:
      print("Error in link!")


