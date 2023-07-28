#program to calculate salary, da and hra of an employee

basic=int(input("enter basic salary amount:"))

da=(basic*(50/100))

hra=(basic*(15/100))

ts=(basic+da+hra)

print("total salary of employee:",ts)
