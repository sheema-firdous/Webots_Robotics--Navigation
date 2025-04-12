"""help controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
import math

# This is written as a function for convenience
def get_yaw():
    v = iu.getRollPitchYaw()
    yaw = round(math.degrees(v[2]))
    # The InertialUnit gives us a reading based on how the robot is oriented with
    # respect to the X axis of the world: EAST 0°, NORTH 90°, WEST 180°, SOUTH -90°.
    # This operation converts these values to a normal, positive circumfrence.
    if yaw < 0:
        yaw += 360
    return yaw

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

MAX_SPEED = 6.28
# Thresholds: maximum allowed error
angle_treshold = 1
distance_threshold = 0.002
# OBJECTIVES
degrees = 90  # Desired amount of rotation
distance = 0.2  # Desired amount of linear translation

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Sensors

iu = robot.getDevice('inertial unit')
iu.enable(timestep)
gps = robot.getDevice('gps')
gps.enable(timestep)

# Some devices, such as the InertialUnit, need some time to "warm up"
robot.step(1000)

# Actuators

leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)

# Calculate the parameters of the simulation

print("Turning {0} degrees".format(degrees))
starting_yaw = get_yaw()
print("Start: " + str(starting_yaw))
target = (starting_yaw - degrees) % 360
print("Target: " + str(target))

# Calculate the desired ending coordinate
destination_coordinate = [
    distance * math.cos(math.radians(target)),
    distance * math.sin(math.radians(target))
]

print("Final coordinate: {0}".format(destination_coordinate))

# Start executing
# Start executing
while robot.step(timestep) != -1:
    # First rotate
    current_yaw = get_yaw()
    if abs(target - current_yaw) > angle_treshold:
        leftSpeed = 0.3 * MAX_SPEED
        rightSpeed = -0.3 * MAX_SPEED
    else:
        # When rotation is complete, go straight
        current_coordinate = gps.getValues()
        distance_to_target_x = abs(current_coordinate[0] - destination_coordinate[0])
        distance_to_target_y = abs(current_coordinate[1] - destination_coordinate[1])
        
        if distance_to_target_x < distance_threshold and distance_to_target_y < distance_threshold:
            leftSpeed = 0
            rightSpeed = 0
            leftMotor.setVelocity(leftSpeed)
            rightMotor.setVelocity(rightSpeed)
            print(f"Goal reached. Final position: {current_coordinate}")
            break  # ✅ Exit the loop (and stop program)
        else:
            leftSpeed = 0.3 * MAX_SPEED
            rightSpeed = 0.3 * MAX_SPEED

    print(f"Current position: {gps.getValues()}")
    leftMotor.setVelocity(leftSpeed)
    rightMotor.setVelocity(rightSpeed)
