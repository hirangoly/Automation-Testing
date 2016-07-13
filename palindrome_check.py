def check_palindrome(str_pali):
	str_pali = str_pali.replace(' ', '')
	i = 0
	j = len(str_pali) - 1
	while(i<j):
		if str_pali[i].lower()!=str_pali[j].lower():
			return False
		else:			
			i+=1
			j-=1
	return True



if __name__ == '__main__':
	valid_pali = 'A man a plan a canal Panama'
	invalid_palindrome = 'race a car'
	valid_spchar_pali = 'A man, a plan a canal: Panama'
	valid_spchar_pali_nosp = ''.join(e for e in valid_spchar_pali if e.isalnum())
	print valid_spchar_pali_nosp
	
	print 'start valid'
	check_palindrome(valid_pali)
	print 'end valid'
	print 'start valid special char'
	check_palindrome(valid_spchar_pali)
	print 'end valid special char'
	print 'start invalid'
	check_palindrome(invalid_palindrome)
	print 'start invalid'
