# def name(first_name):
#     print(first_name)
# name("lucy")

# #DEFAULT PARAMETERS 
# def number(a, b=4):
#     return(a*b)
    
# print(number(2))

# #OVERINDING THE DEFAULT PARAMETER
# def number(a, b=4):
#     return(a*b)
    
# print(number(2,8))

# #POSITIONAL ARGUMENTS 
# # they need to be places in a proprt position or order 
# def func(a,b,c):
#     return(a*b+c)
# print(func(3,2,4))

#KEYWORD ARGUMENTS
# These are arguments passed to a function or methis and which is preceded by a keyword and an equals sign
def marks(math,science, english):
    return(math+science+english)
        #passing values
print(marks(70,80,90))
        #calling function with key arguments
print(marks(math=70, science=80, english=90))
            #calling function by changing position of arguments with keywords
print(marks(science=80, math=70,  english=90))            
