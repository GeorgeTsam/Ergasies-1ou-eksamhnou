"""
Σας δίνεται αρχείο κειμένου με μόνο ASCII χαρακτήρες.
Αρχικά απεικονίστε κάθε χαρακτήρα σε δυαδικό μήκους 7.
Από αυτούς κρατάτε μόνο τα πρώτα δύο και τα τελευταία δύο bits.
Χωρίστε την ακολουθία σας σε αριθμούς των 16 bits και εμφανίστε τα ακόλουθα στατιστικά:
(α) Τι ποσοστό είναι ζυγοί;
(β) Τι ποσοστό διαιρείται ακριβώς με το 3;
(γ) Τι ποσοστό διαιρείται ακριβώς με το 5;
(δ) Τι ποσοστό διαιρείται ακριβώς με το 7;
"""


def tobinary(a):
    l, m = [], []
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    return m

# turn to binary
f = open("two_cities_ascii.txt", "r")
text = f.read()
binary = tobinary(text)
digits = []
for i in range(len(binary)):
    x = [int(d) for d in str(binary[i])]
    while len(x) < 7:
        x.insert(0, 0)
    digits.append(x)
for i in range(len(digits)):  #keep last 2 bits
    digits[i] = digits[i][0], digits[i][1], digits[i][5], digits[i][6]
print(digits)
