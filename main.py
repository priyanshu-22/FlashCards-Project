
from datetime import datetime
from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy


app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database1.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class User(db.Model):
    __tablename__="User"
    user_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String,unique=True,nullable=False)
    password=db.Column(db.String,nullable=False)
   
class Decks(db.Model):
    __tablename__="Decks"
    deck_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    deckname=db.Column(db.String,nullable=False,unique=True)
    description=db.Column(db.String)
    latest_time=db.Column(db.DateTime,default=datetime.now())
    latest_score=db.Column(db.Integer)
    total_score=db.Column(db.Integer,default=0)
    udeck_id=db.Column(db.Integer,db.ForeignKey('User.user_id'),nullable=False)
    no_of_submits=db.Column(db.Integer)
    
class Cards(db.Model):
    __tablename__="Cards"
    card_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    dcard_id=db.Column(db.Integer,db.ForeignKey('Decks.deck_id'),nullable=False)
    ques=db.Column(db.String,nullable=False)
    ans=db.Column(db.String,nullable=False)
  
@app.route("/")
def home():
    return render_template("DISPLAY PAGE.html")


@app.route("/<int:user_id>/user",methods=['GET','POST'])
def user(user_id):
    u1=user_id

    u=db.session.query(User).filter_by(user_id=u1).first()
    if request.method=="POST":
        username=request.form.get('name')
        password=request.form.get('pass')
        u.username=username
        u.password=password      
        db.session.commit()
        
        return redirect(url_for("dash",user_id=u.user_id))
    return render_template("user.html",u=u)

@app.route("/<int:user_id>/dashboard")
def dash(user_id):
    u1=user_id
    u=db.session.query(User).filter_by(user_id=u1).first()
    de=db.session.query(Decks).filter_by(udeck_id=u.user_id)
    return render_template("dashboard_Sample.html",de=de,u=u)






@app.route("/<int:user_id>/<int:deck_id>/deck_dashboard")
def deck_dash(user_id,deck_id):
    u=db.session.query(User).filter_by(user_id=user_id).first()
    de=db.session.query(Decks).filter_by(deck_id=deck_id).first()
    ce=db.session.query(Cards).filter_by(dcard_id=deck_id)
    ce1=db.session.query(Cards).filter_by(dcard_id=deck_id).first()
    return render_template("deck_dashboard_sample.html",de=de,u=u,ce=ce,ce1=ce1)


@app.route("/login_user",methods=['GET','POST'])
def login_user():
    if request.method=="POST":
        u1=request.form['Uname']
        p1=request.form['Pass']
        u=db.session.query(User).filter_by(username=u1).first() 
        print(u)
        return redirect(url_for("dash",user_id=u.user_id))
    return render_template("login_page.html")


@app.route("/new_user",methods=['GET','POST'])
def new_user():
    if request.method=="POST":
        u2=request.form['Uname']
        p2=request.form['Pass']
        u1=User(username=u2,password=p2)
        db.session.add(u1)
        db.session.commit()
        u=db.session.query(User).filter_by(username=u2).first()

        return redirect(url_for("dash",user_id=u.user_id))
    return render_template("New_User.html")


@app.route("/<int:user_id>/add_deck",methods=['GET','POST'])
def add_deck(user_id):
    u1=user_id
    u=db.session.query(User).filter_by(user_id=u1).first()
    de=db.session.query(Decks).filter_by(udeck_id=u.user_id)
    if request.method=="POST":
        d_name=request.form['deck_name']
        desc=request.form['descr']
        d=Decks(deckname=d_name,description=desc,udeck_id=u1,latest_score=0,total_score=0,no_of_submits=0)
        db.session.add(d)
        db.session.commit()
        return redirect(url_for("dash",user_id=u.user_id))
    return render_template("add_deck.html",de=de,u=u)


@app.route("/<int:user_id>/<int:deck_id>/update_deck",methods=['GET','POST'])
def update_deck(user_id,deck_id):
    u1=user_id
    d1=deck_id
   
    u=db.session.query(User).filter_by(user_id=u1).first()
    de=db.session.query(Decks).filter_by(deck_id=d1).first()
    if request.method=="POST":
        d_name=request.form.get('deck_name')
        desc=request.form.get('descr')
        de.deckname=d_name
        de.description=desc
        de.udeck_id=u1
        db.session.commit()
        
        return redirect(url_for("dash",user_id=u.user_id))
    return render_template("update_deck.html",de=de,u=u)


