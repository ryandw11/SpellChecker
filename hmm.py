import json

letterDict = {
    "a": {
        "start": 0,
        "total": 0
    },
    "b": {
        "start": 0,
        "total": 0
    },
    "c": {
        "start": 0,
        "total": 0
    },
    "d": {
        "start": 0,
        "total": 0
    },
    "e": {
        "start": 0,
        "total": 0
    },
    "f": {
        "start": 0,
        "total": 0
    },
    "g": {
        "start": 0,
        "total": 0
    },
    "h": {
        "start": 0,
        "total": 0
    },
    "i": {
        "start": 0,
        "total": 0
    },
    "j": {
        "start": 0,
        "total": 0
    },
    "k": {
        "start": 0,
        "total": 0
    },
    "l": {
        "start": 0,
        "total": 0
    },
    "m": {
        "start": 0,
        "total": 0
    },
    "n": {
        "start": 0,
        "total": 0
    },
    "o": {
        "start": 0,
        "total": 0
    },
    "p": {
        "start": 0,
        "total": 0
    },
    "q": {
        "start": 0,
        "total": 0
    },
    "r": {
        "start": 0,
        "total": 0
    },
    "s": {
        "start": 0,
        "total": 0
    },
    "t": {
        "start": 0,
        "total": 0
    },
    "u": {
        "start": 0,
        "total": 0
    },
    "v": {
        "start": 0,
        "total": 0
    },
    "w": {
        "start": 0,
        "total": 0
    },
    "x": {
        "start": 0,
        "total": 0
    },
    "y": {
        "start": 0,
        "total": 0
    },
    "z": {
        "start": 0,
        "total": 0
    },
    "total": 0
}

letterProb = {
    "a": ["q", "w", "s", "x", "z"],
    "b": ["v", "f","g","h","n"],
    "c": ["x","d","f","v"],
    "e": ["w","s", "d","f","r"],
    "f": ["e","d","c","v","g","t","r"],
    "g": ["f", "v", "b", "h", "y", "t"],
    "h": ["t", "g", "b", "n", "j", "u", "y"],
    "i": ["u", "j", "k", "l", "o"],
    "j": ["h", "n", "m", "k", "i", "u"],
    "k": ["i", "u", "j", "m", "l", "o"],
    "l": ["i", "k", "p", "o"],
    "m": ["n", "j", "k", "l"],
    "n": ["b", "h", "j", "m"],
    "o": ["i", "k", "l", "p"],
    "p": ["o", "l"],
    "q": ["w", "s", "a"],
    "r": ["e", "d", "f", "t"],
    "s": ["q", "w", "e", "d", "x", "z", "a"],
    "t": ["r", "f", "g", "h", "y"],
    "u": ["y", "h", "j", "k", "i"],
    "v": ["c", "f", "g", "b"],
    "w": ["q", "a", "s", "d", "e"],
    "x": ["z", "s", "d", "c"],
    "y": ["t", "g", "h", "j", "u"],
    "z": ["a", "s", "x"]
}

jsonWords = {}

def getProbForLetter(currentL, nextL):
    if nextL not in letterDict.get(currentL):
        letterDict.get(currentL)["nextL"] = 0
    return letterDict.get(currentL)[nextL]

def getMaxProbForLetter(l1, l2):
    return getProbForLetter(l1, l2) / letterDict.get(l1).get("total")


def setProbForLetter(currentL, nextL):
    if currentL not in letterDict:
        return
    if nextL not in letterDict:
        return
    if nextL in letterDict.get(currentL):
        letterDict.get(currentL)[nextL] = getProbForLetter(currentL, nextL) + 1;
    else:
        letterDict.get(currentL)[nextL] = 1
    letterDict["total"] = letterDict["total"] + 1
    letterDict[currentL]["total"] = letterDict[currentL]["total"] + 1

def ifJsonExists(word):
    try:
        if word in jsonWords:
            return True
    except:
        return False

