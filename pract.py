import os
from os import path
import datetime
from datetime import date,time,timedelta
import time


#--------------------------------------------------- Functions ----------------------------------------------------
#----------------- YIELD functions ---------------------

def YieldFunction(x = 2):  # x by default is set to 2 if no value is passed
        while(True):      # it runs forever
            yield x+1     # while running forever, it keeps returning generator which is list but with open brackets
            x +=1         # the good thing about yeild is that it acts like return but upon another call of function, the value of x wont be reset and will start from the same point


def SwapArgu(x=None, y=1):
    return x +y;      # every variable is object as they have class which can find out using type(x)
#------------ Infinite Arguments Function ---------------

def InfiniteFunction(*args):  # can take inifinite number of arguments
    for value in args:
        print(value)

#------ Combination of infinite and normal arguments -------

def InfCombFunction(x, y, *args):
    for item in args:
        print (item)
    return x-y;

#-------------- Take infinite key value (Dict) arguments --------------

def functionTest3(a, b, *args, **kwargs):  # take normal, infinite, and named arguments
    print(kwargs['vege']);
    for i in kwargs:
        print(i + "=" +  kwargs[i])

    #------------- OR --------------
    for i, value in kwargs.items():
        print (i + "=" + value)

#----------------------------String Function -------------------------
def StrFunc():

    z = "String"
    print(z[2:6])    # slice
    print(z[2:6:2])  # the first two argu are range and the last one is the step

    print(z.capitalize())
    print(z.lower())
    print(z.upper())

    print(z.find('ring'))  # --finds the index, it will return 2 because r is at index 2
    print(z.replace('String', '  Replaced String   '))
    print(z.strip())  # Removes the whitespace at the begining and end
    print(z.isdigit())  # checks if there is a number in string







#-------------- Prime Function -------------
def isPrime(n):
    if n == 1:
        print("1 is prime")  # 1 is special
        return False
    for x in range(2, n):  # go from 2 until n-1
        if n % x == 0:     # and figure out if it is divisible by any number
            print("{} is not prime".format(n))
            return False
    else:
        print("The number is prime {}".format(n))  # this means the number is not divisible by any number except on its own
        return True

#------------------------------------------- If Else -------------------------------------------------------
def ifelseTest():
    x, y = 10, 100;
    '''
    if(x<y):
        result = "x is less than y";
    elif(x==y):
        result = "x is equal to y";
    else:
        result = "x is greater than y";
    print result;
    '''
    #---------------Minimized version -------------------------------#
    result = "x is less than y" if(x<y) else "x is greater than y";
    print(result);
     
#------------------------------------------------ For Loop ------------------------------------------------
def forloop():
    print ("The loop will go until 9");
    for i in range(5,10):
        print (i);

    print ("While loop");
    x =0;
    while(x<5):
        print (x);
        x =x +1;

    print ("Loop with index");
    days = ["Mon", "Teu", "Wed"];
    for i, d in enumerate(days):
        print (i, d);

#----------------------------------------------- File Operations -----------------------------------------------------------
def fileOperations():

    f = open("textfile.txt", "w") #--w is for write and + is for creating it if it doesnt exist
    for x in range(10):
        f.write("This is line %d\n" % (x+1)) # -- %d is a placeholder for the variable x


    f = open("textfile.txt", "a+") # adds to the content of file and doesnt overwrite like w
    for x in range(2, 5):
        f.write("Appended content %d\n" % (x+1))

    #-----------Exception ------------  define your own exceptions using raise
    try:
        f = open("textfile1.txt", "r")
        if f.mode == 'r':
            for x in f.readlines():  # f.read can be used but thats reading the whole file, so better is to use readline that justs reads each line and adds to the list
                print(x, end="")  # setting end to empty will remove the extra line from print

    except IOError as e:    # if you dont know the type of erro, then just use except and add a print function
        print("Error {}".format(e))

    print (os.name)
    print ("Item exists " + str(path.exists("textfile.txt")))
    print ("Item is a file " + str(path.isfile("textfile.txt")))
    print ("Item is a directory " + str(path.isdir("textfile.txt")))
    print ("Items path " + str(path.realpath("textfile.txt")))   # returns the path of file

    #Get modification time of file
    t = time.ctime(path.getmtime("textfile.txt"))
    print (t)
    print (datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))) # just a different format of getting modification time

    #Find out how long ago it was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print ("It has been " + str(td) + " The file was modified")  # print the whole time the last modifiied
    print ("Or, " + str(td.total_seconds()) + " seconds") # just prints the seconds and milliseconds


#----------------------------------------------------- Fetch Web Data -----------------------------------------------------

def fetchWebData():
    webURL = urllib2.urlopen("http://strangerschat.herokuapp.com")

    print ("result data " + webURL.read()); # returns the number of lines of code


#--------------------------------------------------- Inheritance ---------------------------------------------------------
class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):    #-- Abstract method ---
        raise NotImplementedError("subclass Must implement it")

class Dog(Animal):

    def __init__(self, name="default", age=0, legs="two"): # default values are set if no value is passed
        super().__init__(name, age)
        self.legs = legs
    
    def talk(self):
        return "Woo Woo"
    
class Cat(Animal):
    
    def __init__(self, name, age, legs):
        super(Cat, self).__init__(name , age)
        self.legs = legs

    def talk(self):
        return "Meow Meow"



#--------------------------------------------------Tuples and Lists ----------------------------------------------------

def TupleList():
    x = (2, 4 ,6)  # immutable (unchangeable) tuple and is low on memory
    print(x);

    y = [2 ,4 ,5]    # mutable
    y.append(7)      # add 7 in end
    y.insert(0, 10)  # add 10 in begining
    print(y)


    a = dict(        # dictionary
        one = 1, two =2 , three =3
    )
    a['seven'] =7    # add to dict

    print(a.get('one', 'not found'))  # get the value by providing key and if not found, message: not found

    for i in a.keys():
        print(i, a[i])

    e = True

    print(type(e))


def main():

    StrFunc()

    d = Dog("jack", 5, "four")
    print("The dog {} is {} years old and  has {} legs".format(d.name, d.age, d.legs))
    print(d.talk())

    #---------------------- Polymorphism ------------------------
    obj = (Dog("Jerry", 7, "four"), Cat("Henry", 2, "four")) # generator function as i used open bracked instead of [] since this takes very little ram

    for item in obj:
        print(item.talk())


    for n in YieldFunction():  # returns an object because of yeild in function def, therefore requires iterator
        if n > 10: break      # once the value reaches greater than 10 it implements break
        print(n)              # otherwisse keep printing the value returned by generator on fly opposed to array or list who occupy the RAM


    #print(SwapArgu(y=2, x=3))
    #InfiniteFunction(4,6,6,7);
    #print(InfCombFunction(10,5,6,7,8,8))
    #functionTest3(3, 5, 6, 7, 8, fruit='apple', vege='cabbage')
    #ifelseTest();
    #forloop();
    #fileOperations();
    #for i in range(1, 20):
    #    isPrime(i)
    #fetchWebData();
    #TupleList()

    
if __name__ == "__main__":
    main()
