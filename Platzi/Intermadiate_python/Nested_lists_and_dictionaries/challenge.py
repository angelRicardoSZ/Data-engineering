from concurrent.futures.thread import _worker


DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]
## Create the following lists using filter and map
# 1.  "all_python_devs" : Developers who use python language 
# 2. "all_Platzi_workers": Developers who work at Platzi 
# 3. "adults": age >= 18
# 4. "old_people": age > 70

def run():
    all_python_devs = list(filter(lambda worker:worker["language"] == "python",DATA ))
    all_python_devs_name = list(map(lambda worker: worker["name"], all_python_devs ))
    
    all_Platzi_workers = list(filter(lambda worker:worker["organization"]=="Platzi", DATA))
    all_Platzi_workers_name = list(map(lambda worker:worker["name"],all_Platzi_workers))    
    
    adults = [worker["name"] for worker in DATA if worker["age"] >= 18]
    #old_people = [worker["name"] for worker in DATA if worker["age"] > 70 ]
    
    old_confirmation = lambda worker_age: worker_age > 70
    old_people = [worker | {'old': old_confirmation(worker['age'])} for worker in DATA]
    
    
    for worker in all_python_devs:
        print(worker)
    
    for worker in all_python_devs_name:
        print(worker)

        
    for worker in all_Platzi_workers:
        print(worker)
        
    for worker in all_Platzi_workers_name:
        print(worker)    
        
    for worker in adults:
        print(worker)    
    
    for worker in old_people:
        print(worker) 
if __name__=="__main__":
    run()
    
    
