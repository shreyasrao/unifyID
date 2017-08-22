import urllib.request


def onlineRandom(low=2**25,high=2**28,num=1000):
    url = 'https://www.random.org/integers/?num={}&min={}&max={}&col=1&base=10&format=plain&rnd=new'.format(num,low,high)

    with urllib.request.urlopen(url) as response:
        html = response.read()

    html = html.decode('utf8').splitlines()
    ints = [int(x) for x in html]

    return ints
