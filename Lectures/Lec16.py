def make_city_state_pairs(list_cities, list_states):
    city_state_pairs={}
    for index in range(len(list_cities)):
        city_state_pairs[list_cities[index]]=list_states[index]
    return(city_state_pairs)
