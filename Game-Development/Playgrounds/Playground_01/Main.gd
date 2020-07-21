extends Node

signal has_checked(succeed, black, white)

export (PackedScene) var Box
export (PackedScene) var Enemy

export (int, 15, 100) var initial_number_of_boxes = 10

var combination = [-1, -1, -1]
var	colors_number = [0, 0, 0, 0, 0]


# Every item is a pile, the last one of each is the current chosen color
var user_combination = [[], [], []]

# Called when the node enters the scene tree for the first time.
func _ready():
#	Create the boxes
	for i in range(initial_number_of_boxes):
		var box = Box.instance()
		add_child(box)
		if i < 15:
			box.set_color(i / 3)
		else:	
			box.set_color(randi() % 5)
		var x = -1000 + randi() % (2000 - 400)
		var y = -1000 + randi() % (2000 - 400)
		if x > -200:
			x += 400
		if y > -200:
			y += 400
		box.global_position = Vector2(x, y)
		
#	Create the magic combinaison
	combination[0] = randi() % 5
	combination[1] = randi() % 5
	combination[2] = randi() % 5
	
#	Check the number of color of the combination
	colors_number = [0, 0, 0, 0, 0]
	for i in range(3):
		colors_number[combination[i]] += 1


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass

func check_combination():
	var is_all_set = true
		
	var succeed = false
	var black = 0
	var white = 0

#	Check the number of color of the user
	var user_colors_number = [0, 0, 0, 0, 0]
	for i in range(3):
		if user_combination[i].size() > 0:
			user_colors_number[user_combination[i][-1]] += 1
		else:
			is_all_set = false
#			At least one location is empty
			return
	
#	White loop (check number of color in each combination)
	for i in range(5):
		white += int(clamp(user_colors_number[i], 0, colors_number[i]))

#	Black loop (decrease white when increasing black)
	for i in range(3):
#		Here, we are sure all the location are set
		if user_combination[i][-1] == combination[i]:
			black += 1
			white -= 1
			
	if black == 3:
		succeed = true
		
	print(user_combination)
	print(combination)
	print("Has Checked with ", succeed, " Black:", black, ", White:", white)
	emit_signal("has_checked", succeed, black, white)

func _on_box_connected(location, color):
	print("Connection of ", location, " with color ", color)
	user_combination[location].append(color)
	
	check_combination()


func _on_box_disconnected(location, color):
	print("Disconnection of ", location, " with color ", color)
	user_combination[location].erase(color)
	check_combination()
