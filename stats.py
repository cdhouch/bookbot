def count_words(text):
    return len(text.split())

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]
  
# need to convert dictionary to a list of dictionaries
# and sort the list of dictionaries
def dict_to_list(unsorted_dict):
    result_list = []
    for key in unsorted_dict:
        result_list.append({"char": key, "num": unsorted_dict[key]})
    #print(result_list)
    sorted_list_dict = sorted(result_list, reverse=True, key=sort_on)
    return sorted_list_dict

def list_to_dict(sorted_list):
    result_dict = {}
    for item in sorted_list:
        result_dict[item["char"]] = item["num"]
    return result_dict
def symbol_count(text):
    resultdict = {}
    result_set = set()
    charcount = 0

    listtext = list(text)
    
    for ctext in listtext:
        if ctext.isalnum():
            ctext = ctext.lower()
            #print (f"SET CHAR {ctext}")
            result_set.add(ctext)
        
    alpha_list = sorted(result_set)

    for ctext in alpha_list:
        #print (ctext) 
        charcount = 0
        for lchar in listtext:
            if ctext == lchar.lower():
                charcount += 1
        resultdict[ctext] = charcount
    #print (resultdict)
    return resultdict