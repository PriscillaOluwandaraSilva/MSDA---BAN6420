import random

# Generate dynamic list of 400 workers
workers = []
for i in range(1, 401):
    name = f"Worker_{i}"
    salary = random.randint(5000, 35000)  # Salary between $5,000 and $35,000
    gender = random.choice(['Male', 'Female'])
    workers.append({'name': name, 'salary': salary, 'gender': gender})

# Generate payment slips
for worker in workers:
    try:
        name = worker['name']
        salary = worker['salary']
        gender = worker['gender']
        
        # Determine employee level
        level = 'Unassigned'
        if 10000 < salary < 20000:
            level = 'A1'
        if 7500 < salary < 30000 and gender == 'Female':
            level = 'A5-F'
        
        # Create slip text
        slip = f"Payment Slip for {name}\nSalary: ${salary}\nGender: {gender}\nLevel: {level}\n{'-'*30}\n"
        
        # Save to file
        with open(f'sample_output/{name}_slip.txt', 'w') as f:
            f.write(slip)
    
    except Exception as e:
        print(f"Error processing {worker}: {e}")
