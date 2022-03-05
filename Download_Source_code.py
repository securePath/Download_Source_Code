import turtle
import urllib.request as u
import pyfiglet
from termcolor import colored

print(colored("*********** Create By sucurePath ***********",'red'))
banner = colored(pyfiglet.figlet_format("source code"),'blue')
print(banner)

website_name = turtle.textinput("name","url")

source_code = u.urlopen(website_name)
read_s = source_code.read()
print(read_s)