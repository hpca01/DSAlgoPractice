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
    print(group.__dict__)
    for each_group in group.groups:
        print(f'Checking group {each_group.__dict__}')
        if user in each_group.get_users():
            return True
    return False
    


if __name__ == "__main__":    
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)
    print(f'Sub child: {sub_child} {sub_child.get_users()}')
    child.add_group(sub_child)
    parent.add_group(child)
    print(f'Searching for {sub_child_user} in AD...found: {is_user_in_group(sub_child_user, parent)}')