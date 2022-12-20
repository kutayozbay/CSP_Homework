#Kutay �zbay
#270201017


#Functions

assigned=[] 


def correction(a, b):
	corrected = False

	a_domain = domains[a]
	b_domain = domains[b]
    
	all_constraints = [constraint for constraint in constraints if constraint[0] == a and constraint[1] == b]
    
	for x in a_domain:
		satisfies = False
		for y in b_domain:
			for constraint in all_constraints:
				constraint_func = constraints[constraint]
				if constraint_func(x, y):
					satisfies = True
		if not satisfies:
			a_domain.remove(x)
			corrected = True
	return corrected


def  apply_arc_consistency(arcs):
	seq = arcs[:]
	while seq:

		(a, b) = seq.pop(0)
		corrected = correction(a, b)
		if corrected:
			print(domains)
			neighbors = [neighbor for neighbor in arcs if neighbor[1] == a]
			seq = seq + neighbors

       

def find_var_mrv(domains)  :
    
    min = 999999999999999
    name ='zzzzzzzzzz'
    for key , value in domains.items():
        if (min >= len(value)) and (key.lower() < name.lower()) and (key not in assigned):
            min = len(value)
            name = key
    return name


def find_val_lcv(key)     :
    i = 0
    current = []
    freq = []
    for value in domains[key]:
        current.append(value)
        freq.append(0)
        for  key1 ,value1 in domains.items(): 
            
            if value in value1 and key!=key1 :
                freq[i]+= 1
        i+= 1
    return  current[freq.index(min(freq))]


def assign(domains):
    x = find_var_mrv(domains)
    assigned.append(x)
    value =find_val_lcv(x)
    list_=[]
    list_.append(value)
    domains[x] = list_
    print(domains)
    
def reachedSolution(domain):
    for key, value in domain.items():
        if len(value)!=1:
            return False
    return True

def solver(domain ,arc):
    while True:
        apply_arc_consistency(arc)
        if reachedSolution(domain):
            break
        assign(domain)
        if reachedSolution(domain):
            break




#I apllied single valued constraint in domain part

# Gingerbread cannot come to party at 4.40
# Brian cannot come to party at 4.40
# Chris cannot come to party at 4.40
domains = {
	'hummus': [430, 435, 440, 445],
	'fries': [430, 435, 440, 445],
	'gingerbread': [430, 435, 445],
	'eggroll': [430, 435, 440, 445],
	
	'Brian': [430, 435, 445],
	'Amber': [430, 435, 440, 445],
	'Chris': [430, 435, 445],
	'Diane':  [430, 435, 440, 445]
}

#Constrains representation with binary.
#I found that method while searching for this homework. 
constraints = {
    ('Amber', 'Brian'): lambda a, b : a  + 5 == b,
    ('Brian', 'Amber'): lambda a, b : a == b + 5,
    
    ('Diane','hummus'): lambda a, b : a == b + 5,
    ('hummus','Diane'): lambda a, b : a + 5 == b,
    
    ('Chris', 'gingerbread'): lambda a, b : a != b,
    ('gingerbread', 'Chris'): lambda a, b : b != a, 
    
    
    
    
    
    
    
    #Persons
    ('Brian', 'Chris'): lambda a, b : a != b, 
    ('Chris', 'Brian'): lambda a, b : b != a,
    
    ('Brian', 'Diane'): lambda a, b : a != b, 
    ('Diane', 'Brian'): lambda a, b : b != a,
    
    ('Amber', 'Chris'): lambda a, b : a != b,
    ('Chris', 'Amber'): lambda a, b : b != a,
    
    ('Amber', 'Diane'): lambda a, b : a != b,
    ('Diane', 'Amber'): lambda a, b : b != a,

    ('Chris', 'Diane'): lambda a, b : a != b,
    ('Diane', 'Chris'): lambda a, b : b != a,


    #Foods
    ('hummus', 'fries'): lambda a, b : a != b,
    ('fries', 'hummus'): lambda a, b : b != a,
    
    ('hummus', 'gingerbread'): lambda a, b : a != b, 
    ('gingerbread', 'hummus'): lambda a, b : b != a,
    
    ('hummus', 'eggroll'): lambda a, b : a != b, 
    ('eggroll', 'hummus'): lambda a, b : b != a,
    
    ('fries', 'gingerbread'): lambda a, b : a != b,
    ('gingerbread', 'fries'): lambda a, b : b != a,
    ('fries', 'eggroll'): lambda a, b : a != b,
    ('eggroll', 'fries'): lambda a, b : b != a,

    ('gingerbread', 'eggroll'): lambda a, b : a != b,
    ('eggroll', 'gingerbread'): lambda a, b : b != a



}



arcs = [
    ('Amber', 'Brian'),
    ('Brian', 'Amber'),
    
    ('Diane','hummus'),
    ('hummus','Diane'),
    
    ('Chris', 'gingerbread'),
    ('gingerbread', 'Chris'),
    
    
    #Persons
    ('Brian', 'Chris'), 
    ('Chris', 'Brian'),
    
    ('Brian', 'Diane'), 
    ('Diane', 'Brian'),
    
    ('Amber', 'Chris'),
    ('Chris', 'Amber'),
    
    ('Amber', 'Diane'),
    ('Diane', 'Amber'),
    
    ('Chris', 'Diane'),
    ('Diane', 'Chris'),
    
    
    #Foods
    ('fries', 'eggroll'),
    ('eggroll', 'fries'),
    ('hummus', 'fries'),
    ('fries', 'hummus'),
    ('hummus', 'gingerbread'), 
    ('gingerbread', 'hummus'),
    ('hummus', 'eggroll'), 
    ('eggroll', 'hummus'),
    ('fries', 'gingerbread'),
    ('gingerbread', 'fries'),
    ('fries', 'eggroll'),
    ('eggroll', 'fries'),
    ('gingerbread', 'eggroll'),
    ('eggroll', 'gingerbread')
]
        
solver(domains ,arcs)    
