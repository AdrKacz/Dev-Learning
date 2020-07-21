extends KinematicBody2D

export (int) var speed = 150
export (int) var rotation_speed = 5

var velocity = Vector2()
var target = Vector2()
var rotation_target = 0

var move_accuracy = 10
var rotation_accuracy = 0.1

# Called when the node enters the scene tree for the first time.
func _ready():
	target = Vector2(450, 300)
	rotation_target = 0

func die():
#	Destroy the element
#	Can have a "little" animation
	$CollisionShape2D.set_deferred("disabled", true)
	$Area2D/CollisionShape2D.set_deferred("disabled", true)
	
	hide()
	queue_free()

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	velocity = (target - position).normalized() * speed
	rotation_target = velocity.angle()
	if abs(rotation - rotation_target) > rotation_accuracy:
		rotation = lerp_angle(rotation, rotation_target, rotation_speed*delta)
	if position.distance_squared_to(target) > move_accuracy:
#		Move and rotate
		velocity = move_and_slide(velocity)
	else:
		target =  Vector2(randi() % 900 + 50, randi() % 500 + 50)
		
