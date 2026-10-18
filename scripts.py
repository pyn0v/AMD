


# ############################################################################
# PROBLEM 1 - INTRODUCTION
# ############################################################################

# ===== Say Hello World With Python =====
print("Hello, World!")

# ===== Python If Else =====
n = int(input().strip())
if n % 2 == 1 or 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")

# ===== Arithmetic Operators =====
a = int(input()); b = int(input())
print(a + b); print(a - b); print(a * b)

# ===== Python Division =====
a = int(input()); b = int(input())
print(a // b); print(a / b)

# ===== Loops =====
n = int(input())
for i in range(n):
    print(i * i)

# ===== Write a function =====
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


year = int(input())
print(is_leap(year))

# ===== Print Function =====
n = int(input())
print(*range(1, n + 1), sep="")


# ############################################################################
# PROBLEM 1 - BASIC DATA TYPES
# ############################################################################

# ===== List Comprehensions =====
x, y, z, n = (int(input()) for _ in range(4))
print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n])

# ===== Find the Runner Up Score =====
n = int(input())
arr = list(map(int, input().split()))
print(sorted(set(arr))[-2])

# ===== Nested Lists =====
records = []
for _ in range(int(input())):
    name = input(); score = float(input())
    records.append([name, score])
second = sorted(set(s for _, s in records))[1]
for name in sorted(n for n, s in records if s == second):
    print(name)

# ===== Finding the percentage =====
n = int(input())
marks = {}
for _ in range(n):
    name, *scores = input().split()
    marks[name] = list(map(float, scores))
query_name = input()
print(f"{sum(marks[query_name]) / len(marks[query_name]):.2f}")

# ===== Lists =====
N = int(input())
lst = []
for _ in range(N):
    cmd, *args = input().split()
    args = list(map(int, args))
    if cmd == "print":
        print(lst)
    else:
        getattr(lst, cmd)(*args)

# ===== Tuples =====
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))


# ############################################################################
# PROBLEM 1 - STRINGS
# ############################################################################

# ===== sWAP cASE =====
import textwrap
import string as _string

def swap_case(s):
    return s.swapcase()


print(swap_case(input()))

# ===== String Split and Join =====
import textwrap
import string as _string

def split_and_join(line):
    return "-".join(line.split(" "))


print(split_and_join(input()))

# ===== What s Your Name =====
import textwrap
import string as _string

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")


first = input(); last = input()
print_full_name(first, last)

# ===== Mutations =====
import textwrap
import string as _string

def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]


s = input(); i, c = input().split()
print(mutate_string(s, int(i), c))

# ===== Find a string =====
import textwrap
import string as _string

def count_substring(string, sub_string):
    return sum(string.startswith(sub_string, i) for i in range(len(string)))


string = input().strip(); sub = input().strip()
print(count_substring(string, sub))

# ===== String Validators =====
import textwrap
import string as _string

s = input()
print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))

# ===== Text Alignment =====
import textwrap
import string as _string

thickness = int(input())
c = 'H'
for i in range(thickness):  # top cone
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))
for i in range(thickness + 1):  # top pillars
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
for i in range((thickness + 1) // 2):  # middle belt
    print((c * thickness * 5).center(thickness * 6))
for i in range(thickness + 1):  # bottom pillars
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
for i in range(thickness):  # bottom cone
    print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))

# ===== Text Wrap =====
import textwrap
import string as _string

def wrap(string, max_width):
    return textwrap.fill(string, max_width)


string, max_width = input(), int(input())
print(wrap(string, max_width))

# ===== Designer Door Mat =====
import textwrap
import string as _string

