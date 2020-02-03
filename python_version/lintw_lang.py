"""
English to Lintwian converter

To use as a standalone script, uncomment the code lines
at the end of the script and run in a Python 3.6 environment.
"""
import re
import csv

DB_MAX_SIZE = 128

db = ("あいうえおかがきぎくぐけげこごさざしじすずせぜそ"
      + "ぞただちぢつづてでとどなにぬねのはばぱひびぴふぶ"
      + "ぷへべぺほぼぽまみむめもやゆよらりるれろわをんぁ")


class LintwCharacter(object):
    """
    A class for Lintwian character instances
    """

    def __init__(self, char, head, body, tail, latin):

        self.char = char
        self.is_head = head
        self.is_body = body
        self.is_tail = tail
        self.latin = latin


"""
A database for the Lintwese characters.
One Lintwese character corresponds
to one of the Japanese hieroglyphs
"""
lintwchars = {'あ': LintwCharacter('あ', 1, 1, 1, 'al'),
              'い': LintwCharacter('い', 1, 0, 0, 'iŵ'),
              'う': LintwCharacter('う', 1, 0, 0, 'uŵ'),
              'え': LintwCharacter('え', 1, 1, 1, 'el'),
              'お': LintwCharacter('お', 1, 1, 1, 'o:'),
              'か': LintwCharacter('か', 0, 1, 1, 'qua'),
              'が': LintwCharacter('が', 0, 1, 1, 'gaŵ'),
              'き': LintwCharacter('き', 1, 1, 1, 'ki:'),
              'ぎ': LintwCharacter('ぎ', 1, 1, 1, 'gil'),
              'く': LintwCharacter('く', 1, 1, 1, 'kul'),
              'ぐ': LintwCharacter('ぐ', 0, 1, 1, 'gue'),
              'け': LintwCharacter('け', 1, 0, 0, 'kel'),
              'げ': LintwCharacter('げ', 0, 0, 1, 'gen'),
              'こ': LintwCharacter('こ', 1, 1, 0, 'kon'),
              'ご': LintwCharacter('ご', 1, 1, 0, 'goŵ'),
              'さ': LintwCharacter('さ', 1, 1, 0, 'san'),
              'ざ': LintwCharacter('ざ', 0, 1, 1, 'za:'),
              'し': LintwCharacter('し', 0, 1, 1, 'ŝio'),
              'じ': LintwCharacter('じ', 1, 1, 1, 'ĵos'),
              'す': LintwCharacter('す', 1, 1, 1, 'sta'),
              'ず': LintwCharacter('ず', 0, 1, 0, 'zwao'),
              'せ': LintwCharacter('せ', 1, 1, 1, 'sel'),
              'ぜ': LintwCharacter('ぜ', 1, 1, 0, 'zei'),
              'そ': LintwCharacter('そ', 1, 1, 1, 'so:'),
              'ぞ': LintwCharacter('ぞ', 0, 0, 1, 'zoi'),
              'た': LintwCharacter('た', 1, 1, 1, 'ta:'),
              'だ': LintwCharacter('だ', 1, 1, 1, 'da:'),
              'ち': LintwCharacter('ち', 0, 1, 1, 'ĉil'),
              'ぢ': LintwCharacter('ぢ', 0, 1, 1, 'diŵ'),
              'つ': LintwCharacter('つ', 1, 1, 1, 'cua'),
              'づ': LintwCharacter('づ', 0, 1, 1, 'dia'),
              'て': LintwCharacter('て', 1, 1, 1, 'ten'),
              'で': LintwCharacter('で', 1, 1, 1, 'den'),
              'と': LintwCharacter('と', 0, 0, 1, 'tŵ'),
              'ど': LintwCharacter('ど', 0, 1, 1, 'din'),
              'な': LintwCharacter('な', 1, 1, 0, 'na:'),
              'に': LintwCharacter('に', 0, 0, 1, 'nia'),
              'ぬ': LintwCharacter('ぬ', 0, 1, 1, 'nus'),
              'ね': LintwCharacter('ね', 1, 1, 0, 'ne:'),
              'の': LintwCharacter('の', 0, 0, 1, 'noa'),
              'は': LintwCharacter('は', 1, 0, 0, 'hal'),
              'ば': LintwCharacter('ば', 1, 1, 1, 'bal'),
              'ぱ': LintwCharacter('ぱ', 1, 1, 1, 'pan'),
              'ひ': LintwCharacter('ひ', 1, 1, 0, 'hyea'),
              'び': LintwCharacter('び', 1, 1, 1, 'viŵ'),
              'ぴ': LintwCharacter('ぴ', 1, 1, 0, 'pi:'),
              'ふ': LintwCharacter('ふ', 1, 1, 1, 'fiŵ'),
              'ぶ': LintwCharacter('ぶ', 1, 1, 0, 'vyu'),
              'ぷ': LintwCharacter('ぷ', 0, 0, 1, 'pia'),
              'へ': LintwCharacter('へ', 1, 0, 0, 'hel'),
              'べ': LintwCharacter('べ', 1, 1, 1, 'bel'),
              'ぺ': LintwCharacter('ぺ', 0, 1, 1, 'pen'),
              'ほ': LintwCharacter('ほ', 1, 1, 1, 'hoi'),
              'ぼ': LintwCharacter('ぼ', 1, 1, 1, 'boŵ'),
              'ぽ': LintwCharacter('ぽ', 1, 1, 1, 'pon'),
              'ま': LintwCharacter('ま', 1, 1, 1, 'ma:'),
              'み': LintwCharacter('み', 1, 1, 1, 'mieŵ'),
              'む': LintwCharacter('む', 0, 1, 1, 'mui'),
              'め': LintwCharacter('め', 1, 1, 1, 'mel'),
              'も': LintwCharacter('も', 1, 1, 1, 'mol'),
              'や': LintwCharacter('や', 1, 1, 0, 'jav'),
              'ゆ': LintwCharacter('ゆ', 1, 1, 0, 'jui'),
              'よ': LintwCharacter('よ', 1, 1, 0, 'jol'),
              'ら': LintwCharacter('ら', 1, 1, 1, 'ran'),
              'り': LintwCharacter('り', 1, 1, 1, 'lin'),
              'る': LintwCharacter('る', 0, 1, 1, 'lua'),
              'れ': LintwCharacter('れ', 1, 1, 0, 'rei'),
              'ろ': LintwCharacter('ろ', 0, 0, 1, 'log'),
              'わ': LintwCharacter('わ', 1, 1, 1, 'waŵ'),
              'を': LintwCharacter('を', 1, 1, 1, 'wol'),
              'ん': LintwCharacter('ん', 1, 1, 1, 'nes'),
              'ぁ': LintwCharacter('ぁ', 1, 1, 1, 'coa'),
              '0': LintwCharacter('0', None, None, None, 'mu:'),
              '1': LintwCharacter('1', None, None, None, 'lil'),
              '2': LintwCharacter('2', None, None, None, 'nin'),
              '3': LintwCharacter('3', None, None, None, 'fei'),
              '4': LintwCharacter('4', None, None, None, 'ĉetŵ'),
              '5': LintwCharacter('5', None, None, None, 'olc'),
              '6': LintwCharacter('6', None, None, None, 'kia'),
              '7': LintwCharacter('7', None, None, None, 'sra')}

