def shipping_cal_ground_flat(weight):
  if weight <= 2:
    price_per_pound = 1.50
  elif weight <= 6:
    price_per_pound = 3.00
  elif weight <= 10:
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75
  return 20 + (price_per_pound * weight)

def shipping_cal_prem(weight):
  return 125.00

def drone_shipping(weight):
  if weight <= 2:
    price_per_pound = 4.50
  elif weight <= 6:
    price_per_pound = 9.00
  elif weight <= 10:
    price_per_pound = 12.00
  else:
    price_per_pound = 14.75
  return price_per_pound * weight


#weight = float(input("Please enter the weight of your package: "))
weight = 7

ground_srv = shipping_cal_ground_flat(weight)
premium_srv = shipping_cal_prem(weight)
drone_srv = drone_shipping(weight)

if ground_srv < premium_srv and ground_srv < drone_srv:
  service = "Ground Shipping"
  cost = ground_srv
elif premium_srv < ground_srv and preimum_srv < drone_srv:
  service = "Ground Shipping Preimum is the best option"
  cost = premium_srv
else:
  service = "Drone Shipping is the best option"
  cost = drone_srv

print("The cheapest method of shipping is " + service + " and it will cost $" + str(cost) + ".")