
input_command = str(input())
town={}
while "Sail" != input_command:
    if input_command == "Sail":
        break
    

    tokens=input_command.split("||")
    town_name=tokens[0]
    population=int(tokens[1])
    gold=int(tokens[2])
    if town_name in town:
        town[town_name]["population"]+=population
        town[town_name]['gold']+=gold
        input_command = str(input())
        continue
    town[town_name]={}
    town[town_name]["population"]=population
    town[town_name]['gold']=gold

    input_command = str(input())

second_input=str(input())
while second_input!="End":
    if second_input=="End":
        break
    data=second_input.split("=>")
    action= data[0]
    
  
    town_name=data[1]
    
    if action == "Plunder":
        
       
        people=int(data[2])
        gold_stolen=int(data[3])
        
        town[town_name]["population"]-=people
        town[town_name]['gold']-=gold_stolen
        p = town[town_name]["population"]
        g = town[town_name]['gold']
        if p<=0 or g<=0:
            deleted_city=town.pop(town_name)
            print(f"{town_name} plundered! {gold_stolen} gold stolen, {people} citizens killed.")
            print(f"{town_name} has been wiped off the map!")
            second_input=str(input())
            continue
        else:
            print(f"{town_name} plundered! {gold_stolen} gold stolen, {people} citizens killed.")

    elif action == "Prosper":
        gold_up=int(data[2])
        
        p =town[town_name]["population"]
        g=town[town_name]['gold']
        
        if gold_up <0:
            print("Gold added cannot be a negative number!")
            second_input=str(input())
            continue
        else:
            town[town_name]['gold']+=gold_up
            print(f"{gold_up} gold added to the city treasury. {town_name} now has {town[town_name]['gold']} gold.")
    second_input=str(input())

print(f'Ahoy, Captain! There are {len(town)} wealthy settlements to go to:')

sorted_towns= sorted(town.keys(),key=lambda c: (-town[c]["gold"], c))
if len(town)<=0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    for x in sorted_towns:
        print(f"{x} -> Population: {town[x]['population']} citizens, Gold: {town[x]['gold']} kg")
