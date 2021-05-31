house_no = 11;
print(type(house_no));
print(id(house_no));
print();

house_no = 12;
print(type(house_no));
print(id(house_no));
print();


count = 0;
print(id(count));
count = count+1;
print(id(count));
print();


captain = "MsDhoni";
print(id(captain));
print();

captain2 = "MsDhoni";
print(id(captain2));
print();


captain = "ViratKohli";
print(id(captain));
print();


captainIpl = captain;
print(id(captainIpl));
print();


city1 = "madurai";
city2 = "madurai";
print(city1 is city2); # is compares memory address
print(city1 == city2); # == compares value
print();


##name = "raja";
##name[0] = "o";
##print(name); # it will throw error because string is immutable


word = "python";
print("J",word[1:]);


