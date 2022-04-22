from flask import Flask,render_template,redirect,request,session
from DBConnection import Db
app = Flask(__name__)
app.secret_key="abc"

@app.route('/a')
def hello_world():
    return 'Hello World!'





@app.route('/',methods=['get','post'])
def login():
    if request.method == "POST":
        username = request.form['textfield']
        password = request.form['textfield2']
        db = Db()
        res = db.selectOne("select * from login where username='" + username + "' and password='" + password + "'")
        if res is not None:
            if res['user_type'] == 'admin':
                session['log'] = "lo"
                return redirect('/admin_home')
            else:
                return '''<script>alert("INVALID");window.location="/"</script>'''
        else:
            return '''<script>alert("INVALID USER");window.location="/"</script>'''

    return render_template('LOGIN.html')


@app.route('/admin_home')
def admin_home():
    if session['log'] == "lo":
        return render_template('ADMIN/ADMIN_HOME.html')
    else:
        return redirect('/')


@app.route('/view_users')
def view_users():
    if session['log'] == "lo":
        db=Db()
        res=db.select("select * from user,login where user.user_id=login.login_id and login.user_type='pending'")
        return render_template('ADMIN/VIEW_&_VERIFY_USER.html',data=res)
    else:
        return redirect('/')


@app.route('/approve_user/<id>')
def approve_user(id):
    if session['log'] == "lo":
        db = Db()
        db.update("update login set user_type='user' where login_id='" + str(id) + "'")
        return redirect('/view_users')
    else:
        return redirect('/')



@app.route('/reject_user/<id>')
def reject_user(id):
    if session['log'] == "lo":
        db = Db()
        db.delete("delete from user where  user_id = '" + str(id) + "'")
        db.update("update login set user_type='reject' where login_id='" + str(id) + "'")
        return redirect('/view_users')
    else:
        return redirect('/')



@app.route('/view_verified_users')
def view_verified_users():
    if session['log'] == "lo":
        db = Db()
        res = db.select("select * from login,user where user.user_id=login.login_id and login.user_type='user' ")
        return render_template('ADMIN/VIEW_VERIFIED_USER.html',data=res)
    else:
        return redirect('/')


@app.route('/add_category',methods=['get','post'])
def add_category():
    if session['log'] == "lo":
        if request.method=="POST":
            category=request.form['textfield']
            db=Db()
            db.insert("insert into category VALUES ('','"+category+"')")
            return '''<script>alert("CATEGORY ADDED");window.location="/admin_home"</script>'''
        else:
            return render_template('ADMIN/ADD_CATEGORY.html')
    else:
        return redirect('/')



@app.route('/view_category')
def view_category():
    if session['log'] == "lo":
        db=Db()
        res=db.select("select * from category")
        return render_template('ADMIN/VIEW_CATEGORY.html',data=res)
    else:
        return redirect('/')


@app.route('/delete_category/<pid>')
def delete_category(pid):
    if session['log'] == "lo":
        db=Db()
        db.delete("delete from category where category_id='"+pid+"' ")
        return '''<script>alert("DELETED");window.location="/admin_home"</script>'''
    else:
        return redirect('/')



@app.route('/add_govt_policy',methods=['get','post'])
def add_govt_policy():
    if session['log'] == "lo":
        if request.method=="POST":
            title=request.form['textfield2']
            content=request.form['textarea']
            url=request.form['textarea2']
            db=Db()
            db.insert("insert into govt_policy VALUES ('',curdate(),'"+title+"','"+content+"','"+url+"')")
            return '''<script>alert("GOVT POLICY ADDED");window.location="/admin_home"</script>'''
        else:
             return render_template('ADMIN/ADD_GOVT_POLICY.html')
    else:
        return redirect('/')


@app.route('/view_govt_policy')
def view_govt_policy():
    if session['log'] == "lo":
        db=Db()
        res=db.select("select * from govt_policy")
        return render_template('ADMIN/VIEW_GOVT_POLICY.html',data=res)
    else:
        return redirect('/')


@app.route('/update_govt_policy/<a>',methods=['get','post'])
def update_govt_policy(a):
    if session['log'] == "lo":
        if request.method=="POST":
            title=request.form['textfield2']
            content=request.form['textarea']
            url=request.form['textarea2']
            db=Db()
            db.update("update govt_policy set date=curdate(),title='"+title+"',content='"+content+"',url='"+url+"' where policy_id='"+a+"'")
            return '''<script>alert("GOVT POLICY UPDATED");window.location="/view_govt_policy"</script>'''
        else:
            db=Db()
            res=db.selectOne("select * from govt_policy where policy_id='"+a+"'")
            return render_template('ADMIN/UPDATE_GOVT_POLICY.html',data=res)
    else:
        return redirect('/')



@app.route('/delete_govt_policy/<did>')
def delete_govt_policy(did):
    if session['log'] == "lo":
        db=Db()
        db.delete("delete from govt_policy where policy_id='"+did+"' ")
        return '''<script>alert("DELETED");window.location="/view_govt_policy"</script>'''
    else:
        return redirect('/')


@app.route('/logout')
def logout():
    session['log']=""
    return redirect('/')


if __name__ == '__main__':
    app.run(port=4000)
