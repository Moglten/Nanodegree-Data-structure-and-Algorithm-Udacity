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
    return is_user_in_group_helper(user,group)

def is_user_in_group_helper(user,group):
    curr_group = group.groups
    curr_user = group.users

    for User in curr_user:
        if User == user :
            return True

    for Group in curr_group:
        output = False
        output = output or is_user_in_group(user, Group)
        return  output

    return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_child_user1 = "large_user"
sub_child_user2 = "sub_child_user"

child.add_group(sub_child)
parent.add_group(child)

sub_child.add_user(sub_child_user1)
print(is_user_in_group(sub_child_user1, parent))    #return True
print(is_user_in_group(sub_child_user2, parent))    #return False

sub_child.add_user(sub_child_user2)                 #add here that child
print(is_user_in_group(sub_child_user2, parent))    #check again is exist return True

print(is_user_in_group("",parent))                  #return False

print(is_user_in_group(4141,parent))                #return False

