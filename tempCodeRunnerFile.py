
def pre_dict(words):
  exclamation = {}
  for i in words.split():
    exclamation[i] = exclamation.get(i, 0) +1
  return exclamation
words = input("Enter: ")
print(pre_dict(words))


def dict_to_tuple(words):
  dictionary = pre_dict(words)
  key_max = max(dictionary, key=lambda k:dictionary[k])
  value_max = dictionary[key_max]
  finally_tuple = (key_max, value_max)
  return finally_tuple
print(dict_to_tuple(words))