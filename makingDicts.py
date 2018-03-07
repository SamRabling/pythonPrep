name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(list1, list2):
  new_dict = {}
  for i in range(len(list1)):
    key = list1[i]
    val = list2[i]
    new_dict[key] = val
  return new_dict

print make_dict(name, favorite_animal)