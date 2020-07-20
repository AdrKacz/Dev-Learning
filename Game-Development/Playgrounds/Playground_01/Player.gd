extends KinematicBody2D

export (int) var speed = 100
export (int) var rotation_speed = 5

export (int) var id

var velocity = Vector2()
var look_goal = Vector2()
var is_shooting = false

var is_dead = false

var hit_pos = null

var rotation_target
var rotation_accuracy = 0.01

func _ready():
	rotation_target = rotation
	is_dead = false
	is_shooting = false

func get_input():
	velocity = Vector2()
	look_goal = Vector2()
	is_shooting = false
	
	if Input.is_action_pressed('right_%s' % id):
		velocity.x += 1
	if Input.is_action_pressed('left_%s' % id):
		velocity.x -= 1
	if Input.is_action_pressed('down_%s' % id):
		velocity.y += 1
	if Input.is_action_pressed('up_%s' % id):
		velocity.y -= 1
		
	velocity = velocity.normalized() * speed
		
	if Input.is_action_pressed('look_right_%s' % id):
		look_goal.x += 1
	if Input.is_action_pressed('look_left_%s' % id):
		look_goal.x -= 1
	if Input.is_action_pressed('look_down_%s' % id):
		look_goal.y += 1
	if Input.is_action_pressed('look_up_%s' % id):
		look_goal.y -= 1
		
	if Input.is_action_pressed('shoot_%s' % id):
		is_shooting = true

	
func die():
	$CollisionShape2D.disabled = true
	$Sprite.self_modulate = Color.gray
	is_dead = true
	
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	update()
	
	if is_dead:
		return
	get_input()
	velocity = move_and_slide(velocity)

	if look_goal.length_squared() > 0:
		rotation_target = look_goal.angle()
	elif velocity.length_squared() > 0:
		rotation_target = velocity.angle()		
		
	if abs(rotation - rotation_target) > rotation_accuracy:
		rotation = lerp_angle(rotation, rotation_target, rotation_speed*delta)
		
	for i in get_slide_count():
		var collision = get_slide_collision(i)
		if collision.collider.is_in_group("enemies"):
			die()
	
	var collider = $RayCast2D.get_collider()
	if collider:
		hit_pos = $RayCast2D.get_collision_point()
	else:
		hit_pos = null
	

func _draw():
	var direction = Vector2(1,0).normalized()
	if hit_pos:
		draw_line(Vector2(), (hit_pos - position).rotated(-rotation), Color(1, 0, 0, 1 if is_shooting else 0.25))
		draw_circle((hit_pos - position).rotated(-rotation), 5, Color(1, 0, 0, 1 if is_shooting else 0.1))
	else:
		draw_line(Vector2(), direction * 1200, Color(1, 0, 0, 1 if is_shooting else 0.25))
