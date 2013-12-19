#!/usr/bin/python

# Copyright 2013 Sumana Harihareswara

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
This is a fake speech generator with a Mad Libs element.
The program takes place on the command line.

The input: raw_input() for three buzzwords.

The ouput is text spit out to the user via the console.
"""

import random

openings = ["*Flag shot*","*Hail to the Chief*","Now for a special announcement from our President."]
closings = ["*Flag shot*","We now return you to your regularly scheduled programming.","*Bugle tones*"]

# bug-related lists
idnums = [43665, 9497, 49727, 50441, 369404, 48693] # real bug numbers from my browser history
titles = ["Gadget settings cannot be changed on MediaWiki 1.22wmf4", "Wrong Path Separator in bzr output on Windows","Spam filter not filtering majority of spam to Junk folder","Thumbnails of large PNGs are not generated","Account Creation leaves broken unusable accounts due to VisualEditorHooks::onAddNewAccount","VisualEditor: [Regression] Edit tab points to the oldid not the newid when saving (except for when creating pages)"] # names of real bugs from my browser history
owners = ["Mary Rose Cook", "Zach Allaun", "Allison Kaptur","Alan O'Donnell","Tom Ballinger"] # names of facilitators at Hacker School


fellow = "\nMy fellow Americans,\n"
important = "I know %s is more important than ever. That's why I have committed the federal government to implementation of %s within the next 100 days.\n"
coordinate = "We will achieve this goal by fixing bug number %s, \"%s\", in close coordination with state and local agencies, as well as bug reporter %s.\n"
thank = "Thank you, and may God bless %s.\n"

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
        elif not newitem.replace(" ","").isalpha():
            raise ValueError("only one word of alphabetical characters allowed in this string")
        else:
            self.contents.append(newitem)

    def buzzGrab(self):
        return random.choice(self.contents)

def getBuzzwordsFromUser():
    buzzwordlist = CuratedList()
    # catch error from CuratedList object, print error msg, try again
    buzzwordlist.addToList(raw_input("What is the first tech buzzword you want to suggest? "))
    buzzwordlist.addToList(raw_input("What is the second tech buzzword you want to suggest? "))
    buzzwordlist.addToList(raw_input("What is the final tech buzzword you want to suggest? "))
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
    print random.choice(openings)
    print fellow
    print important % (bzlist.buzzGrab(),bzlist.buzzGrab())
    print coordinate % (bug.getBugNumber(),bug.getBugTitle(),bug.getBugReporter())
    print thank % bzlist.buzzGrab()
    print random.choice(closings)

if __name__ == "__main__":
    main()
