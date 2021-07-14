########################################
# QUESTION
########################################

# Our football team finished the championship.
# The result of each match look like "x:y".
# Results of all matches are recorded in the collection.

# For example: ["3:1", "2:2", "0:1", ...]

# Write a function that takes such collection and counts the points
# of our team in the championship. Rules for counting points for each match:

# if x>y - 3 points
# if x<y - 0 point
# if x=y - 1 point
# Notes:

# there are 10 matches in the championship
# 0 <= x <= 4
# 0 <= y <= 4


#######################################
# Solution 1
#######################################
def points(games):
    k = len(games)

    z = 0
    for j in range(0,(k)):
        x = int(games[j][0])
        y = int(games[j][2])
        if x > y:
            z += 3
        elif x == y:
            z += 1
        elif x < y:
            z += 0
    return z

games = ['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']
print(points(games))
