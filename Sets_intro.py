# creation of an empty set.
set1=set()

set1.add(1)

print(set1)

# duplicates will be removed.
set1=set([1,2,3,1,3,1,2,3,1,6])

print(set1)

# looping the set.
for item in set1:
    print(item)
    
# membership check.
print(1 in set1)

# adding existent items to set has no effect.
set1.add(6)

print(set1)

# multiple items can be added using below:
set1.update([1,9,6,7,54,223,12])

print(set1)

# removing data from sets.
set1.remove(223)

print(set1)

# set1.remove(111) KeyError (Non-existent element).

# discard has no effect if the set doesn't contain an element.
set1.discard(111)

print(set1)

set2=set1.copy()

print(set1)
print(set2)

set1.discard(54)

print(set1)
print(set2)

blue_eyes={'Al','Bob','Don','Kevin'}
blond_hair={'Al','Lev','Don','Ruth'}
taller_than_six_feet={'Kevin','Don','Paul'}
o_blood={'Al','Bob'}

# people having blue eyes and blond hair.
print(blue_eyes.intersection(blond_hair))
# people having blue eyes and or or blond hair.
print(blue_eyes.union(blond_hair))
# people who have either blue eyes or blond hair.
print(blue_eyes.symmetric_difference(blond_hair))
# people who have blue eyes but not blond haired.
print(blue_eyes.difference(blond_hair))
# people who have blond hair but not blue eyed.
print(blond_hair.difference(blue_eyes))
# subset.
print(o_blood.issubset(blue_eyes))
# subset.
print(blue_eyes.issuperset(o_blood))
# No data in common.
print(o_blood.isdisjoint(taller_than_six_feet))
