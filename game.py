import pgzrun

WIDTH=870
HEIGHT=650
TITLE="trivia game"

marquee_box=Rect(0,0 ,880,80)
question_box=Rect(0,0 ,650,150)
answer_box1=Rect(0,0 ,300,150)
answer_box2=Rect(0,0 ,300,150)
answer_box3=Rect(0,0 ,300,150)
answer_box4=Rect(0,0 ,300,150)
timer_box=Rect(0,0 ,150,150)
skip_box=Rect(0,0 ,150,330)
score_box=Rect(0,0 ,150,50)

score=0
time_left=10
question_file_name="questions.txt"
marquee_msg=""
is_game_over=False

answer_boxes=[answer_box1,answer_box2,answer_box3,answer_box4]
questions=[]
question_count=0
question_index=0


marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)
timer_box.move_ip(700,100)
skip_box.move_ip(700,270)
score_box.move_ip(700,50)

def draw():
    global marquee_msg
    screen.clear()
    screen.fill(color="#2E6C9E")
    screen.draw.filled_rect(marquee_box,"#2E6C9E")
    screen.draw.filled_rect(question_box,"#F3B700")
    screen.draw.filled_rect(timer_box,"#DB5461")

def update():
    pass







pgzrun.go()


