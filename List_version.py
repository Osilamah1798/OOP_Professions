class Professions:
    def __init__(self):
        self.professions = []

    def add_profession(self, name, profession_type, experience) :

        self.professions.append({
            "name" :name,
            "profession_type" : profession_type,
            "experience" : experience
             })

       
    def log_professions(self):

        print("Here's a list of all the Professions:")

        for profession in self.professions:
            print(f"Name: {profession['name']}\nProfession: {profession['profession_type']}\nExperience: {profession['experience']} years")


 
professions = Professions()

while True:
    name = input("Enter the name of the professional (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    profession_type = input(f"Enter the profession of {name}: ")
    experience = input(f"Enter the years of experience of {name}: ")

    professions.add_profession(name, profession_type, experience)

professions.log_professions()