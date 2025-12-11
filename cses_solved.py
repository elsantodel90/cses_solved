import requests
import re

cookie = {"PHPSESSID":"COMPLETAR ACA CON LA COOKIE!!!!!"}

# santo
user=2612

data = requests.get("https://cses.fi/problemset").text
userdata = requests.get("https://cses.fi/problemset/user/{}/".format(user), cookies=cookie).text

solved = set(re.findall('<td ><a href="[^"]*" title="([^"]*)" class="task-score icon full">', userdata))

problems = [(int(a),int(b),name) for name, a, b in re.findall('<li class="task"><a href=[^>]*>([^<]*)</a><span class="detail">([^/]*)/([^<]*)</span>', data)]
problems.sort(reverse=True)

for a, b, name in problems:
    solvedString = "[SOLVED] " if name in solved else "         "
    print("{:6} / {:<6} {}{}".format(a,b,solvedString, name))
