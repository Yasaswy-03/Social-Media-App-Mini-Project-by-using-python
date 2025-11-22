import random     

class cl_1():
    user_name = []
    user_data = {}

    def __init__(self, user, password, p_name):
        self.user_id = user
        self.password = password
        self.p_name = p_name
        self.posts = 0

    @classmethod
    def create_account(cls, q):
        if q.user_id in cl_1.user_name:
            print(f"Sorry, the user id {q.user_id} already exists.\nPlease login with password.")
        else:
            cl_1.user_name.append(q.user_id)
            x = {"password": q.password, "p_name": q.p_name, "posts": q.posts}
            cl_1.user_data[q.user_id] = x

    def save_data(self):
        with open("user_data.txt", "w") as db:
            db.write(str(cl_1.user_data))

    def login(self):
        user_id = str(input("Please enter user_id: "))
        if user_id in cl_1.user_name:
            password = str(input("Please enter your password: "))
        
            otp = random.randint(1000, 9999)
            print(f"Verification OTP: {otp}")
            verify = int(input("Enter OTP: "))
            if verify != otp:
                print("OTP verification failed!")
                return

            if password == cl_1.user_data[user_id]["password"]:
                print(f"Hello {cl_1.user_data[user_id]['p_name']}")
            else:
                print("Wrong password:")
                x = 0
                while x < 3:
                    password = str(input("Re-enter correct password: "))
                    if password == cl_1.user_data[user_id]["password"]:
                        print(f"Hello {cl_1.user_data[user_id]['p_name']}")
                        break
                    else:
                        x += 1
                        if x == 3:
                            print("You reached maximum attempts. Try again later.")
        else:
            print(f"Sorry, the username {user_id} is not registered.")


dummy = cl_1(" ", "", "")
c = cl_1("abc.in", "a1234", "rakul")
c.create_account(c)
d = cl_1("xyz.com", "x1234", "balayya")
d.create_account(d)
m = cl_1("mno.ex", "m1234", "krishna")
m.create_account(m)
s = cl_1("asd.com","a1234","raju")
s.create_account(s)


print(cl_1.user_name)
print(cl_1.user_data)

dummy.save_data()
dummy.login()