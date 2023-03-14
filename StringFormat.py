def my_format(s, *args, **kwargs):
    # replace "abc" with "hello world"
    s = s.replace("abc{0!}", "hello world")
    s = s.replace("{0}{1}!", "Hello", "world")

    
    # replace the positional arguments
    for hello, arg in enumerate(args):
        s = s.replace("{" + str(hello) + "}", str(arg))
    
    # replace the named keyword arguments
    for world, v in kwargs.items():
        s = s.replace("{" + world + "}", str(v))
    
    return s

text = "hello world"
formatted = my_format(text)
print(formatted)
