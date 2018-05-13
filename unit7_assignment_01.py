__author__ = 'Kalyan'

problem = """
 We are going to revisit unit6 assignment3 for this problem.

 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 This program should be written as a command line script. It takes one argument the input file of words and outputs
 <input>-results.txt where <input>.txt is the input file of words.
"""
import sys

def file_out(source,file_name):
    result = run_anagram(source)
    f = open(file_name,"w")
    for i in result:
        for j in range(len(i)):
            f.write(str(i[j]))
            f.write("\n")
    f.close()


if __name__ == "__main__":
    file_name = sys.argv[1]
    f = open(file_name,"r")
    source = f.read()
    file_out(source,file_name)

def are_anagram(first,second):
    first = first.lower()
    second = second.lower()
    x=list(first)
    y=list(second)
    x.sort()
    y.sort()
    if x == y:
        return True
    else:
        return False


def run_anagram(source):
    source=source.replace("\n","")
    source=source.replace(" ","")
    slist = source.split(",")
    result=[]
    while len(slist)!=0 :
        tup=[]
        x=slist[0]
        for i in range(1,len(slist)):
            y = slist[i]
            if are_anagram(x,y):
                tup.append(y)
        if len(tup)!= 0 :
            tup.append(x)
            for i in tup :
                slist.remove(i)
            tup=sorted(tup,key=lambda v:v.upper())
            result.append(tuple(tup))
    result = sorted(result,key = lambda v:v[0].upper())
    return result


