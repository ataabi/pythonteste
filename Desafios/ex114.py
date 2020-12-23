# Crie um código em Python que teste se o site Pudim está acessivel pelo comp
import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://pudim.com.br")
except urllib.error.URLError:
    print('Não foi possivel acessar o site no momento')
else:
    print('Web site is Online (=D)')

print()

for c in site:
    print(c)

