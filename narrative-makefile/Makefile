# narrative-makefile

live-happily-ever-after.goal: introduce-protagonist.goal rescue-damsel.goal
	@touch $@
	@echo "And they lived happily ever after."

introduce-protagonist.goal:
	@touch $@
	@echo "Once upon a time there was a brave knight."

rescue-damsel.goal: slay-dragon.goal
	@touch $@
	@echo "And the brave knight rescued the damsel from the dragon's lair."

slay-dragon.goal: 
	@touch $@
	@echo "And the brave knight slew the dragon with his sword."

clean:
	rm -f *.goal
