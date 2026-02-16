from Hello import *

test_passed = True

ftl = ['Hello', 'World!']
if ft_list != ftl:
    test_passed == False
    print(f"ft_list test failed :\nEspected result : {ftl}\nObtained result : {ft_list}")

ftt = ('Hello', 'France!')
if ft_tuple != ftt:
    test_passed == False
    print(f"ft_tuple test failed :\nEspected result : {ftt}\nObtained result : {ft_tuple}")

fts = {'Hello', 'Paris!'}
fts2 = {'Paris', 'Hello'}
if ft_set != fts and ft_set != fts2:
    test_passed == False
    print(f"ft_set test failed :\nEspected result : {fts} or {fts2}\nObtained result : {ft_set}")

ftd = {'Hello': '42Paris!'}
if ft_dict != ftd:
    test_passed == False
    print(f"ft_dict test failed :\nEspected result : {ftd}\nObtained result : {ft_dict}")

if test_passed == True:
    print("TEST PASSED")
else:
    print("TEST FAILED")
