extends Node2D

export (NodePath) var player_1_path
export (NodePath) var player_2_path

var player_1
var player_2

var height

# Called when the node enters the scene tree for the first time.
func _ready():
	height = get_viewport_rect().size.y
	player_1 = get_node(player_1_path)
	player_2 = get_node(player_2_path)
	if player_1 and player_2:
		set_process(true)


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(_delta):
#	Position of the center of the two player
	var target = (player_1.global_position + player_2.global_position) * .5
#	Minimum zoom needed to see the two players
	var dist = 64 + player_1.global_position.distance_to(player_2.global_position)
	var min_zoom = dist / (.5 * height)
#	Move the camera
	global_position = target
	var zoom = max(min_zoom, 1)
	$Camera2D.zoom = Vector2(zoom, zoom)
