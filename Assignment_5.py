from typing import List

def is_EF1(agents:List[Agent], bundles:List[List[int]])->bool:
    for i in range (0,len(agents)):
        for j in range (0,len(agents)):
            if i == j:
                continue
            i_j_EF1 = Check_Ef1(i,j,agents,bundles)
            if i_j_EF1 == False:
                return False
    return True

def Check_Ef1(i:int , j:int , agents:List[Agent], bundles:List[List[int]])->bool:
    #this method checks if there is EF1 between agent i and agent j
    sum_i = 0
    sum_j = 0

    #sum of the values of agent i items
    for k in range(0, len(bundles[i])):
        sum_i+=agents[i].item_value(bundles[i][k])

    # sum of the values of agent j items , with agent i evaluation
    for k in range(0, len(bundles[j])):
        sum_j+=agents[i].item_value(bundles[j][k])

    #if there is 1 item that make the difference between the sums such that agent i items worth more than agent j items
    # minus these one item , then EF1 exist for agent i and agent j
    for k in range (0,len(bundles[j])):
        if sum_i >= sum_j-agents[i].item_value(bundles[j][k]):
            return True
    return False
