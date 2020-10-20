def sum_weights(weightbeep, weightbop):
  totalweight = weightbeep + weightbop
  return totalweight


def calc_avg_weight(weightbeep, weightbop):
  avgweight = (weightbeep + weightbop) / 2
  return avgweight



def run():
  weightbeep = float(input("What is the weight of Beep?"))
  weightbop = float(input("What is the weight of Bop?"))
  calculate = input("Do you want the sum or the average?")
  if calculate == "sum":
    answer = sum_weights(weightbeep, weightbop)
    answer = round(answer, 2)
    print("The sum of Beep and Bop's weight is {}".format(answer))
  elif calculate == "average":
    answer = calc_avg_weight(weightbeep, weightbop)
    answer = round(answer, 2)
    print("The average of Beep and Bops weight is {}".format(answer))

run()