# One-away - There are three types of edits that can be performed on strings. Insert a character, removed a character, or replaced a character
# Given two strings, write a function to check if they are one edit away
# Example Pale, Ple yields ture
# Example Pale, Bake yields false

def testString(string1,string2):
    if len(string1)==len(string2):
        count=0
        for i in range(len(string1)):
            if string1[i]!=string2[i]:
                count+=1
            if count==2: #If they strings are the same length and more than two characters are different, it cannot be a one away
                return False
        return True
    elif abs(len(string1)-len(string2))==1:
        if len(string1)-len(string2)==-1:
            large_string=string2
            small_string=string1
        else:
            large_string=string1
            small_string=string2
        if string1[len(string1)-1]==string2[len(string2)-1] and string1[0]!=string2[0]:
            test = large_string[1:len(large_string)]==small_string #trim first character of large string
            return test
        if string1[0]==string2[0] and string1[len(string1)-1]!=string2[len(string2)-1]:
            test = large_string[0:len(large_string)-1]==small_string #trim last character of large string
            return test
        if string1[0]==string2[0] and string1[len(string1)-1]==string2[len(string2)-1]:
            j=1
            for i in large_string[1:len(large_string)-1]:
                if i!=small_string[j]:
                    large_string = large_string[:j]+large_string[j+1:]
                    test = large_string == small_string
                    return test
                j+=1


if testString("test","tnot"):
    print("It is a one away")
else:
    print("It is not")