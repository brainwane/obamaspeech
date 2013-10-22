#!/usr/bin/python3
"""
This is a fake speech generator with a Mad Libs element. I'm trying to do Python 3.
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

class item_insertion_test_case(unittest.TestCase):
    def test_valid_item_insertion(self):
    #Try taking a fake list and make sure that when we insert a new valid item,
    #it works.
        pass

    def test_invalid_item_insertion(self):
    #Insert an invalid item into a fake list and ensure it gives the right
    #errors: "that's not English" if it's not all alphabetical characters,
    #"try again; what did you mean?" if it's empty. Rerun the raw_input.
        pass

class bug_test_case(unittest.TestCase):

    def test_get_bug(self):
    #Check that we can actually get a bug via the API.
        pass

    def test_extract_bug_info(self):
    #Check whether, given a mock bug, we can extract the bug number, title,
    #and reporter name.
        pass

    def test_insert_bug_number(self):
    #Given a mock bug # and a mock template, check that inserting the bug #
    #into the template gives us a template with the bug # filled in.
        pass

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

if __name__ == "__main__":
    main()
