from lib.math.vector_2d import Vector2D
from lib.player.action_effector import ActionEffector
from lib.player.messenger.ball_pos_vel_messenger import BallPosVelMessenger
from lib.player.messenger.messenger import Messenger
from lib.player.object_player import PlayerObject
from lib.player.object_ball import BallObject
from lib.player.world_model import WorldModel
from lib.player.messenger.player_pos_unum_messenger import PlayerPosUnumMessenger
from lib.rcsc.game_time import GameTime
from lib.rcsc.types import SideID

def test():
    wm_sender = WorldModel()
    wm_reciever = WorldModel()
    
    wm_sender._our_side = 'l'
    wm_reciever._our_side = 'l'
    
    player= PlayerObject()
    player._pos = Vector2D(10,20)
    player._unum = 5
    player._side = SideID.LEFT
    
    player2= PlayerObject()
    player2._pos = Vector2D(1,2)
    player2._unum = 5
    player2._side = SideID.LEFT
    player2._pos_count = 20
    player2._seen_pos_count = 20

    wm_sender._our_players_array[5] = player
    wm_sender._teammates.append(player)
    wm_reciever._teammates.append(player2)

    ball = BallObject()
    ball._pos = Vector2D(3, 4)
    ball._vel = Vector2D(2, -2)

    wm_sender._ball = ball

    ball2 = BallObject()
    ball2._pos = Vector2D(0, 0)
    ball2._vel = Vector2D(0, 0)

    ball2._pos_count = 10
    ball2._vel_count = 10

    wm_reciever._ball = ball2
    
    wm_sender._time = GameTime(10, 0)    
    wm_reciever._time = GameTime(10, 0)    
    wm_reciever._messenger_memory._time = GameTime(10)
    wm_reciever._messenger_memory._ball_time = GameTime(10)
    wm_reciever._messenger_memory._player_time = GameTime(10)
    
    print(wm_sender._teammates)
    print(wm_reciever._teammates)
    print(wm_sender._ball)
    print(wm_reciever._ball)
    
    
    
    msg = Messenger.encode_all(wm_sender, [PlayerPosUnumMessenger(5), BallPosVelMessenger()])
    print(msg)
    
    Messenger.decode_all(wm_reciever._messenger_memory, msg, 4, wm_reciever.time())
    wm_reciever.update_ball_by_haer(ActionEffector())
    wm_reciever.update_players_by_hear()
    
    print(wm_sender._teammates)
    print(wm_reciever._teammates)
    print(wm_sender._ball)
    print(wm_reciever._ball)

    
if __name__ == "__main__":
    test()