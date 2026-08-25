from faker import Faker

fake = Faker("pt_BR")

nome = fake.name()
email = fake.email()
cidade = fake.city()

print("Nome:", nome)
print("Email:", email)
print("Cidade:", cidade)