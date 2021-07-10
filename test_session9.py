from _pytest.monkeypatch import V
import pytest
import re
from session9 import *
import inspect
import session9
import os
import test_session9

nameddata=generate_10000_profiles()[0]
README_CONTENT_CHECK_FOR = ['Session','9','Generate','10000','blood','age','average','dictionary','namedtuple','company','stock','100','open','high','close']

def test_readme_exists():
    assert os.path.isfile(
        "README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md",
                  "r", encoding="utf8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            print(c)
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10




def test_function_repeatations():
    functions = inspect.getmembers(test_session9, inspect.isfunction)
    names = []
    for function in functions:
        names.append(function)
    assert len(names) == len(set(names)), 'Test cases seems to be repeating...'


def test_function_doc_string():
    """
    Test case to check whether the functions have docstrings or not.
    """
    functions = inspect.getmembers(session9, inspect.isfunction)
    for function in functions:
            assert function[1].__doc__

def test_namedtuple_type():
    assert type(nameddata.__repr__()),"Return type is not a namedtuple!"

def test_namedtuple_generator_values():
    assert type(nameddata.highest_age)==int and nameddata.highest_age>nameddata.avg_age,"There is something wrong with the highest age"
    assert type(nameddata.avg_age)==float and nameddata.avg_age,"The average is not correct!"
    assert type(nameddata.location_mean) and nameddata.location_mean,"Something is wrong with the location average"
    assert type(nameddata.most_frequent_blood_type)==str and nameddata.most_frequent_blood_type,"Are you choosing a blood type?"

def test_namedtuple_generator_with_arguments():
    with pytest.raises(TypeError):
        generate_10000_profiles('hmm','lets',doand='and see what happens')

def test_named_tuple_docstring():
    assert len(nameddata.__doc__)>25,"Did you forget to add a docstring?"

def test_named_tuple_length():
    assert len(nameddata)==4,"Are you returning more unrequired stuff?"

returndict=generate_10000_profiles_but_its_dict()[0]

def test_dict_generator_type():
    assert type(returndict)==dict,"Are you sure it's a dictionary?"

def test_dict_generator_values():
    assert type(returndict["highest_age"])==int and returndict["highest_age"]>returndict["avg_age"],"There is something wrong with the highest age"
    assert type(returndict["avg_age"])==float and returndict["avg_age"],"The average is not correct!"
    assert type(returndict["location_mean"]) and returndict["location_mean"],"Something is wrong with the location average"
    assert type(returndict["most_frequent_blood_type"])==str and returndict["most_frequent_blood_type"],"Are you choosing a blood type?"

def test_dict_generator_with_arguments():
    with pytest.raises(TypeError):
        generate_10000_profiles_but_its_dict("hmm","lets","see",ifthe="program",can="handle",this="")

def test_dict_generator_length():
    assert len(returndict)==4,"Are you returning some extra values?"

def test_namedtuple_faster_than_dict():
    named,nametime=generate_10000_profiles()
    dic,dictime=generate_10000_profiles_but_its_dict()
    assert dictime>nametime,"Named Tuples are supposed to be faster than dictionaries"
fakestock=create_100_companies()
def test_stock_generator_for_empty_values():
    passed=True
    for stock in fakestock:
        if not stock:
            passed=False
    assert passed==True,"There are empty values in the returned list!"
def test_stock_length():
    assert len(fakestock)==100,"100 Companies are not being returned!"

def test_stock_open_validity():
    assert type(random.choice(fakestock).open)==float and random.choice(fakestock).open,"Is open existing?!"

def test_stock_close_validity():
    assert type(random.choice(fakestock).close)==float and random.choice(fakestock).close,"Is close existing?!"

def test_stock_high_validity():
    choice=random.choice(fakestock)
    assert type(choice.high)==float and choice.high>choice.open,"Is high valid?!"

def test_stock_low_validity():
    choice=random.choice(fakestock)
    assert type(choice.open)==float and choice.open<choice.high,"Is low valid?!"

def test_stock_symbol_validity():
    passed=True
    for stock in fakestock:
        if len(stock.symbol)!=3:
            passed=False
    assert passed==True,"Symbols are not three characters long!"

def test_stock_company_name():
    assert random.choice(fakestock).name,"Company name is null?"

notallowedstring='[@_!#$%^&*()<>?/\|}{~:] -'
def test_stock_symbol_characters():
    passed=True
    for stock in fakestock:
        if any(c in notallowedstring for c in stock.symbol):
            passed=False
    assert passed==True,"Symbols contain special characters!"

def test_stock_return_docstring():
    assert len(fakestock)>25,"Why is there no docstring for the fake stock named tuple?"


