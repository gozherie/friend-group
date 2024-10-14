"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {'Jill': 
            {'age': 26, 
            'job': 'biologist', 
            'connection':{
                'friend': 'Zalika',
                'partner': 'John'
            }
            },
            'Zalika':
            {'age': 28,
             'job': 'artist',
             'connection':{
                 'friend': 'Jill'
             }
             },
             'John':
             {'age': 27,
              'job': 'writer',
              'connection': {
                  'partner': 'Jill'
              }
              },
            'Nash':
            {'age': 34,
             'job': 'chef',
             'connection': {
                 'cousin': 'John',
                 'landlord': 'Zalika'
             }

            }  
}

max_age = max(person['age'] for person in my_group.values())
print(max_age)

averge_number_relations = sum(len(person['connection']) for person in my_group.values()) / len(my_group)
print(averge_number_relations)

max_age_at_least_one_relation = max(person['age'] for person in my_group.values() if len(person['connection']) > 0 )
print(max_age_at_least_one_relation)

max_age_at_least_one_friend = max(person['age'] for person in my_group.values() if 'friend' in person['connection'])
print(max_age_at_least_one_friend)