@app.route("/<int:user_id>/<int:deck_id>/delete_deck",methods=['GET','POST'])
def delete_deck(user_id,deck_id):
    u1=user_id
    d1=deck_id
    u=db.session.query(User).filter_by(user_id=u1).first()
    de=db.session.query(Decks).filter_by(deck_id=d1).first()
    ce=db.session.query(Cards).filter_by(dcard_id=de.deck_id).all()
   
    if request.method=="GET":
        for i in range(len(ce)):    
           db.session.delete(ce[i])
           db.session.commit()
        db.session.delete(de)
        db.session.commit()
        return redirect(url_for("dash",user_id=u.user_id))
    return redirect(url_for("dash",user_id=u.user_id))



@app.route("/<int:user_id>/<int:deck_id>/add_card",methods=['GET','POST'])
def add_card(user_id,deck_id):
    u1=user_id
    d1=deck_id
    u=db.session.query(User).filter_by(user_id=u1).first()
    de=db.session.query(Decks).filter_by(deck_id=d1).first()
    if request.method=="POST":
        ques=request.form['q']
        ans=request.form['a']
        c=Cards(ques=ques,ans=ans,dcard_id=d1)
        db.session.add(c)
        db.session.commit()
        ce=db.session.query(Cards).filter_by(dcard_id=d1)
        return redirect(url_for("deck_dash",deck_id=de.deck_id,user_id=u.user_id))
    return render_template("add_card.html",de=de,u=u)


@app.route("/<int:user_id>/<int:deck_id>/<int:card_id>/update_card",methods=['GET','POST'])
def update_card(user_id,deck_id,card_id):
    u1=user_id
    d1=deck_id
    c1=card_id
    u=db.session.query(User).filter_by(user_id=u1).first()
    de=db.session.query(Decks).filter_by(deck_id=d1).first()
    ce=db.session.query(Cards).filter_by(card_id=c1).first()

    if request.method=="POST":
        q=request.form['Q']
        a=request.form['A']
        ce.ques=q
        ce.ans=a
        db.session.commit()
        return redirect(url_for("deck_dash",deck_id=de.deck_id,user_id=u.user_id))
    return render_template("update_Card.html",de=de,u=u,ce=ce)


@app.route("/<int:user_id>/<int:deck_id>/<int:card_id>/delete_card",methods=['GET','POST'])
def delete_card(user_id,deck_id,card_id):
    u1=user_id
    d1=deck_id
    c1=card_id

    u=db.session.query(User).filter_by(user_id=u1).first()
    de=db.session.query(Decks).filter_by(deck_id=d1).first()
    ce=db.session.query(Cards).filter_by(card_id=c1).first()
 
    if request.method=="GET":
        db.session.delete(ce)
        db.session.commit()
        return redirect(url_for("deck_dash",deck_id=de.deck_id,user_id=u.user_id))
    return redirect(url_for("deck_dash",deck_id=de.deck_id,user_id=u.user_id))

current_deck=[]
current_index=0
current_score=0
@app.route("/<int:user_id>/<int:deck_id>/Start",methods=['GET','POST'])
def Start(user_id,deck_id):
    
    global current_deck
    global current_index
    current_deck=[]
    current_index=0
    global current_score
    current_score=0
    d1=deck_id
    u1=user_id
    ce=db.session.query(Cards).filter_by(dcard_id=d1).all()
    for i in ce:
        current_deck.append(i.card_id)
    return redirect("/{}/{}/{}/start1".format(user_id,deck_id,current_deck[current_index]))


@app.route("/<int:user_id>/<int:deck_id>/<int:card_id>/start1",methods=['GET','POST'])
def start1(user_id,card_id,deck_id):
    u1=user_id
    d1=deck_id
    c1=card_id
    global current_index
    global current_deck
    global current_score
    submit_enable=False
    u=db.session.query(User).filter_by(user_id=u1).first()
    de=db.session.query(Decks).filter_by(deck_id=d1).first()
    
    ce=Cards.query.filter_by(card_id=current_deck[current_index]).first()   
    a=len(current_deck)
    
    if request.method=="POST":
        global current_score
        if a==1:
          a=len(current_deck)
        else:
         current_deck.pop(0)
        c=0
        p=request.form.get('options')
        print(p)
        if p=="EASY":
            current_score+=1
        elif p=="MODERATE":
            current_score+=3
        else:
            current_score+=5
        print(current_score)
        if a==1:
         total_cards=len(Cards.query.filter_by(dcard_id=de.deck_id).all())
         de.no_of_submits+=1
         de.latest_score=(current_score/(total_cards*5))*100
         de.total_score=de.total_score+de.latest_score
         de.latest_time=datetime.now()
         db.session.commit()
        ce=Cards.query.filter_by(card_id=current_deck[0]).first()
        print(ce)
        return render_template("start.html",de=de,u=u,ce=ce,a=a,current_index=current_index,)
    return render_template("start.html",de=de,u=u,ce=ce,a=a,current_index=current_index)

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)