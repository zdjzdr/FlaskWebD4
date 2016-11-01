from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, EqualTo
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.config['SECRET_KEY'] = 'zdj'
bootstrap = Bootstrap(app)


class NameForm(FlaskForm):
    name = StringField('你的姓名:  ', validators=[DataRequired()])
    pwd1 = PasswordField('密码:  ')
    pwd2 = PasswordField('密码确认： ', validators=[EqualTo(pwd1, '密码不一致')])
    addr = TextAreaField('地址： ')
    submit = SubmitField('提交')


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    # name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('用户名提交成功啦!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))


if __name__ == '__main__':
    app.run(debug=True)
