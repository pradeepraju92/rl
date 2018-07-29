import random
class Bandit:
    def __init__(self,number_of_actions):
        #action names are the array indices
        self.number_of_actions = number_of_actions
        self.Val = [1 for x in range(0,number_of_actions)]
        self.NoA = [1 for x in range(0,number_of_actions)]
    
    def reward(self):
        return random.randint(1,10)
    
    def compute_new_val(self,x): return x + ((self.reward() - x)/self.NoA[self.Val.index(x)])
    
    def decide(self,prob_val,number_of_iterations):
        count1 = count2 = count = 0
        chose_max_times = prob_val * number_of_iterations
        chose_rand_times = (number_of_iterations - chose_max_times)
        while 1:
            flag = random.randint(0,1) # prob_val governs which piece of code runs
            if flag and (count1 < chose_max_times):
                count1 = count1 + 1
                self.Val = list(map(self.compute_new_val,self.Val))
                print(self.Val)
                action = self.Val.index(max(self.Val))
                action = action + 1
                print("Action to be taken is " + str(action) + " and value is " + str(max(self.Val)) + " and count is " + str(count1))
            if (1-flag) and (count2 < chose_rand_times):
                count2 = count2 + 1
                action = random.randint(1,self.number_of_actions)
                print("Action to be taken is chosen at random and it is "+str(action) + " and value is " + str(self.Val[action-1]) + " and count is " + str(count2))
            self.NoA[action-1] = self.NoA[action-1] + 1
            if(count1 > chose_max_times and count2 > chose_rand_times):
                return

def main():
    b = Bandit(5)
    b.decide(0.6,100)

if __name__ == "__main__":
    main()
            