n, m = map(int, input().split())
top = [('.|.' * (2 * i + 1)).center(m, '-') for i in range(n // 2)]
print('\n'.join(top + ['WELCOME'.center(m, '-')] + top[::-1]))

# ===== String Formatting =====
import textwrap
import string as _string

def print_formatted(number):
    w = len(bin(number)) - 2
    for i in range(1, number + 1):
        print(f"{i:{w}d} {i:{w}o} {i:{w}X} {i:{w}b}")


print_formatted(int(input()))

# ===== Alphabet Rangoli =====
import textwrap
import string as _string

def print_rangoli(size):
    a = _string.ascii_lowercase
    lines = []
    for i in range(size):
        s = '-'.join(a[i:size])
        lines.append((s[::-1] + s[1:]).center(4 * size - 3, '-'))
    print('\n'.join(lines[:0:-1] + lines))


print_rangoli(int(input()))

# ===== Capitalize =====
import textwrap
import string as _string

def solve(s):
    return ' '.join(w[:1].upper() + w[1:] for w in s.split(' '))


import os
fptr = open(os.environ.get('OUTPUT_PATH', '/dev/stdout'), 'w')
fptr.write(solve(input()) + '\n')
fptr.close()

# ===== The Minion Game =====
import textwrap
import string as _string

def minion_game(string):
    n = len(string)
    kevin = sum(n - i for i, ch in enumerate(string) if ch in "AEIOU")
    stuart = n * (n + 1) // 2 - kevin
    if stuart > kevin:
        print("Stuart", stuart)
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Draw")


minion_game(input())

# ===== Merge the Tools =====
import textwrap
import string as _string

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        print(''.join(dict.fromkeys(string[i:i + k])))


string, k = input(), int(input())
merge_the_tools(string, k)


# ############################################################################
# PROBLEM 1 - SETS
# ############################################################################

# ===== Introduction to Sets =====
def average(array):
    s = set(array)
    return round(sum(s) / len(s), 3)


n = int(input())
arr = list(map(int, input().split()))
print(average(arr))

# ===== No Idea =====
n, m = map(int, input().split())
arr = input().split()
A = set(input().split()); B = set(input().split())
print(sum((x in A) - (x in B) for x in arr))

# ===== Symmetric Difference =====
input(); a = set(map(int, input().split()))
input(); b = set(map(int, input().split()))
print(*sorted(a ^ b), sep="\n")

# ===== Set add =====
print(len({input() for _ in range(int(input()))}))

# ===== Set discard remove pop =====
n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    cmd, *args = input().split()
    getattr(s, cmd)(*map(int, args))
print(sum(s))

# ===== Set union Operation =====
input(); a = set(input().split()); input(); b = set(input().split())
print(len(a | b))

# ===== Set intersection Operation =====
input(); a = set(input().split()); input(); b = set(input().split())
print(len(a & b))

# ===== Set difference Operation =====
input(); a = set(input().split()); input(); b = set(input().split())
print(len(a - b))

# ===== Set symmetric difference Operation =====
input(); a = set(input().split()); input(); b = set(input().split())
print(len(a ^ b))

# ===== Set Mutations =====
input(); A = set(map(int, input().split()))
for _ in range(int(input())):
    op, _ = input().split()
    getattr(A, op)(set(map(int, input().split())))
print(sum(A))

# ===== The Captain s Room =====
k = int(input())
rooms = list(map(int, input().split()))
print((sum(set(rooms)) * k - sum(rooms)) // (k - 1))

# ===== Check Subset =====
for _ in range(int(input())):
    input(); A = set(input().split())
    input(); B = set(input().split())
    print(A <= B)

# ===== Check Strict Superset =====
A = set(input().split())
others = [set(input().split()) for _ in range(int(input()))]
print(all(A > o for o in others))


# ############################################################################
# PROBLEM 1 - COLLECTIONS
# ############################################################################

# ===== collections Counter =====
from collections import Counter, defaultdict, namedtuple, OrderedDict, deque

input()
stock = Counter(map(int, input().split()))
earned = 0
for _ in range(int(input())):
    size, price = map(int, input().split())
    if stock[size] > 0:
        stock[size] -= 1
        earned += price
print(earned)

# ===== DefaultDict Tutorial =====
from collections import Counter, defaultdict, namedtuple, OrderedDict, deque

n, m = map(int, input().split())
d = defaultdict(list)
for i in range(1, n + 1):
    d[input()].append(str(i))
for _ in range(m):
    print(' '.join(d.get(input(), ['-1'])))

# ===== Collections namedtuple =====
from collections import Counter, defaultdict, namedtuple, OrderedDict, deque

n = int(input())
Student = namedtuple('Student', input().split())
print(f"{sum(int(Student(*input().split()).MARKS) for _ in range(n)) / n:.2f}")

# ===== Collections OrderedDict =====
from collections import Counter, defaultdict, namedtuple, OrderedDict, deque

od = OrderedDict()
for _ in range(int(input())):
    name, _, price = input().rpartition(' ')
    od[name] = od.get(name, 0) + int(price)
for name, total in od.items():
    print(name, total)

# ===== Word Order =====
from collections import Counter, defaultdict, namedtuple, OrderedDict, deque

c = Counter(input() for _ in range(int(input())))  # dicts keep insertion order
print(len(c)); print(*c.values())

# ===== Collections deque =====
from collections import Counter, defaultdict, namedtuple, OrderedDict, deque

d = deque()
for _ in range(int(input())):
    cmd, *args = input().split()
    getattr(d, cmd)(*map(int, args))
print(*d)

# ===== Company Logo =====
from collections import Counter, defaultdict, namedtuple, OrderedDict, deque

s = input()
for ch, cnt in sorted(Counter(s).items(), key=lambda x: (-x[1], x[0]))[:3]:
    print(ch, cnt)

# ===== Piling Up =====
from collections import Counter, defaultdict, namedtuple, OrderedDict, deque

for _ in range(int(input())):
    input()
    blocks = deque(map(int, input().split()))
    top, ok = float('inf'), True
    while blocks:
        cube = blocks.popleft() if blocks[0] >= blocks[-1] else blocks.pop()
        if cube > top:
            ok = False
            break
        top = cube
    print("Yes" if ok else "No")


# ############################################################################
# PROBLEM 1 - DATE AND TIME
# ############################################################################

# ===== Calendar Module =====
import calendar
from datetime import datetime

m, d, y = map(int, input().split())
print(calendar.day_name[calendar.weekday(y, m, d)].upper())

# ===== Time Delta =====
import calendar
from datetime import datetime

def time_delta(t1, t2):
    fmt = '%a %d %b %Y %H:%M:%S %z'
    diff = datetime.strptime(t1, fmt) - datetime.strptime(t2, fmt)
    return str(int(abs(diff.total_seconds())))


import os
fptr = open(os.environ.get('OUTPUT_PATH', '/dev/stdout'), 'w')
for _ in range(int(input())):
    t1 = input(); t2 = input()
    fptr.write(time_delta(t1, t2) + '\n')
fptr.close()


# ############################################################################
# PROBLEM 1 - EXCEPTIONS
# ############################################################################

# ===== Exceptions =====
for _ in range(int(input())):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)


# ############################################################################
# PROBLEM 1 - BUILT-INS
# ############################################################################

# ===== Zipped =====
import calendar
from datetime import datetime

N, X = map(int, input().split())
rows = [list(map(float, input().split())) for _ in range(X)]
for marks in zip(*rows):
    print(sum(marks) / X)

# ===== Athlete Sort =====
import calendar
from datetime import datetime

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
for row in sorted(arr, key=lambda r: r[k]):  # sort is stable
    print(*row)

# ===== ginortS =====
import calendar
from datetime import datetime

s = input()
print(''.join(sorted(s, key=lambda c: (c.isdigit(), c.isupper(), c.isdigit() and int(c) % 2 == 0, c))))


# ############################################################################
# PROBLEM 1 - PYTHON FUNCTIONALS
# ############################################################################

# ===== Map and Lambda Function =====
import calendar
from datetime import datetime

cube = lambda x: x ** 3

def fibonacci(n):
    out, a, b = [], 0, 1
    for _ in range(n):
        out.append(a)
        a, b = b, a + b
    return out


n = int(input())
print(list(map(cube, fibonacci(n))))


# ############################################################################
# PROBLEM 1 - REGEX AND PARSING
# ############################################################################

# ===== Detect Floating Point Number =====
import re
import email.utils
from html.parser import HTMLParser

for _ in range(int(input())):
    print(bool(re.match(r'^[+-]?\d*\.\d+$', input())))

# ===== Re split =====
import re
import email.utils
from html.parser import HTMLParser

regex_pattern = r"[,.]"


print('\n'.join(re.split(regex_pattern, input())))

# ===== Group Groups Groupdict =====
import re
import email.utils
from html.parser import HTMLParser

m = re.search(r'([a-zA-Z0-9])\1', input())
print(m.group(1) if m else -1)

# ===== Re findall Re finditer =====
import re
import email.utils
from html.parser import HTMLParser

cons = 'qwrtypsdfghjklzxcvbnm'
found = re.findall(rf'(?<=[{cons}])([aeiou]{{2,}})(?=[{cons}])', input(), re.I)
print('\n'.join(found) if found else -1)

# ===== Re start Re end =====
import re
import email.utils
from html.parser import HTMLParser

S, k = input(), input()
hits = [(m.start(1), m.end(1) - 1) for m in re.finditer(rf'(?=({re.escape(k)}))', S)]
print('\n'.join(map(str, hits)) if hits else (-1, -1))

# ===== Regex Substitution =====
import re
import email.utils
from html.parser import HTMLParser

for _ in range(int(input())):
    print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda m: 'and' if m.group() == '&&' else 'or', input()))

