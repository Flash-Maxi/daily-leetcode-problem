### sort the vovels in string ###
class object():
    def sort_vowels(s):
        vowels = 'aeiouAEIOU'
        vowel_list = [char for char in s if char in vowels]
        vowel_list.sort()
        
        result = []
        vowel_index = 0
        
        for char in s:
            if char in vowels:
                result.append(vowel_list[vowel_index])
                vowel_index += 1
            else:
                result.append(char)
        
        return ''.join(result)
    

s=input("enter your sting: ")
print(object.sort_vowels(s))

