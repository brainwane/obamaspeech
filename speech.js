/*This is a fake speech generator with a Mad Libs element.
The program takes place on the command line.

The input: raw_input() for three buzzwords.

The ouput is text spit out to the user via the console.*/

/*
data sets of openings, closings, titles, owners, etc. - DONE

input - way to get buzzwords from user (probably via prompt()) - DONE

way to pick randomly from a collection - DONE

way to assemble strings into larger string --- concatenation via + - DONE

way to return finished giant string to the user - DONE

*/

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


template = ["<br>My fellow Americans,<br> I know ", " is more important than ever. That's why I have committed the federal government to implementation of ", " within the next 100 days.<br> We will achieve this goal by fixing bug number ", ", ", ", in close coordination with state and local agencies, as well as bug reporter ", ".<br>Thank you, and may God bless ", ".<br><br>"];

function choose(collection) {
    function getRandomInt(min, max) {
// gives random int between min & max inclusive
	return Math.floor(Math.random() * (max - min + 1) + min);
    }
    index = getRandomInt(0, collection.length-1);
    return collection[index];
}


// function assemble() {
//     // choose certain things from each collection
//     // return dictionary
//     var choices = new Object();
//     choices.open = choose(openings);
//     choices.buzza = choose(buzzwords);
//     choices.buzzb = choose(buzzwords);
//     choices.buzzc = choose(buzzwords);
//     choices.bug = choose(idnums);
//     choices.title = choose(titles);
//     choices.reporter = choose(owners);
//     choices.close = choose(closings);
//     function interpolate(words, template) {
//     // interpolates words into template in a particular order
//     // takes obj of words (that is length 1 fewer than the # of elements in template)
// 	var resultstring = ""
// 	resultstring += words.open
// 	resultstring += template[0] + words.buzza
// 	resultstring += template[1] + words.buzzb
// 	resultstring += template[2] + words.bug
// 	resultstring += template[3] + words.title
// 	resultstring += template[4] + words.reporter
// 	resultstring += template[5] + words.buzzc
// 	resultstring += template[6] + words.close
// 	return resultstring
//     }
//     return interpolate(choices, template);
// }

// console.log(assemble());

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
    result = document.getElementById("letter");
    result.textContent = interpolate(replacements, template);
    // result.innerHTML = interpolate(replacements, template);
}

window.onload = loading;
