
# VALID STARTING CITY

# O(N) time and O(1) space
def validStartingCity(distances, fuel, mpg):
    # Write your code here.
    validCity = 0
	milesLeft = 0
	idx = 0
	while idx < len(distances):
		milesLeft += fuel[idx] * mpg
		if milesLeft >= distances[idx]:
			milesLeft -= distances[idx]
		else:
			validCity = idx + 1
			milesLeft = 0
		idx += 1
	return validCity
