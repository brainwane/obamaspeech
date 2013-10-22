#!/usr/bin/python

"""
This is a fake speech generator.

It should go something like:

{Flag shot|"Hail to the Chief"|"Now for a special announcement from our President"}

My fellow Americans, 

I know {tech buzzword} is more important than ever. That's why I have committed the federal government to implementation of {other tech buzzword} within the next 100 days.

We will achieve this goal by fixing bug number {bug #}, {bug title}, in close coordination with state and local agencies, as well as bug reporter {reporter name}.

Thank you, and may God bless {another tech buzzword}.

{Flag shot|"We now return you to your regularly scheduled programming"|Bugle tones}
"""

def test_valid_item_insertion():
    #Try taking a fake list and make sure that when we insert a new valid item,
    #it works.
    pass

def test_invalid_item_insertion():
    #Insert an invalid item into a fake list and ensure it gives the right
    #errors: "that's not English" if it's not all alphabetical characters,
    #"try again; what did you mean?" if it's empty. Rerun the raw_input.
