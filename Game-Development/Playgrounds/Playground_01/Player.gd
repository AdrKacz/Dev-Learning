extends KinematicBody2D

export (int) var speed = 100
export (int) var rotation_speed = 5

export (int) var id

var velocity = Vector2()

var rotation_target
var rotation_accuracy = 0.01

func _ready():
	rotation_target = rotation

func get_input():
	velocity = Vector2()
	if Input.is_action_pressed('right_%s' % id):
		velocity.x += 1
	if Input.is_action_pressed('left_%s' % id):
		velocity.x -= 1
	if Input.is_action_pressed('down_%s' % id):
		velocity.y += 1
	if Input.is_action_pressed('up_%s' % id):
		velocity.y -= 1
	velocity = velocity.normalized() * speed
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	get_input()
	velocity = move_and_slide(velocity)
	
	if velocity.length_squared() > 0:
		rotation_target = velocity.angle()
		if abs(rotation - rotation_target) > rotation_accuracy:
			rotation = lerp_angle(rotation, rotation_target, rotation_speed*delta)
