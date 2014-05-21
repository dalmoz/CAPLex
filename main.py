#! /bin/python

# adding PATHs to current project
import sys
sys.path.insert(0, './fetch/')
sys.path.insert(0, './clean/')
sys.path.insert(0, './scan/')
sys.path.insert(0, './heads/')

# unix or other ANSI-comptaible terminals only
# def colBool( dbool ):
#     class colors:
#         OKGREEN = '\033[92m'
#         FAIL    = '\033[91m'
#         ENDC    = '\033[0m'
#     rtn = colors.OKGREEN + "True" if dbool else colors.FAIL + "Fail"
#     rtn = rtn + colors.ENDC
#     return rtn

print "    CAPLex utilization PoC - targeting TextCAPTCHA.com"
print "--=======================================================--"
# fetching - for PoC I've included TextCaptcha custom fetcher
import apiXml

#Definitions for fetched url
furl = 'http://api.textcaptcha.com/d0s5wjhqfa8k0kwgs004sc8co2ugh85b'
qTag = 'question'

print 'Fetching: ' + furl
print 'stripping <' + qTag + '> tag...'

challenge = apiXml.parseUrl( furl , qTag )

print '\nChallenge is: ' + challenge

import scan

print "\nInit. TOKEN marking:"
kIntegers = scan.integers( challenge )
print 'Integers:\t\t\t' + str(kIntegers)
kMath = scan.math( challenge )
print 'Math symbols:\t\t\t' + str(kMath)
kPos = scan.position( challenge )
print 'Positional reference:\t\t' + str(kPos)
kCount = scan.counting( challenge )
print 'Counting indicators:\t\t' + str(kCount)
kDigit = scan.digits ( challenge )
print 'Digits designation:\t\t' + str(kDigit)
kName = scan.names( challenge )
print 'Name indicators:\t\t' + str(kName)
kRelation = scan.compare( challenge )
print 'Relational operators:\t\t' + str(kRelation)
kList = scan.listSelect( challenge )
print 'Listing parameters:\t\t' + str(kList)
kColor = scan.color( challenge )
print 'Selection of colour:\t\t' + str(kColor)
kBody = scan.bodyPart( challenge )
print 'Body part selection:\t\t' + str(kBody)
kDay = scan.dayRef ( challenge )
print 'Day reference:\t\t\t' + str(kDay)
print ''

answer = "NO HEAD SELECTED"
## Boolean logic starts here
import head
# Relation from a list of numbers
if (kIntegers and kRelation):
    print 'Head selection - RELATION'
    answer = head.relation( challenge )
# Colour pick
elif ( kColor and not kCount and not kPos ):
    print 'Head selection - PICK COLOR'
    answer = head.color( challenge )
# Name pick
elif ( kName and not kCount and not kPos ):
    print 'Head selection - PICK NAME'
    answer = head.name( challenge )
# count body parts
elif (kCount and kBody):
    print 'Head selection - COUNT (BODY PARTS)'
    answer = head.countBody( challenge )
# count colors
elif (kCount and kColor):
    print 'Head selection - COUNT (COLOURS)'
    answer = head.countColor( challenge )
# solve math
elif (kIntegers and kMath and not kDigit and not kPos):
    print 'Head selection - EQUATION'
    answer = head.math( challenge )
# digitize
elif (kIntegers and kDigit and not kPos):
    print 'Head selection - DIGITIZE'
    answer = head.digits( challenge )
# enumerative colors
elif (kPos and kColor):
    print 'Head selection - POSITION IN SERIES (COLOUR)'
    answer = head.position( challenge, "c" )
elif (kPos and kIntegers and not kList):
    print 'Head selection - POSITION WITHIN A NUMBER'
    answer = head.position( challenge, "d" )
# spit it out, midget
print '\n\tSolution: ' + str(answer)

# out-of-scope control
if (kIntegers or kMath or kPos or kCount or kName or kRelation or
    kList or kColor or kBody or kDay) == False:
    print "NO INDICATION FOUND - SOMETHING IS MISSING"
