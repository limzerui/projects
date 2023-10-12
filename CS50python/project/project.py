from prettytable import PrettyTable

#class Decision:
 #   def __init__(self, name):
  #      self.name = name

def get_factors():
    factors=[]
    while True:
        factor=input("What factor would you consider?")#only have 5
        factors.append(factor)
        more_decision=get_more_decisions()
        if more_decision=="n":
            break
    return factors

#def get_importance():
 #   while True:
  #      importance=input("How important is that factor from 1-10")
   #     if importance in ["1","2","3","4","5","6","7","8","9","10"]
    #        return factor
     #   print("Invalid input")

def get_more_decisions():
    while True:
        more_decision= input ("Do you want to add more decision? (y/n) ")
        if more_decision in ["y", "n"]:
            return more_decision
        print("Invalid input. Please enter 'y' or 'n'.")


def add_decision():
    decisions=[]
    while True:
        decision=input("What decision would you consider?")
        decisions.append(decision)
        more_decision=get_more_decisions()
        if more_decision=="n":
            break
    return decisions
    #decision1={}
    #decision1.update({"name":name})
    #while True:
    #    factor=get_factor()
    #    importance=int(get_importance())
    #    decision1.update({factor:importance})
    #    more_decision=get_more_decisions
    #    if more_decision=="n":
    #        break
def display_events_table(final, factors, decision):
    table=PrettyTable(["Decision",factors[0],factors[1],factors[2],factors[3],factors[4], "Total"])
    for i in range(len(final)):
        total=final[decision[i]][0]+final[decision[i]][1]+final[decision[i]][2]+final[decision[i]][3]+final[decision[i]][4]
        total=str(total)
        table.add_row([decision[i], final[decision[i]][0],final[decision[i]][1],final[decision[i]][2],final[decision[i]][3],final[decision[i]][4], total])
    print(table)


def get_dictionary(decision,factors,decisions):
    for i in range(len(decision)):
        list=[] #will list be clear after every loop??????????????????????????
        for j in range(len(factors)):
            importance=input(f"How important is {factors[j]} in making {decision[i]} decision? Rate from 1-10:")
            importance=int(importance)
            list.append(importance)
        #if decision[i] not in decisions:
        decisions[decision[i]]=list
        #decisions[decision[i]].extend(list)
    return decisions



def main():
    decisions={}
    #while True:
    decision=add_decision()#returns a list of decisions
    factors=get_factors()#returns a list of factors
    final=get_dictionary(decision,factors,decisions)#final is the final dictionary with key as decision and value as a list of numbers
        #decisions.append(decision_copy)
        #more_decision=get_more_decisions()
        #decision_copy=decision.copy()
        #if more_decision=="n":
        #   break
    display_events_table(final,factors,decision)

#def main():
 #   final={"hokkien mee":[1,2,3,6,7], "chicken rice":[2,3,4,5,8]}
  #  factors=["taste","location","smell","lol","lek"]
   # decision=["hokkien mee","chicken rice"]
   # print("lol")
    #display_events_table(final, factors, decision)

if __name__ == "__main__":
    main()
