#!/usr/bin/python
"""
This is a fake speech generator with a Mad Libs element.
The program takes place on the command line.

The input: raw_input() for three buzzwords.

The ouput should go something like:

random choice of {Flag shot|"Hail to the Chief"|"Now for a special announcement from our President"}

My fellow Americans, 

I know {tech buzzword} is more important than ever. That's why I have committed the federal government to implementation of {other tech buzzword} within the next 100 days.

We will achieve this goal by fixing bug number {bug #}, {bug title}, in close coordination with state and local agencies, as well as bug reporter {reporter name}.

Thank you, and may God bless {another tech buzzword}.

random choice of {Flag shot|"We now return you to your regularly scheduled programming"|Bugle tones}
"""

import random

openings = ["*Flag shot*","*Hail to the Chief*","Now for a special announcement from our President."]
closings = ["*Flag shot*","We now return you to your regularly scheduled programming.","*Bugle tones*"]

# bug-related lists
idnums = [54, 800, 8983, 5132]
titles = ["Gadget settings cannot be changed on MediaWiki 1.22wmf4", "Wrong Path Separator in bzr output on Windows","Spam filter not filtering majority of spam to Junk folder","Thumbnails of large PNGs are not generated","Account Creation leaves broken unusable accounts due to VisualEditorHooks::onAddNewAccount","VisualEditor: [Regression] Edit tab points to the oldid not the newid when saving (except for when creating pages)"] 
owners = ["Mary Rose Cook", "Zach Allaun", "Allison Kaptur"]

class CuratedList(object):
    def __init__(self):
        self.contents = []

    def addToList(self, newitem):
        # check for empty string
        # check for non-alpha
        # in those cases: ValueError
        # when you're writing the app: catch the error, give an error message per test
        if newitem == "":
            raise ValueError("empty string not allowed")
        elif not newitem.isalpha():
            raise ValueError("only one word of alphabetical characters allowed in this string")
        else:
            self.contents.append(newitem)

    def buzzGrab(self):
        return random.choice(self.contents)

def getBuzzwordsFromUser():
    buzzwordlist = CuratedList()
    # catch error from CuratedList object, print error msg, try again
    buzzwordlist.addToList(raw_input("What is the first buzzword you want to insert? "))
    buzzwordlist.addToList(raw_input("What is the second buzzword you want to insert? "))
    buzzwordlist.addToList(raw_input("What is the final buzzword you want to insert? "))
    return buzzwordlist

class Bug(dict):
    """a dict with the stuff I need."""
    def __init__(self,i,t,o):
        self.__setitem__("id",i)
        self.__setitem__("title",t)
        self.__setitem__("owner",o)

    def getBugNumber(self):
        return self.get("id")

    def getBugTitle(self):
        return self.get("title")

    def getBugReporter(self):
        return self.get("owner")

def makeBugValues():
    #choose values for a bug by choosing randomly from bug-related lists
    return random.choice(idnums), random.choice(titles), random.choice(owners)

def insertThing(insertion, template):
    if type(insertion) == str:
        return template % insertion
    else:
        return template % str(insertion)

def main():
    bzlist = getBuzzwordsFromUser()
    bug = Bug(*makeBugValues())

if __name__ == "__main__":
    main()
