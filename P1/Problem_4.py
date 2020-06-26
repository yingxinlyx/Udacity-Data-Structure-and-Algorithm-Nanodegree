class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if group is None:
        return False

    if user in group.get_users():
        return True

    for g in group.get_groups():
        if is_user_in_group(user, g):
            return True

    return False


parent = Group("parent")
child1 = Group("child1")
child2 = Group("child2")
sub_child = Group("subchild")
child1.add_group(sub_child)
parent.add_group(child1)
parent.add_group(child2)

sub_child.add_user("sub_child_user")
child1.add_user("user1")
child1.add_user("user2")
child2.add_user("user3")

# test case 1
print(is_user_in_group("sub_child_user", child2))
# False

# test case 2
print(is_user_in_group("user_a", parent))
# False

# test case 3
print(is_user_in_group("user3", parent))
# True
