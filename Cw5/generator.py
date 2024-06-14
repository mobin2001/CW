def my_range(start, stop, step):
    if not isinstance(start,int) or not isinstance(stop,int) or not isinstance(step,int):
        raise ValueError("start parameter must be an integer!")
 
    if step ==-0:
        raise ValueError("step parameter cannot be zero!")
    if start+step > stop :
        raise ValueError("invalid range, step prevents sequence from reaching stop value")
    for x in range (start,stop+1,step):
        yield x


r=list(my_range(11,30,1))
print(r)

        
