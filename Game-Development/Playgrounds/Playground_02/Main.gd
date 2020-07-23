extends Node2D
signal BackgroundSignal()
signal SquareSignal()

# Declare member variables here. Examples:
# var a = 2
# var b = "text"

var streak = 0
var last_streak = 0
var score = 0

# Called when the node enters the scene tree for the first time.
func _ready():
	emit_signal("BackgroundSignal")
	emit_signal("SquareSignal")
	
	$Control/Score.text = str(score)
	$Control/Streak.text = str(streak)


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass

func _input(event):
	if event is InputEventScreenTouch and event.is_pressed():
		if $Square.color == $Background.color:
			right_touch()
		else:
			wrong_touch()

func right_touch():
	emit_signal("SquareSignal")
	score += streak + 1
	streak += 1
	last_streak = 5
	$Control/Score.text = str(score)
	$Control/Streak.text = str(streak)
	
func wrong_touch():
	lose_streak()

func lose_streak():
	streak = 0
	$Control/Score.text = str(score)
	$Control/Streak.text = str(streak)

func _on_StartTimer_timeout():
	$BackgroundTimer.start()


func _on_BackgroundTimer_timeout():
	if last_streak > 0:
		last_streak -= 1
		if last_streak == 0:
			lose_streak()
			
	if $Background.color == $Square.color:
		lose_streak()
		
	emit_signal("BackgroundSignal")
