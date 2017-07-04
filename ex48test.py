from nose.tools import *
from ex48 import lexion


def test_directions():
    assert_equal(lexicon.csan("north"),[('direction', 'north')])
    result = lexicon.scan("north south east")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south')
                          ('direction', 'east')])
                
def test_verbs():
    assert_equal(lexicon.csan("go"), [('verb', 'go')]
    result = lexicon.scan("go kill eat")
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'kill'),
                          ('verb', 'eat')])
                          
                          
def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the in of")
    assert_equal(result, [('stop', 'the'),
                          ('stop', 'in'),
                          ('stop', 'of')])
                    

def test_nouns():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the in of")
    accert_equal(result, [('stop', 'the'),
                         ('stop', 'in'),
                         ('stop', 'of')])
                         
                                         
def test_numbers():
    assert_equal(lexicon.scan("1234"), [('number', 1234])
    result = lexicon.scan("3 91234")
    accert_equal(result, [('number', 3),
                          ('number', 91234)])
 
 
 
def test_errors():
    assert_equal(lexicon.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
    result = lexicon.scan("bear IAS princess")
    accert_equal(result, [('noun', 'bera'),
                          ('error', 'IAS'),
                          ('noun', 'princess')])                         
'''
def test_
    assert_equal(lexicon.scan(), [()])
    result = lexicon.scan()
    accert_equal(result, [(),
                         (),
                         ()])
'''