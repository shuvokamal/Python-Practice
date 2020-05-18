import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Start running the codes")

# declaring an array:
MLB_team = {
    'Colorado': 'Rockies',
    'Boston': 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle': 'Mariners'
}

MLB_team1 = dict([
    ('Colorado', 'Rockies'),
    ('Boston', 'Red Sox'),
    ('Minnesota', 'Twins'),
    ('Milwaukee', 'Brewers'),
    ('Seattle', 'Mariners')
])

MLB_team2 = dict(
    Colorado='Rockies',
    Boston='Red Sox',
    Minnesota='Twins',
    Milwaukee='Brewers',
    Seattle='Mariners'
)

# print(MLB_team, MLB_team1, MLB_team2)

# Accessing the dictionary:
print(MLB_team2['Colorado'])

# Assigning new value to dictionary:
MLB_team['Kansas City'] = 'Royals'
print(MLB_team)
logger.info('End of creating the dictionary')
# Updating a key value pair with new value replacing the old one
MLB_team['Seattle'] = 'Seahawks'
print(MLB_team)

# Building a dictionary incrementally:
person = {}
print(type(person))

person["First Name"] = "Shuvo"
person["last name"] = "Kamal"
person['age'] = 25
person['car'] = ['lexus', 'toyota']
person['state'] = {'living': 'CT', 'home state': "NJ"}

print(person)
# {'First Name': 'Shuvo', 'last name': 'Kamal', 'age': 25, 'car': {'toyota', 'lexus'}, 'state': {'living': 'CT', 'home state': 'NJ'}}
print(person['First Name'])
print(person['car'])

# Retrieving the values in the sublist or sub dictionary requires an additional index or key:
print(person['car'][-1])  # toyota
print(person['state']['living'])

print(len(person))  # 5
# print(person.clear())
# print(person)

print(MLB_team.get('Seattle'))
print(MLB_team.get('New York', -1))

# print(person.items())
# print(list(person.items()))
print(MLB_team.items())
# {'First Name': 'Shuvo', 'last name': 'Kamal', 'age': 25, 'car': {'toyota', 'lexus'}, 'state': {'living': 'CT', 'home state': 'NJ'}}
print(list(person.items())[3][0])  # car # 0 index give the key
print(list(person.items())[3][1])  # ['lexus', 'toyota'] # 1 index give both the values

print(list(person.keys()))
print(list(person.values()))
person.pop('age')  # pop() to remove a key
print(person)
person.popitem()  # popitem()
print(person)
person.update(MLB_team)  # update()
print(person)
print(dir(person))  # To visualize the methods and attributes of any Python object

for key in person:  # for loops
    print(key, person[key])

for key in person:
    print(key)

for key in person:
    print(person[key])

for key, value in person.items():
    print(key, ">>>", value)
logger.info('Read data from file')
# irrelevant: counting number from the text file
f = open("text_word_count.txt", "rt")
print(f)
data = f.read()
words = data.split()

print(len(words))
logger.info('Finished displaying the count of words')