# ===== Validating Roman Numerals =====
import re
import email.utils
from html.parser import HTMLParser

regex_pattern = r"M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[VX]|V?I{0,3})$"


print(str(bool(re.match(regex_pattern, input()))))

# ===== Validating phone numbers =====
import re
import email.utils
from html.parser import HTMLParser

for _ in range(int(input())):
    print("YES" if re.match(r'^[789]\d{9}$', input()) else "NO")

# ===== Validating and Parsing Email Addresses =====
import re
import email.utils
from html.parser import HTMLParser

for _ in range(int(input())):
    line = input()
    name, addr = email.utils.parseaddr(line)
    if re.match(r'^[a-zA-Z][\w.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$', addr):
        print(line)

# ===== Hex Color Code =====
import re
import email.utils
from html.parser import HTMLParser

for _ in range(int(input())):
    for code in re.findall(r'[\s:,(](#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})(?![0-9a-fA-F])', input()):
        print(code)

# ===== HTML Parser Part 1 =====
import re
import email.utils
from html.parser import HTMLParser

class Parser1(HTMLParser):
    def _attrs(self, attrs):
        for a, v in attrs:
            print("->", a, ">", v)
    def handle_starttag(self, tag, attrs):
        print("Start :", tag); self._attrs(attrs)
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag); self._attrs(attrs)

