/*This is a fake speech generator with a Mad Libs element.
The program takes place on the command line.

The input: prompt() for three buzzwords.

The ouput is text spit out to the user via page.html in this directory.*/

// # Copyright 2013 Sumana Harihareswara

// # This program is free software: you can redistribute it and/or modify
// # it under the terms of the GNU General Public License as published by
// # the Free Software Foundation, either version 3 of the License, or
// # (at your option) any later version.

// # This program is distributed in the hope that it will be useful,
// # but WITHOUT ANY WARRANTY; without even the implied warranty of
// # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// # GNU General Public License for more details.

// # You should have received a copy of the GNU General Public License
// # along with this program.  If not, see <http://www.gnu.org/licenses/>.

buzz1 = prompt("Enter your first buzzword.");
buzz2 = prompt("Enter your next tech buzzword.");
buzz3 = prompt("Enter your final silly buzzword.");

// buzz1 = "NoSQL";
// buzz2 = "cloud data";
// buzz3 = "computational complexity";

buzzwords = [buzz1, buzz2, buzz3];

openings = ["*Flag shot*","*Hail to the Chief*","Now for a special announcement from our President."];
closings = ["*Flag shot*","We now return you to your regularly scheduled programming.","*Bugle tones*"];

// bug-related lists
idnums = [43665, 9497, 49727, 50441, 369404, 48693] // real bug numbers from my browser history;
titles = ["Gadget settings cannot be changed on MediaWiki 1.22wmf4", "Wrong Path Separator in bzr output on Windows","Spam filter not filtering majority of spam to Junk folder","Thumbnails of large PNGs are not generated","Account Creation leaves broken unusable accounts due to VisualEditorHooks::onAddNewAccount","VisualEditor: [Regression] Edit tab points to the oldid not the newid when saving (except for when creating pages)"]; // names of real bugs from my browser history
owners = ["Mary Rose Cook", "Zach Allaun", "Allison Kaptur","Alan O'Donnell","Tom Ballinger"]; // names of facilitators at Hacker School


template = ["<br>My fellow Americans,<br> I know ", " is more important than ever. That's why I have committed the federal government to implementation of ", " within the next 100 days.<br> We will achieve this goal by fixing bug number ", ", \"", "\", in close coordination with state and local agencies, as well as bug reporter ", "<br>Thank you, and may God bless ", ".<br><br>"];

// openingtemplate = []
myfellowtemplate = ["My fellow Americans,"]
commitmenttemplate = ["I know ", " is more important than ever. That's why I have committed the federal government to implementation of ", " within the next 100 days."]
howtoachievetemplate = ["We will achieve this goal by fixing bug number ", ", \"", "\", in close coordination with state and local agencies, as well as bug reporter ", "."]
blessingtemplate = ["Thank you, and may God bless ", "."]
// closingtemplate = []

function choose(collection) {
    function getRandomInt(min, max) {
// gives random int between min & max inclusive
	return Math.floor(Math.random() * (max - min + 1) + min);
    }
    index = getRandomInt(0, collection.length-1);
    return collection[index];
}


function interpolate(replacements, template){
    // for i in template.length,
    // print template[i] + replacements[i]
    var resultstring = ""
    for (var i=0 ; i < template.length ; ++i) {
	resultstring += replacements[i];
	resultstring += template[i];
    }
    resultstring += replacements[replacements.length-1];
    return resultstring;
}

var array = [openings, buzzwords, buzzwords, idnums, titles, owners, buzzwords, closings];

function makechoices(collections) {
    // for each list (which is an item in collections), return a random choice
    var list = [];
    for (var i = 0; i < collections.length; ++i)
	list.push(choose(collections[i]));
    return list;
}

function loading() {
    replacements = makechoices(array);
    result = document.getElementById("blessing");
    result.innerHTML = interpolate(replacements, template);
}

window.onload = loading;
// var open = document.getElementById("opening");
// open.innerText = choose(openings);
