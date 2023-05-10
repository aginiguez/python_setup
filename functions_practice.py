def hello():
    print("Hello, user.")

hello() 

def pack(arg1, arg2, arg3):
    my_list = [arg1, arg2, arg3]
    return my_list

my_packed_list = pack("protein", "gym pass", "roids")
print(my_packed_list) 


def eat_lunch(lunch_items):
    if len(lunch_items) == 0:
        print("My lunchbox is empty!")
    else:
        print("First I eat " + lunch_items[0])
        for item in lunch_items[1:]:
            print("Next I go " + item)

my_lunch = ["protein", "gym", "do roids"]
eat_lunch(my_lunch)