html = '\n'.join(input() for _ in range(int(input())))
Parser1().feed(html)

# ===== HTML Parser Part 2 =====
import re
import email.utils
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print(">>> Multi-line Comment" if '\n' in data else ">>> Single-line Comment")
        print(data)
    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data)


html = ''
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
parser = MyHTMLParser()
parser.feed(html)
parser.close()

# ===== Detect HTML Tags Attributes and Attribute Values =====
import re
import email.utils
from html.parser import HTMLParser

class TagParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for a, v in attrs:
            print("->", a, ">", v)
    handle_startendtag = handle_starttag

TagParser().feed('\n'.join(input() for _ in range(int(input()))))

# ===== Validating UID =====
import re
import email.utils
from html.parser import HTMLParser

for _ in range(int(input())):
    uid = input()
    ok = (len(uid) == 10 and uid.isalnum() and len(set(uid)) == 10
          and sum(c.isupper() for c in uid) >= 2
          and sum(c.isdigit() for c in uid) >= 3)
    print("Valid" if ok else "Invalid")

# ===== Validating Credit Card Numbers =====
import re
import email.utils
from html.parser import HTMLParser

for _ in range(int(input())):
    card = input().strip()
    ok = re.match(r'^[456]\d{3}(-?\d{4}){3}$', card) and not re.search(r'(\d)\1{3}', card.replace('-', ''))
    print("Valid" if ok else "Invalid")

