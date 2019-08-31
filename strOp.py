#strOp.py

string1 = "This is a "
string2 = "short string."
sentence = string1 + string2
print("{}".format(sentence))
print("{}{}{}".format("She is", "very"*4, "beautiful"))
m = len(sentence)
print("{}".format(m))
string1 = "My deliveralbe is due in May"
string_list1 = string1.split()
string_list2 = string1.split(" ",2)
print(string1_list1)
print("FIRST PIECE:{0} SECOND PIECE:{1} THIRD PIECE{2}"\
     .format(string1_list2[0], string1_list2[1], string1_list2[2]))
string2 = "Your,deliveralbe,is,due,in,June"
string2_list = string2.split(',')
print(string2_list)
print("{}{}{}{}.".format(string2_list[1], string2_list[2], string2_list[5],\
                      string_list[-1]))