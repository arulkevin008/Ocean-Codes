#Maximum element
def maximum_element():
    List=[56,34,56,78,34]
    max_element=List[0]
    for i in List:
        if(i>max_element):
            max_element=i
    print(max_element)
maximum_element()
