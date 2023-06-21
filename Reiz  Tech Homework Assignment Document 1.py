def angleCalculator():
    hours = int(input('Please input the current hour: '))
    minutes = int(input ('\nPlease input the current minutes: ')) 
    hourAngle = 0
    minAngle = minutes*6

#considering military time inputs
    if hours>12:
        hourAngle = (hours-12) * 30
    else:
        hourAngle = hours * 30
    print (f'The Hour Hand is at {hourAngle} degrees. \nThe Minute Hand is at {minAngle} degrees. ')

#LesserAngleCalc
    result = hourAngle-minAngle
    if result < 1: #for negative differences 
        result = result * -1 
    if result > 180: #for accuracy on always getting the lower angle
        result = 360 - result  
    print (f'The lesser angle is {result} degrees.')

   
angleCalculator()