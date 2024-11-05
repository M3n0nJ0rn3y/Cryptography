def test():
    i[0] += 1
    index = i[0]
    print(global_list[index])


i = [-1]
global_list = ['TRUMP!','TRUMP!!','TRUMP!!!','TRUMP!!!!','TRUMP!!!!!']

test()
test()
test()