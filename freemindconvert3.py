from array import *
last_position = 0
x = 0
y = 0
initlist = list()
last_position = 0
first_run_flag = 0
position = -1
global num


def init_array():
        global req_array
        req_array = [[0 for x in range(20)] for x in range(400)]

def get_title_and_note(num, pos, position):
	global last_position
	global first_run_flag
	global x
	global y
	#global position


	## GET THE TITLE
    	splitline = initlist[num].split('"')
      	branchtitle = splitline[pos]
      	#print "TITLE IS " + branchtitle
      	## CHECK TO SEE IF THERE ARE ANY NOES

      	if "NOTE" in initlist[num + 1]:
        	## THEN FIND <p>
            	num = num + 1
              	search_num = num

            	for search_num in range(num, num + 20):
             		num = search_num
                     	#print "Req Search Line = " + str(num)
			if "<p>" in initlist[num]:
                  		requirement  = initlist[num + 1]
			elif "</p>" in initlist[num]:
				#print "BREAKOUT"
				break 
		requirement = requirement.replace("\n", "")
		print "The title is " + branchtitle + " and the req is " + requirement + " at position " + str(position)
		
        else:
                print "The title is " + branchtitle + " and there is NO req at position " + str(position)
		requirement = 0
	
	position = position
	if first_run_flag == 0:
		
                position_title = position * 2
                position_note = position_title + 1


		req_array[x][position_title] = branchtitle
		if requirement == 0:
			req_array[x][position_note] = "No notes or requirement"
		else:
		
                        req_array[x][position_note] = requirement
		first_run_flag = 1
	elif (last_position < position):
		position_title = position * 2
		position_note = position_title + 1
		#y = y + 1
                req_array[x][position_title] = branchtitle
                if requirement == 0:
    
                        req_array[x][position_note] = "No notes or requirement"
                else:
                  
                        req_array[x][position_note] = requirement  
	elif (last_position == position): 
		x = x + 1
              	position_title = position * 2
                position_note = position_title + 1
		 #      y = y - 1
                req_array[x][position_title] = branchtitle
                if requirement == 0:
                       
                        req_array[x][position_note] = "No notes or requirement"
                else:
#                        y = y + 1
                        req_array[x][position_note] = requirement 

        elif (last_position > position):
         #        x = x + 1
          #      y = y  
                x = x + 1
                position_title = position * 2
                position_note = position_title + 1  

                req_array[x][position_title] = branchtitle
                if requirement == 0:
                        req_array[x][position_note] = "No notes or requirement"
                else:
                       
                        req_array[x][position_note] = requirement



		
	print "X = " + str(x) + "Y = " + str(y)

	last_position = position

	#print "Ending number = " + str(num)
	return position

### OPEN THE FREEMIND FILE
file = open('THISISTHEBEGINNING.mm', 'r')

### INIT ARRAY
init_array()

## LOAD THE FILE INTO AN ARRAT initlist
for line in file:
        initlist.append(line)

## GET SIZE OF LIST,  WILL BE USED TO SIZE Multi Array
size_of_list =  len(initlist)


## IGNORE THE MAIN BUBBLE OF THE MIND MAP
## START TRAVERSING THE LIST

for num in range(3,size_of_list):
	#print initlist[num, pos]
	print num
	#print "->" + str(num)
	if "POSITION" in initlist[num]:
		pos = 9
		position = position + 1

		position = get_title_and_note(num, pos, position)
	
		# DO AN ELSE FOR NO NOTE
	elif "TEXT" in initlist[num]:
		
		position = position + 1
		pos = 7
		if "/>" in initlist[num]:
			position = position 
	#		print "No child position = " + str(position)
			position = get_title_and_note(num, pos, position)
			position = position  - 1
		else:	
	        #        position = position + 1
			position = get_title_and_note(num, pos, position)	
	elif "</node>" in initlist[num]:
		position = position -1



				#break
	#elif "TEXT" in initlist[num]:
#print initli


print req_array		#position = position - 1



#file = open("file_output.txt", "w")


with open('myfile.csv','w') as f:
    for sublist in req_array:
        for item in sublist:
	    if item == 0:
		item = ""	
            f.write(str(item) + ',')
        f.write('\n')





