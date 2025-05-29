'''

references: https://stackoverflow.com/questions/47403273/how-do-i-print-a-list-vertically-side-by-side
            https://learnpython.com/blog/reverse-range-in-python/
            https://en.wikipedia.org/wiki/ANSI_escape_code#3-bit_and_4-bit
            https://tldp.org/HOWTO/Bash-Prompt-HOWTO/x361.html

'''
'''
Remaining To-dos:
- Add certain error conditions
- Make more comments
'''
import os
from bstack import BondedStack
from bqueue import BondedQueue



os.system("")

def openFile(fileName):
    with open(fileName, 'r') as file1:
        file_contents = file1.read().splitlines()
    
    return file_contents

def getSource(flasks):
    '''
    Gets the index of the source flask
    
    '''
    num_flasks = len(flasks)
    try:
        source_flask = int(input())
    except:
        raise TypeError('Number must be an integer. Try Again') 

    if source_flask <= 0 or source_flask > num_flasks:
            raise ValueError('Flask number out of bounds. Try Again')  
    else:
        return source_flask-1

def getDestination(flasks):
    num_flasks = len(flasks)
    try:
        destination_flask = int(input())
    except:
        raise TypeError('Number must be an integer. Try again.')

    if destination_flask <= 0 or destination_flask > num_flasks:
            raise ValueError('Flask number out of bounds. Try Again.')
    else:    
        return destination_flask-1
def move_cursor(x, y):
    '''
    Moves the cursor to the specified location on the terminal.
    Input:
        - x (int): row number
        - y (int): column number
    Returns: N/A
    '''
    print("\033[{1};{0}H".format(x, y), end='')

def clear_screen():
    if os.name == "nt":
        os.sysetem("cls")
    else:
        os.system("clear")


def print_prompt(what_flask):
    print(f"\033[sSelect {what_flask} flask: ", end='', flush=True)


def putColor(text):
    str(text)
    chemicals = ['AA','BB','CC','DD','EE','FF']
    for i in range(len(chemicals)):
        if text == chemicals[i]:
            if i == 0:
                return "\033[48;5;9m{}\033[0m".format(text) 
            elif i == 1:
                return "\033[48;5;12m{}\033[0m".format(text)
            elif i == 2:
                return "\033[48;5;34m{}\033[0m".format(text)
            elif i == 3:
                return "\033[48;5;208m{}\033[0m".format(text)
            elif i == 4:
                return "\033[48;5;11m{}\033[0m".format(text)
            elif i == 5:
                return "\033[105;31;214;112;214m{}\033[0m".format(text)



def makeBorder(flask_stacks, num_flasks, source=0,destination=0):
    num_flask = len(flask_stacks)
    flask_label = num_flasks
    if num_flask > 4:
        group1 = flask_stacks[0:4]
        group2 = flask_stacks[4:]
        makeBorder(group1,1)
        print()
        makeBorder(group2,5)
    else:
        
        for i in reversed(range(len(flask_stacks))):
            for j in range(len(flask_stacks)):
                try:               
                    print(f"{'|'}{putColor(flask_stacks[j].peek_index(i))}{'|'}",end=' ' )
                except:
                    if isComplete(flask_stacks[j]):
                        print('+--+', end=' ')
                    else:
                        print(f"{'|'}{'  '}{'|'}", end=' ')
            print()
            if i == 0:
                print(f"{'+--+ '*len(flask_stacks)}") 
                for z in range(4):
                    label_color = '\033[91m' if flask_label == source else '\033[94m'
                    if flask_label == source:
                        print(label_color+f"{flask_label:^5}"+'\033[0m',end="")
                    elif flask_label == destination:
                        print(label_color+f"{flask_label:^5}"+'\033[0m',end="")
                    else:
                        print(f" {flask_label:^4}", end="")
                    flask_label += 1
    print()


def isFlaskEmpty(flask_stack):
    return flask_stack.size() == 0


def isFlaskFull(flask_stack):
    return flask_stack.size() == 4 
       
