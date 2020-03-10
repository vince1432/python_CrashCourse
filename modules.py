# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

#COre modules
from datetime import date as d
import time
from time import time

#PIP module
from camelcase import CamelCase

#today = datetime.date.today()
today = d.today()
timestamp = time()

c = CamelCase()
print(c.hump('hello there world'))

print(timestamp)