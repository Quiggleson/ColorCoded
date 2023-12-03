# Idea:
# RGB colors are made with [0,255] Red, [0,255] Green, and [0,255] Blue
# Once we remove a color, we adjust the max of the other two and 1/3 of the 
# removed color to each
# 
# Example
#   Original = [100,100,100]
#   We remove red
#   
#   1. Adjust the others
#       B = old_B * .67 = 67
#       G = old_G * .67 = 67   
#
#   2. Calculate how much red to add
#       R = old_R * .33 = 33
#   
#   3. Add this to the remaining colors
#       New = [0,100,100]
#
#
#   But wait, you just kep green and blue the same, what about R = 255?
#       R = old_R * .33 = 85
#       New = [0,152,152]
#
#   What about two different combinations of R and G,B to get the same New?
#       G and B are independent, so consider just G
#       G_old is in the range [0,255]
#       G_new in in the range [0,170]
#       R_old is in the rnage [0,255]
#       R_new is in the range [0,85]
#       Could there ever be two combinations of G_old and R_old that yield the
#       same G_new + R_new?
#       Consider a G_original, R_original that yiel G_old, R_old, G_new, R_new
#       Now consider prime(G,R) = G_new - 2 + R_new + 2
#       Denoted by G'_original, R'_original, G'_old, R'_old, G'_new, R'_new
#       G'_new = G_new - 2
#       G'_old = G'_new * 3/2
#       G'_old = 3/2G_new - 3
#       .....       
#   