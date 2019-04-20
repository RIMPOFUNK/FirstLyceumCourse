class User:
    def __init__(self, name):
        self.name = name if isinstance(name, str) else None

    def __str__(self):
        return f"User {self.name}"
    

class Server:
    def __init__(self, name='def', user=None):
        self.name = name
        self.users = []
        if isinstance(user, User):
            self.users.append({user: []})
        elif isinstance(user, list) and len(user) and isinstance(user[0], User):
            self.users.extend({i: []} for i in user)
        else:
            print(f"Given wrong user: {user}")
        
    def add_users(self, users: list):
        if isinstance(users, list):
            self.users.extend({i: []} for i in users)
        else:
            print(f"Given wrong user: {users}")
        
    def receive_mail(self, user):
        for i in range(len(self.users)):
            if user in self.users[i].keys():
                ret = self.users[i]
                self.users[i] = {ret.keys(): []}
                return f"{'; '.join(list(ret.values()))} removed from the server {self.name}," + \
                       f"user: {' '.join(list(ret.keys()))}"
        return "Given wrong value"
            
    def get_values(self):
        for i in self.users:
            for key, val in i.items():
                print(f"{key}, messages: {', '.join(val)}")

    def send_mail(self, user, message):
        for i in range(len(self.users)):
            if user in self.users[i]:
                lst = list(self.users[i].values()) + [message]
                key = list(self.users[i].keys())
                self.users[i] = {key: lst}
                

class MailClient:
    def __init__(self, server, user):
        self.serv = server
        self.user = user
        self.serv.add_users([user])

    def receive_mail(self):
        print(self.serv.receive_mail(self.user))

    def send_mail(self, server1, user1, message):
        server1.send_mail(user1, message)
