import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    user_id=session["user_id"]
    transactions_db = db.execute("select symbol, sum(shares) as shares, price from transactions where user_id = ? group by symbol", user_id)
    cash_db = db.execute("select cash from users where id=?", user_id)
    cash=cash_db[0]["cash"]
    return render_template("index.html", database = transactions_db,cash=cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "GET":
        return render_template ("buy.html")
    else:
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))
        if not symbol:
            return apology("input name of stock")
        stock = lookup(symbol.upper())
        if stock == None:
            return apology("symbol no exist")
        if shares<0:
            return apology("shares less than 0")
        transaction_value=shares * stock["price"]
        user_id=session["user_id"]
        user_cash_db=db.execute("SELECT cash from users where id=:id", id=user_id)
        #user_cash_db returns you a list looking like [{"cash": 10000}]
        # for the next line, u use [0] to get the first row's data and ["cash"] to obtain data: [{"cash": 10000}]
        user_cash=user_cash_db[0]["cash"]
        if user_cash<transaction_value:
            return apology("not enough cash")
        uptd_cash=user_cash-transaction_value
        db.execute("UPDATE users SET cash=? where id=?", uptd_cash, user_id)
        date=datetime.datetime.now()
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price, date) values (?,?,?,?,?)", user_id, stock["symbol"], shares, stock["price"], date)
        flash("Bought")
        return redirect ("/")



@app.route("/history")
@login_required
def history():
    user_id=session["user_id"]
    transactions_db = db.execute("select * from transactions where user_id=:id", id=user_id)
    return render_template("history.html", transactions=transactions_db)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "GET":
        return render_template ("quote.html")
    else:
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("give symbol")
        stock = lookup(symbol.upper())

        if stock == None:
            return apology("Symbol not found")

        return render_template ("quoted.html", name=stock["name"], price=stock["price"], symbol=stock["symbol"])

@app.route("/addcash", methods=["GET", "POST"])
@login_required
def addcash():
    if request.method=="GET":
        return render_template("addcash.html")
    else:
        user_id=session["user_id"]
        cash=int(request.form.get("cash"))

        if not cash:
            return apology("no input")
        user_cash_db=db.execute("SELECT cash from users where id=:id", id=user_id)
        user_cash=user_cash_db[0]["cash"]
        user_cash=int(user_cash)

        uptd_cash=user_cash + cash
        uptd_cash=int(uptd_cash)
        db.execute("Update users set cash=? where id=?", uptd_cash, user_id)
        return render_template("addedcash.html", cash=uptd_cash)



@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template ("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("Must Give Username")
        if not password:
            return apology("must give password")
        if not confirmation:
            return apology("must give confirmation")
        if password != confirmation:
            return apology("password dont match")

        hash = generate_password_hash(password)

        try:
            new_user = db.execute("INSERT INTO users (username, hash) VALUES (?,?)", username, hash)
        except:
            return apology("username already exist")

        session["user_id"]=new_user

        return redirect("/")



@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method == "GET":
         user_id=session["user_id"]
         symbols_user=db.execute("select symbol from transactions where user_id=:id group by symbol having sum(shares)>0", id=user_id)
         #this happens as symbols_user returns a list of items
         return render_template ("sell.html", symbols = [row["symbol"]for row in symbols_user])
    else:
        symbol = request.form.get("symbols")
        shares = int(request.form.get("shares"))

        stock = lookup(symbol.upper())
        if stock == None:
            return apology("symbol no exist")
        if shares<0:
            return apology("shares less than 0")
        transaction_value = shares * stock["price"]
        user_id = session["user_id"]
        user_cash_db=db.execute("SELECT cash from users where id=:id", id=user_id)
        user_cash=user_cash_db[0]["cash"]
        user_shares = db.execute("select sum(shares) as shares from transactions where user_id=:id and symbol = :symbol", id=user_id,symbol=symbol)
        user_shares_real=user_shares[0]["shares"]

        if shares > user_shares_real:
            return apology("you dont have that much")
        uptd_cash = user_cash + transaction_value
        db.execute("Update users set cash=? where id=?", uptd_cash, user_id)
        date=datetime.datetime.now()
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price, date) values (?,?,?,?,?)", user_id, stock["symbol"], (-1)*shares, stock["price"], date)
        flash("sold")
        return redirect("/")
