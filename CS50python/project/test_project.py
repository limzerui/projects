
from project import add_decision
from project import get_more_decisions
from project import get_factors
from project import get_dictionary
from tud_test_base import set_keyboard_input, get_display_output



#def test_get_dictionary():
 #   decision=["hokkien mee","chicken rice"]
  #  factors=["taste","location","smell","lol","lek"]
   # decisions={}
    #assert  get_dictionary(decision, factors, decisions)==




def test_get_more_decisions():
    set_keyboard_input(["y"])
    x=get_more_decisions()
    assert x == "y"

def test_add_decision():
    set_keyboard_input(["Hokkien Mee","n"])
    x=add_decision()
    assert x==["Hokkien Mee"]

def test_get_factors():
    set_keyboard_input(["taste","y","location","n"])
    d=get_factors()
    assert d==["taste","location"]

#def test_get_factors():
  #  ...