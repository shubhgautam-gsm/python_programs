# Python complex() function example
# Calling function
a = complex(1) # Passing single parameter
b = complex(1,2) # Passing both parameters
# Displaying result
print(a)
print(b)


# Example: Modeling an AC circuit with complex impedance
z_load = complex(10, 5)  # Impedance of the load
v_source = complex(100, 0)  # Complex voltage source
i_load = v_source / z_load  # Calculate the complex current flowing through the load
print(i_load)