# ===== Validating Postal Codes =====
import re
import email.utils
from html.parser import HTMLParser

regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"


P = input()
print(bool(re.match(regex_integer_in_range, P)) and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

# ===== Matrix Script =====
import re
import email.utils
from html.parser import HTMLParser

n, m = map(int, input().split())
rows = [input().ljust(m) for _ in range(n)]
decoded = ''.join(''.join(col) for col in zip(*rows))
print(re.sub(r'(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])', ' ', decoded))


# ############################################################################
# PROBLEM 1 - XML
# ############################################################################

# ===== XML 1 Find the Score =====
def get_attr_number(node):
    return sum(len(e.attrib) for e in node.iter())


import sys
import xml.etree.ElementTree as etree
sys.stdin.readline()
xml = sys.stdin.read()
tree = etree.ElementTree(etree.fromstring(xml))
print(get_attr_number(tree.getroot()))

# ===== XML2 Find the Maximum Depth =====
maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    maxdepth = max(maxdepth, level)
    for child in elem:
        depth(child, level)


import xml.etree.ElementTree as etree
n = int(input())
xml = ''
for i in range(n):
    xml = xml + input() + '\n'
tree = etree.ElementTree(etree.fromstring(xml))
depth(tree.getroot(), -1)
print(maxdepth)


# ############################################################################
# PROBLEM 1 - CLOSURES AND DECORATORS
# ############################################################################

# ===== Standardize Mobile Number Using Decorators =====
def wrapper(f):
    def fun(l):
        f(['+91 ' + c[-10:-5] + ' ' + c[-5:] for c in l])
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

l = [input() for _ in range(int(input()))]
sort_phone(l)

# ===== Decorators 2 Name Directory =====
def person_lister(f):
    def inner(people):
        return map(f, sorted(people, key=lambda p: int(p[2])))
    return inner


@person_lister
def name_format(person):
    return ('Mr. ' if person[3] == 'M' else 'Ms. ') + person[0] + ' ' + person[1]

people = [input().split() for i in range(int(input()))]
print(*name_format(people), sep='\n')


# ############################################################################
# PROBLEM 1 - NUMPY
# ############################################################################

# ===== Arrays =====
import numpy as np
import numpy

def arrays(arr):
    return numpy.array(arr[::-1], float)


arr = input().strip().split(' ')
print(arrays(arr))

# ===== Shape and Reshape =====
import numpy as np
import numpy

print(np.array(input().split(), int).reshape(3, 3))

# ===== Transpose and Flatten =====
import numpy as np
import numpy

n, m = map(int, input().split())
a = np.array([input().split() for _ in range(n)], int)
print(a.T); print(a.flatten())

# ===== Concatenate =====
import numpy as np
import numpy

n, m, p = map(int, input().split())
a = np.array([input().split() for _ in range(n)], int)
b = np.array([input().split() for _ in range(m)], int)
print(np.concatenate((a, b), axis=0))

# ===== Zeros and Ones =====
import numpy as np
import numpy

dims = tuple(map(int, input().split()))
print(np.zeros(dims, dtype=int)); print(np.ones(dims, dtype=int))

# ===== Eye and Identity =====
import numpy as np
import numpy

np.set_printoptions(legacy='1.13')
n, m = map(int, input().split())
print(np.eye(n, m))

# ===== Array Mathematics =====
import numpy as np
import numpy

n, m = map(int, input().split())
a = np.array([input().split() for _ in range(n)], int)
b = np.array([input().split() for _ in range(n)], int)
print(a + b, a - b, a * b, a // b, a % b, a ** b, sep="\n")

# ===== Floor Ceil and Rint =====
import numpy as np
import numpy

np.set_printoptions(legacy='1.13')
a = np.array(input().split(), float)
print(np.floor(a)); print(np.ceil(a)); print(np.rint(a))

# ===== Sum and Prod =====
import numpy as np
import numpy

n, m = map(int, input().split())
a = np.array([input().split() for _ in range(n)], int)
print(np.prod(np.sum(a, axis=0)))

# ===== Min and Max =====
import numpy as np
import numpy

n, m = map(int, input().split())
a = np.array([input().split() for _ in range(n)], int)
print(np.max(np.min(a, axis=1)))

# ===== Mean Var and Std =====
import numpy as np
import numpy

n, m = map(int, input().split())
a = np.array([input().split() for _ in range(n)], int)
print(np.mean(a, axis=1)); print(np.var(a, axis=0)); print(round(np.std(a), 11))

# ===== Dot and Cross =====
import numpy as np
import numpy

n = int(input())
A = np.array([input().split() for _ in range(n)], int)
B = np.array([input().split() for _ in range(n)], int)
print(np.dot(A, B))

# ===== Inner and Outer =====
import numpy as np
import numpy

a = np.array(input().split(), int); b = np.array(input().split(), int)
print(np.inner(a, b)); print(np.outer(a, b))

# ===== Polynomials =====
import numpy as np
import numpy

p = list(map(float, input().split())); x = float(input())
print(np.polyval(p, x))

# ===== Linear Algebra =====
import numpy as np
import numpy

n = int(input())
a = np.array([input().split() for _ in range(n)], float)
print(round(np.linalg.det(a), 2))


# ############################################################################
# PROBLEM 2 - PROBLEM 2 - ALGORITHMS
# ############################################################################

# ===== Birthday Cake Candles =====
def birthdayCakeCandles(candles):
    return candles.count(max(candles))


import os
fptr = open(os.environ.get('OUTPUT_PATH', '/dev/stdout'), 'w')
input()
candles = list(map(int, input().rstrip().split()))
fptr.write(str(birthdayCakeCandles(candles)) + '\n')
fptr.close()

# ===== Number Line Jumps kangaroo =====
# Meet after j jumps iff x1 + j*v1 == x2 + j*v2  ->  j = (x2-x1)/(v1-v2), integer >= 0
def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        return "YES" if x1 == x2 else "NO"
    d, v = x2 - x1, v1 - v2
    return "YES" if d % v == 0 and d // v >= 0 else "NO"


import os
fptr = open(os.environ.get('OUTPUT_PATH', '/dev/stdout'), 'w')
x1, v1, x2, v2 = map(int, input().split())
fptr.write(kangaroo(x1, v1, x2, v2) + '\n')
fptr.close()

# ===== Viral Advertising =====
def viralAdvertising(n):
    shared, cumulative = 5, 0
    for _ in range(n):
        liked = shared // 2
        cumulative += liked
        shared = liked * 3
    return cumulative


import os
fptr = open(os.environ.get('OUTPUT_PATH', '/dev/stdout'), 'w')
fptr.write(str(viralAdvertising(int(input().strip()))) + '\n')
fptr.close()

# ===== Recursive Digit Sum =====
def superDigit(n, k):
    s = sum(map(int, n)) * k          # avoid building the huge concatenated string
    while s >= 10:
        s = sum(map(int, str(s)))
    return s


import os
fptr = open(os.environ.get('OUTPUT_PATH', '/dev/stdout'), 'w')
n, k = input().split()
fptr.write(str(superDigit(n, int(k))) + '\n')
fptr.close()

# ===== Insertion Sort Part 1 =====
def insertionSort1(n, arr):
    e, i = arr[-1], n - 2
    while i >= 0 and arr[i] > e:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1
    arr[i + 1] = e
    print(*arr)


n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
insertionSort1(n, arr)

# ===== Insertion Sort Part 2 =====
def insertionSort2(n, arr):
    for i in range(1, n):
        key, j = arr[i], i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(*arr)


n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
insertionSort2(n, arr)