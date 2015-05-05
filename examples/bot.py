from pwrapper import Wrapper

b = Wrapper(user_agent="test_bot")

b.token = "vjdOXdRyF52j"

b.me()

print b.raw

print b.new_post("test", "testtest").text
