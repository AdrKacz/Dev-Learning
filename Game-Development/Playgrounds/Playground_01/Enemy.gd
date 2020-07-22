extends KinematicBody2D

export (int) var speed = 50
export (int) var rotation_speed = 5
export (int, 0, 10) var push = 3

var velocity = Vector2()
var target = Vector2()
var rotation_target = 0

var move_accuracy = 64
var rotation_accuracy = 0.01

var first_moves = 100

# Called when the node enters the scene tree for the first time.
func _ready():
	target = Vector2(- 500 + randi() % 1000, - 500 + randi() % 1000)
	rotation_target = 0

func activate_collision():
	$CollisionShape2D.set_deferred("disabled", false)
	$Area2D/CollisionShape2D.set_deferred("disabled", false)
	
	
func die():
#	Destroy the element
#	Can have a "little" animation
	$CollisionShape2D.set_deferred("disabled", true)
	$Area2D/CollisionShape2D.set_deferred("disabled", true)
	
	hide()
	queue_free()
	
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(_delta):
#	If it reach the target, find a new one, near the past one
	if global_position.distance_squared_to(target) < move_accuracy:
		target =  Vector2(- 1000 + randi() % 2000, - 1000 + randi() % 2000)
		
func _physics_process(delta):
#	Activate collision
	if first_moves > 0:
		first_moves -= 1
	if first_moves <= 0:
		activate_collision()
#	Get the direction
	velocity = (target - global_position).normalized() * speed
#	Move without infintie_inertia
	velocity = move_and_slide(velocity, Vector2(0,0), false, 4, PI/4, false)
		
#	Look forward
	rotation_target = velocity.angle()
#	Rotate
	if abs(global_rotation - rotation_target) > rotation_accuracy:
		global_rotation = lerp_angle(global_rotation, rotation_target, rotation_speed*delta)
	
	#	Handle Collision
	for i in get_slide_count():
		var collision = get_slide_collision(i)
#		If boxes, then jus push the box(es)
		if collision.collider.is_in_group("boxes"):
			collision.collider.apply_central_impulse(-collision.normal * push)
