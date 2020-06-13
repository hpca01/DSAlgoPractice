import inspect

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = set()
        self.users = set()

    def add_group(self, group):
        self.groups.add(group)

    def add_user(self, user):
        self.users.add(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name
    
    def __repr__(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.users:
        return True
    for each_group in group.groups:
        if user in each_group.users:
            return True
        else:
            return is_user_in_group(user, each_group)
    return False
    
def test1():
    '''default test case, for nested user'''
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)
    child.add_group(sub_child)
    parent.add_group(child)
    print(f'Looking for user {sub_child_user} in {parent} ... {is_user_in_group(sub_child_user, parent)}')
    assert is_user_in_group(sub_child_user, parent) == True, "Error occured {} failed".format(inspect.stack()[0].function)

def test2():
    '''test case where user does not exist'''
    parent = Group('parent')
    children = [Group(f'Child_{x}') for x in range(10)]
    users = ["User_{}".format(x) for x in range(10)]
    list(map(lambda x: (x.users.update(users)), children))
    parent.groups = children
    user_to_look_for = "User_11"
    print(f'Looking for user {user_to_look_for} in {parent} ... {is_user_in_group(user_to_look_for, parent)}')
    assert is_user_in_group(user_to_look_for, parent) == False, "Error occured {} failed".format(inspect.stack()[0].function)

def test3():
    '''no sub-groups exist'''
    parent = Group('parent')
    parent.users.update(['user_{}'.format(x) for x in range(5)])
    user_to_look_for = "user_3"
    print(f'Looking for user {user_to_look_for} in {parent} ... {is_user_in_group(user_to_look_for, parent)}')
    assert is_user_in_group(user_to_look_for, parent) == True, "Error occured {} failed".format(inspect.stack()[0].function)
    
    pass

if __name__ == "__main__":
    test1()
    test2()
    test3()