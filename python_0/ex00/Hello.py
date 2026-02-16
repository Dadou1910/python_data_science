ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#modify 'tata!' to 'World!' in a list :
ft_list[1] = 'World!'

#modify 'toto!' to 'France!' in a tuple :
ft_tuple = (ft_tuple[0], 'France!')

#modify 'tutu!' to 'Paris!' in a set :
ft_set.remove('tutu!')
ft_set.add('Paris!')

#modify 'titi!' to '42Paris!' in a dict :
ft_dict['Hello'] = '42Paris!'

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)