def train(msg):
    i = 0
    temps = ""
    for c in msg:
        if i == 0:
            print("start fire")
            setProbForLetter(c.lower(), "start")
            temps += c
        if c == " ":
            setProbForLetter(msg[i + 1].lower(), "start")
            if ifJsonExists(temps):
                jsonWords[temps] += 1
            else:
                jsonWords[temps] = 1
            temps = ""
        else:
            try:
                setProbForLetter(c.lower(), msg[i+1].lower())
                if c.lower() in letterDict:
                    temps += c.lower()
            except:
                i += 1
                continue
        i += 1
    print(json.dumps(jsonWords))


train("The United States of America (USA), commonly known as the United States (U.S. or US) or America, is a country comprising 50 states, a federal district, five major self-governing territories, and various possessions.[h] At 3.8 million square miles (9.8 million km2), the United States is the world's third or fourth largest country by total area[d] and is slightly smaller than the entire continent of Europe's 3.9 million square miles (10.1 million km2). With a population of more than 327 million people, the U.S. is the third most populous country. The capital is Washington, D.C., and the most populous city is New York City. Forty-eight states and the capital's federal district are contiguous in North America between Canada and Mexico. The State of Alaska is in the northwest corner of North America, bordered by Canada to the east and across the Bering Strait from Russia to the west. The State of Hawaii is an archipelago in the mid-Pacific Ocean. The U.S. territories are scattered about the Pacific Ocean and the Caribbean Sea, stretching across nine official time zones. The extremely diverse geography, climate, and wildlife of the United States make it one of the world's 17 megadiverse countries.[20] Paleo-Indians migrated from Siberia to the North American mainland at least 12,000 years ago.[21] European colonization began in the 16th century. The United States emerged from the thirteen British colonies established along the East Coast. Following the French and Indian War, numerous disputes between Great Britain and the colonies led to the American Revolution, which began in 1775, and the subsequent Declaration of Independence in 1776. The war ended in 1783 with the United States becoming the first country to gain independence from a European power.[22] The current constitution was adopted in 1788, with the first ten amendments, collectively named the Bill of Rights, being ratified in 1791 to guarantee many fundamental civil liberties. The United States embarked on a vigorous expansion across North America throughout the 19th century, acquiring new territories,[23] displacing Native American tribes, and gradually admitting new states until it spanned the continent by 1848.[23] During the second half of the 19th century, the Civil War led to the abolition of slavery.[24][25] By the end of the century, the United States had extended into the Pacific Ocean,[26] and its economy, driven in large part by the Industrial Revolution, began to soar.[27] The Spanish–American War and World War I confirmed the country's status as a global military power. The United States emerged from World War II as a global superpower, the first country to develop nuclear weapons, the only country to use them in warfare, and a permanent member of the United Nations Security Council. Sweeping civil rights legislation, notably the Civil Rights Act of 1964, the Voting Rights Act of 1965 and the Fair Housing Act of 1968, outlawed discrimination based on race or color. During the Cold War, the United States and the Soviet Union competed in the Space Race, culminating with the 1969 U.S. Moon landing. The end of the Cold War and the collapse of the Soviet Union in 1991 left the United States as the world's sole superpower.[28] A multicultural country, the United States is the world's oldest surviving federation. It is a federal republic and a representative democracy. The United States is a founding member of the United Nations, World Bank, International Monetary Fund, Organization of American States (OAS), and other international organizations. The United States is a highly developed country, with the world's largest economy by nominal GDP and second-largest economy by PPP, accounting for approximately a quarter of global GDP.[29] The U.S. economy is largely post-industrial, characterized by the dominance of services and knowledge-based activities, although the manufacturing sector remains the second-largest in the world.[30] The United States is the world's largest importer and the second largest exporter of goods, by value.[31][32] Although its population is only 4.3% of the world total,[33] the U.S. holds 31% of the total wealth in the world, the largest share of global wealth concentrated in a single country.[34] Despite income and wealth disparities, the United States continues to rank very high in measures of socioeconomic performance, including average wage, human development, per capita GDP, and worker productivity.[35][36] The United States is the foremost military power in the world, making up a third of global military spending,[37] and is a leading political, cultural, and scientific force internationally.[38] The Americas are believed to be named for the Italian explorer Amerigo Vespucci.[39] In 1507, the German cartographer Martin Waldseemüller produced a world map on which he named the lands of the Western Hemisphere America in honor of the Italian explorer and cartographer Amerigo Vespucci (Latin: Americus Vespucius).[40] The first documentary evidence of the phrase United States of America is from a letter dated January 2, 1776, written by Stephen Moylan, Esq., to George Washington's aide-de-camp and Muster-Master General of the Continental Army, Lt. Col. Joseph Reed. Moylan expressed his wish to go with full and ample powers from the United States of America to Spain to seek assistance in the revolutionary war effort.[41][42][43] The first known publication of the phrase United States of America was in an anonymous essay in The Virginia Gazette newspaper in Williamsburg, Virginia, on April 6, 1776.[44] The second draft of the Articles of Confederation, prepared by John Dickinson and completed by June 17, 1776, at the latest, declared The name of this Confederation shall be the 'United States of America'.[45] The final version of the Articles sent to the states for ratification in late 1777 contains the sentence The Stile of this Confederacy shall be 'The United States of America'.[46] In June 1776, Thomas Jefferson wrote the phrase UNITED STATES OF AMERICA in all capitalized letters in the headline of his original Rough draught of the Declaration of Independence.[45] This draft of the document did not surface until June 21, 1776, and it is unclear whether it was written before or after Dickinson used the term in his June 17 draft of the Articles of Confederation.[45] The short form United States is also standard. Other common forms are the U.S., the USA, and America. Colloquial names are the U.S. of A. and, internationally, the States. Columbia, a name popular in poetry and songs of the late 18th century, derives its origin from Christopher Columbus; it appears in the name District of Columbia, many landmarks and institutions in the Western Hemisphere bear his name, including the country of Colombia.[47] The phrase United States was originally plural, a description of a collection of independent states—e.g., the United States are—including in the Thirteenth Amendment to the United States Constitution, ratified in 1865.[48] The singular form—e.g., the United States is—became popular after the end of the American Civil War. The singular form is now standard; the plural form is retained in the idiom these United States. The difference is more significant than usage; it is a difference between a collection of states and a unit.[49] A citizen of the United States is an American. United States, American and U.S. refer to the country adjectivally (American values, U.S. forces). In English, the word American rarely refers to topics or subjects not directly connected with the United States.[50] History Main articles: History of the United States, Timeline of United States history, American business history, Economic history of the United States, and Labor history of the United States Indigenous peoples and pre-Columbian history Further information: Native Americans in the United States")
while True:
    a = input("Input a phrase")
    prob = []
    i = 0
    corrections = 0
    for c in a:
        try:
            prob.append(getMaxProbForLetter(c, a[i + 1]))
        except:
            break
        if getMaxProbForLetter(c, a[i + 1]) < 0.07:
            print("Possible spelling error with: " + c + " and " + a[i + 1])
            l = a[i + 1]
            for lp in letterProb.get(l):
                cp = a.replace(l, lp)
                try:
                    if getMaxProbForLetter(c, lp) >= 0.05:
                        print("Possible fix found: Did you mean " + cp + "?")
                        corrections += 1
                except:
                    continue
        i += 1

# prob = []
# i = 0
# for c in a:
#     try:
#         prob.append(getMaxProbForLetter(c, a[i + 1]))
#     except:
#         break
#     i+=1
#
#
# out = 0.0
# i=0
# for p in prob:
#     if i == 0: out = p
#     out *= p
#
# print(str(out))
#
# if(out > 0.00001): print("it is a word!")
# else: print("it is not a word!")