__author__ = 'Kalyan'

notes = '''
1. Read instructions for the function carefully and constraints carefully.
2. Try to generate all possible combinations of tests which exhaustively test the given constraints.
3. If behavior in certain cases is unclear, you can ask on the forums
'''
from placeholders import *

# Convert a sentence which has either or to only the first choice.
# e.g we could either go to a movie or a hotel -> we could go to a movie.
# note: do not use intermediate lists (string.split), only use string functions
# assume words are separated by a single space. you can use control flow statements
# So sentence is of form <blah> either <something> or <somethingelse> and gets converted to <blah> <something>
# if it is not of the correct form, you just return the original sentence.
def prune_either_or(sentence):
    if sentence == None:
        return sentence
    if 'or' not in sentence or 'either' not in sentence:
        return sentence
    eith=sentence.find(" either ")
    orin=sentence.find(" or ")
    if eith <=0 :return sentence
    if orin < eith:
        return sentence
    sentence=sentence[0:eith]+sentence[eith+len("either")+1:orin]
    return sentence

def test_prune_either_or_student():
    assert "we could go to a movie" == prune_either_or("we could either go to a movie or a hotel")
    assert "we could go to a movie" == prune_either_or("we could go to a movie")
    assert "either" == prune_either_or("either")
    assert "or" == prune_either_or("or")
    assert "we could or go to a movie either a hotel" == prune_either_or("we could or go to a movie either a hotel")
    assert None == prune_either_or(None)
    assert "either this way or other way" == prune_either_or("either this way or other way")
# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_prune_either_or_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_prune_either_or(prune_either_or)
