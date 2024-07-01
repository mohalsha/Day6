import pickle

class dictionary:
    def __init__(self, element1, element2):
        self.element1 = element1
        self.element2 = element2
    
first_entry = dictionary("title", "Head First Python")
second_entry = dictionary("author", "Paul Barry")
third_entry = dictionary("price", "50 USD")

with open('c:/Users/mohalsha/Desktop/Python_training/file3.pkl', 'wb') as file:
    pickle.dump(first_entry, file)
    pickle.dump(second_entry, file)
    pickle.dump(third_entry, file)


with open('c:/Users/mohalsha/Desktop/Python_training/file3.pkl', 'rb') as file:
    second_entry = pickle.load(file)
    print(second_entry.element1)
    print(second_entry.element2)