def all_thing_is_obj(object: any) -> int:
    if type(object).__name__ == 'int':
        print("Type not found")
    elif object == 'Brian' or object == 'Toto':
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        print(f"{type(object).__name__.title()} : {type(object)}")
    
    return 42