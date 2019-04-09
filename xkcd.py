from urllib.parse import quote
import requests

START = 1597

past = []


def get_xkcd_transcript(code):
    return requests.get('https://xkcd.com/{}/info.0.json'.format(code)).json()['transcript']


def get_xkcd_reccomendation(text):
    response = requests.get(
        'https://relevantxkcd.appspot.com/process?action=xkcd&query={}'.format(quote(text))).text
    return [int(x.split(" ")[0]) for x in response.split("\n")[3:-1]]


def main():
    number = START
    while True:
        numbers = get_xkcd_reccomendation(get_xkcd_transcript(number))
        new = [x for x in numbers if not x in past]
        number = new[0]
        print(number)
        past.append(number)


if __name__ == '__main__':
    main()
