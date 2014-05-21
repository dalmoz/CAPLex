import numbers

# extract numbers and expected extra words    
def get( chlng ):
    numbers.text2int( chlng )
    return solution

def str2list( chlng ):
    import re
    
    wlist = re.sub("[^\w]+|[+-]", " ", chlng).split()
    # wlist = re.findall(r"[\w']+|[.,!?;]", chlng )
    return wlist

def str2listall( chlng ):
    import re
    
    #wlist = re.sub("[^\w]", " ", chlng).split()
    wlist = re.findall(r"[\w']+|[.,!?;]", chlng )
    return wlist

def whitelist( chlng, sList ):
    
    chlng = chlng.lower()    
    lchlng = str2list( chlng )
    counter = 0
    newlist = []
    
    for i in lchlng:
        if i in sList:
            newlist = newlist + [i]
    
    return newlist

def blacklist( chlng, sList ):
    
    lchlng = str2list( chlng )
    counter = 0
    newlist = []
    
    for i in sList:
        if i in lchlng:
            newlist = newlist + [i]
               
    print "count = " + str(counter)

def simpleout( chlng ):
    simples = ["what's", "what", "is", "who","if ","then", "as", "digits", "numbers",
               "number", "digit", "?", ":", "which", "of", "these", "the",
               "equals", "equal", "=", "in ", " a ", "enter"]
    
    chlng = chlng.lower()
    
    for i in simples:
        chlng = chlng.replace(i, "")
    
    return chlng

def extraout( chlng ):
    extras = ["enter", "numbers", "digits", "number", "digit"]
    
    chlng = chlng.lower()
    
    for i in extras:
        chlng = chlng.replace(i, "")
    
    return chlng  