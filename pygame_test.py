# import pygame


# # Display rules
# x = 1500
# y = 950



# pygame.init()

# screen = pygame.display.set_mode((x, y))
# screen.fill((0, 0, 0))

# clock = pygame.time.Clock()

# #Image location
# loc_x = x/2
# loc_y = y/2

# pygame.draw.circle(screen, (0, 255, 0), (loc_x, loc_y), 50)

# # screen.blit(image, (loc_x, loc_y))

# keys = pygame.key.get_pressed()

# pygame.display.update()

# running  = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         # For holding down keys
#         keys = pygame.key.get_pressed()

#     if keys[pygame.K_w]:
#         loc_y -= 10
#     if keys[pygame.K_s]:
#         loc_y += 10
#     if keys[pygame.K_a]:
#         loc_x -= 10
#     if keys[pygame.K_d]:
#         loc_x += 10

#     # if pygame.mouse.get_pressed():
#     #     mouse_x, mouse_y = pygame.mouse.get_pos()
#     #     loc_x = mouse_x - image.get_width()/2
#     #     loc_y = mouse_y - image.get_height()/2

#     # Redraw screen
#     screen.fill((0, 0, 0))
#     pygame.draw.circle(screen, (0, 255, 0), (loc_x, loc_y), 50)
#     pygame.display.flip()

#     clock.tick(60)


# pygame.quit()


digits = [0,2,2]
even = []
last_even = []
if len(digits) < 3:
    print (0)
else:
    for i in range(len(digits)):
        for x in range(len(digits)):
            for y in range(len(digits)):
                if i != x and i != y and x != y:
                    even.append(int(str(digits[i]) + str(digits[x]) + str(digits[y])))
for i in even:
    if i % 2 == 0 and len(str(i)) == 3 and i not in last_even:
        last_even.append(i)
print(even)
print (last_even)