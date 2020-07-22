extends Node2D


export (NodePath) var player_1_path
export (NodePath) var player_2_path



var player_1
var player_2

var height
var max_zoom

# Called when the node enters the scene tree for the first time.
func _ready():
	height = get_viewport_rect().size.y
	max_zoom = 2600 / height
	player_1 = get_node(player_1_path)
	player_2 = get_node(player_2_path)
	if player_1 and player_2:
		set_process(true)


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(_delta):
	position = (player_1.position + player_2.position) / 2
#	Minimum zoom needed to see the two players
	var dist = player_1.global_position.distance_to(player_2.global_position) + 264
	var min_zoom = dist / (height)
#	Zoom out
	var zoom = clamp(min_zoom, 1, max_zoom)
	$Camera2D.zoom = Vector2(zoom, zoom)
