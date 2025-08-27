import random

# Είσοδος δεδομένων
def input_data():
    print("Εισαγωγή δεδομένων πακέτων:")
    packages = []
    num_packages = int(input("Πλήθος πακέτων: "))
    for i in range(num_packages):
        weight = float(input(f"Βάρος πακέτου σε Kg {i + 1}: "))
        length = float(input(f"Μήκος πακέτου σε m {i + 1}: "))
        width = float(input(f"Πλάτος πακέτου σε m {i + 1}: "))
        price = float(input(f"Τιμή πακέτου {i + 1}: "))
        packages.append((weight, length, width, price))
    
    print("\nΕισαγωγή δεδομένων φορτηγών:")
    trucks = []
    num_trucks = int(input("Πλήθος φορτηγών: "))
    for i in range(num_trucks):
        max_weight = float(input(f"Μέγιστο βάρος φορτηγού σε Kg {i + 1}: "))
        length = float(input(f"Μήκος καμπίνας φορτηγού σε m {i + 1}: "))
        width = float(input(f"Πλάτος καμπίνας φορτηγού σε m {i + 1}: "))
        trucks.append((max_weight, length, width))
    
    return packages, trucks

# Γενετικός αλγόριθμος: Δημιουργία αρχικού πληθυσμού
def generate_initial_population(num_packages, num_trucks, population_size):
    return [[random.randint(-1, num_trucks - 1) for _ in range(num_packages)] for _ in range(population_size)]

# Συνάρτηση καταλληλότητας (fitness)
def fitness(chromosome, packages, trucks):
    total_price = 0
    penalties = 0
    
    for truck_id in range(len(trucks)):
        max_weight, max_length, max_width = trucks[truck_id]
        current_weight = 0
        current_area = 0
        
        for i, package in enumerate(packages):
            if chromosome[i] == truck_id:  # Πακέτο στο φορτηγό
                weight, length, width, price = package
                current_weight += weight
                current_area += length * width
                total_price += price
        
        # Ποινές για παραβίαση περιορισμών
        if current_weight > max_weight:
            penalties += (current_weight - max_weight) * 10
        if current_area > max_length * max_width:
            penalties += (current_area - max_length * max_width) * 10
    
    return total_price - penalties

# Επιλογή πληθυσμού (Selection)
def select_population(population, fitness_scores, num_parents):
    selected = sorted(zip(population, fitness_scores), key=lambda x: x[1], reverse=True)
    return [x[0] for x in selected[:num_parents]]

# Διασταύρωση (Crossover)
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:]

# Μετάλλαξη (Mutation)
def mutate(chromosome, num_trucks):
    index = random.randint(0, len(chromosome) - 1)
    chromosome[index] = random.randint(-1, num_trucks - 1)
    return chromosome

# Γενετικός Αλγόριθμος
def genetic_algorithm(packages, trucks, population_size=100, generations=100):
    num_packages = len(packages)
    num_trucks = len(trucks)
    population = generate_initial_population(num_packages, num_trucks, population_size)
    
    for generation in range(generations):
        # Υπολογισμός fitness
        fitness_scores = [fitness(chromosome, packages, trucks) for chromosome in population]
        
        # Εμφάνιση προόδου
        best_fitness = max(fitness_scores)
        print(f"Γενιά {generation + 1}: Καλύτερη τιμή fitness = {best_fitness}")
        
        # Επιλογή γονέων
        parents = select_population(population, fitness_scores, population_size // 2)
        
        # Δημιουργία νέου πληθυσμού
        next_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = random.sample(parents, 2)
            offspring1 = crossover(parent1, parent2)
            offspring2 = crossover(parent2, parent1)
            next_population.append(mutate(offspring1, num_trucks))
            next_population.append(mutate(offspring2, num_trucks))
        
        population = next_population
    
    # Επιστροφή καλύτερης λύσης
    best_solution = max(population, key=lambda c: fitness(c, packages, trucks))
    return best_solution, fitness(best_solution, packages, trucks)

# Κύριο πρόγραμμα
if __name__ == "__main__":
    packages, trucks = input_data()
    solution, score = genetic_algorithm(packages, trucks)

 
    print("\nΚαλύτερη λύση:")

unplaced_packages = []  # Πακέτα που δεν μπορούν να τοποθετηθούν
for truck_id in range(len(trucks)):
    max_weight, max_length, max_width = trucks[truck_id]
    current_weight = 0
    current_area = 0

    
    print(f"\nΦορτηγό {truck_id + 1}:")
    for i, assigned_truck in enumerate(solution):
        if assigned_truck == truck_id:
            weight, length, width, price = packages[i]
            if current_weight + weight <= max_weight and current_area + (length * width) <= max_length * max_width:
                current_weight += weight
                current_area += length * width
                print(f"  Πακέτο {i + 1}: Βάρος={weight}kg, Διαστάσεις={length}x{width}m, Τιμή={price}€")
            else:
                unplaced_packages.append(i + 1)

# Εμφάνιση πακέτων που δεν μπορούν να τοποθετηθούν
for i, assigned_truck in enumerate(solution):
    if assigned_truck == -1:  # Πακέτο χωρίς φορτηγό
        unplaced_packages.append(i + 1)

if unplaced_packages:
    print("\nΤα παρακάτω πακέτα δεν μπορούν να τοποθετηθούν σε κανένα φορτηγό:")
    for package_id in unplaced_packages:
        print(f"  Πακέτο {package_id}")
else:
    print("\nΌλα τα πακέτα τοποθετήθηκαν επιτυχώς.")

