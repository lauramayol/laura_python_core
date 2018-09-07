'''
Write the necessary code to print the following to the console:

	PPPP   Y     Y  TTTTTTTTT  H    H      O     N       N
	P   P   Y   Y       T      H    H     O O    N N     N
	P   P    Y Y        T      H    H    O   O   N  N    N
	PPPP      Y         T      HHHHHH    O   O   N   N   N
	P         Y         T      H    H    O   O   N    N  N
	P         Y         T      H    H     O O    N     N N
	P         Y         T      H    H      O     N       N

'''
def print_character(letter,num_repeats):
    ans = letter * num_repeats
    return ans



#first line below
print print_character('P',4) +print_character(' ',3)+'Y'+print_character(' ',5)+'Y'+'  '+print_character('T',9)+'  '+'H'+print_character(' ',4)+'H'+print_character(' ',6)+'O'+print_character(' ',5)+'N'+print_character(' ',7)+'N'
#second line below
print 'P' +print_character(' ',3)+'P'+print_character(' ',3)+'Y'+print_character(' ',3)+'Y'+print_character(' ',7)+'T'+print_character(' ',6)+'H'+print_character(' ',4)+'H'+print_character(' ',5)+'O O'+print_character(' ',4)+'N N'+print_character(' ',5)+'N'
#third line below
print 'P' +print_character(' ',3)+'P'+print_character(' ',4)+'Y'+print_character(' ',1)+'Y'+print_character(' ',8)+'T'+print_character(' ',6)+'H'+print_character(' ',4)+'H'+print_character(' ',4)+'O'+print_character(' ',3)+'O'+print_character(' ',3)+'N'+print_character(' ',2)+'N'+print_character(' ',4)+'N'
#fourth line below
print print_character('P',4) +print_character(' ',6)+'Y'+print_character(' ',9)+'T'+print_character(' ',6)+print_character('H',6)+print_character(' ',4)+'O'+print_character(' ',3)+'O'+print_character(' ',3)+'N'+print_character(' ',3)+'N'+print_character(' ',3)+'N'
#fourth line below
print 'P' +print_character(' ',9)+'Y'+print_character(' ',9)+'T'+print_character(' ',6)+'H'+print_character(' ',4)+'H'+print_character(' ',4)+'O'+print_character(' ',3)+'O'+print_character(' ',3)+'N'+print_character(' ',4)+'N'+print_character(' ',2)+'N'
#fifth line below
print 'P' +print_character(' ',9)+'Y'+print_character(' ',9)+'T'+print_character(' ',6)+'H'+print_character(' ',4)+'H'+print_character(' ',5)+'O'+print_character(' ',1)+'O'+print_character(' ',4)+'N'+print_character(' ',5)+'N'+print_character(' ',1)+'N'
#final line below
print 'P' +print_character(' ',9)+'Y'+print_character(' ',9)+'T'+print_character(' ',6)+'H'+print_character(' ',4)+'H'+print_character(' ',6)+'O'+print_character(' ',5)+'N'+print_character(' ',7)+'N'

