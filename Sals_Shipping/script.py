premium_shipping = 125

def ground_shipping(weight):
  if weight <= 2:
    return (weight * 1.5) + 20
  elif (weight > 2) and (weight <= 6):
    return (weight * 3) + 20
  elif (weight > 6) and (weight <= 10):
    return (weight * 4) + 20
  else:
    return (weight * 4.75) + 20

print(ground_shipping(8.4))

def drone_shipping(weight):
  if weight <= 2:
    return (weight * 4.5)
  elif (weight > 2) and (weight <= 6):
    return weight * 9
  elif (weight > 6) and (weight <= 10):
    return weight * 12
  else:
    return weight * 14.25

print(drone_shipping(1.5))



def cheapest_shipping(weight):
  ground = ground_shipping(weight)
  drone =  drone_shipping(weight)
  premium_shipping = 125

  if  (ground > drone) and (ground > premium_shipping):
    return "Drone shipping is cheaper"
  elif (ground < drone) and (ground < premium_shipping):
    return "Ground shipping weight is cheaper"
  else:
    return "premium shipping is cheaper"

print(cheapest_shipping(8))
