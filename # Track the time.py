    # Track the time
    current_time = pygame.time.get_ticks()

    # Variables
    game_state = "start"
    start_time = 0
    name = ""
    count = 0

    # Detect key presses
    if event.type == pygame.KEYDOWN:
        # Tell the game to run or wait
        if game_state == "start":
            game_state = "wait"
            start_time = current_time + random.randint(1000, 4000)
        if game_state == "wait_for_reaction":
            game_state = "wait"
            reaction_time = (current_time - start_time) / 1000
            start_time = current_time + random.randint(1000, 4000)
            count += 1

    if game_state == "wait":
        if current_time >= start_time:
            game_state = "wait_for_reaction"

    screen.fill(background)

    # Running the game
    if game_state == "start":
        # Draw the info text
        Text(size=50, text="Press any key to start", color=white, center=center)
    if game_state == "wait_for_reaction":
        # Prompt the user text
        Text(size=50, text="PRESS ANY KEY", color=red, center=center)

    # Draw the number of tries
    Text(size=30, text=("Number of tries: " + str(count)), color=white, center=(center[0], center[1]+100))
