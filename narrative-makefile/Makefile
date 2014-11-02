# narrative-makefile

live-happily-ever-after.goal: introduce-protagonist.goal rescue-damsel.goal
	@touch $@
	@echo "And they lived happily ever after."

introduce-protagonist.goal:
	@touch $@
	@echo "Once upon a time there was a brave knight."

learn-of-damsel.goal:
	@touch $@
	@echo "And one day a troubador brought news of a damsel in distress."

rescue-damsel.goal: learn-of-damsel.goal slay-dragon.goal
	@touch $@
	@echo "And the brave knight rescued the damsel from the dragon's lair."

enter-forest.goal:
	@touch $@
	@echo "So the brave knight entered the Great Forest."

find-griffon.goal: enter-forest.goal
	@touch $@
	@echo "And there the knight found a fearsome griffon."

quested-with-fleece.goal: find-griffon.goal
	@touch $@
	@echo "'I have what you seek but you must fetch for me the golden fleece.'"

locate-fleece.goal:
	@touch $@
	@echo "So the knight travelled far and wide until he found the golden fleece."

fetch-golden-fleece.goal: quested-with-fleece.goal locate-fleece.goal
	@touch $@
	@echo "And the knight returned with the golden fleece."

appease-griffon.goal: find-griffon.goal fetch-golden-fleece.goal
	@touch $@
	@echo "'Very good, brave knight,' said the griffon, and flew off, leaving behind a magic sword."

acquire-sword.goal: appease-griffon.goal
	@touch $@
	@echo "So the brave knight made off with the enchanted blade."

slay-dragon.goal: acquire-sword.goal
	@touch $@
	@echo "And the brave knight slew the dragon with his sword."

clean:
	rm -f *.goal