def clear_lines(where_from, to):
    for i in range(where_from, to+1):
        move_cursor(0,i)
        print("\033[K")


def isComplete(flask_stack):
    chemical_checked = []
    
    if flask_stack.size() == 3:
        for i in range(3):
            current = flask_stack.peek_index(i)
            if current not in chemical_checked:
                chemical_checked.append(current)
    
        
    return len(chemical_checked) == 1
        

def transfer(source_flask, destination_flask):
    if isFlaskFull(destination_flask) or isComplete(destination_flask):
        raise ValueError('Cannot pour onto a full flask. Try Again')
    elif source_flask == destination_flask:
        raise Exception('Cannot pour into the same flask. Try Again.')
    else:
        chemical = source_flask.pop()
        destination_flask.push(chemical)
    
def prompts(what_flask):
    return f"Select {what_flask} flask: "


def reset(prompt_loc_x,prompt_loc_y,arguement):
    move_cursor(prompt_loc_x,prompt_loc_y)
    print("\033[K")
    move_cursor(0,5)
    print(arguement)

def main():
    
    file1 = openFile('8f6c.txt')
    info= (file1[0])
    num_flask = int(info[0])
    chemical_count = int(info[2])

    CHEM_QUANTITY = chemical_count

    instruction = file1[1:]

    flasks = []
    chemicals = []

    for i in range(num_flask):
        x = BondedStack()
        flasks.append(x)

    for contents in instruction:
        if len(contents) == 2:
            chemicals.append(contents)


    chemicals_queue = BondedQueue(4)
    # Sorting Initial Queue
    for content in instruction:
        if content in chemicals:
            if not chemicals_queue.isFull():
                chemicals_queue.enqueue(content)
        else: # Transfering to Stated Stack
            dequeue_amount = int(content[0])
            flask_num = int(content[len(content)-1])

            for i in range(dequeue_amount):
                a = chemicals_queue.dequeue()
                flasks[flask_num-1].push(a)


    # Game initiation
    gameOver = False
    num_completed = 0
    while not gameOver:
        clear_screen()
        print('Game')
        print()
        
        
        source_valid = False
        destination_valid = False
        while not source_valid and not destination_valid:
            move_cursor(0,6)
            makeBorder(flasks,1,0,0)
            move_cursor(0,3)
            s_prompt = prompts('source')
            d_prompt = prompts('destination')

                
            print(s_prompt,end="")
            move_cursor(0,4)
            print(d_prompt)
            while not source_valid:
                try:
                    move_cursor(len(s_prompt),3)
                    source_flask = getSource(flasks)
                    clear_lines(5,5)
                    if isFlaskEmpty(flasks[source_flask]):
                        raise Exception
                    source_valid = True
                    move_cursor(0,6)
                    makeBorder(flasks,1,source_flask+1,0)
                except TypeError as arg:
                    reset(len(s_prompt),3,arg)
                except ValueError as arg:
                    reset(len(s_prompt),3,arg)
                except Exception as arg:
                    reset(len(s_prompt),3,'Cannot take from an empty flask. Try Again')
                

            


            move_cursor(len(d_prompt),4)
            while not destination_valid:
                try:
                    move_cursor(len(d_prompt),4)
                    destination_flask = getDestination(flasks)
                    clear_lines(5,5)
                    try:
                        transfer(flasks[source_flask],flasks[destination_flask])
                        destination_valid = True
                    except ValueError as arg:
                        reset(len(d_prompt),4,arg)
                    except Exception as arg:
                        reset(len(d_prompt),4,arg)
                    move_cursor(0,6)
                    makeBorder(flasks,source_flask+1,destination_flask+1)
                except TypeError as arg:
                    reset(len(d_prompt),4,arg)
                except ValueError as arg:
                    reset(len(d_prompt),4,arg)
        
        for containers in flasks:
            if isComplete(containers):
                num_completed += 1

        if num_completed == CHEM_QUANTITY:
            gameOver = True

        num_completed = 0
    
    clear_screen()
    print('Congratulations!')
    makeBorder(flasks, 1)
  
   
    
main()