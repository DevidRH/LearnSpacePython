#ANCHOR - Character Class EX2
"""
Implement a function which extracts year, month and date from an url by using regular expression pattern.

url = https://www.apmillers.com/news/daily/wp/2022/02/02/regular-expressions-patterns/

extract_date(url)

Output

[('2022', '02', '2')]

"""

import re

v_url = "https://www.apmillers.com/news/daily/wp/2022/02/02/regular-expressions-patterns/"

v_regex_pattern = re.compile(r'(\d{4})/(\d{2})/(\d{2})')

x = v_regex_pattern.findall(v_url)
print(x)