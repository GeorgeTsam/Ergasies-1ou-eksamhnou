"""
H υπηρεσία https://www.cloudflare.com/en-gb/leagueofentropy/ προσφέρει τυχαίους αριθμούς.
Χρησιμοποιείστε αρχικά τη διεύθυνση https://drand.cloudflare.com/public/latest για να βρείτε ποιος είναι ο τελευταίος γύρος
και στη συνέχεια πάρτε τις τελευταίες 100 τιμές (πεδίο randomness) μέσα από το https://drand.cloudflare.com/public/{round}.
Μετατρέψτε αυτές τις τιμές σε δυαδικό και εμφανίστε το μήκος της μεγαλύτερης ακολουθίας με συνεχόμενα μηδενικά
και το μήκος της μεγαλύτερης ακολουθίας με συνεχόμενες μονάδες.

"""


from urllib.request import Request, urlopen
import ast

def tobinary(a):
    l, m = [], []
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    return m



req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()

data1 = data.decode('utf-8')
data1 = ast.literal_eval(data1)
round = data1['round']
number = ''
for j in range(round-100, round+1):
    url = "https://drand.cloudflare.com/public/%s" % j
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data2 = urlopen(req).read()
    data2 = data.decode('utf-8')
    data2 = ast.literal_eval(data2)
    number = number+data2['randomness']

binary = tobinary(data2)
