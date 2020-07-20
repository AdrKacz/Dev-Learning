extends KinematicBody2D

export (int) var speed = 0
export (int) var rotation_speed = 5

var velocity = Vector2()
var target = Vector2()

var move_accuracy = 10

# Called when the node enters the scene tree for the first time.
func _ready():
	target = Vector2(450, 300)


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(_delta):
	velocity = (target - position).normalized() * speed
	if position.distance_squared_to(target) > move_accuracy:
		velocity = move_and_slide(velocity)
	else:
		target =  Vector2(randi() % 900 + 50, randi() % 500 + 50)
