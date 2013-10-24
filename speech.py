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

import unittest
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

def getBuzzwordsFromUser():
    buzzwordlist = CuratedList()
    # catch error from CuratedList object, print error msg, try again
    buzzwordlist.addToList(raw_input("What is the first buzzword you want to insert?"))
    buzzwordlist.addToList(raw_input("What is the second buzzword you want to insert?"))
    buzzwordlist.addToList(raw_input("What is the final buzzword you want to insert?"))
    return buzzwordlist

class item_insertion_test_case(unittest.TestCase):
    def test_valid_item_insertion(self):
    #Try taking an empty list and make sure that when we insert a new valid item,
    #it works.
        testlist = CuratedList()
        testitem = "bottle"
        expectedresult = ["bottle"]
        testlist.addToList(testitem)
        self.assertEqual(testlist.contents, expectedresult)    

    def test_invalid_item_insertion(self):
    #Insert an invalid item into a list and ensure it gives the right
    #errors: "that's not one English word" if it's not all alphabetical characters,
    #"try again; what did you mean?" if it's empty. Rerun the raw_input.
        testlist = CuratedList()
        testnumber = "6"
        self.assertRaisesRegexp(ValueError, ".*word.*", testlist.addToList, testnumber)
        self.assertRaisesRegexp(ValueError, ".*empty.*", testlist.addToList, "")

class Bug(dict):
    """a dict with the stuff I need."""
    def __init__(self,i,t,o):
        self.__setitem__("id",i)
        self.__setitem__("title",t)
        self.__setitem__("owner",o)

    def getBugNumber(self):
        return self.get["id"]

    def getBugTitle(self):
        return self.get["title"]

    def getBugReporter(self):
        return self.get["owner"]

def makeBugValues():
    #choose values for a bug by choosing randomly from bug-related lists
    return random.choice(idnums), random.choice(titles), random.choice(owners)

def insertBugNumber(insertion, template):
    return template % insertion

class bug_test_case(unittest.TestCase):

    def test_make_bug(self):
        #The makeBugValues function is too trivial to test.
        testnumber = 1
        testowner = "Martin Pool"
        testtitle = "bad version number"
        expectedbug = {"id":1,"title":"bad version number","owner":"Martin Pool"}
        self.assertEqual(Bug(testnumber,testtitle,testowner),expectedbug)

    def test_extract_bug_info(self):
    #Check whether, given a mock bug, we can extract the bug number, title,
    #and reporter name.
        testbug = {"id":1,"title":"bad version number","owner":"Martin Pool"}
        testnumber = 1
        testowner = "Martin Pool"
        testtitle = "bad version number"
        self.assertEqual(testbug.getBugNumber,testnumber)
        self.assertEqual(testbug.getBugTitle,testtitle)
        self.assertEqual(testbug.getBugReporter,testowner)

    def test_insert_bug_number(self):
    #Given a mock bug # and a mock template, check that inserting the bug #
    #into the template gives us a template with the bug # filled in.
        bugnumber = "567"
        template = "I know %s is more important than ever."
        expectedresult = "I know 567 is more important than ever."
        self.assertEqual(insertBugNumber(bugnumber, template), expectedresult)

    def test_insert_bug_title(self):
    #Given a mock bug title and a mock template, check that inserting the bug
    #title into the template gives us a template with the bug title filled in.
        pass

    def test_insert_bug_reporter(self):
    #Given a mock bug reporter and a mock template, check that inserting the
    #reporter name into the template gives us a template with the bug
    #reporter's name filled in.
        pass

class buzzword_test_case(unittest.TestCase):

    def test_buzzword_grab(self):
    #Grab a buzzword from the list.
        pass

    def test_buzzword_insert(self):
    #Check that the buzzword inserted into the template is the one you 
    #wanted to insert.
        pass

class output_test_case(unittest.TestCase):

    def test_print_to_console(self):
    #not sure how to test this.
        pass

def main():
    unittest.main()
    getBuzzwordsFromUser()

if __name__ == "__main__":
    main()
