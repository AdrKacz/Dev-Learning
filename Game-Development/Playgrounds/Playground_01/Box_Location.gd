extends Area2D
signal box_connected(location, color)
signal box_disconnected(location, color)

export (int, 0, 2) var location

# Positive > Has Connection , Zero OR Negative > No Connection
var connection_level = 0

# Called when the node enters the scene tree for the first time.
func _ready():
	connection_level = 0


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


func _on_Area2D_body_entered(body):
#	Change the appearance and emit signal
	connection_level += 1
	$Sprite.self_modulate = Color.purple
	emit_signal("box_connected", location, body.color)


func _on_Area2D_body_exited(body):
#	Change the appearance and emit signal
	connection_level -= 1
	if connection_level <= 0:
		$Sprite.self_modulate = Color.black	
	emit_signal("box_disconnected", location, body.color)