'''
Original dictionaries by nkymtky, left here for reference
'''
'''
rule_db = {"あ" : [1,1,1], "い" : [1,0,0], "う" : [1,0,0], "え" : [1,1,1], "お" : [1,1,1],
           "か" : [0,1,1], "が" : [0,1,1], "き" : [1,1,1], "ぎ" : [1,1,1], "く" : [1,1,1],
           "ぐ" : [0,1,1], "け" : [1,0,0], "げ" : [0,0,1], "こ" : [1,1,0], "ご" : [1,1,0],
           "さ" : [1,1,0], "ざ" : [0,1,1], "し" : [0,1,1], "じ" : [1,1,1], "す" : [1,1,1],
           "ず" : [0,1,0], "せ" : [1,1,1], "ぜ" : [1,1,0], "そ" : [1,1,1], "ぞ" : [0,0,1],
           "た" : [1,1,1], "だ" : [1,1,1], "ち" : [0,1,1], "ぢ" : [0,1,1], "つ" : [1,1,1],
           "づ" : [0,1,1], "て" : [1,1,1], "で" : [1,1,1], "と" : [0,0,1], "ど" : [0,1,1],
           "な" : [1,1,0], "に" : [0,0,1], "ぬ" : [0,1,1], "ね" : [1,1,0], "の" : [0,0,1],
           "は" : [1,0,0], "ば" : [1,1,1], "ぱ" : [1,1,1], "ひ" : [1,1,0], "び" : [1,1,1],
           "ぴ" : [1,1,0], "ふ" : [1,1,1], "ぶ" : [1,1,0], "ぷ" : [0,0,1], "へ" : [1,0,0],
           "べ" : [1,1,1], "ぺ" : [0,1,1], "ほ" : [1,1,1], "ぼ" : [1,1,1], "ぽ" : [1,1,1],
           "ま" : [1,1,1], "み" : [1,1,1], "む" : [0,1,1], "め" : [1,1,1], "も" : [1,1,1],
           "や" : [1,1,0], "ゆ" : [1,1,0], "よ" : [1,1,0],
           "ら" : [1,1,1], "り" : [1,1,1], "る" : [0,1,1], "れ" : [1,1,0], "ろ" : [0,0,1],
           "わ" : [1,1,1], "を" : [1,1,1], "ん" : [1,1,1],
           "ぁ" : [1,1,1], # lai rut ton fua vilon sto ad fja kai nish dron
}

latin_db = {"あ" : "al"  , "い" : "iŵ"  , "う" : "uŵ"  , "え" : "el"  , "お" : "o:"  ,
            "か" : "qua" , "が" : "gaŵ" , "き" : "ki:" , "ぎ" : "gil" , "く" : "kul" ,
            "ぐ" : "gue" , "け" : "kel" , "げ" : "gen" , "こ" : "kon" , "ご" : "goŵ" ,
            "さ" : "san" , "ざ" : "za:" , "し" : "ŝio" , "じ" : "ĵos" , "す" : "sta" ,
            "ず" : "zwao", "せ" : "sel" , "ぜ" : "zei" , "そ" : "so:" , "ぞ" : "zoi" ,
            "た" : "ta:" , "だ" : "da:" , "ち" : "ĉil" , "ぢ" : "diŵ" , "つ" : "cua" ,
            "づ" : "dia" , "て" : "ten" , "で" : "den" , "と" : "tŵ"  , "ど" : "din" ,
            "な" : "na:" , "に" : "nia" , "ぬ" : "nus" , "ね" : "ne:" , "の" : "noa" ,
            "は" : "hal" , "ば" : "bal" , "ぱ" : "pan" , "ひ" : "hyea", "び" : "viŵ" ,
            "ぴ" : "pi:" , "ふ" : "fiŵ" , "ぶ" : "vyu" , "ぷ" : "pia" , "へ" : "hel" ,
            "べ" : "bel" , "ぺ" : "pen", "ほ" : "hoi" , "ぼ" : "boŵ" , "ぽ" : "pon" ,
            "ま" : "ma:" , "み" : "mieŵ", "む" : "mui" , "め" : "mel" , "も" : "mol" ,
            "や" : "jav" , "ゆ" : "jui" , "よ" : "jol" ,
            "ら" : "ran" , "り" : "lin" , "る" : "lua" , "れ" : "rei" , "ろ" : "log",
            "わ" : "waŵ" , "を" : "wol" , "ん" : "nes" ,
            "ぁ" : "coa" ,
            "0" : "mu:"  , "1" : "lil" , "2" : "nin" , "3" : "fei",
            "4" : "ĉetŵ" , "5" : "olc" , "6" : "kia" , "7" : "sra",
}
'''

