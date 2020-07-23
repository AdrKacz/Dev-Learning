extends Area2D

var color
# Called when the node enters the scene tree for the first time.
func _ready():
	color = -1


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


func change_color():
	var new_color = randi() % 3
	if new_color >= color:
		new_color += 1
		
	$AnimatedSprite.frame = new_color
	color = new_color


func _on_Main_SquareSignal():
	change_color()
