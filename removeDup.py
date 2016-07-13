# remove duplicate itmes from list but keep 1
# remove duplicate from list and sort
def remove_dup(dup_lst):
    no_dup_lst = []

    for item in dup_lst:
	    if item not in no_dup_lst:
		    no_dup_lst.append(item)

    return sorted(no_dup_lst)
    

# this remove duplicate and sort as well
def remove_dup_set(dup_lst):
    no_dup_lst = set(dup_lst)
    return no_dup_lst
