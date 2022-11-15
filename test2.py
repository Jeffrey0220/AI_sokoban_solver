l1=[(1,2),(2,3)]
l2=[(0,1),(1,4)]

boxNotInTarget = [element for element in l1 if element not in l2]

print(boxNotInTarget)
print(boxNotInTarget[0])

        boxNotInTarget = [box for box in n.state[1:] if box not in self.targets]
        w_to_b=[]
        for i in range(len( boxNotInTarget)):            
            b_x,b_y=boxNotInTarget[i]
            w_x,w_y=n.state[0]
            w_to_b.append(abs(b_x-w_x)+abs(b_y-w_y))
        
        if len(w_to_b)!=0:   
            h_costs+=max(w_to_b)