from utils import *

if __name__ == '__main__':
    name = 'Ya-qin Zhang'
    scientist = Scientist(name)
    link = scientist.get_scientist_link()
    result = scientist.get_articlelist(link)
    print(result)
    