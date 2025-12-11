import requests

if __name__ == "__main__":
    
    searched = set(["luanzito","MarcosK"])
    cookies = {
                "PHPSESSID" : "COMPLETAR ACA CON LA COOKIE!!!!",
              }
    
    for page in range(1,20000):
        found = []
        print(".",end="",flush=True)
        body = str(requests.get("https://cses.fi/problemset/stats/p/{}".format(page), cookies=cookies).content)
        if "Please login to see the statistics" in body:
            print()
            print("BAD PHPSESSID !!!")
            exit()
        for user in searched:
            if user in body:
                print()
                print("{} is in page {}".format(user, page))
                found.append(user)
        for user in found:
            searched.remove(user)
            if not searched:
                exit()
