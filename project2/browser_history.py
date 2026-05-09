
def visit_page(page):
    global current_page 
    if current_page is not None:
        back_stack.append(current_page)
    forward_stack.clear()
    current_page = page
    
def go_back():
    global current_page
    if not back_stack:
        print("Cannot go back")
    else: 
        popped_page = back_stack.pop()
        forward_stack.append(current_page)
        current_page = popped_page

def go_forward():
    global current_page
    if not forward_stack:
        print("Cannot go forward")
    else: 
        back_stack.append(current_page)
        current_page = forward_stack.pop()

def show_state():
    print("History:", back_stack)
    print("Current Page:", current_page)
    print("Next Page:", forward_stack)

back_stack = []
current_page = "google.com"
forward_stack = []

visit_page("github.com")
visit_page("youtube.com")
visit_page("reddit.com")

go_back()

go_forward()

go_back()

visit_page("shein.com")
visit_page("argos.com")
visit_page("asda.com")
visit_page("nike.com")

go_back()
go_back()

show_state()


