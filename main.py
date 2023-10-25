from flask import Flask, render_template, request, redirect, url_for, session ,flash
from datetime import timedelta
from database_coding import Book , db, app ,User



app.secret_key= "anystring" # this add so we can control the session flask function
app.permanent_session_lifetime = timedelta(days=5) # how long the session data stored 




@app.route("/")
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", all_books_1=all_books)


@app.route("/add", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        new_book = Book(
            title=request.form["book_name"],
            author=request.form["book_author"],
            rating=request.form["rating"],
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")




@app.route("/edit", methods=["GET", "POST"])
def edit_rating():
    if request.method == "POST":
        #UPDATE RECORD
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template("edit_rating.html", book=book_selected)

@app.route("/delete")
def delete ():
    
    book_id = request.args.get('id')
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))




@app.route("/login",methods = ["POST","GET"])
def login ():
    if request.method == "POST":
        flash('Logged in successfully')
        session.permanent= True # control how long session stored on server
        username =request.form["user_name_field"] # get the input data from the form
        session["new_variable_user"]= username    # store the session on the server
        return redirect(url_for("user_function"))
    else:
        if "new_variable_user" in session:  
            flash("Already logged in")
            return redirect(url_for("user_function"))
        return render_template("login.html")


@app.route("/create_acount",methods = ["POST","GET"])
def create_account_function():
    
    if request.method == "POST":
        new_user = User(
        username_v1 =request.form["user_name_field"], # get the input data from the form
        email_v1 =request.form["email_field"] , 
        password_v1 =request.form["password_field"] 
        )
        
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))

    return render_template("create_account.html")




@app.route("/user")
def user_function ():
    if "new_variable_user" in session:
        user_v1 = session["new_variable_user"]
        return render_template(("user_file.html"), user_file_html_variable = user_v1)
    else:
        flash("You are not logged in ")
        return redirect(url_for("login"))





@app.route("/logout")
def logout ():
    if "new_variable_user" in session:
        user_v2 = session["new_variable_user"]
        session.pop("new_variable_user",None)
        flash(f"Logged out successfully {user_v2}" ,"info")
    else:
        flash("You are not logged in","info")
    return render_template("logout.html")
    

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)
        
        
