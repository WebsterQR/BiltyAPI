import requests
import os
import argparse
from dotenv import load_dotenv

load_dotenv()

def arguments():
  parser = argparse.ArgumentParser()
  parser.add_argument('link', help="The link what you want to cut")
  args = parser.parse_args()
  return args.link

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
  link = arguments()
  token = os.getenv("BITLY_API_TOKEN")

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


