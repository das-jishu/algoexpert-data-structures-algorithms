
# PHONE NUMBER MNEMONICS

# O(4^N * N) time and space
def phoneNumberMnemonics(phoneNumber):
    # Write your code here.
    individualCodes = {
		"0": ["0"],
		"1": ["1"],
		"2": ["a", "b", "c"],
		"3": ["d", "e", "f"],
		"4": ["g", "h", "i"],
		"5": ["j", "k", "l"],
		"6": ["m", "n", "o"],
		"7": ["p", "q", "r", "s"],
		"8": ["t", "u", "v"],
		"9": ["w", "x", "y", "z"]
	}
	return getAllMnemonics(phoneNumber, 0, individualCodes)
	
	
def getAllMnemonics(phoneNumber, index, individualCodes):
	if index == len(phoneNumber) - 1:
		return individualCodes[phoneNumber[index]]
	
	mnemonics = []
	for code in individualCodes[phoneNumber[index]]:
		getMnemonics = getAllMnemonics(phoneNumber, index+1, individualCodes)
		for mnemonic in getMnemonics:
			mnemonics.append(code + mnemonic)
			
	return mnemonics

