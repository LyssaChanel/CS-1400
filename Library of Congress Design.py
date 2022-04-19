"""
Library of Congress
Alyssa Simmonds Smederovac
3/14/2022
"""

"""
1. Sort
"""

book_list = []
bookcode = 0

book_list.sort(key=bookcode)

def bookecode(line):
    return line[1], line[2]

book_dict = {}

for line in book_list:
    book_dict[line[1]]=line[0], line[2]

# A dictionary is similar to an object in JavaScript

"""
Use Try Except:
    Finally:
"""

"""
ALC
A large rose-tree stood near the entrance of the garden: the roses
growing on it were white, but there were three gardeners at it, busily
painting them red. Alice thought this a very curious thing, and she
went nearer to watch them, and just as she came up to them she heard
one of them say, "Look out now, Five! Don’t go splashing paint over me
like that!"
"I couldn’t help it," said Five, in a sulky tone; "Seven jogged my
elbow."
On which Seven looked up and said, "That’s right, Five! Always lay the
blame on others!"
-----
TRI
SQUIRE TRELAWNEY, Dr. Livesey, and the rest of these gentlemen having
asked me to write down the whole particulars about Treasure Island, from
the beginning to the end, keeping nothing back but the bearings of the
island, and that only because there is still treasure not yet lifted, I
take up my pen in the year of grace 17__ and go back to the time when
my father kept the Admiral Benbow inn and the brown old seaman with the
sabre cut first took up his lodging under our roof.
I remember him as if it were yesterday, as he came plodding to the
inn door, his sea-chest following behind him in a hand-barrow--a
tall, strong, heavy, nut-brown man, his tarry pigtail falling over the
-----
WOO
All this time Dorothy and her companions had been walking through the
thick woods. The road was still paved with yellow brick, but these were
much covered by dried branches and dead leaves from the trees, and the
walking was not at all good.
There were few birds in this part of the forest, for birds love the
open country where there is plenty of sunshine. But now and then there
came a deep growl from some wild animal hidden among the trees. These
sounds made the little girl’s heart beat fast, for she did not know
what made them; but Toto knew, and he walked close to Dorothy’s side,
and did not even bark in return.
"""

# RUBRIC

"""
(12 points) The program produces a correct summary for book_data.txt.
(12 points) The program produces the correct text for book_data.txt.
(4 points) The program prints nothing to the terminal when processing book_data.txt.
(12 points) The program produces a correct summary for another input file.
(12 points) The program produces the correct text for another input file.
(4 points) The program prints nothing to the terminal when processing book_data.txt.
(6 points) The module docstring is included and contains the required information.
(6 points) The program contains a main function (that takes no parameters) with conditional execution. There is no global code.
(6 points) The program uses snake case for variable names.
(6 points) The style checker emits no warnings.
"""