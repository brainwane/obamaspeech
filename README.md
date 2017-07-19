**[Command-line version](#command-line-version)** |
**[Web version](#web-version)** |
**[Change it up](#change-it-up)**


# Silly speech generator

I wrote this command-line speech generator just after Barack Obama [gave a televised speech](http://www.whitehouse.gov/the-press-office/2013/10/21/remarks-president-affordable-care-act) partially about trouble with HealthCare.gov. I thought, "what if Barack Obama gave LOTS of speeches about tech?"

Also, I wanted to try out test-driven development, so speech-tests.py has the tests I wrote (using Python's `unittest` module) before or as I wrote functionality.

So, here you go.

## Command-line version

Run `speech.py` at a command line and type in three tech buzzwords when asked. (Alphabetical characters and spaces work, but no other punctuation -- "the cloud" and "NoSQL" are fine, but "object-oriented" won't work.) You'll then get a short speech incorporating at least one of the buzzwords you've provided.

Example:

>$ python speech.py

>What is the first tech buzzword you want to suggest? REST

>What is the second tech buzzword you want to suggest? eventual consistency

>What is the final tech buzzword you want to suggest? Agile

>*Hail to the Chief*

>My fellow Americans,

>I know Agile is more important than ever. That's why I have committed the federal government to implementation of REST within the next 100 days.

>We will achieve this goal by fixing bug number 9497, "Account Creation leaves broken unusable accounts due to VisualEditorHooks::onAddNewAccount", in close coordination with state and local agencies, as well as bug reporter Mary Rose Cook.

>Thank you, and may God bless Agile.

>*Bugle tones*


## Web version
Then I decided I need to brush up on JavaScript!

`page.html` calls jQuery, `speech.js` and `style.css`. It asks the user to `input` three buzzwords, then hides the input `<div>` when displaying the finished speech. There's a footer that floats right.


## Change it up

You could add:

1. An API call to a real bug tracker to get the titles, bug IDs, and reporter names for real live open bugs. (I was trying to do this originally, then gave up for expediency's sake. The point of the original exercise was learning TDD, not learning Bugzilla's or Launchpad's API.)
1. Better placement or better-than-random usage of the buzzwords.
1. More or better openings and closings.

[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)