VAL_MAX = 9999943
VAL_DIV = 5035651


def loop(v, mini, maxi):
    """
    If v is not in the [mini, maxi] range,
    it is looped back so that it's in the range and returned.
    It is better shown what happens in this function on this graph:
    https://www.desmos.com/calculator/ipfckj63ou
    """
    v -= mini
    r = maxi - mini
    v = v % r
    return v + mini


def hashc(c, i):
    """
    Returns a hash for a character based on its Unicode code
    and the hash of a previous character
    """
    i = abs(i)
    i += 1
    # val = ((i + c*187) * (i - c + 3443443))
    val = (abs(i - c * 443) * (i * 223 + c)) % VAL_DIV

    return val


def init(string):
    """
    Returns a hash for a string using the hashc() function
    """
    val = 0
    for c in string:
        c = ord(c)
        val = hashc(c, val)

    return val


def getchar(index, head, body, tail):
    """
    Returns a Lintwese character from the lintwchars dictionary
    based on the given index, the position in the
    original English word and whether the chosen
    Lintwese character corresponds to the
    required position in the word.
    """
    while True:

        index = loop(index, 0, DB_MAX_SIZE)

        if index < len(db):
            lintw_char = db[index]
        else:
            index += int(DB_MAX_SIZE / 2)
            continue

        if ((head and lintwchars[lintw_char].is_head == 0) or
                (body and lintwchars[lintw_char].is_body == 0) or
                (tail and lintwchars[lintw_char].is_tail == 0)):
            index += 1
            continue
        else:
            return lintw_char


def tolatin(lintwese):
    """
    Returns a string containing the pronunciation
    of a Lintwese word
    """
    latin = ""
    for c in lintwese:
        lat = lintwchars[c].latin
        if lat is not None:
            latin += lat
    return latin


