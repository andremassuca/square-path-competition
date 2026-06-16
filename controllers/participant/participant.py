"""Sample Webots controller for the square path benchmark."""

from controller import Robot

# Get pointer to the robot.
robot = Robot()

# Get pointer to each wheel of our robot.
leftWheel = robot.getDevice('left wheel')
rightWheel = robot.getDevice('right wheel')
rightWheelSensor = robot.getPositionSensor('right wheel sensor')
rightWheelSensor.enable(16) # Refreshes the sensor every 16ms.

diametro_roda = 0.195
r = diametro_roda/2
lado_quadrado = 2
L = 0.33
#Calculo do angulo a ser percorrido pela roda na linha recta
angulo_linha_recta = 2*lado_quadrado/diametro_roda
#Calculo do angulo a ser percorrido pela roda na viragem
percurso_roda_viragem = 1/4*3.141592*(0.33/2)
angulo_viragem = 2*percurso_roda_viragem/r * 0.866
robot.step(16)
# Repeat the following 4 times (once for each side).
for i in range(0, 4):
    valor_inicial_roda_direita = rightWheelSensor.getValue()
    #print("Angulo inicial direita: %f"%valor_inicial_roda_direita)
    # First set both wheels to go forward, so the robot goes straight.
    leftWheel.setPosition(1000)
    rightWheel.setPosition(1000)
    
    # Malha fechada - trajetoria em linha recta
    valor_actual_roda_direita = rightWheelSensor.getValue()
    while valor_actual_roda_direita - valor_inicial_roda_direita <= angulo_linha_recta:
        valor_actual_roda_direita = rightWheelSensor.getValue()
        robot.step(16)
    # Virar a direita em malha fechada
    valor_inicial_roda_direita = rightWheelSensor.getValue()
    leftWheel.setPosition(1000)
    rightWheel.setPosition(-1000)
    valor_actual_roda_direita = rightWheelSensor.getValue()
    while abs(valor_actual_roda_direita - valor_inicial_roda_direita) <= angulo_viragem:
        valor_actual_roda_direita = rightWheelSensor.getValue()
        print(valor_actual_roda_direita - valor_inicial_roda_direita)
        print(angulo_viragem)
        robot.step(16)
   
# Stop the robot when path is completed, as the robot performance
# is only computed when the robot has stopped.
leftWheel.setVelocity(0)
rightWheel.setVelocity(0)
