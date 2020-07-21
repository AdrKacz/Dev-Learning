extends KinematicBody2D

export (int) var speed = 100
export (int) var rotation_speed = 5
export (int, 0, 200) var push = 5
export (int, 1, 5) var max_shooting_time = 1
export (int, 0, 10) var healing_time_out = 1

export (int) var id

var velocity = Vector2()
var look_goal = Vector2()
var is_shooting = false

var is_being_healed = false
var healed_timer = 0

var shooting_time_remaining = max_shooting_time

var is_dead = false

var hit_pos = null

var rotation_target
var rotation_accuracy = 0.01

func _ready():
	rotation_target = rotation
	is_dead = false
	is_shooting = false
	is_being_healed = false
	healed_timer = 0
	shooting_time_remaining = max_shooting_time

func get_input():
	velocity = Vector2()
	look_goal = Vector2()
	is_shooting = false
	
	# Do not check for Input if is dead
	if is_dead:
		return
	
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
	set_deferred("collision_layer", 0)
	set_deferred("collision_mask", 0)
	$Sprite.self_modulate = Color.gray
	is_dead = true
	healed_timer = 0
	
func reborn():
	set_deferred("collision_layer", 1)
	set_deferred("collision_mask", 1)
	$Sprite.self_modulate = Color.white
	is_dead = false
	healed_timer = 0
	
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
#	Updata Drawing
	update()
	
#	Get Input
	get_input()
	
#	Burn the shooting reserve
	if is_shooting:
		shooting_time_remaining -= delta
	else:
		shooting_time_remaining += delta
	
	if shooting_time_remaining <= 0:
		is_shooting = false
	
	shooting_time_remaining = clamp(shooting_time_remaining, 0, max_shooting_time)
	
#	RayCast Projection, stop on contact with anything.
	var collider = $RayCast2D.get_collider()
	if collider:
		hit_pos = $RayCast2D.get_collision_point()
		if collider.is_in_group("enemies") and is_shooting:
			collider.die()
	else:
		hit_pos = null
		
#	If is dead and is being healed, heal every frame.
	if is_dead and is_being_healed:
		healed_timer += delta
		if healed_timer >= healing_time_out:
			reborn()

func _physics_process(delta):
	
#	Move without the infinite inertia
	velocity = move_and_slide(velocity, Vector2(0,0), false, 4, PI/4, false)

#	Rotate
	if look_goal.length_squared() > 0:
		rotation_target = look_goal.angle()
	elif velocity.length_squared() > 0:
		rotation_target = velocity.angle()			
	if abs(rotation - rotation_target) > rotation_accuracy:
		rotation = lerp_angle(rotation, rotation_target, rotation_speed*delta)
		
	#	Handle Collision
	for i in get_slide_count():
		var collision = get_slide_collision(i)
#		If enemies, then the player die
		if collision.collider.is_in_group("enemies"):
			die()
#		If boxes, then jus push the box(es)
		elif collision.collider.is_in_group("boxes"):
			collision.collider.apply_central_impulse(-collision.normal * push)

func _draw():
#	Direction the player is looking at
	var direction = Vector2(1,0).normalized()
	
#	Draw circle for healing if is dead
	if is_dead:
		draw_circle(Vector2(), 64, Color(0,1,1 if is_being_healed else 0, 0.5))
	else:
		#	Else, if the RayCast hits something, draw a circle on hit, else, just draw a line
		if hit_pos:
			draw_line(Vector2(), (hit_pos - position).rotated(-rotation), Color(1, 0, 0, 1.0 if is_shooting else 0.25))
			draw_circle((hit_pos - position).rotated(-rotation), 5, Color(1, 0, 0, 1.0 if is_shooting else 0.1))
		else:
			draw_line(Vector2(), direction * 1200, Color(1, 0, 0, 1.0 if is_shooting else 0.25))


func _on_Area2D_body_entered(_body):
	if is_dead:
		is_being_healed = true


func _on_Area2D_body_exited(_body):
	is_being_healed = false
