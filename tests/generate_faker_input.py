from faker import Faker

faker = Faker()
def generate_input(num_of_contanct=5):
    with open ("test_input.txt", "w") as f:
        for _ in range(num_of_contanct):
            contact=[
                faker.first_name(),
                faker.last_name(),
                faker.address().replace("\n", ", "),
                faker.city(),
                faker.state(),
                faker.zipcode(),
                faker.phone_number(),
                faker.email()  
            ]
            for data in contact:
                f.write((f"{data}\n"))
                
            f.write("\n")
            
if __name__ == "__main__":
    generate_input(10)        