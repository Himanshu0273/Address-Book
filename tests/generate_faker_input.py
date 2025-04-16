from faker import Faker
from random import randint,choice

faker = Faker()
def generate_input(num_of_contanct=5):
    with open ("tests/test_input.txt", "w") as f:
        for _ in range(num_of_contanct):
            phone_number = str(randint(1000000000,9999999999))
            if choice([True, False]):
                phone_number=f"+{randint(1,999)} {phone_number}"
                
            contact=[
                faker.first_name(),
                faker.last_name(),
                faker.address().replace("\n", ", "),
                faker.city(),
                faker.state(),
                # faker.zipcode(),
                str(randint(100000, 999999)),
                phone_number,
                faker.email()  
            ]
            for data in contact:
                f.write((f"{data}\n"))
                
            f.write("\n")
            
if __name__ == "__main__":
    generate_input(10)        