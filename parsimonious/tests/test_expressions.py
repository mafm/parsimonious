from nose.tools import eq_

from parsimonious.expressions import Regex, Sequence, OneOf


def test_regex():
    eq_(Regex('hello')._match('ehello', 1), 5)  # simple
    eq_(Regex('hello*')._match('hellooo'), 7)  # *
    eq_(Regex('hello*')._match('goodbye'), None)  # no match

def test_sequence():
    eq_(Sequence(Regex('hi*'), Regex('lo'), Regex('.ingo'))._match('hiiiilobingo1234'),
        12)  # succeed
    eq_(Sequence(Regex('hi*'), Regex('lo'), Regex('.ingo'))._match('hiiiilobing'),
        None)  # don't
    eq_(Sequence(Regex('hi*'))._match('>hiiii', 1),
        5)  # non-0 pos

def test_one_of():
    eq_(OneOf(Regex('aaa'), Regex('bb'))._match('aaa'), 3)  # first alternative
    eq_(OneOf(Regex('aaa'), Regex('bb'))._match('bbaaa'), 2)  # second
    eq_(OneOf(Regex('aaa'), Regex('bb'))._match('aa'), None)  # no match
