from faker import Faker

faker1 = Faker()

for _ in range(1,100):
	print(faker1.time(),",", faker1.name())

