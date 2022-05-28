#20224221 강민석
planets = set('해달별')
fruits = set(['감', '귤'])
nuts = {'밤', '잣'}
things = {('밤', '잣'), ('감', '귤'), '해달'}
#things = {['밤', '잣'], ('감', '귤'), '해달'} #오류 발생이요.

print(planets)
print(fruits)
print(nuts)
print(things)

# def setFunction(arg_Bomb, arg_Jot, arg_Gam, arg_Gyul):
#     planetes = set('해달별')
#     fruits = set([arg_Gyul, arg_Gam])
#     nuts = {arg_Jot, arg_Bomb}
#     things = {(arg_Bomb, arg_Jot), (arg_Gam, arg_Gyul), '해달'}
#     #things = {['밤', '잣'], ('감', '귤'), '해달'} #오류 발생이요.
#
#     print(planetes)
#     print(fruits)
#     print(nuts)
#     print(things)
#
# setFunction('밤', '잣', '감', '귤')