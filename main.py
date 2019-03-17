from py_mini_racer import py_mini_racer #javascript embedding
import sys
import os

#include other folders

for libdir in os.listdir("."):
    sys.path.insert(0, libdir)

from entity_generator import EntityGenerator
#import entity

ctx = py_mini_racer.MiniRacer()

def eval_file(fname):           
    f = file(fname)
    lines = f.readlines()       
    [ctx.eval(l.rstrip("\r\n")) for l in lines]
    f.close()
    return lines


def main():
    entity_list = []
    gen = EntityGenerator()
    

    eval_file("test_script.js")
    while True:
        cmd = raw_input(">")
        
        if cmd == "r":
            eval_file("test_script.js")
        if cmd == "g":
            entity_list.append(gen.generate_entity([1,3,4]))
        if cmd == "ls":
            print([l for l in entity_list])
        else:
            print(ctx.call("fun2") + "\n")

            
if __name__ == "__main__":
    main()


