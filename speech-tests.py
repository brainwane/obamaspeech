#!/usr/bin/python
"""
This file contains the unit tests for the speech generator.
"""
import unittest
from speech import *

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

class bug_test_case(unittest.TestCase):
    def test_make_bug(self):
        #The makeBugValues function is too trivial to test.
        #Update: Not too trivial to test (it emits a tuple. Who would have
        #thought this? but anyway that's the only tricky thing.)
        testnumber = 1
        testowner = "Martin Pool"
        testtitle = "bad version number"
        expectedbug = {"id":1,"title":"bad version number","owner":"Martin Pool"}
        self.assertEqual(Bug(testnumber,testtitle,testowner),expectedbug)

    def test_extract_bug_info(self):
    #Check whether, given a mock bug, we can extract the bug number, title,
    #and reporter name.
        testbug = Bug(1,"bad version number","Martin Pool")
        testnumber = 1
        testowner = "Martin Pool"
        testtitle = "bad version number"
        self.assertEqual(testbug.getBugNumber(),testnumber)
        self.assertEqual(testbug.getBugTitle(),testtitle)
        self.assertEqual(testbug.getBugReporter(),testowner)

    def test_insert_bug_number(self):
    #Given a mock bug # and mock template, check that inserting the bug # into
    #the template gives us a template with the bug # stringified and filled in.
    #All the other insertions (buzzwords, owners, and titles) are already
    #strings, so I don't expect any trouble with them.
        bugnumber = 567
        template = "I know %s is more important than ever."
        expectedresult = "I know 567 is more important than ever."
        self.assertEqual(insertThing(bugnumber, template), expectedresult)

class buzzword_test_case(unittest.TestCase):

    def test_buzzword_grab(self):
        testlist = CuratedList()
        testlist.contents = ["NoSQL","distributed"]
        self.assertIn(testlist.buzzGrab(),testlist.contents)        

    def test_buzzword_insert(self):
    #Check that the buzzword inserted into the template is the one you 
    #wanted to insert.
        testword = "NoSQL"
        template = "I know %s is more important than ever."
        expectedresult = "I know NoSQL is more important than ever."        
        self.assertIn(insertThing(testword,template),expectedresult)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
