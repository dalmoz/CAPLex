import clean, lists, numbers
import re
import unicodedata

def digits( chlng ):
    
    chlng = clean.simpleout( chlng )
    chlng = clean.extraout( chlng )
    chlng = chlng.lower()
    #print "after lower - " + chlng
    chlng = numbers.text2int( chlng )
    
    return chlng
    
    
def relation( chlng ):
    hi = ["highest", "maximum", "maximal", "largest", "biggest"]
    lo = ["lowest", "minimum", "minimal", "smallest"]
    relations = hi + lo
    
    chlng = chlng.lower()
    
    relationHi = False
    
    for i in clean.str2listall( chlng ):
        if i in hi:
            relationHi = True
            break
    
    nchlng = clean.str2listall( chlng )
    nchlng = " ".join( nchlng )
    nchlng = clean.simpleout( nchlng )
    nchlng = nchlng.replace(" or ", ",")
#     nchlng = clean.str2listall( chlng )
    
    
    for i in relations:
        nchlng = nchlng.replace(i, "") 
        
    chlngsplit = nchlng.split(",")
   
    
    for c in range(0,8):
        counter = 0
        for i in chlngsplit:
            if i[:1] == " ":
                chlngsplit[counter] = i[1:]
            if i[-1:] == " ":
                chlngsplit[counter] = i[:-1] 
            counter = counter + 1
    
#     print chlngsplit
    
    counter = 0 

    for i in chlngsplit:
        m = re.search('[a-z]', i)
        if m:
            chlngsplit[counter] = str(numbers.text2int( str( i ) ) )
        else:
            chlngsplit[counter] = str( i )
        counter = counter + 1

    #print nchlng + " ......  split: " + " ".join(chlngsplit)
    if relationHi:
        return max(filter(None, chlngsplit))
    else:
        return min(filter(None, chlngsplit))
        

def countBody( chlng ):
    
    bodyparts = lists.listBody()
    
    chlng = chlng.lower()
    chlng = clean.str2listall( chlng )
    counter = 0
    
    for i in chlng:
        if i in bodyparts:
            counter = counter + 1
            
    return counter

def countColor( chlng ):
    colors = lists.colors()
    
    chlng = chlng.lower()
    chlng = clean.simpleout( chlng )
    chlng = clean.str2listall( chlng )
    counter = 0
    
    for i in chlng:
        if i in colors:
            counter = counter + 1
            
    return counter

def color( chlng ):
    sColors = lists.colors()
    
    for i in sColors:
        if i in chlng:
            return i
    
    return False

def name( chlng ):
    import names
    
    lnames = names.listNames()
    chlist = clean.str2list( chlng )
    
    for i in lnames:
        if i in chlist:
            return i

def math( chlng ):
    chlng = clean.simpleout( chlng )
    #print "before lowering - " + chlng
    chlng = chlng.lower()
    chlng = chlng.replace("add", "+")
    chlng = chlng.replace("plus", "+")
    chlng = chlng.replace("minus", "-")
    #print "after lowering - " + chlng
#     lchlng = clean.str2list( chlng )
#     nchlng = " ".join( lchlng )
    nchlng = clean.simpleout( chlng )
    #print "nchlng - " + nchlng
    
#     print "after replace - " + nchlng
    
    part1 = ""
    part2 = ""
    moper = ""
    
    if "+" in nchlng:
        part1, part2 = nchlng.split("+", 1)
        moper = "+"
    elif "-" in nchlng:
        part1, part2 = nchlng.split("-", 1)
        moper = "-"
#     print "part1 = " + part1 + "      part2 = " + part2
    part1f = part1
    part2f = part2
    
    for i in part1.split():
        if i in lists.numbers():
            part1f = str(numbers.text2int( part1 )) 
            break
        
    for i in part2.split():
        if i in lists.numbers():
            part2f = str(numbers.text2int( part2 ))
            break
    
    nchlng = part1f + moper + part2f
    solution = str(eval( nchlng ))
    
    return solution

def position( chlng, k ):
    
    if k == "c":
        hits = lists.colors()
    elif k == "d":
        hits = range(0,10)
    
    # find out enumeration value
    pos = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th"]
    num = 0
    for i in clean.str2listall( chlng ):
        if i in pos:
            num = i[:1]
            break
    
    counter = 0
    solution = ""
    
    if k == "c":
        for i in clean.str2listall( chlng ):
            if i in hits:
                counter = counter + 1
                if num == str(counter):
                    solution = i
    elif k == "d":
        numb = [int(s) for s in clean.str2listall( chlng ) if s.isdigit()]
#         for i in clean.str2listall( chlng ):
#             m = re.search('[0-9]{3,}', i)
#             if m:
#                 solution = i[ num + 1 ]
        foo = str(numb[0])
        solution = foo[int(num) -1]
    return solution