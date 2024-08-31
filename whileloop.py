# Define the parameters
thief_step = 2  # meters per step for the thief
police_step = 5  # meters per step for the police
initial_distance = 40  # initial distance between thief and police in meters

# Initialize the distance and step counter
distance = initial_distance
steps = 0

# Use a while loop to simulate the process
while distance > 0:
    # The thief and the police each take a step
    distance -= (police_step - thief_step)
    steps += 1

# Print the number of steps needed
print(f"The police will catch the thief in {steps} steps.")


