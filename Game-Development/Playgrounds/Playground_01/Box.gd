extends RigidBody2D

export (int, 1, 10) var friction_factor = 10

export (int, 0, 4) var color

# Called when the node enters the scene tree for the first time.
#func _ready():
#	pass

func set_color(new_color):
	color = new_color
	match color:
		0:
			$Sprite.self_modulate = Color.blue
		1:
			$Sprite.self_modulate = Color.red
		2:
			$Sprite.self_modulate = Color.green
		3:
			$Sprite.self_modulate = Color.yellow
		4:
			$Sprite.self_modulate = Color.darkorange
		_:
			print("Error with the color code")
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _physics_process(delta):
#	Apply dynamic friction
	apply_central_impulse(-linear_velocity*delta*friction_factor)
