def hotel_cost(nights):
  total_cost = 140 * nights
  return total_cost

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

def rental_car_cost(days):
  total_cost_car = days * 40
  if days >= 7:
    total_cost_car = total_cost_car - 50
  elif days >= 3:
    total_cost_car = total_cost_car - 20
  return total_cost_car

def trip_cost(city,days,spending_money):
  return hotel_cost(days-1) + rental_car_cost(days) + plane_ride_cost(city) + spending_money

print trip_cost("Los Angeles", 5, 600)
