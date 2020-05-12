#trial Division algorithm
def trial_division(num):
    for i in range (2,num):
      if (num % i) == 0:
        return False
      return True

def main():
  x = 11
  if trial_division(x) == False:
    print(x,"is not a prime number")
  else:
    print(x,"is a prime number")

if __name__ == '__main__':
  main()
