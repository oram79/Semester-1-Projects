def start():
    # Setting MoboCop Perameters and moving from A to start of B
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    for count in range(2):
        chassis_ctrl.set_trans_speed(0.75)
        chassis_ctrl.move_with_distance(0,2.89)
    # Executing movements along the B route
    chassis_ctrl.set_rotate_speed(60)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    chassis_ctrl.move_with_distance(0,0.74)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,0.41)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90 )
    chassis_ctrl.move_with_distance(0,1.5)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    chassis_ctrl.move_with_distance(0,0.5)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    chassis_ctrl.move_with_distance(0,0.55)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 40)
    chassis_ctrl.move_with_distance(0,1.48)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,48)
    chassis_ctrl.move_with_distance(0,0.475)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,0.79)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    chassis_ctrl.move_with_distance(0,0.41)
    time.sleep(5)
    # End of point B to Entering room 227(Point C)
    chassis_ctrl.move_with_distance(0,3.285)
    chassis_ctrl.move_with_distance(0,3.285)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,2.12)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,2.12)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    time.sleep(5)
    # Leaving room 227
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,2.12)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    chassis_ctrl.move_with_distance(0,2.12)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    time.sleep(5)
    # Outside Room 227 starting towards reset point D
    chassis_ctrl.move_with_distance(0,2.62)
    chassis_ctrl.move_with_distance(0,2.62)
    time.sleep(5)
    # Point D, entering room 225 (Point E)
    chassis_ctrl.move_with_distance(0,2.55)
    chassis_ctrl.move_with_distance(0,2.55)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,2.58)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,1.63)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    chassis_ctrl.move_with_distance(0,4.49)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,1.20)
    time.sleep(3)
    # Leaving room 225
    chassis_ctrl.move_with_distance(180,1.20)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,4.52)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,1.63)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    chassis_ctrl.move_with_distance(0,2.55)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    time.sleep(3)
    # Point E to reset point F
    chassis_ctrl.move_with_distance(0,3.95)
    time.sleep(5)
    # Point F, entering room 224 (Point G)
    chassis_ctrl.move_with_distance(0,5.00)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
    chassis_ctrl.move_with_distance(0,0.70)
    time.sleep(5)
    # Backing out of posion room to point H
    chassis_ctrl.move_with_distance(180,0.70)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)
    chassis_ctrl.move_with_distance(0,2.635)
    chassis_ctrl.move_with_distance(0,2.635)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise,180)
    # Completly turned around headed from point H to D
    for count in range(4):
        chassis_ctrl.move_with_distance(0, 4.75)
    # Travelling from D to point A and lining up (Start Point)
    for count in range(5):
        chassis_ctrl.move_with_distance(0,4.07)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,180)

    


    








    








    

