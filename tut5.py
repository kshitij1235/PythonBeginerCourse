# tuple

meripasandkatupple=("python","dark mode",20.00,666)
                    # 0      1            2    3
                    #-4     -3          -2   -1 
                    
print(meripasandkatupple[0:3:2])

meripasandkatupple=("python","dark mode",20.00,666)
meridastkituppl   =("php","light mode",30.00,666)

milan=meripasandkatupple+meridastkituppl
print(milan)
# ('python', 'dark mode', 20.0, 666, 
# 'php', 'light mode', 30.0, 666)

print(milan.count(666))
print(milan.index("python"))