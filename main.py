import requests
from bs4 import BeautifulSoup
i = 140001

while i<=164004:
    if (i-1)%100==10:
        #11-10=01
        #11-9=02
        i+=1000
        i-=10
    r = requests.get('https://www.indiabix.com/electronics-and-communication-engineering/communication-systems/'+str(i))
    # print(i)

    soup = BeautifulSoup(r.content,"html.parser")
    data = []
    i+=1
    for data in soup.select(".bix-div-container"):
        print()
        print(data.select_one(".bix-td-qtxt").get_text(strip=True))
        m=0
        for option in data.select(".bix-td-option"):
            if m%2==0 and m!=0:
                print()
            print(option.get_text(),end=" ")
            m+=1
        print()
        print("Answer is: "+ data.select_one(".jq-hdnakq")["value"])