def convertword(seed):
    """
    Converts an English word to Lintwese.
    Returns a dictionary that contains the original
    English word, the Lintwian translation and the
    pronunciation

    If the input string contains a number instead of
    an English word, it is converted to octal.

    If the English word is in the lintw_dictionary,
    the corresponding pre-existing translation
    is chosen from it instead.
    """
    seed = seed.lower().strip()

    ret = {"seed": seed, "lintwese": "", "latin": ""}

    if re.search("^[0-9]+$", seed) is not None:

        ret["lintwese"] = oct(int(seed)).lstrip("0o")
        if len(ret["lintwese"]) % 2 != 0:
            ret["lintwese"] = "0" + ret["lintwese"]

    elif re.search("^['/a-z]+$", seed) is not None:

        dictword = None

        with open('lintwDict.csv', newline='') as csvdict:
            dictionary_reader = csv.DictReader(csvdict, fieldnames=["latin", "lintwese", "lexical_category"])
            for row in dictionary_reader:
                if row["latin"] == seed:
                    dictword = row["lintwese"]
                    break

        if dictword is not None:
            ret["lintwese"] = dictword
        else:
            head = True
            body = False
            tail = (len(seed) == 1)

            val = loop(init(seed), 0, VAL_DIV)

            ret["lintwese"] = getchar(val % DB_MAX_SIZE, head, body, tail)

            i = 0
            for c in seed:

                if i == len(seed) - 1:
                    body = False
                    tail = True
                else:
                    body = True
                    tail = False

                val += hashc(ord(c), i)

                if val >= VAL_MAX:
                    val = loop(val, 0, VAL_DIV)
                    ret["lintwese"] += getchar(val % DB_MAX_SIZE, head, body, tail)

                head = False
                i += 1
    else:
        ret["lintwese"] = seed

    ret["latin"] = tolatin(ret["lintwese"])

    return ret


def convertsentence(seed_sentence):
    """
    Returns a dictionary containing the convertword()
    returns, hyphens and whitespaces.
    Hyphens are omitted in Lintwese
    because they don't exist in that language.
    Whitespaces are replaced with a special Lintwese
    character represented by Japanese '点'
    """
    ret = []
    seeds = re.split("\s*[- ]\s*", seed_sentence)
    # print(seeds)
    splitchars = re.findall("\s*[- ]\s*", seed_sentence)
    # print(splitChars)
    splitchars.append(" ")

    i = 0
    for seed in seeds:

        if not seed:
            i += 1
            continue

        splitchar = splitchars[i][0]
        word = convertword(seed)
        ret.append(word)

        if splitchar == "-":
            ret.append({"seed": splitchar, "lintwese": "", "latin": "-"})
        else:
            ret.append({"seed": splitchar, "lintwese": "点", "latin": " "})

        i += 1

    if ret:
        ret.pop()

    return ret


def converttext(seedtext):
    """
    Returns a dictionary containing the convertsentence()
    returns and punctuation marks (!.).
    In Lintwese (!)'s are represented by leading and trailing
    symbols represented by (!)'s, similarly to Spanish.
    """
    ret = []
    seedtext = re.sub("\r\n", " ", seedtext)
    seedtext = re.sub("\n", " ", seedtext)
    seedtext = re.sub("[^\w!.\-/ ]+|_+", "", seedtext)
    seedsentences = re.split("\s*[!.]\s*", seedtext) or []
    splitchars = re.findall("[!.]", seedtext) or []
    splitchars.append(".")

    i = 0
    for seedsentence in seedsentences:

        if not seedsentence:
            i += 1
            continue

        splitchar = splitchars[i][0]

        words = convertsentence(seedsentence)

        if splitchar == "!":
            ret.append({"seed": "", "lintwese": "！", "latin": " "})
        else:
            ret.append({"seed": "", "lintwese": "点", "latin": " "})

        for word in words:
            ret.append(word)

        if splitchar == "!":
            ret.append({"seed": "!", "lintwese": "！", "latin": "!"})
        else:
            ret.append({"seed": ". ", "lintwese": "点", "latin": ". "})

        # Legacy code, left in case of necessity
        # ret.pop()
        # if len(seedSentences) > 1:
        #    ret.append({"seed" : ".", "lintwese" : "点", "latin" : ". "})
        i += 1

    return ret

# Uncomment these for in-console use
# print(convertword(str(input('Type in a word: '))))
# print(converttext(str(input('Type in text:'))))
# print('db: ' + str(len(db)))
# print('rule_db: ' + str(len(rule_db.keys())))
# print('latin_db: ' + str(len(latin_db.keys())))
# print('dict: ' + str(len(lintw_dictionary.keys())))
