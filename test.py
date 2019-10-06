from bs4 import BeautifulSoup 
import requests 
import time
import os
clear = lambda: os.system('cls')
clear()
data = ["1de", "2de", "3de", "4de", "5de", "6de","7","8", "9", "10", "11", "12", "13", "14", "15","16", "17", "18", "19", "20", "21", "22", "23", "24", "27de","28","29", "30", "31", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro","janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro","1963", "1940" ]
_de = ["de"]
vr = []
b = "[0]","[1]","[2]","[3]","[4]","[5]","[6]","[7]","[8]","[9]","[", "]"
replace_2 = "´","~","´", "^"
bbbb = "<p>","<br>", "<a>", "href=", "<a","</p>","</br>", "</a>"
name = str(input("Qual o seu nome?\n "))
print("Prazer, {}! Meu nome é SEA! \n ".format(name))
time.sleep(2)
clear()
searching_for_what = str(input("Sobre o que você quer saber hoje, {}? \n ".format(name)))

url = "https://pt.wikipedia.org/wiki/"+searching_for_what

#for vv2 in range(0, len(replace_2)):
    #url = url.replace(replace_2[vv2],"")





r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lyric = soup.find_all('div', class_='mw-parser-output')
#print(lyric)
x = ""
for lyric_p in lyric:
    result = lyric_p.find_all('p' or 'br')
    for result_data in result:
        x = x + str(result_data.next_element)
        print(result_data.next_element)


#print(x)

for vv in range(0, len(b)):
  x=x.replace(b[vv], " ")


i = 0
cont = 0
tam = len(x.split())
_i = 0
'''
print("Texto: \n ======== \n {}".format(x))
print("\n =========== \n ")
print("Data encontrada: \n")
'''
string_result = ""   
print(x.split())
for b in range (0,int(len(x.split()))):
    vr.append(x.split()[b])  

    if x.split()[b]+x.split()[b-1] in data:
        print(x.split()[b]+" "+x.split()[b+1]) 
    i=i+1
#print(x)
 
print(string_result+".")

